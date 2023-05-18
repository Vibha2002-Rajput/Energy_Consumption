from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import PhotoImage
from PIL import ImageTk,Image

def sign_out():
    welcome_window.destroy()
    import signin

def next_page():
    welcome_window.destroy()
    import main

welcome_window = Tk()
welcome_window.title('Energy Consumption Forecasting')
welcome_window.wm_iconbitmap("image/icon.ico")
welcome_window.geometry('1500x770+10+10')

background = ImageTk.PhotoImage(file = "image/bg1.jpg")

bgLabel = Label(welcome_window, image = background)
bgLabel.place(x = 0, y = 0)

wc = Label(welcome_window, text = "Welcome to \nEnergy Consumption Forecasting", bg = "black",
               font = ("Edwardian Script ITC", 45, "bold"), fg = "white", borderwidth = 0, relief = 'solid')
wc.place(x = 320, y = 350)

Next = Button(welcome_window, text = "Next-->>", font = ("Open Sans", 16, "bold"), bg = "gold", fg = "black",
              bd = 1, activebackground = "gold", activeforeground = "black", command = next_page)
Next.place(x = 1340, y = 520)

signout = Button(welcome_window, text = "Sign Out", font = ("Open Sans", 14), bg = "white", fg = "red",
              bd = 0, activebackground = "white", activeforeground = "red", command = sign_out)
signout.place(x = 1410, y = 10)

welcome_window.mainloop()
