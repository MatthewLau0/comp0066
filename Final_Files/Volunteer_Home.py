from tkinter import *

import Login
import Volunteer_Create_Family
import Volunteer_View_Family
import Volunteer_Update_Family
import Volunteer_Add_Availability
import Volunteer_Settings

current_refugee_id = ""
current_refugee_name = ""

def camp_id_generate():
    global current_refugee_id
    global current_refugee_name
    logins_file = open("successful_login.txt", "r")

    logins_list = []
    for line in logins_file:
        line_string = line.split("%")
        logins_list.append(line_string)
    if len(logins_list) > 0:
        current_refugee_id = logins_list[-1][0]
        current_refugee_name = logins_list[-1][2]
    else:
        pass
camp_id_generate()

def volunteer_home_page():
    #Define Functions


    open_volunteer_file = open("volunteer_database.txt", 'r')
    volunteer_actual_database_list = []
    for line in open_volunteer_file:
        x = line.split("%")
        volunteer_actual_database_list.append(x)

    #Load Create new emergency
    def Edit_Refugee():
        Volunteer_Create_Family.create_family()


    def modify_refugee():
        Volunteer_Update_Family.modify_family()

    def View_Refugee():
        Volunteer_View_Family.table()

    def Calendly_Refugees():
        Volunteer_Add_Availability.add_calendar()

    def Settings():
        Volunteer_Settings.user_details_generate()
        Volunteer_Settings.run()




    open_volunteer_file = open("volunteer_database.txt", 'r')
    volunteer_actual_database_list = []
    for line in open_volunteer_file:
        x = line.split("%")
        volunteer_actual_database_list.append(x)

    #Create main window of the application
    global refugee_home
    refugee_home = Tk()
    refugee_home.minsize(320,435)
    refugee_home.maxsize(320,435)
    refugee_home.title("Volunteer Home Page")
    refugee_home_label = Label(refugee_home, text="Welcome, %s" %current_refugee_name, height = 2, font = ('Avenir', 20, 'bold', 'underline'))
    refugee_home_label.pack()
    refugee_camp_label = Label(refugee_home, text="You are in camp %s" %current_refugee_id, height = 1, font = ('Avenir', 14))
    refugee_camp_label.pack()

    #Add buttons to the window
    create_new_refugee_button = Button(refugee_home, text="Add Refugee", command=Edit_Refugee, width = 30, height = 2)
    create_new_refugee_button.pack(pady = 10)

    update_refugee_button = Button(refugee_home, text="Modify refugees in your camp", command=modify_refugee, width = 30, height = 2)
    update_refugee_button.pack(pady = 10)

    view_refugee_button = Button(refugee_home, text="View list of refugees in your camp", command=View_Refugee, width = 30, height = 2)
    view_refugee_button.pack(pady = 10)

    change_availability_button = Button(refugee_home, text = "Edit/Manage your availability", command = Calendly_Refugees, width = 30, height = 2)
    change_availability_button.pack(pady = 10)

    manage_details = Button(refugee_home, text="Account Settings", command=Settings, width = 30, height = 2)
    manage_details.pack()

    quit_button = Button(refugee_home, text = 'Log Out', command =lambda: [refugee_home.destroy(), Login.main()], width= 30, height= 2)
    quit_button.pack(pady = 10)

    refugee_home.mainloop()
