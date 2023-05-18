from tkinter import *
from tkinter import messagebox
from tkinter import PhotoImage
from PIL import ImageTk,Image
import pymysql

# Funtionality part
def signin_user():
    if usernameEntry.get() == '' or passwordEntry.get() == '':
        messagebox.showerror('Error', 'All Fields are Required')
    else:
        try:
            con = pymysql.connect(host = 'localhost' , user = 'root', password = 'shreya@123tc')
            mycursor = con.cursor()
        except:
            messagebox.showerror('Error', 'Connection is not established Try Again')
            return

        query = 'use userdata'
        mycursor.execute(query)
        query = 'select * from details where username = %s and password = %s'
        mycursor.execute(query, (usernameEntry.get(), passwordEntry.get()))
        row = mycursor.fetchone()
        if row == None:
            messagebox.showerror('Error', 'Invalid Username or Password')
        else:
            messagebox.showinfo('Success', 'Login is Successful')
            signin_window.destroy()
            import welcome

def user_enter(e):
    if usernameEntry.get() == "Username":
        usernameEntry.delete(0,'end')

def password_enter(e):
    if passwordEntry.get() == "Password":
        passwordEntry.delete(0,'end')

def hide():
    openeye.config(file = "image/closeeye.png")
    passwordEntry.config(show="*")
    eyeButton.config(command = show)
    
def show():
    openeye.config(file = "image/openeye.png")
    passwordEntry.config(show="")
    eyeButton.config(command = hide)

def forget_pass():
    # Funtionality part
    def hide1():
        openeye.config(file = "image/closeeye.png")
        newpass_Entry.config(show = "*")
        confrimpass_Entry.config(show = "*")
        eye_Button.config(command = show1)
    
    def show1():
        openeye.config(file = "image/openeye.png")
        newpass_Entry.config(show = "")
        confrimpass_Entry.config(show = "")
        eye_Button.config(command = hide1)
        
    def change_password():
        if user_Entry.get() == '' or newpass_Entry.get() == '' or confrimpass_Entry.get() == '':
            messagebox.showerror('Error', 'All Feilds are Required', parent = window)
        elif newpass_Entry.get() != confrimpass_Entry.get():
            messagebox.showerror('Error', 'Password and Confirm Password are not matching', parent = window)
        else:
            con = pymysql.connect(host = 'localhost' , user = 'root', password = '', database = 'userdata')
            mycursor = con.cursor()
            query = 'select * from details where username = %s'
            mycursor.execute(query, (user_Entry.get()))
            row = mycursor.fetchone()
            if row == None:
                messagebox.showerror('Error', 'Incorrect Username', parent = window)
            else:
                query = 'update details set password = %s where username = %s'
                mycursor.execute(query, (newpass_Entry.get(), user_Entry.get()))
                con.commit()
                con.close()
                messagebox.showinfo('Success', 'Password is reset Successfully, please login in with new password', parent = window)
                window.destroy()
                
    # Forget Password GUI
    window = Toplevel()
    window.title('Change Password')
    window.geometry("790x512+10+10")
    window.resizable(False,False)

    bgPic = ImageTk.PhotoImage(file = "image/background.jpg")
    bglabel = Label(window, image = bgPic)
    bglabel.grid()

    heading = Label(window, text = "RESET PASSWORD", bg = "white", font = ("arial", 18, "bold"), fg = "DodgerBlue4")
    heading.place(x = 70,y = 70)
    
    # User entry 
    userLabel = Label(window, text = "Username", bg = "white", font = ("arial", 11), 
                      bd = 0, fg = "DodgerBlue3")
    userLabel.place(x = 50, y = 130)
    
    user_Entry = Entry(window, bg = "white", font = ("arial", 11), width = 25, 
                      bd = 0, fg = "DodgerBlue3")
    user_Entry.place(x = 50, y = 160)
    frame1 = Frame(window, width = 250, height = 2, bg = "DodgerBlue3").place(x = 50, y = 180)
    
    # New Password
    passwordLabel = Label(window, text = "New Password", bg = "white", font = ("arial", 11), 
                      bd = 0, fg = "DodgerBlue3")
    passwordLabel.place(x = 50, y = 210)
    
    newpass_Entry = Entry(window, bg = "white", font = ("arial", 11), width = 25, 
                      bd = 0, fg = "DodgerBlue3")
    newpass_Entry.place(x = 50, y = 240)
    Frame(window, width = 250, height = 2, bg = "DodgerBlue3").place(x = 50, y = 260)
    
    # Confrim Password
    confrimpassLabel = Label(window, text = "Confrim Password", bg = "white", font = ("arial", 11), 
                      bd = 0, fg = "DodgerBlue3")
    confrimpassLabel.place(x = 50, y = 290)
    
    confrimpass_Entry = Entry(window, bg = "white", font = ("arial", 11), width = 25, 
                      bd = 0, fg = "DodgerBlue3")
    confrimpass_Entry.place(x = 50, y = 320)
    Frame(window, width = 250, height = 2, bg = "DodgerBlue3").place(x = 50, y = 340)
    
    # eye
    openeye = PhotoImage(file = "image/openeye.png")
    eye_Button = Button(window, image = openeye, bd = 0, bg = "white", activebackground = "white", cursor = 'hand2', command = hide1)
    eye_Button.place(x = 50, y = 360)
    
    eye = Label(window, text = "Show Password", font = ("arial", 10), bd = 0, fg = "DodgerBlue3", bg = "white")
    eye.place(x = 80, y = 360)
    
    # Submit
    submitButton = Button(window, text = "Submit", font = ("Open Sans", 16, "bold"), bg = "DodgerBlue3", 
                     fg = "white", bd = 0, activebackground = "DodgerBlue3", activeforeground = "white", width = 19, cursor = 'hand2', command = change_password)
    submitButton.place(x = 50,y = 400)
    
    window.mainloop()

