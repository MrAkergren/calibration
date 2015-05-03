import tkinter as tk 


# For ease of use and readability
N = tk.N
S = tk.S
E = tk.E
W = tk.W

class GUI(tk.Frame):
    """docstring for GUI
    """
    def __init__(self, master=None):
        self.tkRoot = master

        tk.Frame.__init__(self, self.tkRoot)
        self.tkRoot.rowconfigure(0, weight=1)
        self.tkRoot.columnconfigure(0, weight=1)
        self.grid(sticky=(N, S, E, W))
        self.rowconfigure(0, weight=100)
        self.rowconfigure(1, weight=1)
        self.columnconfigure(0, weight=1)
        
        self.control_frame = ControlFrame(self)
        # Initiate frames and start the first frame, the steering controls
        self.control_frame.showFrame()
        
        self.statusLabelText = tk.StringVar()
        self.statusLabelText.set('The calibration testing app \nApplication started')
        self.statusLabel = tk.Label(self, textvariable=self.statusLabelText, height=2)
        self.statusLabel.grid(row=1, column=0, sticky=(E, W))


    def updateStatusbar(self, text):
        self.statusLabelText.set(text)
        print('Serial read:', text)

class ControlFrame(tk.Frame):
    # Constructor
    def __init__(self, master=None):
        self.master = master
        tk.Frame.__init__(self, self.master, bg='black')
        self.setupControlButtons()

    def showFrame(self):
        self.grid(row=0, column=0, sticky=(N, S, E, W))

    # Setup of control buttons
    def setupControlButtons(self):
        self.btnUp = tk.Button(self, text='UP', width=5, height=3)
        self.btnUp.grid(row=0, column=1, pady=5, padx=5, sticky=(E, W))

        self.btnLeft = tk.Button(self, text='LEFT', width=5, height=3)
        self.btnLeft.grid(row=1, column=0, pady=5, padx=5, sticky=(E, W))
        
        self.btnStop = tk.Button(self, text='STOP', width=5, height=3)
        self.btnStop.grid(row=1, column=1, pady=5, padx=5, sticky=(E, W))
        
        self.btnRight = tk.Button(self, text='RIGHT', width=5, height=3)
        self.btnRight.grid(row=1, column=2, pady=10, padx=5, sticky=(E, W))
        
        self.btnDown = tk.Button(self, text='DOWN', width=5, height=3)
        self.btnDown.grid(row=2, column=1, pady=5, padx=5, sticky=(E, W))

     #   self.btnCon = tk.Button(self, text='CONNECT', width=5, \
     #       command=self.master.connectRemote)
     #   self.btnCon.grid(row=3, column=0, pady=30, padx=5, sticky=(E, W))

     #   self.btnCommands = tk.Button(self, text='COMMAND', width=5, \
     #       command=lambda:self.master.switchFrame('launchCommand'))
     #   self.btnCommands.grid(row=3, column=2, pady=30, padx=5, sticky=(E, W))

    # Bind the control buttons to commands
    def bindButtons(self):
        # Lambda function to use for 'run stop' on button release
        stopCommand = lambda x:self.master.runCommand('run stop')

        self.btnUp.bind('<Button-1>', lambda x:self.master.runCommand('run u'))
        self.btnUp.bind('<ButtonRelease-1>', stopCommand)
        self.btnLeft.bind('<Button-1>', lambda x:self.master.runCommand('run l'))
        self.btnLeft.bind('<ButtonRelease-1>', stopCommand)
        self.btnStop.bind('<Button-1>', stopCommand)
        self.btnRight.bind('<Button-1>', lambda x:self.master.runCommand('run r'))
        self.btnRight.bind('<ButtonRelease-1>', stopCommand)
        self.btnDown.bind('<Button-1>', lambda x:self.master.runCommand('run d'))
        self.btnDown.bind('<ButtonRelease-1>', stopCommand)

    # Unbind the commands from the control buttons
    def unbindButtons(self):
        self.btnUp.unbind('<Button-1>')
        self.btnUp.unbind('<ButtonRelease-1>')
        self.btnLeft.unbind('<Button-1>')
        self.btnLeft.unbind('<ButtonRelease-1>')
        self.btnStop.unbind('<Button-1>')
        self.btnRight.unbind('<Button-1>')
        self.btnRight.unbind('<ButtonRelease-1>')
        self.btnDown.unbind('<Button-1>')
        self.btnDown.unbind('<ButtonRelease-1>')

root = tk.Tk()
root.geometry('240x320')
root.wm_title('Solar Panel Remote')
gui_app = GUI(root)

root.mainloop()