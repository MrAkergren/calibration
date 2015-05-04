import serial
from time import sleep


class SerialCommunication(object):
    """docstring for Serial
    """

    def __init__(self):
        self.connection = None

    def serial_connect(self, unit):
        """The method to handle the connection to the panel.
        """
        try:
            if self.connection is not None:
                self.connection.close()
            self.connection = serial.Serial(str(unit[0]),int(unit[1]), timeout=int(unit[2]))
            sleep(1)
        except serial.SerialException:
            print('Connection failed')
           # raise 
        else:
            if self.connection.isOpen():
                self.connection.flushInput()
                self.connection.flushOutput()
                print("Connection open")
            else:
                print('Serial connection is not open')

    def _serial_write(self, command):
        command += '\r'  # Append to the command so the panel to executes it
        try:
            if self.connection.write(command.encode('utf-8')) > 0:
                pass
            else:
                print('Serial write failed')

        except serial.SerialTimeoutException:
            print('Timeout on serial write')

        except serial.SerialException:
            print('Serial communication failed')

    def _serial_read(self):
            # To decode the information from the panel to a utf-8 string

            text = self.connection.readline()
            text = text.decode(encoding='utf-8')
            return text
