#Import modules

import tkinter
import sys
import subprocess

subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'tkcalendar'])
subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'tkintermapview'])

import volunteer_view_family_gui


#Define Functions
#Load Create new emergency
def Edit_Refugee():
    import volunteer_create_family_gui

def View_Refugee():
    volunteer_view_family_gui.table()

def Manage_Refugees():
    pass

#Create main window of the application
refugee_home = tkinter.Tk()
refugee_home.geometry("500x1000")
refugee_home.title("Volunteer Home Page")
refugee_home_label = tkinter.Label(refugee_home, text="Welcome to the volunteer homepage.")
refugee_home_label.pack()

#Add buttons to the window
create_new_refugee_button = tkinter.Button(refugee_home, text="Add Refugee", command=Edit_Refugee)
create_new_refugee_button.place(x = 100, y = 100, width = 300)
update_refugee_button = tkinter.Button(refugee_home, text="View list of refugees in your camp", command=View_Refugee)
update_refugee_button.place(x = 100, y = 300, width = 300)
manage_refugees_button = tkinter.Button(refugee_home, text="Return to home page", command=Manage_Refugees)
manage_refugees_button.place(x = 100, y = 500, width = 300)


refugee_home.mainloop()
