import serial
import re
from time import sleep


class SCom(object):
    def __init__(self):
        super(SCom, self).__init__()
        self.connection = None
        self.regex = re.compile('[-+]?[0-9]*\.?[0-9]+')
        self.x = 0
        self.y = 0

    def serial_connect(self):
        if self.connection is not None:
            self.connection.close()
        self.connection = serial.Serial('/dev/tty.SLAB_USBtoUART', 38400, timeout=1)
        sleep(1)

    def connect_remote(self):
        try:
            self.serial_connect()
        except serial.SerialException:
            print('Connection failed')
        else:
            if self.connection.isOpen():
                self.connection.flushInput()
                self.connection.flushOutput()
                print("Connection open")
            else:
                print('Serial connection is not open')

    def get_value(self):
        pass

    def get_this_value(self, x, y):
        pass

    def get_coordinates(self):
        self.serial_write('zeroposx')

        for x in range(0, 2):
            indata = self.connection.readline()
            indata = indata.decode(encoding='utf-8')
            m = self.regex.findall(indata)

        # print(m[0])
        # print(m[1])
        return m

    def set_x_coordinate(self, num):
        self.serial_write('zeroposx ' + num)
        print('position set to: zeroposx ' + num)

    def set_y_coordinate(self, num):
        self.serial_write('zeroposy ' + num)
        print('position set to: zeroposy ' + num)

    def step_east(self):
        self.x += 1

    def step_south(self):
        self.y += 1

    def step_west(self):
        self.x -= 1

    def step_north(self):
        self.y -= 1

    def serial_write(self, command):

        command += '\r'
        try:
            if self.connection.write(command.encode('utf-8')) > 0:
                pass
            else:
                print('Serial write failed')

        except serial.SerialTimeoutException:
            print('Timeout on serial write')

        except serial.SerialException:
            print('Serial communication failed')

a = SCom()
a.connect_remote()
a.get_coordinates()
