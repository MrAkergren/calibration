from serial import Serial


class Arduino(Serial):
    """docstring for Arduino"""
    def __init__(self):
       super(Arduino, self).__init__()
       unit = ['/dev/tty.usbmodem1411', '9600', '1']

    def get_value(self):
        print(self._serial_read())