automated embedded testing using python

# SETUP

pip install -r requirements.txt

On Linux, add your user to the `dialout` group to access the serial port
(`sudo usermod -aG dialout $USER`, then log out and back in).

# Running test
1. Flash the firmware (PlatformIO project) to the Arduino.
2. Run:

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
