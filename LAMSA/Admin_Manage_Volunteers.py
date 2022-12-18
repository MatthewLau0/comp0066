from tkinter import *
from tkinter import ttk


def manageVolunteers():

    volunteer_file = open("volunteer_database.txt", "r")
    volunteer_file_extract = []

    for line in volunteer_file:
        line_list = line.split("%")
        volunteer_file_extract.append(line_list)
    volunteer_file.close()

    current_volunteer_list = []

    for i in range(0, len(volunteer_file_extract)):
        current_volunteer_list.append(volunteer_file_extract[i])

    current_volunteer_list_print = []
    for i in range(0, len(volunteer_file_extract)):
        if volunteer_file_extract[i][-3] == "Deleted":
            pass
        else:
            current_volunteer_list_print.append(volunteer_file_extract[i])

    current_volunteer_list_print_IDs = []
    for i in range(0, len(current_volunteer_list_print)):
        current_volunteer_list_print_IDs.append(current_volunteer_list_print[i][1])

    manage_volunteer_home_screen = Toplevel()
    manage_volunteer_home_screen.title("Manage Volunteer Homescreen")
    screen_width1 = manage_volunteer_home_screen.winfo_screenwidth()
    screen_height1 = manage_volunteer_home_screen.winfo_screenheight()
    window_height1 = screen_height1
    window_width1 = 1100

    center_x1 = int(screen_width1 / 2 - window_width1 / 2)
    center_y1 = int(screen_height1 / 2 - window_height1 / 2)
    manage_volunteer_home_screen.geometry(f'{window_width1}x{window_height1}+{center_x1}+{center_y1}')

    view_volunteers_screen_label = Label(manage_volunteer_home_screen, text="Please see below a list of the current volunteers and the camps they are associated with.")
    view_volunteers_screen_label.pack()

    view_volunteer_frame = Frame(manage_volunteer_home_screen)
    view_volunteer_frame.pack()

    my_game = ttk.Treeview(view_volunteer_frame)

    my_game['columns'] = (
        "Camp ID",
        "Volunteer ID",
        "Volunteer Name",
        "Volunteer Username",
        "Volunteer Email",
        "Volunteer Number",
        "Volunteer Gender",
        "Volunteer DoB",
        "Volunteer Age",
        "Volunteer Account Status",
        "Volunteer Status"
    )

    my_game.column("#0", width=0, stretch=NO)
    my_game.column("Camp ID", anchor=CENTER, width=70)
    my_game.column("Volunteer ID", anchor=CENTER, width=75)
    my_game.column("Volunteer Name", anchor=CENTER, width=140)
    my_game.column("Volunteer Username", anchor=CENTER, width=140)
    my_game.column("Volunteer Email", anchor=CENTER, width=160)
    my_game.column("Volunteer Number", anchor=CENTER, width=100)
    my_game.column("Volunteer Gender", anchor=CENTER, width=100)
    my_game.column("Volunteer DoB", anchor=CENTER, width=85)
    my_game.column("Volunteer Age", anchor=CENTER, width=50)
    my_game.column("Volunteer Account Status", anchor=CENTER, width=80)
    my_game.column("Volunteer Status", anchor=CENTER, width=80)

    my_game.heading("#0", text="", anchor=CENTER)
    my_game.heading("Camp ID", text="Camp ID", anchor=CENTER)
    my_game.heading("Volunteer ID", text="Volunteer ID", anchor=CENTER)
    my_game.heading("Volunteer Name", text="Name", anchor=CENTER)
    my_game.heading("Volunteer Username", text="Username", anchor=CENTER)
    my_game.heading("Volunteer Email", text="Email", anchor=CENTER)
    my_game.heading("Volunteer Number", text="Number", anchor=CENTER)
    my_game.heading("Volunteer Gender", text="Gender", anchor=CENTER)
    my_game.heading("Volunteer DoB", text="DoB", anchor=CENTER)
    my_game.heading("Volunteer Age", text="Age", anchor=CENTER)
    my_game.heading("Volunteer Account Status", text="Account Status", anchor=CENTER)
    my_game.heading("Volunteer Status", text="Volunteer Status", anchor=CENTER)

    for i in range(0, len(current_volunteer_list_print)):
        current_number = current_volunteer_list_print[i][6].split('#')
        my_game.insert(parent='', index=i, iid=i, values=(
            current_volunteer_list_print[i][0],
            current_volunteer_list_print[i][1],
            current_volunteer_list_print[i][2],
            current_volunteer_list_print[i][3],
            current_volunteer_list_print[i][5],
            f"+{current_number[0]} {current_number[1]}",
            current_volunteer_list_print[i][7],
            current_volunteer_list_print[i][8],
            current_volunteer_list_print[i][9],
            current_volunteer_list_print[i][10],
            current_volunteer_list_print[i][11]
        ))

    my_game.pack()

    def activestatusVolunteer():

        active_status_volunteer = Toplevel()
        active_status_volunteer.title("Activate a Volunteer")
        activestatusVolunteer_frame = Frame(active_status_volunteer)
        activestatusVolunteer_frame.pack()

        deactivated_volunteers = []
        for x in range(0, len(current_volunteer_list)):
            if current_volunteer_list[x][-3] == "Deactivated":
                deactivated_volunteers.append(current_volunteer_list[x])

        deactivated_volunteers_IDs = []
        for n in range(0, len(deactivated_volunteers)):
            deactivated_volunteers_IDs.append(int(deactivated_volunteers[n][1]))

        deactivated_volunteer = IntVar()
        deactivated_volunteer_activate_label = Label(activestatusVolunteer_frame, text="See activation status above for those volunteers who are deactivated. Please select the index number of the volunteer that you would like to activate")
        deactivated_volunteer_activate_label.pack()

        deactivated_volunteer_combobox = ttk.Combobox(activestatusVolunteer_frame, textvariable=deactivated_volunteer)
        deactivated_volunteer_combobox['values'] = deactivated_volunteers_IDs
        deactivated_volunteer_combobox.pack()

        def activatevolunteerVerify():

            deactivated_volunteer_activate_label.config(
                text="See activation status above for those volunteers who are deactivated. Please select the index number of the volunteer that you would like to activate")

            try:
                if deactivated_volunteer.get() not in deactivated_volunteers_IDs:
                    deactivated_volunteer_activate_label.config(
                    text="Invalid ID. Please enter the ID of a volunteer who has been deactivated (see above table).",
                    fg="#f00")
                elif deactivated_volunteer.get() == ' ' or len(
                    str(deactivated_volunteer.get())) == 0 or deactivated_volunteer.get() == 0:
                    deactivated_volunteer_activate_label.config(text="Please enter a value.", fg="#f00")
                else:
                    submitvolunteerStatus()
            except TclError:
                deactivated_volunteer_activate_label.config(
                    text="Invalid ID. Please enter the ID of a volunteer who has been deactivated (see above table).",
                    fg="#f00")
        deactivated_volunteer_entry_button = Button(activestatusVolunteer_frame, text="Confirm", command=activatevolunteerVerify)
        deactivated_volunteer_entry_button.pack()

        def submitvolunteerStatus():
            active_status_volunteer.destroy()
            volunteer_file_write = open("volunteer_database.txt", "r+")
            volunteer_file_write.truncate(0)
            for y in range(0, len(current_volunteer_list)):
                if y == (deactivated_volunteer.get()-1):
                    current_volunteer_list[y][-3] = "Active"
                    current_volunteer_string = '%'.join(current_volunteer_list[y])
                    volunteer_file_write.write(current_volunteer_string)
                elif y != (deactivated_volunteer.get()-1):
                    current_volunteer_string = '%'.join(current_volunteer_list[y])
                    volunteer_file_write.write(current_volunteer_string)

            volunteer_file_write.close()

            successful_update_label = Label(manage_volunteer_home_screen,
                                            text="You have successfully updated the activation status of volunteer %d. To view an updated table, please refresh the screen." % (
                                                deactivated_volunteer.get()))
            successful_update_label.pack()

    def deactivateVolunteer():

        deactivate_volunteer_screen = Toplevel()
        deactivate_volunteer_screen.title("Deactivate a Volunteer")
        deactivatedVolunteer_frame = Frame(deactivate_volunteer_screen)
        deactivatedVolunteer_frame.pack()

        activated_volunteers = []
        for x in range(0, len(current_volunteer_list)):
            if current_volunteer_list[x][-3] == "Active":
                activated_volunteers.append(current_volunteer_list[x])

        activated_volunteers_IDs = []
        for n in range(0, len(activated_volunteers)):
            activated_volunteers_IDs.append(int(activated_volunteers[n][1]))

        activated_volunteer = IntVar()
        deactivate_volunteer_activate_label = Label(deactivatedVolunteer_frame,
                                                     text="See activation status above for those volunteers who are active. Please select the index number of the volunteer that you would like to deactivate")
        deactivate_volunteer_activate_label.pack()

        activated_volunteer_combobox = ttk.Combobox(deactivatedVolunteer_frame,
                                                      textvariable=activated_volunteer)
        activated_volunteer_combobox['values'] = activated_volunteers_IDs
        activated_volunteer_combobox.pack()

        def deactivatevolunteerVerify():

            deactivate_volunteer_activate_label.config(
                text="See activation status above for those volunteers who are deactivated. Please select the index number of the volunteer that you would like to activate")

            try:
                if activated_volunteer.get() not in activated_volunteers_IDs:
                    deactivate_volunteer_activate_label.config(
                        text="Invalid ID. Please enter the ID of a volunteer who is active (see above table).",
                        fg="#f00")
                elif activated_volunteer.get() == ' ' or len(
                        str(activated_volunteer.get())) == 0 or activated_volunteer.get() == 0:
                    deactivate_volunteer_activate_label.config(text="Please select a value.", fg="#f00")
                else:
                    deactivevolunteerStatus()
            except TclError:
                deactivate_volunteer_activate_label.config(
                    text="Invalid ID. Please enter the ID of a volunteer who is active (see above table).",
                    fg="#f00")
        activated_volunteer_entry_button = Button(deactivatedVolunteer_frame, text="Confirm",
                                                    command=deactivatevolunteerVerify)
        activated_volunteer_entry_button.pack()

        def deactivevolunteerStatus():

            volunteer_file_write = open("volunteer_database.txt", "r+")
            volunteer_file_write.truncate(0)
            for y in range(0, len(current_volunteer_list)):
                if y == (activated_volunteer.get() - 1):
                    current_volunteer_list[y][-3] = "Deactivated"
                    current_volunteer_string = '%'.join(current_volunteer_list[y])
                    volunteer_file_write.write(current_volunteer_string)
                elif y != (activated_volunteer.get() - 1):
                    current_volunteer_string = '%'.join(current_volunteer_list[y])
                    volunteer_file_write.write(current_volunteer_string)

            volunteer_file_write.close()
            deactivate_volunteer_screen.destroy()

            successful_deactivate_update_label = Label(manage_volunteer_home_screen, text="You have successfully updated the activation status of volunteer %d. To view an updated table, please refresh the screen." % (activated_volunteer.get()))
            successful_deactivate_update_label.pack()

    def leadstatusVolunteer():

        leadstatusVolunteer_screen = Toplevel()
        leadstatusVolunteer_screen.title("Assign a Camp Lead")
        leadstatusVolunteer_frame = Frame(leadstatusVolunteer_screen)
        leadstatusVolunteer_frame.pack()

        standard_volunteers = []
        for q in range(0, len(current_volunteer_list)):
            if current_volunteer_list[q][-2] == "Standard":
                standard_volunteers.append(current_volunteer_list[q])

        promote_volunteer = IntVar()
        promote_volunteer_label = Label(leadstatusVolunteer_frame, text="Please select the index number of the volunteer you wish to promote to lead.")
        promote_volunteer_label.pack()

        promote_volunteer_combobox = ttk.Combobox(leadstatusVolunteer_frame, textvariable=promote_volunteer)
        promote_volunteer_combobox['values'] = current_volunteer_list_print_IDs
        promote_volunteer_combobox.pack()

        def promoteVolunteerVerify():

            promote_volunteer_label.config(
                text="See Volunteer Classification above for the volunteers who are not currently leads. Please select the index number of the volunteer you wish to promote to lead.")

            try:
                promote_volunteer_camp = current_volunteer_list[(promote_volunteer.get()) - 1][0]

                promote_volunteer_camp_list = []
                for j in range(0, len(current_volunteer_list)):
                    if current_volunteer_list[j][0] == str(promote_volunteer_camp) and current_volunteer_list[j][-2] == "Lead":
                        promote_volunteer_camp_list.append(current_volunteer_list[j])
                    else:
                        pass
                if len(promote_volunteer_camp_list) > 0:
                    promote_volunteer_label.config(
                        text="This volunteer's camp already has a lead. Please select a volunteer whose camp does not yet have a lead.",
                        fg="#f00")
                elif str(promote_volunteer.get()) not in current_volunteer_list_print_IDs:
                    promote_volunteer_label.config(
                        text="Invalid ID. Please enter the ID of a volunteer who is not yet lead.", fg="#f00")
                elif promote_volunteer.get() == ' ' or len(
                        str(promote_volunteer.get())) == 0 or promote_volunteer.get() == 0:
                    promote_volunteer_label.config(text="Please enter a value.", fg="#f00")
                else:
                    submitNewLead()
            except TclError:
                promote_volunteer_label.config(
                    text="Invalid ID. Please enter the ID of a volunteer who is not yet lead.", fg="#f00")
        promote_volunteer_entry_button = Button(leadstatusVolunteer_frame, text="Confirm", command=promoteVolunteerVerify)
        promote_volunteer_entry_button.pack()

        def submitNewLead():
            volunteer_file_write = open("volunteer_database.txt", "r+")
            volunteer_file_write.truncate(0)
            for y in range(0, len(current_volunteer_list)):
                if y == (promote_volunteer.get()-1):
                    current_volunteer_list[y][-2] = "Lead"
                    current_volunteer_string = '%'.join(current_volunteer_list[y])
                    volunteer_file_write.write(current_volunteer_string)
                elif y != (promote_volunteer.get()-1):
                    current_volunteer_string = '%'.join(current_volunteer_list[y])
                    volunteer_file_write.write(current_volunteer_string)

            leadstatusVolunteer_screen.destroy()
            volunteer_file_write.close()
            successful_promotion_label = Label(manage_volunteer_home_screen, text="You have successfully promoted volunteer %d. To view an updated table, please refresh the screen." % (promote_volunteer.get()))
            successful_promotion_label.pack()

    def deleteVolunteer():

        current_volunteer_list_1 = []

        for s in range(0, len(volunteer_file_extract)):
            current_volunteer_list_1.append(volunteer_file_extract[s])

        current_volunteer_list_print_1 = []
        for s in range(0, len(volunteer_file_extract)):
            if volunteer_file_extract[s][-3] == "Deleted":
                pass
            else:
                current_volunteer_list_print_1.append(volunteer_file_extract[s])

        current_volunteer_list_print_IDs_1 = []
        for p in range(0, len(current_volunteer_list_print)):
            current_volunteer_list_print_IDs_1.append(current_volunteer_list_print[p][1])

        delete_volunteer_screen = Toplevel()
        delete_volunteer_screen.title("Delete a Volunteer")
        delete_volunteer_screen_frame = Frame(delete_volunteer_screen)
        delete_volunteer_screen_frame.pack()

        delete_volunteer = IntVar()
        delete_volunteer_label = Label(delete_volunteer_screen_frame,
                                        text="Please select the index number of the volunteer you wish to delete from the database.")
        delete_volunteer_label.pack()

        delete_volunteer_combobox = ttk.Combobox(delete_volunteer_screen_frame, textvariable=delete_volunteer)
        delete_volunteer_combobox['values'] = current_volunteer_list_print_IDs
        delete_volunteer_combobox.pack()

        def delete_volunteer_verify():

            delete_volunteer_label.config(
                text="Please select the index number of the volunteer you wish to delete from the database.")
            try:
                if str(delete_volunteer.get()) not in current_volunteer_list_print_IDs:
                    delete_volunteer_label.config(text="Invalid ID. Please enter the ID of a current volunteer.",
                                                  fg="#f00")
                elif delete_volunteer.get() == ' ' or len(
                        str(delete_volunteer.get())) == 0 or delete_volunteer.get() == 0:
                    delete_volunteer_label.config(text="Please enter a value.", fg="#f00")
                else:
                    deletevolunteerSubmit()
            except TclError:
                delete_volunteer_label.config(text="Invalid ID. Please enter the ID of a current volunteer.", fg="#f00")
        delete_volunteer_entry_button = Button(delete_volunteer_screen_frame, text="Confirm",
                                                command=delete_volunteer_verify)
        delete_volunteer_entry_button.pack()

        def deletevolunteerSubmit():
            volunteer_file_write = open("volunteer_database.txt", "r+")
            volunteer_file_write.truncate(0)
            for y in range(0, len(current_volunteer_list)):
                if y == (delete_volunteer.get() - 1):
                    current_volunteer_list[y][-3] = "Deleted"
                    current_volunteer_string = '%'.join(current_volunteer_list[y])
                    volunteer_file_write.write(current_volunteer_string)
                elif y != (delete_volunteer.get() - 1):
                    current_volunteer_string = '%'.join(current_volunteer_list[y])
                    volunteer_file_write.write(current_volunteer_string)

            volunteer_file_write.close()
            delete_volunteer_screen.destroy()

            successful_delete_update_label = Label(manage_volunteer_home_screen,
                                                       text="You have successfully deleted the volunteer %d. To view an updated table, please refresh the screen." % (
                                                           delete_volunteer.get()))
            successful_delete_update_label.pack()

    def view_availability():

        emergency_database_file = open("emergency_database.txt", "r")

        emergency_database_list = []
        for line1 in emergency_database_file:
            line_list1 = line1.split("%")
            emergency_database_list.append(line_list1)

        emergency_database_file.close()

        view_availability_id_window = Toplevel()
        view_availability_id_window.title("Select Volunteer")

        screen_width2 = view_availability_id_window.winfo_screenwidth()
        screen_height2 = view_availability_id_window.winfo_screenheight()
        window_height2 = 100
        window_width2 = 300

        center_x2 = int(screen_width2 / 2 - window_width2 / 2)
        center_y2 = int(screen_height2 / 2 - window_height2 / 2)
        view_availability_id_window.geometry(f'{window_width2}x{window_height2}+{center_x2}+{center_y2}')

        id_list = []

        for n in emergency_database_list:
            id_list.append(n[0])

        selected_camp_id = StringVar()

        id_select_label = Label(view_availability_id_window, text="Please select the Camp ID at which you wish to view volunteer availabilities")
        id_select_label.pack()
        selected_camp_id.set("Select ID")
        id_select_option = ttk.Combobox(view_availability_id_window, textvariable=selected_camp_id, values=id_list)
        id_select_option.pack()

        def view_availability_table():
            view_availability_table_screen = Toplevel()
            view_availability_table_screen.title("Manage Volunteers")
            screen_width3 = view_availability_table_screen.winfo_screenwidth()
            screen_height3 = view_availability_table_screen.winfo_screenheight()
            window_height3 = screen_height3
            window_width3 = 1100

            center_x3 = int(screen_width3 / 2 - window_width3 / 2)
            center_y3 = int(screen_height3 / 2 - window_height3 / 2)
            view_availability_table_screen.geometry(f'{window_width3}x{window_height3}+{center_x3}+{center_y3}')

            view_volunteers_availability_label = Label(view_availability_table_screen, text="Please see below a list of the current volunteers and the camps they are associated with.")
            view_volunteers_availability_label.pack()

            view_availability_frame = Frame(view_availability_table_screen)
            view_availability_frame.pack()

            my_game1 = ttk.Treeview(view_availability_frame)

            my_game1['columns'] = (
                "Camp ID",
                "Volunteer ID",
                "Volunteer Name",
                "Start Date",
                "End Date",
                "Monday",
                "Tuesday",
                "Wednesday",
                "Thursday",
                "Friday",
                "Saturday",
                "Sunday"
            )

            my_game1.column("#0", width=0, stretch=NO)
            my_game1.column("Camp ID", anchor=CENTER, width=70)
            my_game1.column("Volunteer ID", anchor=CENTER, width=75)
            my_game1.column("Volunteer Name", anchor=CENTER, width=140)
            my_game1.column("Start Date", anchor=CENTER, width=140)
            my_game1.column("End Date", anchor=CENTER, width=160)
            my_game1.column("Monday", anchor=CENTER, width=100)
            my_game1.column("Tuesday", anchor=CENTER, width=100)
            my_game1.column("Wednesday", anchor=CENTER, width=85)
            my_game1.column("Thursday", anchor=CENTER, width=50)
            my_game1.column("Friday", anchor=CENTER, width=80)
            my_game1.column("Saturday", anchor=CENTER, width=80)
            my_game1.column("Sunday", anchor=CENTER, width=80)

            my_game1.heading("#0", text="", anchor=CENTER)
            my_game1.heading("Camp ID", text="Camp ID", anchor=CENTER)
            my_game1.heading("Volunteer ID", text="Volunteer ID", anchor=CENTER)
            my_game1.heading("Volunteer Name", text="Name", anchor=CENTER)
            my_game1.heading("Start Date", text="Start Date", anchor=CENTER)
            my_game1.heading("End Date", text="End Date", anchor=CENTER)
            my_game1.heading("Monday", text="Monday", anchor=CENTER)
            my_game1.heading("Tuesday", text="Tuesday", anchor=CENTER)
            my_game1.heading("Wednesday", text="Wednesday", anchor=CENTER)
            my_game1.heading("Thursday", text="Thursday", anchor=CENTER)
            my_game1.heading("Friday", text="Friday", anchor=CENTER)
            my_game1.heading("Saturday", text="Saturday", anchor=CENTER)
            my_game1.heading("Sunday", text="Sunday", anchor=CENTER)

            list_for_availability = []

            for volunteer in current_volunteer_list_print:
                if volunteer[0] == str(selected_camp_id.get()):
                    list_for_availability.append(volunteer)

            for num in range(0, len(list_for_availability)):
                availability = list_for_availability[num][12].split('#')
                my_game1.insert(parent='', index=num, iid=num, values=(
                    list_for_availability[num][0],
                    list_for_availability[num][1],
                    list_for_availability[num][2],
                    availability[0],
                    availability[1],
                    availability[2],
                    availability[3],
                    availability[4],
                    availability[5],
                    availability[6],
                    availability[7],
                    availability[8]
                ))


            my_game1.pack()

            Button(view_availability_table_screen, text="Close", command=view_availability_table_screen.destroy).pack()

        def run_the_update():
            if selected_camp_id.get() not in id_list:
                id_select_label.config(text="Please enter the ID of a current volunteer", fg="#f00")
            else:
                view_availability_id_window.destroy()
                view_availability_table()

        id_done = Button(view_availability_id_window, text="Done", command=run_the_update)
        id_done.pack()

    view_availability_button = Button(manage_volunteer_home_screen, text="View Volunteer Availability", command=view_availability)
    view_availability_button.pack()
    deactivate_volunteer_button = Button(manage_volunteer_home_screen, text="Deactivate a Volunteer", command=deactivateVolunteer)
    deactivate_volunteer_button.pack()
    update_volunteer_button = Button(manage_volunteer_home_screen, text="Activate a Volunteer", command=activestatusVolunteer)
    update_volunteer_button.pack()
    promote_volunteer_button = Button(manage_volunteer_home_screen, text="Assign a Camp Lead", command=leadstatusVolunteer)
    promote_volunteer_button.pack()
    delete_volunteer_button = Button(manage_volunteer_home_screen, text="Delete a Volunteer", command=deleteVolunteer)
    delete_volunteer_button.pack()
    return_home_button = Button(manage_volunteer_home_screen, text="Home", command=manage_volunteer_home_screen.destroy)
    return_home_button.pack()

    manage_volunteer_home_screen.mainloop()
