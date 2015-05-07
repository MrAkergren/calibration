import tkinter as tk

# For ease of use and readability
N = tk.N
S = tk.S
E = tk.E
W = tk.W


class GUI(tk.Frame):
    """docstring for GUI
    """
    def __init__(self, serial_handler, search, master=None):
        self.search_alg = search
        self.sh = serial_handler
        self.coordinates = self.sh.get_coordinates()
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

        # Initiate frames and start the first frame, the steering controls
        self.control_frame = ControlFrame(self)
        self.control_frame.show_frame()

        self.statusLabelText = tk.StringVar()
        self.statusLabelText.set('The calibration testing app \nApplication started')
        self.statusLabel = tk.Label(self, textvariable=self.statusLabelText, height=2)
        self.statusLabel.grid(row=1, column=0, sticky=(E, W))
        self.tkRoot.mainloop()

    def update_statusbar(self, text):
        self.statusLabelText.set(str(text))
        print('Statusbar text: \n', str(text).strip())

    def move(self, direction):
        try:
            self.sh.move(self.coordinates, direction)
            self.coordinates = self.sh.get_coordinates()
            self.update_statusbar("Current coordinates:\n %.4f, %.4f" % self.coordinates)
        except:
            print("Sun sensor not active")

    def value(self):
        self.update_statusbar(str(self.sh.get_value()))


class ControlFrame(tk.Frame):
    # Constructor
    def __init__(self, master=None):
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

        self.vluBtn = tk.Button(self, text='VALUE', width=5, height=3)
        self.vluBtn.grid(row=1, column=1, pady=5, padx=5, sticky=(E, W))

        self.btnRight = tk.Button(self, text='RIGHT', width=5, height=3)
        self.btnRight.grid(row=1, column=2, pady=10, padx=5, sticky=(E, W))

        self.btnDown = tk.Button(self, text='DOWN', width=5, height=3)
        self.btnDown.grid(row=2, column=1, pady=5, padx=5, sticky=(E, W))

        self.btnSearch = tk.Button(self, text='SEARCH', width=5,)
        self.btnSearch.grid(row=3, column=1, pady=30, padx=2, sticky=(E, W))

        #   self.btnCommands = tk.Button(self, text='COMMAND', width=5, \
        #       command=lambda:self.master.switchFrame('launchCommand'))
        #   self.btnCommands.grid(row=3, column=2, pady=30, padx=5, sticky=(E, W))

    def bind_buttons(self):
        #  Bind the control buttons to commands
        self.btnUp.bind('<Button-1>', lambda x: self.master.move('NORTH'))

        self.btnDown.bind('<Button-1>', lambda x: self.master.move('SOUTH'))

        self.btnLeft.bind('<Button-1>', lambda x: self.master.move('WEST'))

        self.btnRight.bind('<Button-1>', lambda x: self.master.move('EAST'))

        self.vluBtn.bind('<Button-1>', lambda x: print(self.master.value()))

        self.btnSearch.bind('<Button-1>', lambda x: self.master.search_alg.labyrinth())

    def unbind_buttons(self):
        # Unbind the commands from the control buttons
        self.btnUp.unbind('<Button-1>')
        self.btnLeft.unbind('<Button-1>')
        self.vluBtn.unbind('<Button-1>')
        self.btnRight.unbind('<Button-1>')
        self.btnDown.unbind('<Button-1>')
