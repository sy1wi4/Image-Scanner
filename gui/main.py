import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

w = 800
h = 800
image_path = None

window = tk.Tk()


def center_window(width, height):
    screen_w = window.winfo_screenwidth()
    screen_h = window.winfo_screenheight()

    pos_right = screen_w/2 - width/2
    pos_down = screen_h/2 - height/2

    # .geometry("window width x window height + position right + position down")
    window.geometry("{w}x{h}+{r}+{d}".format(w=width, h=height, r=int(pos_right), d=int(pos_down)))


def display_image(path):
    load = Image.open(path)
    load = load.resize((200, 320))
    render = ImageTk.PhotoImage(load)
    img = tk.Label(image=render)
    img.image = render
    img.place(relx=0.3, rely=0.7, anchor=tk.CENTER)


def load_image():
    global image_path
    image_path = filedialog.askopenfilename()
    print(image_path)
    return image_path


window.title('Image-Scanner')
center_window(w, h)
window.configure(background='gray13')


title = tk.Label(window, text="Welcome to Image-Scanner", bg='gray13', fg='Azure')
title.config(font=('helvetica', 35, 'bold'))
title.place(relx=0.5, rely=0.2, anchor=tk.CENTER)

button = tk.Button(window, command=load_image, text="Choose an image", height=3, width=20, bg='Azure')
button.place(relx=0.5, rely=0.4, anchor=tk.CENTER)


# TODO: how to display loaded image ???


window.mainloop()
