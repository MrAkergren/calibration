# from serial_com import SerialCommunication
from panel import Panel
from arduino import Arduino
from yocto_lux import Yocto
import sys
from statistics import median


class SerialHandler:
    """The class that connects the serial objects to GUI and search algorithm.

    This class will create the serial objects and contain the logic needed
    for communication to and between those objects.

    Arguments:
        x (float): The offset "how far will the panel move" on the x axis
        y (float): The offset "how far will the panel move" on the y axis

    Raises:
        EnvironmentError    raises the error from Panel if the device do not 
                            move, most likely due to inactive sun sensor
    """
    def __init__(self):
        pass

    def connect_devices(self, win_panel_com=None, win_ard_com=None):
        """Tries to connect the panel and arduino.

        Arguments:
            win_panel_com (str): If not on windows OS, defaults to None
            win_ard_com (str): If not on windows OS, defaults to None
        """
        try:
            self.pan = Panel(win_panel_com)
        except Exception as e:
            print(e.strerror)
            print("Panel failed")
            #sys.exit(0)

        try:
            self.lux = Arduino(win_ard_com)
        except:
            print("Ada lux meter failed")
            try: 
                self.lux = Yocto()
                print("Yocto lux meter connected")
            except Exception as e:
                print(e)
                print("Yocto lux meter failed")
               # sys.exit(0)

    def get_value(self):
        """Returns the value give by the lux-meter

        Returns:    
            value (int)
        """
        results = []
        for x in range(0, 4):
            results.append(self.lux.get_value())
        return round(median(results), -2)

    def get_log(self):
        """Returns the log-string from the panel. 

        Returns:
            log_file (list[floats]):    The 'logga' string from the panel as a 
                                        list of floats
        """
        return self.pan.get_log()

    def move(self, coordinates, direction):
        """Turns the panel to the direction given with the coordinates as base.

        Attributes:
            coordinates (tuple[float]): two floats to represent the x,y coord.
            direction (str): The direction in caps as north, west, south, east

        Returns:    
            value (int)

        Raises:
            EnvironmentError:   raises the error from Panel if the device do not 
                                move, most likely due to inactive sun sensor

        """
        try:
            self.pan.move(coordinates, direction)
            return self.get_value()
        except Exception as e:
            print(e)
            raise

    def get_coordinates(self):
        """Returns the current coordinates of the panel as a tuple of floats,
        x, y"""
        return self.pan.get_coordinates()

    def set_coordinates(self, x, y):
        self.pan.set_coordinates(x, y)

    def set_x_coordinate(self, num):
        """Set the desired x coordinate, as a float in num"""
        self.pan.set_x_coordinate(num)

    def set_y_coordinate(self, num):
        """Set the desired y coordinate, as a float in num"""
        self.pan.set_y_coordinate(num)

    def get_offset(self):
        """Return the offset-argument currently set on the panel.
        """
        return self.pan.get_offset()

    def set_offset(self, x, y):
        """Sets the offset for the search steps on the panel.
        """
        self.pan.set_offset(x, y)

    def wait_for_panel_position(self):
        """ Waits for the panel arrive at a set position
        """
        self.pan.wait_for_correct_position
