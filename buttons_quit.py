import tkinter as tk

class BuckysButtons(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        # self.pack(padx = 20, pady = 20)

        frame = tk.Frame(master)
        frame.pack()

        self.printButton = tk.Button(frame, text = "Print Message", command = self.printMessage)
        self.printButton.pack(side = 'left')

        self.quitButton = tk.Button(frame, text = "Quit", command = frame.quit)
        self.quitButton.pack(side = 'left')

    def printMessage(self):
        print("Hello world")


class DoubleButtons(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.pack()

        frame1 = tk.Frame(self)
        frame1.grid(row=0, column=0, columnspan=2)

        BuckysButtons(frame1)

        frame2 = tk.Frame(self)
        frame2.grid(row=1, column=0)

        BuckysButtons(frame2)


# root = tk.Tk()
# d = DoubleButtons(root)
# root.mainloop()
