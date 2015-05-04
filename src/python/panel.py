import re
from time import sleep
from serial_com import SerialCommunication


class Panel(SerialCommunication):
    """docstring for Panel
    """

    def __init__(self, x, y):
        self.connection = None
        unit = ['/dev/tty.SLAB_USBtoUART', '38400', '1']
        self.regex = re.compile('[-+]?[0-9]*\.?[0-9]+')  # regex to extract float
        self.x_offset = x       # determines the size of adj. steps in the sensor
        self.y_offset = y       # determines the size of adj. steps in the sensor

        try:
            SerialCommunication.serial_connect(self, unit)
        except:
            raise

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
            print("New coordinates is: %f, %f" % (x, y))
            #self.set_y_coordinate(str(y))

        if check_x:
            print("New coordinates is: %f, %f" % (x, y))
            #self.set_x_coordinate(str(x))

        #while not self._correct_position():
            pass

    def _correct_position(self):
        # The index 4&5 contains the difference between the set value and
        # current position of the panel.

        # If the values are below 0.01 it is to be considered that the panel
        # is in the right place, according to empirical evidence.

        log = self.get_log()
        if(abs(float(log[4]) < 0.01) and abs(float(log[5]) < 0.01)):
            return True
        return False
