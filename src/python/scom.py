import serial
import re
from mock_read import MockRead
from time import sleep


class SCom(object):
    """The class that handles the serial communication to the SP3 panel.
    """
    def __init__(self, x, y):
        super(SCom, self).__init__()
        self.connection = None
        self.regex = re.compile('[-+]?[0-9]*\.?[0-9]+')  # regex to extract float
        self.x_offset = x       # determines the size of adj. steps in the sensor
        self.y_offset = y       # determines the size of adj. steps in the sensor
        self.mock = MockRead()  # when lightvalue can't be read, use mock
        self.serial_connect()   # auto connect when object is created

    def serial_connect(self):
        """The method to handle the connection to the panel.
        """
        try:
            if self.connection is not None:
                self.connection.close()
            self.connection = serial.Serial('/dev/tty.SLAB_USBtoUART', 38400, timeout=1)
            sleep(1)
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
        """Returns a 'logga'-string from the panel as a list of strings.
        """
        self._serial_write('logga')
        sleep(2)
        while self.connection.inWaiting() > 0:
            log = self._serial_read()
        self._serial_write('logga')
        info = self.regex.findall(log)
        return info

    def get_coordinates(self):
        """ Tries to return the coordinates 10 times, if it failes it returns 
        None.

        Retrns a tuple of the two floats that is the coordinates.
        """
        for x in range(0, 10):
            self._serial_write('zeroposx')
            sleep(1)
            while self.connection.inWaiting() > 0:
                indata = self._serial_read()
                coordinates = self.regex.findall(indata)
                if(coordinates):
                    return (float(coordinates[0]), float(coordinates[1]))
        return None

    def set_x_coordinate(self, num):
        """'num' needs to be a string.
        """
        self._serial_write('zeroposx ' + num)
        print('position set to: zeroposx ' + num)  # Debug print
        sleep(2)

    def set_y_coordinate(self, num):
        """'num' needs to be a string.
        """
        self._serial_write('zeroposy ' + num)
        print('position set to: zeroposy ' + num)  # Debug print
        sleep(2)

    def move(self, coordinates, direction):
        """The method that sends the move command to the panel.
        """
        x, y = coordinates
        check_x = False  # If the x-value is changed, set the x coordinate
        check_y = False  # If the y-value is changed, set the y coordinate

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

        if check_y:
            self.set_y_coordinate(str(y))
        if check_x:
            self.set_x_coordinate(str(x))

        while not self._correct_position():
            pass

        return self.get_value()

    def _serial_write(self, command):

        command += '\r'  # Append to the command so the panel to executes it
        try:
            if self.connection.write(command.encode('utf-8')) > 0:
                pass
            else:
                print('Serial write failed')

        except serial.SerialTimeoutException:
            print('Timeout on serial write')

        except serial.SerialException:
            print('Serial communication failed')

    def _serial_read(self):
        # To decode the information from the panel to a utf-8 string

        text = self.connection.readline()
        text = text.decode(encoding='utf-8')
        return text

    def _correct_position(self):
        # The index 4&5 contains the difference between the set value and
        # current position of the panel.

        # If the values are below 0.01 it is to be considered that the panel
        # is in the right place, according to empirical evidence.

        log = self.get_log()
        if(abs(float(log[4]) < 0.01) and abs(float(log[5]) < 0.01)):
            return True
        return False

# a = SCom()
# a.connect_remote()
# a.set_x_coordinate('-0.15')
# b = a.get_log()
# print(b[4], b[5])
# print(a._correct_position())