def signup_page():
    signin_window.destroy()
    import signup
    
# GUI
signin_window = Tk()
signin_window.title("Energy Consumption Forecasting Login Page")
signin_window.wm_iconbitmap("image/icon.ico")
signin_window.geometry("1168x747+10+10")
signin_window.resizable(False,False)

bgImage = ImageTk.PhotoImage(file = "image/bg.jpg")

bgLabel = Label(signin_window, image = bgImage)
bgLabel.place(x = 0, y = 0)

heading = Label(signin_window, text = "LOGIN", bg = "white", font = ("MicrosoftYahei UI Light", 23, "bold"), fg = "purple1")
heading.place(x = 230,y = 150)

# Username
usernameEntry = Entry(signin_window, bg = "white", font = ("MicrosoftYahei UI Light", 12), width = 30, 
                      bd = 0, fg = "purple1")
usernameEntry.place(x = 130, y = 240)
usernameEntry.insert(0,"Username")
usernameEntry.bind("<FocusIn>", user_enter)
frame1 = Frame(signin_window, width = 300,height = 2, bg = "black")
frame1.place(x= 130, y = 270)

# Password
passwordEntry = Entry(signin_window, bg = "white", font = ("MicrosoftYahei UI Light", 12), width = 30, 
                      bd = 0, fg = "purple1")
passwordEntry.place(x = 130, y = 320)
passwordEntry.insert(0,"Password")
passwordEntry.bind("<FocusIn>", password_enter)
frame2 = Frame(signin_window, width = 300,height = 2, bg = "black")
frame2.place(x= 130, y = 350)

# eye
openeye = PhotoImage(file = "image/openeye.png")
eyeButton = Button(signin_window, image = openeye, bd = 0, bg = "white", activebackground = "white", cursor = 'hand2',
                   command = hide)
eyeButton.place(x = 390, y = 320)

# Forget Password
forgetButton = Button(signin_window, text = "Forget Password?", bd = 0, font = ("Open Sans", 10), bg = "white",
                      activebackground = "white", cursor = 'hand2', fg = "purple1", activeforeground = "purple1", command = forget_pass)
forgetButton.place(x = 325, y = 360)

# Login
loginButton = Button(signin_window, text = "Login", font = ("Open Sans", 16, "bold"), bg = "purple1", 
                     fg = "white", bd = 0, activebackground = "purple1", activeforeground = "white", width = 23, command = signin_user)
loginButton.place(x = 130,y = 410)

orLabel = Label(signin_window, text = "------------------ OR ------------------", font = ("Open Sans", 16), 
                fg = "purple1", bg = "white")
orLabel.place(x = 130, y = 460)

facebook_logo = PhotoImage(file = "image/facebook.png")
fbLabel = Label(signin_window, image = facebook_logo, bg = "white")
fbLabel.place(x = 170, y = 510)

google_logo = PhotoImage(file = "image/google.png")
googleLabel = Label(signin_window, image = google_logo, bg = "white")
googleLabel.place(x = 260, y = 510)

twitter_logo = PhotoImage(file = "image/twitter.png")
twitterLabel = Label(signin_window, image = twitter_logo, bg = "white")
twitterLabel.place(x = 350, y = 510)

signupLabel = Label(signin_window, text = "Don't have an account?", font = ("Open Sans", 10, "bold"), fg = "purple1",
                    bg = "white")
signupLabel.place(x = 150, y = 570)

newaccountButton = Button(signin_window, text = "Create New Account", font = ("Open Sans", 10, "bold underline"), bg = "white", 
                     fg = "blue", bd = 0, activebackground = "white", activeforeground = "blue", cursor = "hand2", 
                          command = signup_page)
newaccountButton.place(x = 305,y = 570)

signin_window.mainloop()
