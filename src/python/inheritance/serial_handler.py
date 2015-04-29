from panel import Panel
from arduino import Arduino


class SerialHandler(object):
    """docstring for SerialHandler"""
    def __init__(self, arg):
        super(SerialHandler, self).__init__()
        self.arg = arg
        
        self.ard = Arduino()
        self.pan = Panel(0.01, 0.01)

sh = SerialHandler()