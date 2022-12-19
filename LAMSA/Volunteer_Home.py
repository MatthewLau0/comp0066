from tkinter import *
from tkinter import ttk
import datetime
import Login
import Volunteer_Create_Family
import Volunteer_View_Family
import Volunteer_Add_Availability

def volunteer_home_page():
    user_camp_id = ""
    user_id = ""
    user_name = ""
    user_username = ""
    user_password = ""
    user_email = ""
    user_number_area = ""
    user_number = ""
    user_gender = ""
    user_dob = ""
    user_age = ""
    user_status = ""
    user_role = ""
    user_availability = ""

    logins_file = open("successful_login.txt", "r")

    logins_list = []
    for line in logins_file:
        line_string = line.split("%")
        logins_list.append(line_string)
    logins_file.close()
    if len(logins_list) > 0:
        user_camp_id = logins_list[-1][0]
        user_id = logins_list[-1][1]
        user_name = logins_list[-1][2]
        user_username = logins_list[-1][3]
        user_password = logins_list[-1][4]
        user_email = logins_list[-1][5]
        if "#" in logins_list[-1][6]:
            number = []
            number_string = logins_list[-1][6].split("#")
            for i in number_string:
                number.append(i)
            user_number_area = number[0]
            user_number = number[1]
        else:
            user_number = logins_list[-1][6]
        user_gender = logins_list[-1][7]
        user_dob = logins_list[-1][8]
        user_age = logins_list[-1][9]
        user_status = logins_list[-1][10]
        user_role = logins_list[-1][11]
        user_availability = logins_list[-1][12]

    open_volunteer_file = open("volunteer_database.txt", 'r')
    volunteer_actual_database_list = []
    for line in open_volunteer_file:
        x = line.split("%")
        volunteer_actual_database_list.append(x)
    open_volunteer_file.close()

    def Settings():

        volunteer_entry_screen = Toplevel()
        volunteer_entry_screen.title("Volunteer Entry Screen")

        screen_width3 = volunteer_entry_screen.winfo_screenwidth()
        screen_height3 = volunteer_entry_screen.winfo_screenheight()
        window_height3 = screen_height3
        window_width3 = 900

        center_x3 = int(screen_width3 / 2 - window_width3 / 2)
        center_y3 = int(screen_height3 / 2 - window_height3 / 2)
        volunteer_entry_screen.geometry(f'{window_width3}x{window_height3}+{center_x3}+{center_y3}')

        emergency_database_file = open("emergency_database.txt", "r")
        emergency_database_list = []
        for line1 in emergency_database_file:
            line_list1 = line1.split("%")
            emergency_database_list.append(line_list1)
        emergency_database_file.close()

        camp_ID_list = []
        for a in range(0, len(emergency_database_list)):
            camp_ID_list.append(emergency_database_list[a][0])

        def campTable():

            headings_frame = Frame(volunteer_entry_screen)

            Label(headings_frame, text="Camp ID:").pack()
            Label(headings_frame, text=f"{user_camp_id}").pack()
            Label(headings_frame, text="Volunteer ID:").pack()
            Label(headings_frame, text=f"{user_id}").pack()
            Label(headings_frame, text="Full Name:").pack()
            Label(headings_frame, text=f"{user_name}").pack()
            Label(headings_frame, text="Username:").pack()
            Label(headings_frame, text=f"{user_username}").pack()
            Label(headings_frame, text="Email:").pack()
            Label(headings_frame, text=f"{user_email}").pack()
            Label(headings_frame, text="Phone Number:").pack()
            Label(headings_frame, text=f"+{user_number_area} {user_number}").pack()
            Label(headings_frame, text="Gender:").pack()
            Label(headings_frame, text=f"{user_gender}").pack()
            Label(headings_frame, text="Date of Birth:").pack()
            Label(headings_frame, text=f"{user_dob} (Age: {user_age})").pack()
            Label(headings_frame, text="Account Status:").pack()
            Label(headings_frame, text=f"{user_status}").pack()
            Label(headings_frame, text="Account Role:").pack()
            Label(headings_frame, text=f"{user_role}").pack()
            Label(headings_frame, text="Your Availability:").pack()
            Label(headings_frame, text=f"{user_availability}").pack()
            Label(headings_frame,
                  text="To edit your availability, please go back to the home page and use Edit Availability Section").pack()

            headings_frame.pack()

            form_frame = Frame(volunteer_entry_screen)
            form_frame.pack()

            def volunteerEntry():
                headings_frame.destroy()

                select_camp_table_button.destroy()

                select_camp_table_label = Label(form_frame,
                                                text="See below the respective locations of the available camps that you could volunteer at. \n Make note of the camp that is closest to your current location.")
                select_camp_table_label.pack()

                select_camp_table_frame = Frame(form_frame)
                select_camp_table_frame.pack()

                select_camp_table = ttk.Treeview(form_frame)
                select_camp_table['columns'] = ("Camp ID", "Camp Name", "Location")

                select_camp_table.column("#0", width=0, stretch=NO)
                select_camp_table.column('Camp ID', anchor=CENTER, width=100)
                select_camp_table.column("Camp Name", anchor=CENTER, width=100)
                select_camp_table.column("Location", anchor=CENTER, width=100)

                select_camp_table.heading('Camp ID', text="Camp ID", anchor=CENTER)
                select_camp_table.heading("Camp Name", text="Camp Name", anchor=CENTER)
                select_camp_table.heading("Location", text="Location", anchor=CENTER)

                for n in range(0, len(emergency_database_list)):
                    select_camp_table.insert(parent='', index=n, iid=n, values=(
                        emergency_database_list[n][0], emergency_database_list[n][1],
                        emergency_database_list[n][4]))

                select_camp_table.pack()

                select_camp = StringVar()
                full_name = StringVar()
                email = StringVar()
                phone_area_code = StringVar()
                phone_number = StringVar()
                gender = StringVar()
                volunteer_date = StringVar()
                volunteer_month = StringVar()
                volunteer_year = StringVar()

                select_camp_label = Label(form_frame, text="Please enter the Camp ID")
                select_camp_label.pack()
                select_camp_select = Entry(form_frame, textvariable=select_camp)
                select_camp_select.insert(END, f"{user_camp_id}")
                select_camp_select.pack()

                full_name_label = Label(form_frame, text="Please enter your full name")
                full_name_label.pack()
                full_name_entry = Entry(form_frame, textvariable=full_name)
                full_name_entry.insert(END, f"{user_name}")
                full_name_entry.pack()

                email_label = Label(form_frame, text="Please enter an email address")
                email_label.pack()
                email_entry = Entry(form_frame, textvariable=email)
                email_entry.insert(END, f"{user_email}")
                email_entry.pack()

                phone_frame = Frame(form_frame)
                phone_frame.pack()

                phone_number_label = Label(phone_frame, text="Please enter a phone number")
                phone_number_label.pack()
                area_code_sign = Label(phone_frame, text="+")
                area_code_sign.pack(side=LEFT)
                phone_number_area_code_entry = Entry(phone_frame, textvariable=phone_area_code)
                phone_number_area_code_entry.insert(END, f"{user_number_area}")
                phone_number_area_code_entry.pack(side=LEFT)
                phone_number_entry = Entry(phone_frame, textvariable=phone_number)
                phone_number_entry.insert(END, f"{user_number}")
                phone_number_entry.pack(side=LEFT)

                gender_list = ["Male", "Female", "Other", "Prefer not to say"]

                gender_label = Label(form_frame, text="Gender:")
                gender_label.pack()
                gender_entry = ttk.Combobox(form_frame, textvariable=gender, values=gender_list)
                gender_entry.insert(END, user_gender)
                gender_entry.pack()

                today = datetime.datetime.today()

                day_list = [str(s) for s in range(1, 32)]
                month_list = [str(s) for s in range(1, 13)]
                year_list = [str(s) for s in range(2023, 1899, -1)]

                dob_label = Label(form_frame, text="Enter your date of birth")
                dob_label.pack()
                dob_frame = Frame(form_frame)
                dob_frame.pack()
                date_day_combobox = ttk.Combobox(dob_frame, textvariable=volunteer_date, values=day_list)
                date_day_combobox.insert(END, user_dob[8:10])
                date_day_combobox.pack(side=LEFT)
                date_month_combobox = ttk.Combobox(dob_frame, textvariable=volunteer_month, values=month_list)
                date_month_combobox.insert(END, user_dob[5:7])
                date_month_combobox.pack(side=LEFT)
                date_year_combobox = ttk.Combobox(dob_frame, textvariable=volunteer_year, values=year_list)
                date_year_combobox.insert(END, user_dob[0:4])
                date_year_combobox.pack(side=LEFT)

                def generate_dob():
                    if len(volunteer_date.get()) == 0 or len(volunteer_month.get()) == 0 or len(
                            volunteer_year.get()) == 0:
                        return "empty"
                    else:
                        try:
                            startdateComplete = ("%s-%s-%s" % (
                            volunteer_year.get(), volunteer_month.get(), volunteer_date.get()))
                            startDateTime = datetime.datetime.strptime(startdateComplete, "%Y-%m-%d")
                            startDate = datetime.datetime.date(startDateTime)
                            return startDate
                        except ValueError:
                            return "empty"

                def generate_age():
                    gx = generate_dob()
                    if gx == "empty":
                        pass
                    else:
                        DOB = datetime.datetime.strptime(str(gx), "%Y-%m-%d").date()
                        volunteer_age = 0

                        if DOB.month < today.month and today.year > DOB.year:
                            volunteer_age = today.year - DOB.year

                        elif DOB.month > DOB.month and today.year > DOB.year:
                            volunteer_age = today.year - DOB.year - 1

                        elif DOB.month == today.month and today.year > DOB.year and today.day < DOB.day:
                            volunteer_age = today.year - DOB.year - 1

                        elif DOB.month == today.month and today.year > DOB.year and today.day > DOB.day:
                            volunteer_age = today.year - DOB.year
                        return volunteer_age

                new_volunteer_error_list = []

                def newvolunteerVerify():
                    dob_label.config(text="DoB is Valid!", fg="green")
                    select_camp_label.config(text="Camp ID is Valid!", fg="green")
                    full_name_label.config(text="Name is Valid!", fg="green")
                    email_label.config(text="Email is Valid!", fg="green")
                    phone_number_label.config(text="Phone Number is Valid!", fg="green")
                    gender_label.config(text="Gender is Valid!", fg="green")
                    new_volunteer_error_list.clear()
                    if generate_age() == 0:
                        dob_label.config(
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
                    if all(char.isalpha() for char in full_name.get().replace(" ", "")) is False:
                        full_name_label.config(text="Name can only contain alphabetical characters", fg='#f00')
                        new_volunteer_error_list.append(1.1)
                    if '@' not in email.get() or '.' not in email.get():
                        email_label.config(
                            text="Please enter a valid email address",
                            fg='#f00')
                        new_volunteer_error_list.append("e3")
                    if len(phone_area_code.get()) > 4 or len(phone_area_code.get()) == 0 or phone_area_code.get().isalnum() is not True:
                        phone_number_label.config(
                            text="Please enter a valid phone area code and a valid phone number",
                            fg='#f00')
                        new_volunteer_error_list.append("e4")
                    if len(phone_number.get()) > 15 or len(
                            phone_number.get()) < 7 or phone_number.get().isalnum() is not True:
                        phone_number_label.config(
                            text="Please enter a valid phone area code and a valid phone number",
                            fg='#f00')
                        new_volunteer_error_list.append("e5")
                    if gender.get() not in gender_list:
                        gender_label.config(text="Please enter a gender from the provided list", fg='#f00')
                        new_volunteer_error_list.append("gender")
                    if generate_dob() == "empty":
                        dob_label.config(text="Please enter DoB", fg='#f00')
                        new_volunteer_error_list.append(5)
                    if generate_dob() != "empty":
                        test_start_date = datetime.datetime.strptime(str(generate_dob()), "%Y-%m-%d")
                        if test_start_date > today:
                            dob_label.config(text="Please enter a valid DoB", fg='#f00')


                    if len(new_volunteer_error_list) > 0:
                        pass
                    else:
                        def createvolunteerSubmit():

                            phone_number_complete = ("%s#%s" % (phone_area_code.get(), phone_number.get()))

                            updated_user = ["NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA"]

                            updated_user[0] = select_camp.get()
                            updated_user[1] = user_id
                            updated_user[2] = full_name.get()
                            updated_user[3] = user_username
                            updated_user[4] = user_password
                            updated_user[5] = email.get()
                            updated_user[6] = phone_number_complete
                            updated_user[7] = gender.get()
                            updated_user[8] = str(generate_dob())
                            updated_user[9] = str(generate_age())
                            if select_camp.get() == user_camp_id:
                                updated_user[10] = user_status
                            else:
                                updated_user[10] = "Deactivated"
                            updated_user[11] = user_role
                            updated_user[12] = user_availability

                            update_details_toplevel = Toplevel()

                            Label(update_details_toplevel,
                                  text="You will now be logged out. Please log back in to see your updated details").pack()
                            if select_camp.get() == user_camp_id:
                                pass
                            else:
                                Label(update_details_toplevel,
                                      text=f"As you have changed the Camp you wish to volunteer at,\nyour account will be temporarily deactivated.\nPlease contact the admin to get your account reactivated at Camp {select_camp.get()}").pack()

                            def logout_login():
                                global main_window

                                volunteer_read = open("volunteer_database.txt", "r")

                                volunteer_list = []
                                for line2 in volunteer_read:
                                    line_string2 = line2.split("%")
                                    volunteer_list.append(line_string2)

                                volunteer_read.close()

                                volunteer_list = [updated_user if num[1] == str(user_id) else num for num in volunteer_list]

                                clear_file = open("volunteer_database.txt", "w")
                                clear_file.close()

                                for entry in volunteer_list:
                                    with open("volunteer_database.txt", "a") as volunteer_write:
                                        updated_user_string = "%".join(entry)
                                        volunteer_write.write(updated_user_string)
                                volunteer_write.close()

                                update_details_toplevel.destroy()
                                volunteer_entry_screen.destroy()
                                volunteer_home.destroy()
                                Login.main()

                            update_details_toplevel_button = Button(update_details_toplevel, text="Proceed", command=logout_login)
                            update_details_toplevel_button.pack()

                            cancel_details_toplevel_button = Button(update_details_toplevel, text="Cancel", command=update_details_toplevel.destroy)
                            cancel_details_toplevel_button.pack()

                        createvolunteerSubmit()

                log_out_info = Label(form_frame, text="Please log out and log back in to see updated details")
                log_out_info.pack()

                emergency_submit_button = Button(form_frame, text="Submit", command=newvolunteerVerify)
                emergency_submit_button.pack()

            select_camp_table_button = Button(volunteer_entry_screen, text="Edit Details", command=volunteerEntry)
            select_camp_table_button.pack()
            back_button = Button(volunteer_entry_screen, text="Cancel", command=volunteer_entry_screen.destroy)
            back_button.pack()

        campTable()

        volunteer_entry_screen.mainloop()

    open_volunteer_file = open("volunteer_database.txt", 'r')
    volunteer_actual_database_list = []
    for line in open_volunteer_file:
        x = line.split("%")
        volunteer_actual_database_list.append(x)
    open_volunteer_file.close()

    volunteer_home = Tk()
    volunteer_home.title("Volunteer Home Page")

    screen_width = volunteer_home.winfo_screenwidth()
    screen_height = volunteer_home.winfo_screenheight()
    window_height = screen_height
    window_width = 900

    center_x = int(screen_width / 2 - window_width / 2)
    center_y = int(screen_height / 2 - window_height / 2)
    volunteer_home.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

    Label(volunteer_home, text="LAMSA", font=("TkDefaultFont", 80, "bold")).pack()
    Label(volunteer_home, text=f"Welcome to Your Portal, {user_name}.\nYou are Volunteering in Camp {user_camp_id}\n", font=("TkDefaultFont", 22)).pack()

    create_new_refugee_button = Button(volunteer_home, text="Add Refugee", command=Volunteer_Create_Family.create_family)
    create_new_refugee_button.pack()

    view_refugee_button = Button(volunteer_home, text="View list of refugees in your camp", command=Volunteer_View_Family.table)
    view_refugee_button.pack()

    change_availability_button = Button(volunteer_home, text="Edit/Manage your availability", command=Volunteer_Add_Availability.add_calendar)
    change_availability_button.pack()

    manage_details = Button(volunteer_home, text="Account Settings", command=Settings)
    manage_details.pack()

    quit_button = Button(volunteer_home, text='Log Out', command=lambda: [volunteer_home.destroy(), Login.main()])
    quit_button.pack()

    volunteer_home.mainloop()
