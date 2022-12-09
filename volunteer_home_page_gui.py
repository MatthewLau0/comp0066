#Import modules

from tkinter import *
import sys
import subprocess
import volunteer_create_family_gui
import LoginPage_v3_Arjun
#subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'tkcalendar'])
#subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'tkintermapview'])

import volunteer_view_family_gui
import volunteer_update_family_gui
#import volunteer_add_availability


def volunteer_home_page():
    #Define Functions


    open_volunteer_file = open("volunteers.txt", 'r')
    volunteer_actual_database_list = []
    for line in open_volunteer_file:
        x = line.split("%")
        volunteer_actual_database_list.append(x)

    #Load Create new emergency
    def Edit_Refugee():
        volunteer_create_family_gui.create_family()

    def modify_refugee():
        volunteer_update_family_gui.modify_family()

    def View_Refugee():
        volunteer_view_family_gui.table()

    #def Calendly_Refugees():
        #volunteer_add_availability.calendly_volunteer()


    def Log_out():
        refugee_home.destroy()


    current_refugee_id = LoginPage_v3_Arjun.haha
    print(current_refugee_id)
    open_volunteer_file = open("volunteers.txt", 'r')
    volunteer_actual_database_list = []
    for line in open_volunteer_file:
        x = line.split("%")
        volunteer_actual_database_list.append(x)

    #Create main window of the application
    refugee_home = Tk()
    refugee_home.minsize(320,435)
    refugee_home.maxsize(320,435)
    refugee_home.title("Volunteer Home Page")
    refugee_home_label = Label(refugee_home, text="Welcome, %s" %volunteer_actual_database_list[current_refugee_id-1][2], height = 2, font = ('Avenir', 20, 'bold', 'underline'))
    refugee_home_label.pack()
    refugee_camp_label = Label(refugee_home, text="You are in camp %s" %volunteer_actual_database_list[current_refugee_id-1][1], height = 1, font = ('Avenir', 14))
    refugee_camp_label.pack()

    #Add buttons to the window
    create_new_refugee_button = Button(refugee_home, text="Add Refugee", command=Edit_Refugee, width = 30, height = 2)
    create_new_refugee_button.pack(pady = 10)

    update_refugee_button = Button(refugee_home, text="Modify refugees in your camp", command=modify_refugee, width = 30, height = 2)
    update_refugee_button.pack(pady = 10)

    view_refugee_button = Button(refugee_home, text="View list of refugees in your camp", command=View_Refugee, width = 30, height = 2)
    view_refugee_button.pack(pady = 10)

    #change_availability_button = Button(refugee_home, text = "Edit/Manage your availability", command = Calendly_Refugees, width = 30, height = 2)
    #change_availability_button.pack(pady = 10)

    #manage_refugees_button = Button(refugee_home, text="Return to home page", command=Manage_Refugees, width = 30, height = 2)
    #manage_refugees_button.pack()

    quit_button = Button(refugee_home, text = 'Log Out', command = Log_out, width= 30, height= 2)
    quit_button.pack(pady = 10)
    refugee_home.mainloop()
