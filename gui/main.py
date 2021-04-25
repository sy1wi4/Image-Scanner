import sys
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

sys.path.insert(0, '..')
from app.main import adaptive_mean_thresholding, global_thresholding, otsu_thresholding_filtered

w = 1100
h = 900
image_path = None
size = (300, 480)

window = tk.Tk()
block_size = 7
var = tk.StringVar()


def center_window(width, height):
    screen_w = window.winfo_screenwidth()
    screen_h = window.winfo_screenheight()

    pos_right = screen_w / 2 - width / 2
    pos_down = screen_h / 2 - height / 2

    # .geometry("window width x window height + position right + position down")
    window.geometry("{w}x{h}+{r}+{d}".format(w=width, h=height, r=int(pos_right), d=int(pos_down)))


def set_title():
    title = tk.Label(window, text="Welcome to Image-Scanner", bg='gray13', fg='Azure')
    title.config(font=('helvetica', 35, 'bold'))
    title.place(relx=0.5, rely=0.1, anchor=tk.CENTER)


def add_scan_button():
    text = tk.Label(window, text="...and scan!", bg='gray13', fg='Azure')
    text.config(font=('helvetica', 15, 'bold'))
    text.place(relx=0.75, rely=0.2, anchor=tk.CENTER)

    button_block = tk.Button(window, command=scan_image, text="Scan", height=2, width=16, bg='Azure')
    button_block.place(relx=0.75, rely=0.25, anchor=tk.CENTER)


def show_block_size_value(val):
    global block_size
    block_size = int(val) - 1
    var.set(str(block_size))
    text = tk.Label(window, textvariable=var, bg='gray13', fg='Azure')
    text.config(font=('helvetica', 15, 'bold'))
    text.place(relx=0.55, rely=0.3, anchor=tk.CENTER)
    window.configure(background='gray13')

    # # every time the slider is moved scanned image is updated
    # scan_image()


def add_slider():
    text = tk.Label(window, text="Select block size...", bg='gray13', fg='Azure')
    text.config(font=('helvetica', 15, 'bold'))
    text.place(relx=0.55, rely=0.2, anchor=tk.CENTER)

    # resolution is 2 because block_size must be an odd number
    # THERE IS A BUG IN TKINKER!!! cannot set resolution=2 and get odd numbers
    # - there are only even WTF?!?!
    # so real block_size is 1 unit less
    s = tk.Scale(window, from_=4, to=400, command=show_block_size_value, orient=tk.HORIZONTAL, bg='Azure',
                 length=200, resolution=2, showvalue=0)
    s.place(relx=0.55, rely=0.25, anchor=tk.CENTER)
    print(block_size)


def load_image():
    global image_path
    image_path = filedialog.askopenfilename()
    print(image_path)
    return image_path


# chosen by user or from TkPhoto object
def display_image(img=None, path=None, location='l'):
    if img is None:
        path = load_image()
        load = Image.open(path)
        load = load.resize(size)
        render = ImageTk.PhotoImage(load)
    else:
        render = img

    img = tk.Label(image=render)
    img.image = render
    if location == 'l':
        img.place(relx=0.3, rely=0.7, anchor=tk.CENTER)
        or_title = tk.Label(window, text="Original", bg='gray13', fg='Azure')
        or_title.config(font=('helvetica', 15, 'bold'))
        or_title.place(relx=0.3, rely=0.4, anchor=tk.CENTER)

    else:
        img.place(relx=0.7, rely=0.7, anchor=tk.CENTER)
        sc_title = tk.Label(window, text="Scanned", bg='gray13', fg='Azure')
        sc_title.config(font=('helvetica', 15, 'bold'))
        sc_title.place(relx=0.7, rely=0.4, anchor=tk.CENTER)

    return path


# Convert the Image object into a TkPhoto object
def convert_image(img):
    im = Image.fromarray(img)
    im = im.resize(size)
    imgtk = ImageTk.PhotoImage(image=im)
    return imgtk


def choose_image():
    # original
    display_image()


def scan_image():
    # scanned
    # img = global_thresholding(path)
    # img = otsu_thresholding_filtered(path)
    img = adaptive_mean_thresholding(image_path, block_size)
    im = convert_image(img)
    display_image(img=im, location='r')


if __name__ == '__main__':

    window.title('Image-Scanner')
    center_window(w, h)
    window.configure(background='gray13')

    set_title()

    button_choose = tk.Button(window, command=choose_image, text="Choose an image",
                              height=3, width=20, bg='pink3')
    button_choose.place(relx=0.25, rely=0.25, anchor=tk.CENTER)

    add_slider()
    add_scan_button()

    window.mainloop()
