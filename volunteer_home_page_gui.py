#Import modules

from tkinter import *
import sys
import subprocess
import volunteer_create_family_gui

#subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'tkcalendar'])
#subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'tkintermapview'])

import volunteer_view_family_gui
import volunteer_update_family_gui
#import volunteer_add_availability

#Define Functions
#Load Create new emergency
def Edit_Refugee():
    volunteer_create_family_gui.create_family()

def modify_refugee():
    volunteer_update_family_gui.modify_family()

def View_Refugee():
    volunteer_view_family_gui.table()

def Calendly_Refugees():
    volunteer_add_availability.calendly_volunteer()


def Log_out():
    refugee_home.destroy()

#Create main window of the application
refugee_home = Tk()
refugee_home.minsize(320,435)
refugee_home.maxsize(320,435)
refugee_home.title("Volunteer Home Page")
refugee_home_label = Label(refugee_home, text="Welcome, VOLUNTEER", height = 2, font = ('Avenir', 20, 'bold', 'underline'))
refugee_home_label.pack()

#Add buttons to the window
create_new_refugee_button = Button(refugee_home, text="Add Refugee", command=Edit_Refugee, width = 30, height = 2)
create_new_refugee_button.pack(pady = 10)

update_refugee_button = Button(refugee_home, text="Modify refugees in your camp", command=modify_refugee, width = 30, height = 2)
update_refugee_button.pack(pady = 10)

view_refugee_button = Button(refugee_home, text="View list of refugees in your camp", command=View_Refugee, width = 30, height = 2)
view_refugee_button.pack(pady = 10)

change_availability_button = Button(refugee_home, text = "Edit/Manage your availability", command = Calendly_Refugees, width = 30, height = 2)
change_availability_button.pack(pady = 10)

#manage_refugees_button = Button(refugee_home, text="Return to home page", command=Manage_Refugees, width = 30, height = 2)
#manage_refugees_button.pack()

quit_button = Button(refugee_home, text = 'Log Out', command = Log_out, width= 30, height= 2)
quit_button.pack(pady = 10)
refugee_home.mainloop()
