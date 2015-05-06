import serial
from time import sleep
# import sys
# import glob


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
            print('Connection failed to: ' + str(unit[0]))
            raise 
        else:
            if self.connection.isOpen():
                self.connection.flushInput()
                self.connection.flushOutput()
                print('Connection open')
            else:
                print('Serial connection is not open')

    def _serial_write(self, command):
        command += '\r'  # Append to the command so the panel to executes it
        self.connection.flushInput()
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

    # def serial_port_list():
    #     """ Returns a list of available serial ports on a linux or darwin based system
    #     """
    #     if sys.platform.startswith('darwin'):
    #         ports = glob.glob('/dev/tty.*')
    #         platform = 'darwin'
        
    #     elif sys.platform.startswith('linux'):
    #         ports = glob.glob('/dev/tty[A-Za-z]*')
    #         platform = 'linux'

    #     else:
    #         raise EnvironmentError('System not supported')

    #     serial_ports = []
    #     for port in ports:
    #         try:
    #             s = serial.Serial(port)
    #             s.close()
    #             serial_ports.append(port)
    #         except (OSError, serial.SerialException):
    #             pass
    #     return platform, serial_ports
