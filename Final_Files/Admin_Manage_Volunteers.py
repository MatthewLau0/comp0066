from tkinter import *
from tkinter import ttk


def manageVolunteers():

    def viewexistingvolunteersSetUp():
        global current_volunteer_list

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

        view_volunteers_screen = Toplevel(manage_volunteer_home_screen)
        view_volunteers_screen.title("View Current Volunteers")
        view_volunteers_screen.geometry("500x650")

        view_volunteers_screen_label = Label(view_volunteers_screen, text="Please see below a list of the current volunteers and the camps they are associated with.")
        view_volunteers_screen_label.pack()

        view_volunteer_frame = Frame(view_volunteers_screen)
        view_volunteer_frame.pack()

        view_volunteer_table = ttk.Treeview(view_volunteers_screen)

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

        view_volunteer_return_home_button = Button(view_volunteers_screen, text="Return Home", command=deleteTable)
        view_volunteer_return_home_button.pack()

    def deleteTable():
        import view_volunteers_screen
        view_volunteers_screen.destroy()

    def activestatusVolunteer():
        pass


    def manageVolunteerScreen():
        global manage_volunteer_home_screen
        manage_volunteer_home_screen = Toplevel()
        manage_volunteer_home_screen.title("Manage Volunteer Homescreen")
        manage_volunteer_home_screen.geometry("500x650")
        manage_volunteer_home_screen_label = Label(manage_volunteer_home_screen, text="Please select an option below")
        manage_volunteer_home_screen_label.pack()
        view_existing_volunteers_button = Button(manage_volunteer_home_screen, text="View Existing Volunteers", command=viewexistingvolunteersSetUp)
        view_existing_volunteers_button.pack()
        active_status_volunteers_button = Button(manage_volunteer_home_screen, text="Activate/Deactivate/Delete Volunteers", command=activestatusVolunteer)
        active_status_volunteers_button.pack()


        manage_volunteer_home_screen.mainloop()

    manageVolunteerScreen()

manageVolunteers()