from serial_com import SerialCommunication
from time import sleep


class Arduino(SerialCommunication):
    """docstring for Arduino
    """
    def __init__(self):
        self.connection = None
        self.EXIT_CONSTANT = 20
        unit = ['/dev/tty.usbmodem1411', '9600', '1']

        try:
            SerialCommunication.serial_connect(self, unit)
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
