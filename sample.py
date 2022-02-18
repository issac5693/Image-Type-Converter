
import webbrowser
import tkinter as tk
import ctypes


from PIL import ImageTk, Image

from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage,Label


ctypes.windll.shcore.SetProcessDpiAwareness(2,3)
#creating a window

root = tk.Tk()
root.geometry('1300x850+290+50')
root.title('   ')

canvas = Canvas(
    root,
    height = 1300,
    width = 850)


img = ImageTk.PhotoImage(Image.open('D:\pyexpo\img kwi last 22.jpg'))
panel = tk.Label(root, image = img)
panel.pack(side = "bottom", fill = "both", expand = "yes")

#continue def
def Continue():
    root.destroy()
    import samp
def insta():
    new = 1
    url = 'https://www.instagram.com/cedar_conversions2022/'
    webbrowser.open(url, new=new)
def fb():
    new = 1
    url = 'https://www.facebook.com/cedar.conversions'
    webbrowser.open(url, new=new)
#continue
button_image_0 = ImageTk.PhotoImage(Image.open('D:\pyexpo\continue.jpg'))
button_0 = Button(
    image=button_image_0,
    borderwidth=0,
    highlightthickness=0,
    command=lambda:Continue()
    ,

    relief="flat"
)

button_0.place(
    x=846.4,
    y=414.3,
    width=121,
    height=48
)

#insta
button_image_1= ImageTk.PhotoImage(Image.open('D:\pyexpo\insta.jpg'))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda:insta()
    ,

    relief="flat"
)

button_1.place(
    x=490.7,
    y=599.7,
    width=457,
    height=67
)

#facebook
button_image_4= ImageTk.PhotoImage(Image.open('D:\pyexpo\insta2.jpg'))
button_4 = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=lambda:fb()
    ,

    relief="flat"
)

button_4.place(
    x=490.7,
    y=697.3,
    width=457,
    height=66
)


#click
button_image_3 = ImageTk.PhotoImage(Image.open('D:\pyexpo\click.jpg'))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda:print('he is my every thing')
    ,

    relief="flat"
)

button_3.place(
    x=606.3,
    y=159.2,
    width=91,
    height=26
)


root.mainloop()