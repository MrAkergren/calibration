from serial_com import SerialCommunication
from panel import Panel
from arduino import Arduino
from mock_read import MockRead
import sys


class SerialHandler:
    """docstring for SerialHandler
    """
    def __init__(self, x, y):
        #self.m = MockRead()
        try:
            self.pan = Panel(x, y)
        except:
            print("Panel failed")
            sys.exit(0)

        try:
            self.ard = Arduino()
        except:
            print("Lux meter failed")
            sys.exit(0)

    def get_value(self):
        return self.ard.get_value()
        #return self.m.get_value()

    def get_log(self):
        return self.pan.get_log()

    def move(self, coordinates, direction):
        self.pan.move(coordinates, direction)
        return self.get_value()

    def get_coordinates(self):
        return self.pan.get_coordinates()

    def set_x_coordinate(self, num):
        self.pan.set_x_coordinate(num)

    def set_y_coordinate(self, num):
        self.pan.set_y_coordinate(num)

