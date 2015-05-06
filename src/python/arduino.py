from serial_com import SerialCommunication
from time import sleep


class Arduino(SerialCommunication):
    """docstring for Arduino
    """
    def __init__(self):
        self.connection = None
        self.EXIT_CONSTANT = 20
        unit = ['/dev/tty.usbmodem1421', '9600', '1']
        connect_bool = False

        try:
            SerialCommunication.serial_connect(self, unit)
            print("Connected to lux-meter on \'usbmodem1421\'")
        except:
            try:
                unit[0] = '/dev/tty.usbmodem1411'
                SerialCommunication.serial_connect(self, unit)
                print("Connected to lux-meter on \'usbmodem1411\'")
            except:
                raise


    def get_value(self, arg=0):
        sleep(0.1)
        while self.connection.inWaiting() > 0:
            text = self._serial_read()
            if(text is not None):
                return int(text)

        if(arg < self.EXIT_CONSTANT):
            return self.get_value(arg+1)
        else:
            return None
