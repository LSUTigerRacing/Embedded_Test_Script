import serial
import time

class Device:
    # initialize port,baud, and timeout.
    def __init__(self, port, baud=115200, timeout=2):
        self.ser = serial.Serial(port,baud,timeout=timeout)
        time.sleep(2)
        self.ser.reset_input_buffer()
    def send_command(self, cmd: str)->None:
        self.ser.write((cmd+ "\n").encode())

    def read_response(self)->str:
        line = self.ser.readline()
        if not line:
            raise TimeoutError("no response from device")
        return line.decode(errors="replace").strip()
    def query(self,cmd:str)->str:
        self.send_command(cmd)
        response = self.read_response()
        print(f"  -> {cmd!r}  <- {response!r}")
        return response
    def close(self):
        self.ser.close()