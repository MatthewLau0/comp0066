from tkinter import *
from tkinter import ttk
from tkcalendar import Calendar
import datetime
import Login

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


def user_details_generate():
    global user_camp_id
    global user_id
    global user_name
    global user_username
    global user_password
    global user_email
    global user_number_area
    global user_number
    global user_gender
    global user_dob
    global user_age
    global user_status
    global user_role
    global user_availability
    logins_file = open("successful_login.txt", "r")

    logins_list = []
    for line in logins_file:
        line_string = line.split("%")
        logins_list.append(line_string)
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
    else:
        pass
    logins_file.close()

def run():
    user_details_generate()

    volunteer_entry_screen = Toplevel()
    volunteer_entry_screen.geometry("600x1000")
    volunteer_entry_screen.title("Volunteer Entry Screen")

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

        headings_frame = Frame(volunteer_entry_screen)

        Label(headings_frame, text="Camp ID:", font=("Avenis", 16, "bold")).pack()
        Label(headings_frame, text=f"{user_camp_id}").pack()
        Label(headings_frame, text="Volunteer ID:", font=("Avenis", 16, "bold")).pack()
        Label(headings_frame, text=f"{user_id}").pack()
        Label(headings_frame, text="Full Name:", font=("Avenis", 16, "bold")).pack()
        Label(headings_frame, text=f"{user_name}").pack()
        Label(headings_frame, text="Username:", font=("Avenis", 16, "bold")).pack()
        Label(headings_frame, text=f"{user_username}").pack()
        Label(headings_frame, text="Email:", font=("Avenis", 16, "bold")).pack()
        Label(headings_frame, text=f"{user_email}").pack()
        Label(headings_frame, text="Phone Number:", font=("Avenis", 16, "bold")).pack()
        Label(headings_frame, text=f"+{user_number_area} {user_number}").pack()
        Label(headings_frame, text="Gender:", font=("Avenis", 16, "bold")).pack()
        Label(headings_frame, text=f"{user_gender}").pack()
        Label(headings_frame, text="Date of Birth:", font=("Avenis", 16, "bold")).pack()
        Label(headings_frame, text=f"{user_dob} (Age: {user_age})").pack()
        Label(headings_frame, text="Account Status:", font=("Avenis", 16, "bold")).pack()
        Label(headings_frame, text=f"{user_status}").pack()
        Label(headings_frame, text="Account Role:", font=("Avenis", 16, "bold")).pack()
        Label(headings_frame, text=f"{user_role}").pack()
        Label(headings_frame, text="Your Availability:", font=("Avenis", 16, "bold")).pack()
        Label(headings_frame, text=f"{user_availability}").pack()

        headings_frame.pack()

        form_frame = Frame(volunteer_entry_screen)
        form_frame.pack()

        def volunteerEntry():
            headings_frame.destroy()

            select_camp_table_button.destroy()

            for widget in form_frame.winfo_children():
                widget.destroy()

            select_camp = StringVar()
            full_name = StringVar()
            email = StringVar()
            phone_area_code = StringVar()
            phone_number = StringVar()
            gender = StringVar()

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
            phone_number_area_code_entry.pack(side=LEFT, ipadx=1)
            phone_number_entry = Entry(phone_frame, textvariable=phone_number)
            phone_number_entry.insert(END, f"{user_number}")
            phone_number_entry.pack(side=LEFT)

            gender_label = Label(form_frame, text="Please enter the gender you identify with")
            gender_label.pack()
            gender_entry = Entry(form_frame, textvariable=gender)
            gender_entry.insert(END, f"{user_gender}")
            gender_entry.pack()

            today = datetime.datetime.today()
            user_day = user_dob[8:10]
            int_day = int(user_day)
            user_month = user_dob[5:7]
            int_month = int(user_month)
            user_year = user_dob[0:4]
            int_year = int(user_year)


            DOB_calendar_label = Label(form_frame, text="Please enter your date of birth")
            DOB_calendar_label.pack()
            DOB_calendar = Calendar(form_frame, date_pattern="d/m/y", selectmode='day', maxdate=today, day=int_day, month=int_month, year=int_year)
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
                   # if str(volunteer_age) == str(0):
                    #    DOB_calendar_label.config(
                     #       text="Please enter your DOB",
                      #      fg="#f00")
                       # new_volunteer_error_list.append("d1")
                    if select_camp.get() not in camp_ID_list:
                        select_camp_label.config(
                            text="Please enter a valid Camp ID",
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

                        updated_user = ["NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA"]

                        updated_user[0] = select_camp.get()
                        updated_user[1] = user_id
                        updated_user[2] = full_name.get()
                        updated_user[3] = user_username
                        updated_user[4] = user_password
                        updated_user[5] = email.get()
                        updated_user[6] = phone_number_complete
                        updated_user[7] = gender.get()
                        updated_user[8] = str(DOB)
                        updated_user[9] = volunteer_age
                        updated_user[10] = user_status
                        updated_user[11] = user_role
                        updated_user[12] = user_availability


                        volunteer_read = open("volunteer_database.txt", "r")

                        volunteer_list = []
                        for line in volunteer_read:
                            line_string = line.split("%")
                            volunteer_list.append(line_string)

                        for i in volunteer_list:
                            if i[1] == str(user_id):
                                volunteer_list.remove(i)
                                volunteer_list.append(updated_user)

                        clear_file = open("volunteer_database.txt", "w")
                        clear_file.close()

                        for entry in volunteer_list:
                            with open("volunteer_database.txt", "a") as volunteer_write:
                                updated_user_string = "%".join(entry)
                                volunteer_write.write(updated_user_string)


                        closeScreen()

                    createvolunteerSubmit()

            emergency_submit_button = Button(form_frame, text="Submit", command=confirmAge)
            emergency_submit_button.pack()

        select_camp_table_button = Button(volunteer_entry_screen, text="Edit Details", command=volunteerEntry)
        select_camp_table_button.pack()
        back_button = Button(volunteer_entry_screen, text="Cancel",
                             command=lambda: [volunteer_entry_screen.destroy(), Login.main()])
        back_button.pack()

    campTable()

    def closeScreen():
        volunteer_entry_screen.destroy()
        Create_Volunteer_Close_Screen = Tk()
        Create_Volunteer_Close_Screen.title("Volunteer Request Successfully Submitted")
        Create_Volunteer_Close_Screen.geometry("500x650")

        close_label = Label(Create_Volunteer_Close_Screen,
                            text="Thank you for submitting a request to become a volunteer. \n The admin will review your request, and once approved you will be able to access our services.")
        close_label.pack()
        return_home_button = Button(Create_Volunteer_Close_Screen, text="Return to Homescreen",
                                    command=lambda: [Create_Volunteer_Close_Screen.destroy(), Login.main()])
        return_home_button.pack()

    volunteer_entry_screen.mainloop()

