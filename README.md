# automated embedded testing using python

# SETUP ON UBUNTU

    sudo apt install python3-venv git
    python3 -m venv .venv
    source .venv/bin/activate
    pip install -r requirements.txt

Add your user to the `dialout` group to access the serial port
(`sudo usermod -aG dialout $USER`, then log out and back in).

## ST-Link (Nucleo) udev rules
Without these, pyOCD can't open the ST-Link unless run as root.

    git clone --depth 1 https://github.com/pyocd/pyOCD.git /tmp/pyocd-src
    sudo cp /tmp/pyocd-src/udev/*.rules /etc/udev/rules.d/
    sudo udevadm control --reload-rules && sudo udevadm trigger

Then unplug and replug the board.

## J-Link
Install the SEGGER J-Link Software Pack (.deb) from
https://www.segger.com/downloads/jlink/ :

    sudo apt install ./JLink_Linux_*_x86_64.deb

It provides `libjlinkarm.so` and its own udev rules. The Python side
(`pylink-square`) is installed with pyocd.

## Check the probe is seen

    pyocd list                       # shows probes and their unique IDs
    pyocd list --targets             # built-in target names
    pyocd pack install stm32f4       # only if your chip isn't built in

# Running test

pytest or pytest --port=/dev/ttyACM0

//lets you see the test case you passed and failed
pytest -v -s or pytest --port=/dev/ttyACM0 -v -s

The code currently in test_device.py need to be implemented and uploaded to your microcontroller for it to work.

# Basic implementation in main.cpp

#include <Arduino.h>


void setup() {
  Serial.begin(115200);
  Serial.println("Ready");
}

void loop() {
  if (!Serial.available()) return;

  String line = Serial.readStringUntil('\n');
  line.trim();

  if (line.startsWith("ADD1 ")) {
    Serial.println(line.substring(5).toInt() + 1);
  } else if (line.startsWith("Double ")) {
    Serial.println(line.substring(7).toInt() * 2);
  } else {
    Serial.println("ERR unknown command");
  }
}
