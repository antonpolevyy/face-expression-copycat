from PIL import Image, ImageTk
import tkinter as tk

class ImgShow(tk.Frame):
    def __init__(self, master, img_path, width = None, height = None):
        tk.Frame.__init__(self, master)
        self.master = master
        self.pack(fill=tk.BOTH, expand=1)
        # load image from img_path
        load = Image.open(img_path)
        # get width & height of the image
        if width is not None and height is not None:
            load = load.resize((width, height))
        width, height = load.size
        # set width & height of the frame
        frame = tk.Frame(master, height=height, width=width)
        frame.pack()
        # display image
        render = ImageTk.PhotoImage(load)
        img = tk.Label(self, image=render)
        img = tk.Label(frame, image=render)
        img.image = render
        img.place(x=0, y=0)

        
# img_path = 'images/1.jpg'
# frame_width = 400
# frame_height = 400

# root = tk.Tk()
# # app = ImgShow(root, img_path)
# app = ImgShow(root, img_path, 400, 300)
# root.wm_title("Tkinter window")
# # root.geometry("400x300")
# root.mainloop()