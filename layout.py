import tkinter as tk

from img_show import ImgShow

class TwoPicLayout(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.master = master
        self.pack()

        img_path = 'images/1.jpg'
        w = 400
        h = 400

        frame1 = tk.Frame(self)
        frame1.pack(side = 'left')

        ImgShow(frame1, img_path, w, h)

        frame2 = tk.Frame(self)
        frame2.pack(side = 'right')

        ImgShow(frame2, img_path, w, h)


root = tk.Tk()
app = TwoPicLayout(root)
root.mainloop()

