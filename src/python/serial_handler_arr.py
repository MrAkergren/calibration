from serial_com import SerialCommunication
from panel import Panel
from arduino import Arduino
from mock_read import MockRead
from legacy.acom import Com
from search import Search
import sys


class SerialHandlerArr:
    """The class that will connect the serial objects for the GUI and the search
    algorithms. It will create the serial objects and contain the logic needed
    for communication to and between those objects.
    """
    def __init__(self, x, y):
        self.m = Com(1, 1)
        self.offset = (x, y)

        try:
            self.pan = Panel(x, y)
        except:
            print("Panel failed")
            sys.exit(0)

        try:
            self.ard = Arduino()
        except Exception as e:
            print(e)
            print("Lux meter failed")
            sys.exit(0)

    def get_value(self):
        """Returns the value give by the lux-meter as an integer"""
        return self.m.get_value()

    def get_log(self):
        """Returns the log-string from the panel as a list of floats"""
        return self.pan.get_log()

    def move(self, coordinates, direction):
        """Turns the panel to the coordinates given in 'coordiantes',
        'coordinates' is a tuple of x, y """
        try:
            self.m.move(coordinates, direction)
            return self.get_value()
        except:
            raise

    def get_coordinates(self):
        """Returns the current coordinates of the panel as a tuple of floats,
        x, y"""
        return self.m.get_coordinates()

    def set_x_coordinate(self, num):
        """Set the desired x coordinate, as a float in num"""
        self.m.set_x_coordinate(num)

    def set_y_coordinate(self, num):
        """Set the desired y coordinate, as a float in num"""
        self.m.set_y_coordinate(num)

    def get_offset(self):
        """Return the offset-argument given when creating the SerialHandler obj
        """
        return self.offset

sh = SerialHandlerArr(1, 1)
s = Search(sh)
s.labyrinth()
