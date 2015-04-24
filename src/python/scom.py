import serial
import re
from mock_read import MockRead
from time import sleep

class SCom(object):
    def __init__(self, x, y):
        super(SCom, self).__init__()
        self.connection = None
        self.regex = re.compile('[-+]?[0-9]*\.?[0-9]+')
        self.x_offset = x
        self.y_offset = y
        self.mock = MockRead()
        self.connect_remote()

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
        return self.mock.get_value()

    def get_this_value(self, x, y):
        pass

    def get_log(self):
        self.serial_write('logga')
        sleep(2)
        while self.connection.inWaiting() > 0:
            log = self.connection.readline()
            log = log.decode(encoding='utf-8')
        self.serial_write('logga')
        info = self.regex.findall(log)
        print(info[4], info[5])
        return info

    def get_coordinates(self):
        for x in range(0, 10):
            self.serial_write('zeroposx')
            sleep(1)

            while self.connection.inWaiting() > 0:
                indata = self.connection.readline()
                indata = indata.decode(encoding='utf-8')
                coordinates = self.regex.findall(indata)
                if(coordinates):
                    return (float(coordinates[0]), float(coordinates[1]))
        return None

    def set_x_coordinate(self, num):
        self.serial_write('zeroposx ' + num)
        print('position set to: zeroposx ' + num)
        sleep(2)

    def set_y_coordinate(self, num):
        self.serial_write('zeroposy ' + num)
        print('position set to: zeroposy ' + num)
        sleep(2)

    def move(self, coordinates, direction):
        x, y = coordinates
        check_x = False
        check_y = False

        if direction == 'EAST':
            x += self.x_offset
            check_x = True
        elif direction == 'SOUTH':
            y -= self.y_offset
            check_y = True
        elif direction == 'WEST':
            x -= self.x_offset
            check_x = True
        elif direction == 'NORTH':
            y += self.y_offset
            check_y = True

        if(check_y):
            self.set_y_coordinate(str(y))
        if(check_x):
            self.set_x_coordinate(str(x))

        while not self.correct_position():
            print(self.correct_position())
            

        return self.get_value()

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

    def correct_position(self):
        log = self.get_log()
        if(abs(float(log[4]) < 0.01) and abs(float(log[5]) < 0.01)):
            return True
        return False

# a = SCom()
# a.connect_remote()
# a.set_x_coordinate('-0.15')
# b = a.get_log()
# print(b[4], b[5])
# print(a.correct_position())

