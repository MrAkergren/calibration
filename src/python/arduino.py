from serial_com import SerialCommunication
from time import sleep


class Arduino(SerialCommunication):
    """docstring for Arduino
    """
    def __init__(self):
        self.connection = None
        self.EXIT_CONSTANT = 20
        #device = self._serial_device() 
        unit = ['/dev/tty.usbmodem1411', '9600', '1']
        try:
            SerialCommunication.serial_connect(self, unit)
            #print("Connected to lux-meter on \'" + device + "\'")
        except:
            raise


    def _serial_device(self):
        platform, ports = SerialCommunication.serial_port_list()
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
        sleep(0.1)
        while self.connection.inWaiting() > 0:
            text = self._serial_read()
            if(text is not None):
                return int(text)

        if(arg < self.EXIT_CONSTANT):
            return self.get_value(arg+1)
        else:
            return None
