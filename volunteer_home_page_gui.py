#Import modules
from tkinter import *
import sys
import subprocess
subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'tkcalendar'])
subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'tkintermapview'])
import os
from tkcalendar import Calendar
import datetime

#Define Functions
#Load Create new emergency
def Create_Refugee():
    import volunteer_create_family_gui

def Update_Refugee():
    pass

def Manage_Refugees():
    pass

#Create main window of the application
refugee_home = Tk()
refugee_home.geometry("500x1000")
refugee_home.title("Volunteer Home Page")
refugee_home_label = Label(refugee_home, text="Welcome to the volunteer homepage.")
refugee_home_label.pack()

#Add buttons to the window
create_new_refugee_button = Button(refugee_home, text="Add New Refguee", command=Create_Refugee)
create_new_refugee_button.place(x = 100, y = 100, width = 300)
update_refugee_button = Button(refugee_home, text="Update an Emergency", command=Update_Refugee)
update_refugee_button.place(x = 100, y = 300, width = 300)
manage_refugees_button = Button(refugee_home, text="Manage Volunteers", command=Manage_Refugees)
manage_refugees_button.place(x = 100, y = 500, width = 300)


refugee_home.mainloop()
