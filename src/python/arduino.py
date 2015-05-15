from serial_com import SerialCommunication
from time import sleep


class Arduino(SerialCommunication):
    """The class responsible for the communication to the Arduino lux-meter.

    Inherits from SerialCommunication.

    Automatically tries connects to the unit during init.

    Arguments:
        win_ard_com (str):  a string of the integer that is the port on the 
                            windows machine to the Arduino

    Raises:
        SerialException:    raises the error from SerialCommunication if the
                            device cannot connect
    """
    def __init__(self, win_ard_com):
        SerialCommunication.__init__(self)
        self._EXIT_CONSTANT = 20
        if win_ard_com is not None:
            device = "COM" + win_ard_com
        else:
            device = self._serial_device()
        unit = [device, '9600', '1']
        try:
            self.serial_connect(unit)
            print("Connected to lux-meter on \'" + device + "\'")
        except:
            raise

    def _serial_device(self):
        #Connects to linux or darwin automatically 
        platform, ports = self.serial_port_list()
        matching = []
        if platform == 'darwin':
            matching = [p for p in ports if '/dev/tty.usbmodem14' in p]
        elif platform == 'linux':
            matching = [p for p in ports if '/dev/ttyACM' in p]
        if len(matching) > 0:
            return matching[0]
        else:
            print("No matching serial device found")

    def get_value(self, arg=0):
        """ Recursively tries to get a value from the Arduino.

            Arguments:
                arg (int):  Stop measurement, if higher then EXIT_CONSTANT, 
                            the recursion will stop. Set to 0 if not given.

            Returns: 
                value (int):    The value from the lux-meter or None if value is
                                not available
        """
        sleep(0.1)
        while self.connection.inWaiting() > 0:
            self.connection.flushInput()
            value = self._serial_read().strip()
            if value is not None and value.isdigit() and int(value) < 65200:
                return int(value)

        if arg < self._EXIT_CONSTANT:
            return self.get_value(arg+1)
        else:
            return None
