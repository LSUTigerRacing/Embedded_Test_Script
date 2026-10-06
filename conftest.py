import pytest
from device import Device


def pytest_addoption(parser):
    parser.addoption("--port", default="/dev/ttyACM0")
    parser.addoption("--use-probe", action="store_true", help="connect to ST-Link/J-Link via pyOCD")
    parser.addoption("--probe", default=None, help="probe unique ID from `pyocd list`")
    parser.addoption("--target", default=None, help="pyOCD target name, e.g. stm32f411re")
    parser.addoption("--firmware", default=None, help=".elf/.hex file to flash before tests")


@pytest.fixture(scope="session")
def probe(request):
    opt = request.config.getoption
    if not (opt("--use-probe") or opt("--firmware")):
        yield None
        return

    # imported here so serial-only runs don't need pyocd installed
    from probe import Probe

    p = Probe(unique_id=opt("--probe"), target=opt("--target"))
    if opt("--firmware"):
        p.flash(opt("--firmware"))
    p.reset()
    yield p
    p.close()


# probe runs first, so the serial port opens after the board has been flashed and reset
@pytest.fixture(scope="session")
def dut(request, probe):
    d = Device(request.config.getoption("--port"))
    yield d
    d.close()
