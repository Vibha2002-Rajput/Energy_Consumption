from tkinter import *
from PIL import Image, ImageTk, ImageDraw
from datetime import *
import time

class Dashboard:
    def __init__(self, window):
        def sign_out():
            self.window.destroy()
            import signin
            
        self.window = window
        self.window.title("Energy Consumption Forecasting Dashboard")
        self.window.geometry("1155x643+10+10")
        #self.window.state("zoomed")
        self.window.config(background = '#eff5f6')
        #window icon
        icon = ImageTk.PhotoImage(file = "image/icon.ico")
        self.window.iconphoto(True, icon)

        #Header
        self.header = Frame(self.window, bg = '#009df4')
        self.header.place(x = 250, y = 0, width = 1070, height = 50)
        self.logout_text = Button(self.window, text = "Sign Out", bg = "#32cf8e", font = ("", 13,"bold"),
                                  bd = 0, fg = "white", cursor = "hand2", activebackground = "#32cf8e",
                                  command = sign_out)
        self.logout_text.place(x = 1055, y = 8)

        self.graph = Label(self.window, text = "Energy Consumption Forecasting", bg = "#009df4",
                           font = ("Arial Rounded MT Bold", 22, "bold"), fg = "#ffffff")
        self.graph.place(x = 400, y = 6)

        #Sidebar
        self.sidebar = Frame(self.window, bg = "#ffffff")
        self.sidebar.place(x = 0, y = 0, width = 250, height = 643)

        #Body
        self.heading = Label(self.window, text = "Dashboard", font = ("", 13,"bold"), fg = "#0064d3",
                             bg = "#eff5f6")
        self.heading.place(x = 275, y = 60)

        #Body Frame1
        self.bodyframe1 = Frame(self.window, bg = 'powder blue')
        self.bodyframe1.place(x = 276, y = 90, width = 860, height = 535)
        
        #Body Frame2
        self.bodyframe2 = Frame(self.sidebar, bg = '#eff5f6')
        self.bodyframe2.place(x = 20, y = 20, width = 210, height = 603)
        
        #Body Frame3
        #self.bodyframe3 = Frame(self.window, bg = '#e21f26')
        #self.bodyframe3.place(x = 570, y = 380, width = 280, height = 250)
        
        #Body Frame4
        #self.bodyframe4 = Frame(self.window, bg = '#ffcb1f')
        #self.bodyframe4.place(x = 864, y = 380, width = 280, height = 250)

        #date Range
        self.logo = Label(self.sidebar, text = "Date Range", bg = "#eff5f6", font = ("Bahnschrift", 18, "bold"),
                          fg = "#0064d3")
        self.logo.place(x = 65, y = 120)

        self.check1 = IntVar()
        self.checkbox18_19 = Checkbutton(self.sidebar, text = "2018 - 2019",
                                         font = ("Times New Roman", 12), fg = "black", bg = "#eff5f6",
                                         activebackground = "floral white", activeforeground = "white", cursor = "hand2", variable = self.check1)
        self.checkbox18_19.place(x = 40, y = 160)
        
        self.check2 = IntVar()
        self.checkbox19_20 = Checkbutton(self.sidebar, text = "2019 - 2020",
                                         font = ("Times New Roman", 12), fg = "black", bg = "#eff5f6",
                                         activebackground = "floral white", activeforeground = "white", cursor = "hand2", variable = self.check2)
        self.checkbox19_20.place(x = 40, y = 185)
        
        self.check3 = IntVar()
        self.checkbox20_21 = Checkbutton(self.sidebar, text = "2020 - 2021",
                                         font = ("Times New Roman", 12), fg = "black", bg = "#eff5f6",
                                         activebackground = "floral white", activeforeground = "white", cursor = "hand2", variable = self.check3)
        self.checkbox20_21.place(x = 40, y = 210)
        
        self.check4 = IntVar()
        self.checkbox21_22 = Checkbutton(self.sidebar, text = "2021 - 2022",
                                         font = ("Times New Roman", 12), fg = "black", bg = "#eff5f6",
                                         activebackground = "floral white", activeforeground = "white", cursor = "hand2", variable = self.check4)
        self.checkbox21_22.place(x = 40, y = 235)
        
        self.check5 = IntVar()
        self.checkbox18_20 = Checkbutton(self.sidebar, text = "2018 - 2020",
                                         font = ("Times New Roman", 12), fg = "black", bg = "#eff5f6",
                                         activebackground = "floral white", activeforeground = "white", cursor = "hand2", variable = self.check5)
        self.checkbox18_20.place(x = 40, y = 260)
        
        self.check6 = IntVar()
        self.checkbox19_21 = Checkbutton(self.sidebar, text = "2019 - 2021",
                                         font = ("Times New Roman", 12), fg = "black", bg = "#eff5f6",
                                         activebackground = "floral white", activeforeground = "white", cursor = "hand2", variable = self.check6)
        self.checkbox19_21.place(x = 40, y = 285)
        
        self.check7 = IntVar()
        self.checkbox20_22 = Checkbutton(self.sidebar, text = "2020 - 2022",
                                         font = ("Times New Roman", 12), fg = "black", bg = "#eff5f6",
                                         activebackground = "floral white", activeforeground = "white", cursor = "hand2", variable = self.check7)
        self.checkbox20_22.place(x = 40, y = 310)
        
        self.check8 = IntVar()
        self.checkbox18_21 = Checkbutton(self.sidebar, text = "2018 - 2021",
                                         font = ("Times New Roman", 12), fg = "black", bg = "#eff5f6",
                                         activebackground = "floral white", activeforeground = "white", cursor = "hand2", variable = self.check8)
        self.checkbox18_21.place(x = 40, y = 335)
        
        self.check9 = IntVar()
        self.checkbox19_22 = Checkbutton(self.sidebar, text = "2019 - 2022",
                                         font = ("Times New Roman", 12), fg = "black", bg = "#eff5f6",
                                         activebackground = "floral white", activeforeground = "white", cursor = "hand2", variable = self.check9)
        self.checkbox19_22.place(x = 40, y = 360)
        
        self.check10 = IntVar()
        self.checkbox18_22 = Checkbutton(self.sidebar, text = "2018 - 2022",
                                         font = ("Times New Roman", 12), fg = "black", bg = "#eff5f6",
                                         activebackground = "floral white", activeforeground = "white", cursor = "hand2", variable = self.check10)
        self.checkbox18_22.place(x = 40, y = 385)
        
        self.show = Button(self.window, text = "Show", bg = "#32cf8e", font = ("", 13,"bold"),
                                  bd = 0, fg = "white", cursor = "hand2", activebackground = "#32cf8e",
                                  command = sign_out)
        self.show.place(x = 90, y = 430)

def win():
        
    window = Tk()
    Dashboard(window)
    window.mainloop()

if __name__ == '__main__':
    win()
