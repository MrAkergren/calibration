import sys
import tkinter as tk


class WinCom(tk.Frame):
    def __init__(self, master):
        self.master = master

        tk.Frame.__init__(self, self.master, background="gray")
        self.grid()

        self.panel_label = tk.Label(self, text="Panel COM port:")
        self.panel_label.grid(row=0, column=0, pady=(3, 2), sticky=(tk.E, tk.N, tk.S, tk.W))

        self.panel_port = tk.StringVar()
        self.panel_entry = tk.Entry(self, textvariable=self.panel_port, width=5)
        self.panel_entry.grid(row=0, column=1, pady=(3, 2), padx=5)

        self.ard_label = tk.Label(self, text="Arduino COM port:")
        self.ard_label.grid(row=1, column=0, pady=(1, 3), sticky=(tk.E, tk.N, tk.S, tk.W))

        self.ard_port = tk.StringVar()
        self.ard_entry = tk.Entry(self, textvariable=self.ard_port, width=5)
        self.ard_entry.grid(row=1, column=1, pady=(2, 3), padx=5)

        self.send_button = tk.Button(self, text='OK', width=5, command=self.read_entry)
        self.send_button.grid(row=0, column=2, rowspan=2, pady=(2, 3), padx=(0, 3), sticky=(tk.E, tk.N, tk.S, tk.W))

        self.status_label_text = tk.StringVar()
        self.status_label_text.set('Please enter COM ports for\nserial devices')
        self.status_label = tk.Label(self, textvariable=self.status_label_text, width=28, height=2)
        self.status_label.grid(row=3, column=0, columnspan=3, sticky=(tk.E, tk.W))

    def show_frame(self):
        self.grid(row=0, column=0, sticky=(tk.N, tk.S, tk.E, tk.W))


    def read_entry(self):
        p = self.panel_port.get()
        a = self.ard_port.get()
        if not p.isdigit() or not a.isdigit() or int(p) < 1 or int(p) > 256 or int(a) < 1 or int(a) > 256:
            self.status_label_text.set("Please enter valid COM port numbers")
        else:
            self.master.panel_port = p
            self.master.ard_port = a
            self.master.start_controls()
        print("Panel: " + self.panel_port.get() +"\nArduino: " + self.ard_port.get())
