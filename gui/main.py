import sys
import tkinter as tk
from tkinter import filedialog

import PIL
import cv2 as cv
from PIL import Image, ImageTk

sys.path.insert(0, '..')  # to import from different dir
from app.main import adaptive_gaussian_thresholding
from app.otsu_binarization import binarization

WIDTH = 1100
HEIGHT = 900
SIZE = (300, 480)
START_BLOCK_SIZE = 7

class GUI:
    def __init__(self, win, b_size):
        self.window = win
        self.image_path = None
        self.block_size = b_size
        self.title = None
        self.var_block_size = tk.StringVar()
        self.var_block_size.set(str(START_BLOCK_SIZE))
        self.var_method = tk.StringVar()
        self.var_method.set("adaptive")  # default - adaptive method
        self.scan_arr = None
        self.button_choose = tk.Button(self.window, command=self.choose_image, text="Choose an image",
                                       height=3, width=20, bg='pink3')
        self.radio_group = tk.LabelFrame(self.window, text="  METHOD  ", bg='Azure')
        self.otsu_method = tk.Radiobutton(self.radio_group, text="otsu      ", variable=self.var_method,
                                          value="otsu", bg='Azure')
        self.adaptive_method = tk.Radiobutton(self.radio_group, text="adaptive", variable=self.var_method,
                                              value="adaptive", bg='Azure')
        self.window.title('Image-Scanner')
        self.center_window(WIDTH, HEIGHT)
        self.window.configure(background='gray13')
        self.set_title()
        self.button_choose.place(relx=0.25, rely=0.2, anchor=tk.CENTER)
        self.radio_group.place(relx=0.25, rely=0.3, anchor=tk.CENTER)
        self.otsu_method.pack()
        self.adaptive_method.pack()
        self.add_slider()
        self.add_scan_button()
        self.add_save_button()

    def center_window(self, width, height):
        screen_w = self.window.winfo_screenwidth()
        screen_h = self.window.winfo_screenheight()

        pos_right = screen_w / 2 - width / 2
        pos_down = screen_h / 2 - height / 2

        # .geometry("window width x window height + position right + position down")
        self.window.geometry("{w}x{h}+{r}+{d}".format(w=width, h=height, r=int(pos_right), d=int(pos_down)))

    def set_title(self):
        self.title = tk.Label(self.window, text="Welcome to Image-Scanner", bg='gray13', fg='Azure')
        self.title.config(font=('helvetica', 35, 'bold'))
        self.title.place(relx=0.5, rely=0.1, anchor=tk.CENTER)

    def add_scan_button(self):
        text = tk.Label(self.window, text="...and scan!", bg='gray13', fg='Azure')
        text.config(font=('helvetica', 15, 'bold'))
        text.place(relx=0.7, rely=0.2, anchor=tk.CENTER)

        button_block = tk.Button(self.window, command=self.scan_image, text="Scan", height=2, width=16, bg='Azure')
        button_block.place(relx=0.7, rely=0.25, anchor=tk.CENTER)

    def add_save_button(self):
        text = tk.Label(self.window, text="Save as file", bg='gray13', fg='Azure')
        text.config(font=('helvetica', 15, 'bold'))
        text.place(relx=0.9, rely=0.2, anchor=tk.CENTER)

        button_block = tk.Button(self.window, command=self.save_to_file, text="Save", height=2, width=16, bg='Azure')
        button_block.place(relx=0.9, rely=0.25, anchor=tk.CENTER)

    def show_block_size_value(self, val):
        self.block_size = int(val) - 1
        self.var_block_size.set(str(self.block_size))

        text = tk.Label(self.window, textvariable=self.var_block_size, bg='gray13', fg='Azure')
        text.config(font=('helvetica', 15, 'bold'))
        text.place(relx=0.5, rely=0.3, anchor=tk.CENTER)
        self.window.configure(background='gray13')

        # every time the slider is moved scanned image is updated

    def add_slider(self):
        text = tk.Label(self.window, text="Select block size...", bg='gray13', fg='Azure')
        text.config(font=('helvetica', 15, 'bold'))
        text.place(relx=0.5, rely=0.2, anchor=tk.CENTER)

        # resolution is 2 because block_size must be an odd number
        # THERE IS A BUG IN TKINKER!!! cannot set resolution=2 and get odd numbers
        # - there are only even WTF?!?!
        # so real block_size is 1 unit less
        s = tk.Scale(self.window, from_=4, to=200, command=self.show_block_size_value, orient=tk.HORIZONTAL, bg='Azure',
                     length=200, resolution=2, showvalue=0)
        s.place(relx=0.5, rely=0.25, anchor=tk.CENTER)
        # default value
        self.show_block_size_value(self.block_size + 1)

    def load_image(self):
        self.image_path = filedialog.askopenfilename()
        return self.image_path

    def save_to_file(self):
        if self.scan_arr is None:
            print("No image scanned!")
            return

        filename = filedialog.asksaveasfile(mode='w', defaultextension=".jpg")

        if not filename:
            return

        Image.fromarray(self.scan_arr).save(filename)

    # chosen by user or from TkPhoto object
    def display_image(self, img=None, path=None, location='l'):

        if img is None:
            path = self.load_image()

            try:
                load = Image.open(path)
                load = load.resize(SIZE)
                render = ImageTk.PhotoImage(load)
            except AttributeError:
                print("Load image!")
                return
            except PIL.UnidentifiedImageError:
                print("Loaded file is not an image!")
                return

        else:
            render = img

        img = tk.Label(image=render)
        img.image = render

        if location == 'l':
            x = 0.3
            text = "Original"
        else:
            x = 0.7
            text = "Scanned"

        img.place(relx=x, rely=0.7, anchor=tk.CENTER)
        or_title = tk.Label(window, text=text, bg='gray13', fg='Azure')
        or_title.config(font=('helvetica', 15, 'bold'))
        or_title.place(relx=x, rely=0.4, anchor=tk.CENTER)

        return path

    def scan_image(self):
        # scanned
        try:
            if self.var_method.get() == "otsu":
                img = binarization(self.image_path, self.block_size)[1]
            else:
                img = adaptive_gaussian_thresholding(self.image_path, self.block_size)
            self.scan_arr = img
            im = convert_image(img)
            self.display_image(img=im, location='r')
        except cv.error as e:
            print("Load file of proper format!")
            print(e)

    def choose_image(self):
        # original
        self.display_image()


# Convert the Image object into a TkPhoto object
def convert_image(img):
    im = Image.fromarray(img)
    im = im.resize(SIZE)
    imgtk = ImageTk.PhotoImage(image=im)
    return imgtk


if __name__ == '__main__':
    window = tk.Tk()
    gui = GUI(window, START_BLOCK_SIZE)
    window.mainloop()
