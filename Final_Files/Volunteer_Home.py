from tkinter import *

import Login
import Volunteer_Create_Family
import Volunteer_View_Family
import Volunteer_Update_Family
import Volunteer_Add_Availability


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


    def Log_out():
        refugee_home.destroy()
        Login.main()


    current_refugee_id = 1
    print(current_refugee_id)
    open_volunteer_file = open("volunteer_database.txt", 'r')
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

    change_availability_button = Button(refugee_home, text = "Edit/Manage your availability", command = Calendly_Refugees, width = 30, height = 2)
    change_availability_button.pack(pady = 10)

    #manage_refugees_button = Button(refugee_home, text="Return to home page", command=Manage_Refugees, width = 30, height = 2)
    #manage_refugees_button.pack()

    quit_button = Button(refugee_home, text = 'Log Out', command = Log_out, width= 30, height= 2)
    quit_button.pack(pady = 10)
    refugee_home.mainloop()
