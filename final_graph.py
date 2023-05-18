from tkinter import *
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from tkinter import ttk
from tkinter import messagebox
from tkinter import PhotoImage
from PIL import ImageTk,Image

pd.set_option('display.max_rows', None)
pd.set_option('display.min_rows', None)

energy = pd.read_csv("Monthly Electricity Consumption.csv")

energy['Coal, Peat and Manufactured Gases']. fillna(energy['Coal, Peat and Manufactured Gases'].mean(), inplace=True)
energy['Oil and Petroleum Products']. fillna(energy['Oil and Petroleum Products'].mean(), inplace=True)
energy['Natural Gas']. fillna(energy['Natural Gas'].mean(), inplace=True)
energy['Total Renewables (Geo, Solar, Wind, Other)'].fillna(energy['Total Renewables (Geo, Solar, Wind, Other)'].mean(),inplace=True)

Jan18_Dec18 = energy[(energy['Country'] == "India") & (energy['Date'] >= "2018-01")]
Jan18_Dec18.plot(x="Date", y="Electricity", figsize = (16,12))
plt.xlabel("Date",  size = 20)
plt.ylabel("Electricity", size = 20)
plt.title("Electricity used in India", size = 25)
'''
def sign_out():
    finalgraph_window.destroy()
    import signin

finalgraph_window = Tk()
finalgraph_window.title('Energy Consumption Forecasting')
finalgraph_window.wm_iconbitmap("icon.ico")
finalgraph_window.configure(bg='#525561')
finalgraph_window.geometry('1150x643+10+10')

#graph = Frame(window, bg = "orange")
#graph.place(x = 700, y = 100)

signout = Button(finalgraph_window, text = "Sign Out", font = ("Open Sans", 14), bg = "white", fg = "red",
              bd = 0, activebackground = "white", activeforeground = "red", command = sign_out)
signout.place(x = 1055, y = 10)

finalgraph_window.mainloop()
'''
