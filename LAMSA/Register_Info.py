from tkinter import *
from tkinter import ttk
from tkcalendar import Calendar
import datetime

import Login


def volunteerList():

    volunteer_entry_screen = Tk()
    volunteer_entry_screen.title("Volunteer Entry Screen")

    screen_width = volunteer_entry_screen.winfo_screenwidth()
    screen_height = volunteer_entry_screen.winfo_screenheight()
    window_height = screen_height
    window_width = 900

    center_x = int(screen_width / 2 - window_width / 2)
    center_y = int(screen_height / 2 - window_height / 2)
    volunteer_entry_screen.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

    Label(volunteer_entry_screen, text="LAMSA", font=("Avenir", 80, "bold")).pack()

    current_volunteer_list = []
    volunteer_file = open("volunteer_database.txt", "r")
    for line in volunteer_file:
        line_list = line.split("%")
        current_volunteer_list.append(line_list)

    volunteer_file.close()

    new_volunteer = ["NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA"]

    new_volunteer[1] = current_volunteer_list[-1][1]
    new_volunteer[3] = current_volunteer_list[-1][3]
    new_volunteer[4] = current_volunteer_list[-1][4]
    new_volunteer[10] = current_volunteer_list[-1][10]
    new_volunteer[11] = current_volunteer_list[-1][11]
    new_volunteer[12] = current_volunteer_list[-1][12]
    del current_volunteer_list[-1]

    emergency_database_file = open("emergency_database.txt", "r")
    emergency_database_list = []
    for line in emergency_database_file:
        line_list = line.split("%")
        emergency_database_list.append(line_list)
    emergency_database_file.close()

    camp_ID_list = []
    for i in range(0, len(emergency_database_list)):
        camp_ID_list.append(emergency_database_list[i][0])

    def campTable():

        volunteer_number_print = Label(volunteer_entry_screen, text="Your Volunteer ID is %s" %(new_volunteer[1]), font=("Avenir", 20, "bold"))
        volunteer_number_print.pack()

        select_camp_table_label = Label(volunteer_entry_screen, text="Scroll through the table below to see below the LAMSA Camps which you can volunteer at.\n")
        select_camp_table_label.pack()

        select_camp_table_frame = Frame(volunteer_entry_screen)
        select_camp_table_frame.pack()

        select_camp_table = ttk.Treeview(volunteer_entry_screen, height=3)
        select_camp_table['columns'] = ("Camp ID", "Camp Name", "Location")

        select_camp_table.column("#0", width=0, stretch=NO)
        select_camp_table.column('Camp ID', anchor=CENTER, width=100)
        select_camp_table.column("Camp Name", anchor=CENTER, width=100)
        select_camp_table.column("Location", anchor=CENTER, width=100)

        select_camp_table.heading('Camp ID', text="Camp ID", anchor=CENTER)
        select_camp_table.heading("Camp Name", text="Camp Name", anchor=CENTER)
        select_camp_table.heading("Location", text="Location", anchor=CENTER)

        for i in range(0, len(emergency_database_list)):
            select_camp_table.insert(parent='', index=i, iid=i, values=(emergency_database_list[i][0], emergency_database_list[i][1], emergency_database_list[i][4]))

        select_camp_table.pack()

        form_frame = Frame(volunteer_entry_screen)
        form_frame.pack()


        def volunteerEntry():

            select_camp_table_button.destroy()
            empty_label.destroy()

            for widget in form_frame.winfo_children():
                widget.destroy()

            select_camp = StringVar()
            full_name = StringVar()
            email = StringVar()
            phone_area_code = StringVar()
            phone_number = StringVar()
            gender = StringVar()

            select_camp_label = Label(form_frame, text="\nPlease enter the Camp ID")
            select_camp_label.pack()
            select_camp_select = Entry(form_frame, textvariable=select_camp)
            select_camp_select.pack()

            full_name_label = Label(form_frame, text="Please enter your full name")
            full_name_label.pack()
            full_name_entry = Entry(form_frame, textvariable=full_name)
            full_name_entry.pack()

            email_label = Label(form_frame, text="Please enter an email address")
            email_label.pack()
            email_entry = Entry(form_frame, textvariable=email)
            email_entry.pack()

            phone_frame = Frame(form_frame)
            phone_frame.pack()

            phone_number_label = Label(phone_frame, text="Please enter a phone number")
            phone_number_label.pack()
            area_code_sign = Label(phone_frame, text="+")
            area_code_sign.pack(side=LEFT)
            phone_number_area_code_entry = Entry(phone_frame, textvariable=phone_area_code)
            phone_number_area_code_entry.pack(side=LEFT, ipadx=1)
            phone_number_entry = Entry(phone_frame, textvariable=phone_number)
            phone_number_entry.pack(side=LEFT)

            gender_label = Label(form_frame, text="Please enter the gender you identify with")
            gender_label.pack()
            gender_entry = Entry(form_frame, textvariable=gender)
            gender_entry.pack()

            today = datetime.datetime.today()

            DOB_calendar_label = Label(form_frame, text="Please enter your date of birth")
            DOB_calendar_label.pack()
            DOB_calendar = Calendar(form_frame, date_pattern="d/m/y", selectmode='day', maxdate=today)
            DOB_calendar.pack()


            def confirmAge():

                DOB = datetime.datetime.strptime(DOB_calendar.get_date(), "%d/%m/%Y").date()

                volunteer_age = 0

                if DOB.month < today.month and today.year > DOB.year:
                    volunteer_age = today.year - DOB.year

                elif DOB.month > DOB.month and today.year > DOB.year:
                    volunteer_age = today.year - DOB.year - 1

                elif DOB.month == today.month and today.year > DOB.year and today.day < DOB.day:
                    volunteer_age = today.year - DOB.year - 1

                elif DOB.month == today.month and today.year > DOB.year and today.day > DOB.day:
                    volunteer_age = today.year - DOB.year

                volunteer_age = str(volunteer_age)

                new_volunteer_error_list = []

                def newvolunteerVerify():
                    DOB_calendar_label.config(text="DoB is Valid!", fg="green")
                    select_camp_label.config(text="Camp ID is Valid!", fg="green")
                    full_name_label.config(text="Name is Valid!", fg="green")
                    email_label.config(text="Email is Valid!", fg="green")
                    phone_number_label.config(text="Phone Number is Valid!", fg="green")
                    gender_label.config(text="Gender is Valid!", fg="green")
                    new_volunteer_error_list.clear()
                    if str(volunteer_age) == str(0):
                        DOB_calendar_label.config(
                            text="Please enter your DOB",
                            fg="#f00")
                        new_volunteer_error_list.append("d1")
                    if select_camp.get() not in camp_ID_list:
                        select_camp_label.config(
                            text="\nPlease enter a valid Camp ID",
                            fg="#f00")
                        new_volunteer_error_list.append("e1")
                    if len(full_name.get()) == 0 or full_name.get() == ' ':
                        full_name_label.config(
                            text="Please enter your full name.",
                            fg='#f00')
                        new_volunteer_error_list.append("e2")
                    if '@' not in email.get() or '.' not in email.get():
                        email_label.config(
                            text="Please enter a valid email address",
                            fg='#f00')
                        new_volunteer_error_list.append("e3")
                    if len(phone_area_code.get()) > 4:
                        phone_number_label.config(
                            text="Please enter a valid phone area code and a valid phone number",
                            fg='#f00')
                        new_volunteer_error_list.append("e4")
                    if len(phone_number.get()) > 15 or len(
                            phone_number.get()) < 7 or phone_number.get().isalnum() != True:
                        phone_number_label.config(
                            text="Please enter a valid phone area code and a valid phone number",
                            fg='#f00')
                        new_volunteer_error_list.append("e5")
                    if len(gender.get()) == 0 or gender.get() == ' ':
                        gender_label.config(
                            text="Please enter a gender. If you prefer not to specify a gender, enter n/a.",
                            fg='#f00')
                        new_volunteer_error_list.append("e6")

                newvolunteerVerify()
                if len(new_volunteer_error_list) > 0:
                    pass
                else:
                    def createvolunteerSubmit():

                        phone_number_complete = ("%s#%s" % (phone_area_code.get(), phone_number.get()))

                        new_volunteer[0] = select_camp.get()
                        new_volunteer[2] = full_name.get()
                        new_volunteer[5] = email.get()
                        new_volunteer[6] = phone_number_complete
                        new_volunteer[7] = gender.get()
                        new_volunteer[8] = str(DOB)
                        new_volunteer[9] = volunteer_age

                        current_volunteer_list.append(new_volunteer)
                        volunteer_file_write = open("volunteer_database.txt", "r+")
                        for i in range(0, len(current_volunteer_list)):
                            current_volunteer_string = '%'.join(current_volunteer_list[i])
                            volunteer_file_write.write("%s" % (current_volunteer_string))
                        volunteer_file_write.close()
                        closeScreen()

                    createvolunteerSubmit()

            emergency_submit_button = Button(form_frame, text="Submit", command=confirmAge, width=30, height=2)
            emergency_submit_button.pack()


        empty_label = Label(volunteer_entry_screen)
        empty_label.pack()
        select_camp_table_button = Button(volunteer_entry_screen, text="Continue", command=volunteerEntry, width=30, height=2)
        select_camp_table_button.pack()
        back_button = Button(volunteer_entry_screen, text="Cancel", command=lambda: [volunteer_entry_screen.destroy(), Login.main()], width=30, height=2)
        back_button.pack()

    campTable()

    def closeScreen():
        volunteer_entry_screen.destroy()
        Create_Volunteer_Close_Screen = Tk()
        Create_Volunteer_Close_Screen.title("Volunteer Request Successfully Submitted")
        Create_Volunteer_Close_Screen.geometry("500x650")

        close_label = Label(Create_Volunteer_Close_Screen, text="Thank you for submitting a request to become a volunteer. \n The admin will review your request, and once approved you will be able to access our services.")
        close_label.pack()
        return_home_button = Button(Create_Volunteer_Close_Screen, text="Return to Homescreen", command=lambda: [Create_Volunteer_Close_Screen.destroy(), Login.main()], width=30, height=2)
        return_home_button.pack()

    volunteer_entry_screen.mainloop()

