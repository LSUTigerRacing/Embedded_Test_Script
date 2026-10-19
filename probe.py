from pyocd.core.helpers import ConnectHelper
from pyocd.flash.file_programmer import FileProgrammer


class Probe:
    # Connect to a debug probe (ST-Link or J-Link) through pyOCD.
    # and pyOCD detects it from the on-board ST-Link.
    def __init__(self, unique_id=None, target=None):
        options = {"target_override": target} if target else {}
        self.session = ConnectHelper.session_with_chosen_probe(
            unique_id=unique_id,
            blocking=False,
            options=options,
        )
        if self.session is None:
            raise RuntimeError("no debug probe found (check `pyocd list` and udev rules)")
        self.session.open()

    # Program a .elf/.hex/.bin file into flash. .bin needs a base address.
    def flash(self, path, base_address=None):
        FileProgrammer(self.session).program(path, base_address=base_address)

    # Reset the target and let it run
    def reset(self):
        self.session.target.reset()

    def close(self):
        self.session.close()
