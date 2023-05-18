from tkinter import *
from tkinter import messagebox
from tkinter import PhotoImage
from PIL import ImageTk,Image
import pymysql

def hide():
    openeye.config(file = "image/closeeye.png")
    passwordEntry.config(show="*")
    confirmEntry.config(show="*")
    eyeButton.config(command = show)
    
def show():
    openeye.config(file = "image/openeye.png")
    passwordEntry.config(show="")
    confirmEntry.config(show="")
    eyeButton.config(command = hide)

def login_page():
    signup_window.destroy()
    import signin

def clear():
    emailEntry.delete(0, END)
    userEntry.delete(0, END)
    passwordEntry.delete(0, END)
    confirmEntry.delete(0, END)
    check.set(0)

def connect_database():
    if emailEntry.get() == '' or userEntry.get() == '' or passwordEntry.get() == '' or confirmEntry.get() == '':
        messagebox.showerror('Error', 'All Field are Required')
    elif passwordEntry.get() != confirmEntry.get():
        messagebox.showerror('Error', 'Password Mismatch')
    elif check.get() == 0:
        messagebox.showerror('Error', 'Please Accept Terms and Conditions')
    else:
        try:
            con = pymysql.connect(host = 'localhost' , user = 'root', password = 'shreya@123tc')
            mycursor = con.cursor()
        except:
            messagebox.showerror('Error', 'Database Connectivity Issue, Please Try Again')
            return

        try:
            query = 'create database userdata'
            mycursor.execute(query)
            query = 'use userdata'
            mycursor.execute(query)
            query = 'create table details(id int auto_increment primary key not null, email varchar(50), username varchar(100), password varchar(20))'
            mycursor.execute(query)
        except:
            mycursor.execute('use userdata')
        
        query = 'select * from details where username = %s'
        mycursor.execute(query, (userEntry.get()))

        row = mycursor.fetchone()
        if row != None:
            messagebox.showerror('Error', 'Usename Already Exists')

        else:
            query = 'insert into details(email, username, password) values(%s, %s, %s)'
            mycursor.execute(query, (emailEntry.get(), userEntry.get(), passwordEntry.get()))

            con.commit()
            con.close()
            messagebox.showinfo('Success', 'Registration is Successful')
            clear()
            signup_window.destroy()
            import signin

signup_window = Tk()
signup_window.title("Energy Consumption Forecasting Signup Page")
signup_window.wm_iconbitmap("image/icon.ico")
signup_window.geometry("1168x747+50+90")
signup_window.resizable(False,False)

background = ImageTk.PhotoImage(file = "image/bg.jpg")

bgLabel = Label(signup_window, image = background)
bgLabel.place(x = 0, y = 0)

heading = Label(signup_window, text = "CREATE AN ACCOUNT", bg = "white", 
                font = ("MicrosoftYahei UI Light", 23, "bold"), fg = "purple1")
heading.place(x = 100,y = 130)

# Email
emailLabel = Label(signup_window, text = "Email", bg = "white", font = ("MicrosoftYahei UI Light", 12), 
                      bd = 0, fg = "purple1")
emailLabel.place(x = 120, y = 220)

emailEntry = Entry(signup_window, width = 33, font = ("MicrosoftYahei UI Light", 12), bg = "purple1", 
                     fg = "white")
emailEntry.place(x = 120, y = 250)

# Username
userLabel = Label(signup_window, text = "Username", bg = "white", font = ("MicrosoftYahei UI Light", 12), 
                      bd = 0, fg = "purple1")
userLabel.place(x = 120, y = 300)

userEntry = Entry(signup_window, width = 33, font = ("MicrosoftYahei UI Light", 12), bg = "purple1", 
                     fg = "white")
userEntry.place(x = 120, y = 330)

# Password
passwordLabel = Label(signup_window, text = "Password", bg = "white", font = ("MicrosoftYahei UI Light", 12), 
                      bd = 0, fg = "purple1")
passwordLabel.place(x = 120, y = 380)

passwordEntry = Entry(signup_window, width = 33, font = ("MicrosoftYahei UI Light", 12), bg = "purple1", 
                     fg = "white")
passwordEntry.place(x = 120, y = 410)

# ConformPassword
confirmLabel = Label(signup_window, text = "Conform Password", bg = "white", font = ("MicrosoftYahei UI Light", 12), 
                      bd = 0, fg = "purple1")
confirmLabel.place(x = 120, y = 460)

confirmEntry = Entry(signup_window, width = 33, font = ("MicrosoftYahei UI Light", 12), bg = "purple1", 
                     fg = "white")
confirmEntry.place(x = 120, y = 490)

# eye button
openeye = PhotoImage(file = "image/openeye.png")
eyeButton = Button(signup_window, image = openeye, bd = 0, bg = "white", activebackground = "white", cursor = 'hand2',
                   command = hide)
eyeButton.place(x = 120, y = 520)

eye = Label(signup_window, text = "Show Password", font = ("MicrosoftYahei UI Light", 10), bd = 0, 
                       fg = "purple1", bg = "white")
eye.place(x = 150, y = 520)

# terms and conditions
check = IntVar()
terms_and_conditions = Checkbutton(signup_window, text = "I agree to the Terms & Conditions", 
                                   font = ("MicrosoftYahei UI Light", 10), bg = "white", activebackground = "white", 
                                   fg = "purple1", activeforeground = "purple1", cursor = "hand2", variable = check)
terms_and_conditions.place(x = 120, y = 540)

# signup
signupButton = Button(signup_window, text = "SignUp", font = ("Open Sans", 16, "bold"), bg = "purple1", 
                     fg = "white", bd = 0, activebackground = "purple1", activeforeground = "white", width = 23, command = connect_database)
signupButton.place(x = 120,y = 570)

# signin
alreadyaccount = Label(signup_window, text = "Already have an Account?", font = ("Open Sans", 10, "bold"), 
                       fg = "purple1", bg = "white")
alreadyaccount.place(x = 155, y = 620)

loginButton = Button(signup_window, text = "Log in", font = ("Open Sans", 10, "bold underline"), bg = "white", 
                     fg = "blue", bd = 0, activebackground = "white", activeforeground = "blue", cursor = "hand2", command = login_page)
loginButton.place(x = 325,y = 620)

signup_window.mainloop()
