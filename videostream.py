import cv2
from PIL import Image
from PIL import ImageTk
import tkinter

class VideoStream:
    root = None
    panel = None
    camera = None

    def __init__(self):
        self.root = tkinter.Tk()
        self.root.title('videa stream')
        self.root.geometry('400x400')
        # self.destructor function gets fired when the window is closed
        self.root.protocol('WM_DELETE_WINDOW', self.destructor)
        # make Esc exit the program
        self.root.bind('<Escape>', lambda e: self.destructor())
        # initialise panel
        self.panel = tkinter.Label()
        self.panel.pack()
        # initialise camera
        self.camera = cv2.VideoCapture(0)
        self.cameraToPanel()
        self.root.mainloop()

    def cameraToPanel(self):
        _, img = self.camera.read()
        img = cv2.resize(img, (400, 400) )
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        # print(img.shape)
        img = Image.fromarray(img)
        img = ImageTk.PhotoImage(img)
        self.panel.configure(image=img)
        self.panel.image = img
        self.panel.after(1, self.cameraToPanel)

    def destructor(self):
        """ Destroy the root object and release all resources """
        print("[INFO] closing...")
        self.root.destroy()
        self.camera.release()  # release web camera
        cv2.destroyAllWindows()  # it is not mandatory in this application



if __name__ == '__main__':
    objVideo = VideoStream()