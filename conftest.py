import pytest
from device import Device

def pytest_addoption(parser):
    parser.addoption("--port", default="/dev/ttyACM0")

@pytest.fixture(scope="session")
def dut(request):
    d = Device(request.config.getoption("--port"))
    yield d
    d.close()