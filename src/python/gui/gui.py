import tkinter as tk
from gui.win_com import WinCom

# For ease of use and readability
N = tk.N
S = tk.S
E = tk.E
W = tk.W


class GUI(tk.Frame):
    """The root frame for the Graphical User Interface

    Attributes:
        serial_handler (SerialHandler): The class that connects the serial devices
        search (Search):    The search class that executes the search algorithm
        windows (Boolean):  If the app is running on Windows OS, this is true, 
                            default to False.
    """
    def __init__(self, serial_handler, search, windows=False):
        self.search_alg = search
        self.sh = serial_handler
        self.coordinates = None
        self.start_x = None
        self.start_y = None
        self.tkRoot = tk.Tk()

        tk.Frame.__init__(self, self.tkRoot)
        self.tkRoot.geometry('240x320')
        self.tkRoot.wm_title('Parans Panel Calibration')
        self.tkRoot.rowconfigure(0, weight=1)
        self.tkRoot.columnconfigure(0, weight=1)
        self.grid(sticky=(N, S, E, W))
        self.rowconfigure(0, weight=100)
        self.rowconfigure(1, weight=1)
        self.columnconfigure(0, weight=1)

        self.panel_port = None
        self.ard_port = None
        self.win_com = None
        if windows:
            self.win_com = WinCom(self)
            self.win_com.show_frame()
        else:
            self.start_controls()

        self.statusLabelText = tk.StringVar()
        self.statusLabelText.set('The calibration testing app \nApplication started')
        self.statusLabel = tk.Label(self, textvariable=self.statusLabelText, height=2)
        self.statusLabel.grid(row=1, column=0, sticky=(E, W))
        self.tkRoot.mainloop()

    def start_controls(self):
        self.sh.connect_devices(self.panel_port, self.ard_port)        
        self.coordinates = self.sh.get_coordinates()
        self.start_x, self.start_y = self.coordinates

        # Initiate and start the control frame (steering controls)
        if self.win_com is not None:
            print("GUI panel port: " + self.panel_port) #debug
            print("GUI arduino port: " + self.ard_port) #debug
            self.win_com.grid_forget()
        self.control_frame = ControlFrame(self)
        self.control_frame.show_frame()

    def update_statusbar(self, text):
        self.statusLabelText.set(text)
        print('Statusbar text: \n', text.strip())

    def move(self, direction):
        last_x, last_y = self.coordinates
        try:
            self.sh.move(self.coordinates, direction)
            self.coordinates = self.sh.get_coordinates()
            self.update_statusbar("Current coordinates:\n %.4f, %.4f" % self.coordinates)
        except:
            print("Reseting to: %.4f, %.4f" % (last_x, last_y))
            self.sh.set_x_coordinate(str(last_x))
            self.sh.set_y_coordinate(str(last_y))

    def value(self):
        self.update_statusbar(str(self.sh.get_value()))

    def reset(self):
        print("Reseting to start values: %.4f, %.4f " % (self.start_x, self.start_y))
        self.sh.set_coordinates(str(self.start_x), str(self.start_y))
        self.coordinates = self.sh.get_coordinates()
        self.update_statusbar("Current coordinates:\n %.4f, %.4f" % self.coordinates)


class ControlFrame(tk.Frame):
    # Constructor
    def __init__(self, master):
        self.master = master

        tk.Frame.__init__(self, self.master, bg='black')
        self.setup_control_buttons()
        self.bind_buttons()

    def show_frame(self):
        self.grid(row=0, column=0, sticky=(N, S, E, W))

    # Setup of control buttons
    def setup_control_buttons(self):
        self.btnUp = tk.Button(self, text='UP', width=5, height=3)
        self.btnUp.grid(row=0, column=1, pady=5, padx=5, sticky=(E, W))

        self.btnLeft = tk.Button(self, text='LEFT', width=5, height=3)
        self.btnLeft.grid(row=1, column=0, pady=5, padx=5, sticky=(E, W))

        self.btnValue = tk.Button(self, text='VALUE', width=5, height=3)
        self.btnValue.grid(row=1, column=1, pady=5, padx=5, sticky=(E, W))

        self.btnRight = tk.Button(self, text='RIGHT', width=5, height=3)
        self.btnRight.grid(row=1, column=2, pady=10, padx=5, sticky=(E, W))

        self.btnDown = tk.Button(self, text='DOWN', width=5, height=3)
        self.btnDown.grid(row=2, column=1, pady=5, padx=5, sticky=(E, W))

        self.btnSearch = tk.Button(self, text='SEARCH', width=5,)
        self.btnSearch.grid(row=3, column=0, pady=30, padx=2, sticky=(E, W))

        self.btnReset = tk.Button(self, text='RESET', width=5,)
        self.btnReset.grid(row=3, column=2, pady=30, padx=5, sticky=(E, W))

    def bind_buttons(self):
        #  Bind the control buttons to commands
        self.btnUp.bind('<Button-1>', lambda x: self.master.move('NORTH'))

        self.btnDown.bind('<Button-1>', lambda x: self.master.move('SOUTH'))

        self.btnLeft.bind('<Button-1>', lambda x: self.master.move('WEST'))

        self.btnRight.bind('<Button-1>', lambda x: self.master.move('EAST'))

        self.btnValue.bind('<Button-1>', lambda x: self.master.value())

        self.btnSearch.bind('<Button-1>', lambda x: self.master.search_alg.labyrinth())

        self.btnReset.bind('<Button-1>', lambda x: self.master.reset())

    def unbind_buttons(self):
        # Unbind the commands from the control buttons
        self.btnUp.unbind('<Button-1>')
        self.btnLeft.unbind('<Button-1>')
        self.btnValue.unbind('<Button-1>')
        self.btnRight.unbind('<Button-1>')
        self.btnDown.unbind('<Button-1>')
