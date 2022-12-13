from tkinter import *
from tkinter import ttk


def manageVolunteers(screen):
    global admin_home_screen
    admin_home_screen = screen

    def viewexistingvolunteersSetUp():
        global current_volunteer_list
        global manage_volunteer_home_screen


        volunteer_file = open("volunteer_database.txt", "r")

        current_volunteer_list = []
        for line in volunteer_file:
            line_list = line.split("%")
            current_volunteer_list.append(line_list)
        volunteer_file.close()
        viewexistingVolunteers()

    def viewexistingVolunteers():
        global manage_volunteer_home_screen
        global current_volunteer_list


        view_volunteers_screen_label = Label(manage_volunteer_home_screen, text="Please see below a list of the current volunteers and the camps they are associated with.")
        view_volunteers_screen_label.pack()

        view_volunteer_frame = Frame(manage_volunteer_home_screen)
        view_volunteer_frame.pack()

        view_volunteer_table = ttk.Treeview(manage_volunteer_home_screen)

        view_volunteer_table['columns'] = ("Camp ID", "Volunteer ID", "Full Name", "Email", "Phone Number", "Gender", "Date of Birth", "Age", "Activation Status", "Volunteer Classification")

        view_volunteer_table.column("#0", width=0, stretch=NO)
        view_volunteer_table.column("Camp ID", anchor=CENTER, width=100)
        view_volunteer_table.column("Volunteer ID", anchor=CENTER, width=100)
        view_volunteer_table.column("Full Name", anchor=CENTER, width=100)
        view_volunteer_table.column("Email", anchor=CENTER, width=100)
        view_volunteer_table.column("Phone Number", anchor=CENTER, width=100)
        view_volunteer_table.column("Gender", anchor=CENTER, width=100)
        view_volunteer_table.column("Date of Birth", anchor=CENTER, width=100)
        view_volunteer_table.column("Age", anchor=CENTER, width=100)
        view_volunteer_table.column("Activation Status", anchor=CENTER, width=100)
        view_volunteer_table.column("Volunteer Classification", anchor=CENTER, width=100)

        view_volunteer_table.heading("Camp ID", text="Camp ID", anchor=CENTER)
        view_volunteer_table.heading("Volunteer ID", text="Volunteer ID", anchor=CENTER)
        view_volunteer_table.heading("Full Name", text="Full Name", anchor=CENTER)
        view_volunteer_table.heading("Email", text="Email", anchor=CENTER)
        view_volunteer_table.heading("Phone Number", text="Phone Number", anchor=CENTER)
        view_volunteer_table.heading("Gender", text="Gender", anchor=CENTER)
        view_volunteer_table.heading("Date of Birth", text="Date of Birth", anchor=CENTER)
        view_volunteer_table.heading("Age", text="Age", anchor=CENTER)
        view_volunteer_table.heading("Activation Status", text="Activation Status", anchor=CENTER)
        view_volunteer_table.heading("Volunteer Classification", text="Volunteer Classification", anchor=CENTER)

        for i in range (0, len(current_volunteer_list)):
            view_volunteer_table.insert(parent='', index=i, iid=i, values=(current_volunteer_list[i][0], current_volunteer_list[i][1], current_volunteer_list[i][2], current_volunteer_list[i][5], current_volunteer_list[i][6], current_volunteer_list[i][7], current_volunteer_list[i][8], current_volunteer_list[i][9], current_volunteer_list[i][10], current_volunteer_list[i][11]))
            i += 1

        view_volunteer_table.pack()

        def activestatusVolunteer():
            global current_volunteer_list
            global manage_volunteer_home_screen
            global deactivated_volunteer
            global deactivated_volunteers
            global deactivated_volunteer_activate_label
            global deactivated_volunteers_IDs


            deactivated_volunteers = []
            for i in range(0, len(current_volunteer_list)):
                if current_volunteer_list[i][-3] == "Deactivated":
                    deactivated_volunteers.append(current_volunteer_list[i])
                i += 1

            deactivated_volunteers_IDs = []
            for i in range(0, len(deactivated_volunteers)):
                deactivated_volunteers_IDs.append(int(deactivated_volunteers[i][1]))
                i += 1

            deactivated_volunteer = IntVar()
            deactivated_volunteer_activate_label = Label(manage_volunteer_home_screen, text="See activation status above for those volunteers who are deactivated. \nPlease select the index number of the volunteer that you would like to activate")
            deactivated_volunteer_activate_label.pack()

            deactivated_volunteer_combobox = ttk.Combobox(manage_volunteer_home_screen, textvariable=deactivated_volunteer)
            deactivated_volunteer_combobox['values'] = deactivated_volunteers_IDs
            deactivated_volunteer_combobox.pack()
            deactivated_volunteer_entry_button = Button(manage_volunteer_home_screen, text="Confirm", command=activatevolunteerVerify)
            deactivated_volunteer_entry_button.pack()

        def activatevolunteerVerify():
            global deactivated_volunteer
            global deactivated_volunteers
            global deactivated_volunteer_activate_label
            global deactivated_volunteers_IDs


            deactivated_volunteer_activate_label.config(
                text="See activation status above for those volunteers who are deactivated. Please select the index number of the volunteer that you would like to activate", fg="#000000")

            if deactivated_volunteer.get() not in deactivated_volunteers_IDs:
                 deactivated_volunteer_activate_label.config(
                         text="Invalid ID. Please enter the ID of a volunteer who has been deactivated (see above table).",
                         fg="#f00")
            elif deactivated_volunteer.get() == ' ' or len(str(deactivated_volunteer.get())) == 0 or deactivated_volunteer.get() == 0:
                 deactivated_volunteer_activate_label.config(text="Please enter a value.", fg="#f00")
            else:
                 submitvolunteerStatus()



        def submitvolunteerStatus():
            volunteer_file_write = open("volunteer_database.txt", "r+")
            volunteer_file_write.truncate(0)
            for i in range(0, len(current_volunteer_list)):
                if i == (deactivated_volunteer.get()-1):
                    current_volunteer_list[i][-3] = "Active"
                    current_volunteer_string = '%'.join(current_volunteer_list[i])
                    volunteer_file_write.write(current_volunteer_string)
                elif i != (deactivated_volunteer.get()-1):
                    current_volunteer_string = '%'.join(current_volunteer_list[i])
                    volunteer_file_write.write(current_volunteer_string)

            volunteer_file_write.close()

            successful_update_label = Label(manage_volunteer_home_screen,
                                            text="You have successfully updated the activation status of volunteer %d. To view an updated table, please refresh the screen." % (
                                                deactivated_volunteer.get()))
            successful_update_label.pack()

        def leadstatusVolunteer():
            global current_volunteer_list
            global manage_volunteer_home_screen
            global standard_volunteers_IDs
            global promote_volunteer_label
            global promote_volunteer
            global standard_volunteers

            standard_volunteers = []
            for i in range(0, len(current_volunteer_list)):
                if current_volunteer_list[i][-2] == "Standard":
                    standard_volunteers.append(current_volunteer_list[i])
                i += 1

            standard_volunteers_IDs = []
            for i in range(0, len(standard_volunteers)):
                standard_volunteers_IDs.append(int(standard_volunteers[i][1]))

            promote_volunteer = IntVar()
            promote_volunteer_label = Label(manage_volunteer_home_screen, text="See Volunteer Classification above for the volunteers who are not currently leads. Please select the index number of the volunteer you wish to promote to lead.")
            promote_volunteer_label.pack()

            promote_volunteer_combobox = ttk.Combobox(manage_volunteer_home_screen, textvariable=promote_volunteer)
            promote_volunteer_combobox['values'] = standard_volunteers_IDs
            promote_volunteer_combobox.pack()
            promote_volunteer_entry_button = Button(manage_volunteer_home_screen, text="Confirm", command=promoteVolunteerVerify)
            promote_volunteer_entry_button.pack()

        def promoteVolunteerVerify():
            global promote_volunteer_label
            global promote_volunteer
            global standard_volunteers_IDs
            global current_volunteer_list

            promote_volunteer_label.config(
                text="See Volunteer Classification above for the volunteers who are not currently leads. Please select the index number of the volunteer you wish to promote to lead.",
                fg="#000000")

            promote_volunteer_camp = current_volunteer_list[(promote_volunteer.get())-1][0]
            print(promote_volunteer_camp)


            promote_volunteer_camp_list = []
            for i in range(0, len(current_volunteer_list)):
                if current_volunteer_list[i][0] == str(promote_volunteer_camp) and current_volunteer_list[i][-2] == "Lead":
                    promote_volunteer_camp_list.append(current_volunteer_list[i])
                    i += 1
                else:
                    i += 1
            print(promote_volunteer_camp_list)

            if len(promote_volunteer_camp_list) > 0:
                promote_volunteer_label.config(text="This volunteer's camp already has a lead. Please select a volunteer whose camp does not yet have a lead.", fg="#f00")
            elif promote_volunteer.get() not in standard_volunteers_IDs:
                promote_volunteer_label.config(text="Invalid ID. Please enter the ID of a volunteer who is not yet lead (see above).", fg="#f00")
            elif promote_volunteer.get() == ' ' or len(str(promote_volunteer.get())) == 0 or promote_volunteer.get() == 0:
                promote_volunteer_label.config(text="Please entere a value.", fg="#f00")
            else:
                submitNewLead()

        def submitNewLead():
            volunteer_file_write = open("volunteer_database.txt", "r+")
            volunteer_file_write.truncate(0)
            for i in range(0, len(current_volunteer_list)):
                if i == (promote_volunteer.get()-1):
                    current_volunteer_list[i][-2] = "Lead"
                    current_volunteer_string = '%'.join(current_volunteer_list[i])
                    volunteer_file_write.write(current_volunteer_string)
                elif i != (promote_volunteer.get()-1):
                    current_volunteer_string = '%'.join(current_volunteer_list[i])
                    volunteer_file_write.write(current_volunteer_string)

            volunteer_file_write.close()
            successful_promotion_label = Label(manage_volunteer_home_screen, text="You have successfully promoted volunteer %d. To view an updated table, please refresh the screen." %(promote_volunteer.get()))
            successful_promotion_label.pack()





        update_volunteer_button = Button(manage_volunteer_home_screen, text="Activate a Volunteer", command=activestatusVolunteer)
        update_volunteer_button.pack()
        promote_volunteer_button = Button(manage_volunteer_home_screen, text="Assign a lead volunteer", command=leadstatusVolunteer)
        promote_volunteer_button.pack()



    def manageVolunteerScreen():
        global manage_volunteer_home_screen
        manage_volunteer_home_screen = Toplevel(admin_home_screen)
        manage_volunteer_home_screen.title("Manage Volunteer Homescreen")
        manage_volunteer_home_screen.geometry("500x650")
        viewexistingvolunteersSetUp()


        manage_volunteer_home_screen.mainloop()

    manageVolunteerScreen()

manageVolunteers(Tk())