import re
import sys
from time import sleep, time
from serial_com import SerialCommunication


class Panel(SerialCommunication):
    """The class responsible for the communication to the panel,
    contains the specific methods for the panel.
    Inherits:
        SerialCommunication

    Arguments:
        offset (tuple[float]):  the offsets in x and y, how big steps it should
                                be taking
        win_panel_com (str):    If it's not None it should contain the digit on
                                which COM-port the panel is connected to.

    Raises:
        SerialException:    if the panel can't connect.
    """

    def __init__(self, offset, win_panel_com):
        SerialCommunication.__init__(self)
        if win_panel_com is not None:
            device = "COM" + win_panel_com
        else:
            device = self._serial_device()
        unit = [device, '38400', '1']
        self.regex = re.compile('[-+]?[0-9]*\.?[0-9]+')  # regex to extract float
        self.x_offset = offset[0]       # determines the size of adj. steps in the sensor
        self.y_offset = offset[1]       # determines the size of adj. steps in the sensor

        try:
            self.serial_connect(unit)
            print("Connected to panel on \'" + device + "\'")
            self._logga_off()
        except:
            raise

    def _serial_device(self):
        #  detects OS and returns the correct pathway to the panel
        #  windows not affected, that OS is dealt with earlier.
        if sys.platform.startswith('darwin'):
            return '/dev/tty.SLAB_USBtoUART'

        elif sys.platform.startswith('linux'):
            return '/dev/ttyUSB0'

        else:
            raise EnvironmentError('System not supported')

    def _logga_off(self):
        # turns off logga for the panel if it is on
        sleep(2)
        if self.connection.inWaiting() > 0:
            self._serial_write('logga')
            self.connection.flushInput()
            print("\'logga\' has been turned Off")
        else:
            print("\'logga\' was Off from start")

    def get_log(self):
        """Returns a 'logga'-string from the panel as a list of strings.
        """
        self._serial_write('logga')
        sleep(1)
        while self.connection.inWaiting() > 0:
            log = self._serial_read()
        self._serial_write('logga')
        info = self.regex.findall(log)
        return info

    def get_coordinates(self):
        """ Tries to return the coordinates 10 times, if it fails it returns
        None.

        Returns a tuple of the two floats that is the coordinates.
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
        coordinates is a tuple and direction a string.
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
            print("New coordinates is: %f, %f" % (x, y))
            self.set_y_coordinate(str(y))

        if check_x:
            print("New coordinates is: %f, %f" % (x, y))
            self.set_x_coordinate(str(x))

        start_time = time()
        while not self._correct_position():
            if time() - start_time > 15.0:
                print("Something went wrong, not \'run auto\'?")
                raise EnvironmentError('Panel not turning')
            pass

    def stop_panel(self):
        self._serial_write('run stop')

    def _correct_position(self):
        # The index 4&5 contains the difference between the set value and
        # current position of the panel.

        # If the current out from the sensor is below 504, the sensor does
        # not control the panel

        # If the values are below 0.01 it is to be considered that the panel
        # is in the right place, according to empirical evidence.

        log = self.get_log()
        if (float(log[0])+float(log[1])+float(log[2])+float(log[4])) < 504:
            raise EnvironmentError('Sun sensor not active')
        if(abs(float(log[4]) < 0.01) and abs(float(log[5]) < 0.01)):
            return True
        return False
