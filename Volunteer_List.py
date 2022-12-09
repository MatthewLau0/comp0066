#Import Files
from tkinter import *
from tkinter import ttk
import sys
import subprocess
subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'tkcalendar'])
from tkcalendar import Calendar
import datetime

def volunteerList(screen):
    volunteer_screen = screen
    def setupScreen():
        global new_volunteer
        global volunteer_name_list
        global emergency_database_list
        global camp_ID_list
        global current_volunteer_list
        global username
        global password


        current_volunteer_list = []
        volunteer_file = open("volunteers.txt", "r")
        for line in volunteer_file:
            line_list = line.split("%")
            current_volunteer_list.append(line_list)

        volunteer_file.close()
        #del current_volunteer_list[-1]

        new_volunteer = ["NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA"]

        new_volunteer[1] = current_volunteer_list[-1][1]
        new_volunteer[3] = current_volunteer_list[-1][3]
        new_volunteer[4] = current_volunteer_list[-1][4]
        del current_volunteer_list[-1]


        #List of camp names
        emergency_database_file = open("Emergency_Database", "r")
        emergency_database_list = []
        for line in emergency_database_file:
            line_list = line.split("%")
            emergency_database_list.append(line_list)
        emergency_database_file.close()

        camp_ID_list = []
        for i in range(0, len(emergency_database_list)):
            camp_ID_list.append(emergency_database_list[i][0])

        campTable()



    def campTable():
        global select_camp_table
        global emergency_database_list
        global select_camp_table_label
        global select_camp_table_button
        global volunteer_entry_screen
        global emergency_database_list
        global camp_ID_list
        global new_volunteer

        volunteer_number_print = Label(volunteer_entry_screen, text="Your volunteer numbers is %s" %(new_volunteer[1]))
        volunteer_number_print.pack()

        select_camp_table_label = Label(volunteer_entry_screen, text="See below the respective locations of the available camps that you could volunteer at. \n Make note of the camp that is closest to your current location.")
        select_camp_table_label.pack()

        select_camp_table_frame = Frame(volunteer_entry_screen)
        select_camp_table_frame.pack()

        select_camp_table = ttk.Treeview(volunteer_entry_screen)
        select_camp_table['columns'] = ("Camp ID", "Camp Name", "Location")

        select_camp_table.column("#0", width=0, stretch=NO)
        select_camp_table.column('Camp ID', anchor=CENTER, width=100)
        select_camp_table.column("Camp Name", anchor=CENTER, width=100)
        select_camp_table.column("Location", anchor=CENTER, width=100)

        select_camp_table.heading('Camp ID', text="Camp ID", anchor=CENTER)
        select_camp_table.heading("Camp Name", text="Camp Name", anchor=CENTER)
        select_camp_table.heading("Location", text="Location", anchor=CENTER)

        for i in range(0, len(emergency_database_list)):
            select_camp_table.insert(parent='', index=i, iid=i,
                                     values=(emergency_database_list[i][0], emergency_database_list[i][1], emergency_database_list[i][4]))
            i += 1

        select_camp_table.pack()

        select_camp_table_button = Button(volunteer_entry_screen, text="Continue", command=deleteTable)
        select_camp_table_button.pack()


    def deleteTable():
        global select_camp_table
        global select_camp_table_label
        global select_camp_table_button

        select_camp_table.destroy()
        select_camp_table_button.destroy()
        select_camp_table_button.destroy()
        volunteerEntry()


    def volunteerEntry():
        global camp_ID_list
        global volunteer_entry_screen
        global select_camp_label
        global username_label
        global password_label
        global email_label
        global phone_number_label
        global gender_label
        global age_label
        global availability_label
        global email
        global phone_area_code
        global phone_number
        global gender
        global age
        global volunteer_availability
        global select_camp
        global volunteer_age
        global full_name
        global DOB
        global age

        select_camp = StringVar()
        full_name = StringVar()
        email = StringVar()
        phone_area_code = StringVar()
        phone_number = StringVar()
        gender = StringVar()
        age = StringVar()
        volunteer_availability = StringVar()

        select_camp_label = Label(volunteer_entry_screen, text="Please select a camp")
        select_camp_label.pack()
        select_camp_select = OptionMenu(volunteer_entry_screen, select_camp, *camp_ID_list)
        select_camp_select.pack()

        full_name_label = Label(volunteer_entry_screen, text="Please enter your full name")
        full_name_label.pack()
        full_name_entry = Entry(volunteer_entry_screen, textvariable=full_name)
        full_name_entry.pack()


        email_label = Label(volunteer_entry_screen, text="Please enter an email address")
        email_label.pack()
        email_entry = Entry(volunteer_entry_screen, textvariable=email)
        email_entry.pack()

        phone_frame = Frame(volunteer_entry_screen)
        phone_frame.pack()

        phone_number_label = Label(phone_frame, text="Please enter a phone number")
        phone_number_label.pack()
        area_code_sign = Label(phone_frame, text="+")
        area_code_sign.pack(side=LEFT)
        phone_number_area_code_entry = Entry(phone_frame, textvariable=phone_area_code)
        phone_number_area_code_entry.pack(side=LEFT, ipadx=1)
        phone_number_entry = Entry(phone_frame, textvariable=phone_number)
        phone_number_entry.pack(side=LEFT)

        gender_label = Label(volunteer_entry_screen, text="Please enter the gender you identify with")
        gender_label.pack()
        gender_entry = Entry(volunteer_entry_screen, textvariable=gender)
        gender_entry.pack()

        today = datetime.datetime.today()

        DOB_calendar_label = Label(volunteer_entry_screen, text="Please enter your date of birth")
        DOB_calendar_label.pack()
        DOB_calendar = Calendar(volunteer_entry_screen, date_pattern="d/m/y", selectmode='day', maxdate=today)
        DOB_calendar.pack()

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

        availability_label = Label(volunteer_entry_screen, text="Please enter your weekly availability")
        availability_label.pack()
        availability_entry = Entry(volunteer_entry_screen, textvariable=volunteer_availability)
        availability_entry.pack()

        emergency_submit_button = Button(volunteer_entry_screen, text="Submit", command=newvolunteerVerify)
        emergency_submit_button.pack()


    def newvolunteerVerify():
        global volunteer_name_list
        global volunteer_entry_screen
        global select_camp_label
        global username_label
        global password_label
        global email_label
        global phone_number_label
        global gender_label
        global age_label
        global availability_label
        global username
        global password
        global email
        global phone_area_code
        global phone_number
        global gender
        global age
        global volunteer_availability

        if '@' not in email.get() or '.' not in email.get():
            email_label.config(text="Please enter a valid email address", fg='#f00')
        elif len(phone_area_code.get())>4:
            phone_number_label.config(text="Please enter a valid phone area code (including a + symbol) and a valid phone number", fg='#f00')
        elif len(phone_number.get())>15 or len(phone_number.get()) < 7 or phone_number.get().isalnum() != True:
            phone_number_label.config(text="Please enter a valid phone area code (including a + symbol) and a valid phone number", fg='#f00')
        elif len(gender.get()) == 0 or gender.get() == ' ':
            gender_label.config(text="Please enter a gender. If you prefer not to specify a gender, enter n/a.", fg='#f00')
        elif len(volunteer_availability.get()) == 0 or (volunteer_availability.get() == ' '):
            availability_label.config(text="Please enter a valid availabilty", fg='#f00')
        else:
            createvolunteerSubmit()



    # Status will be determined by the admin
    def createvolunteerSubmit():
        global new_volunteer
        global username
        global password
        global email
        global phone_area_code
        global phone_number
        global gender
        global age
        global volunteer_availability
        global select_camp
        global DOB
        global age
        global current_volunteer_list
        global volunteer_age

        phone_number_complete = ("%s%s"%(phone_area_code.get(), phone_number.get()))

        new_volunteer[0] = select_camp.get()
        new_volunteer[2] = full_name.get()
        new_volunteer[5] = email.get()
        new_volunteer[6] = phone_number_complete
        new_volunteer[7] = gender.get()
        new_volunteer[8] = str(DOB)
        new_volunteer[9] = volunteer_age
        new_volunteer[10] = "Deactivated"
        new_volunteer[11] = "Standard"

        current_volunteer_list.append(new_volunteer)
        volunteer_file_write = open("volunteers.txt", "r+")
        for i in range(0, len(current_volunteer_list)):
            current_volunteer_string = '%'.join(current_volunteer_list[i])
            volunteer_file_write.write("%s" %(current_volunteer_string))
            i += 1
        volunteer_file_write.close()
        closeScreen()


    def closeScreen():
        global volunteer_entry_screen
        Create_Volunteer_Close_Screen = Toplevel(volunteer_entry_screen)
        Create_Volunteer_Close_Screen.title("Volunteer Request Successfully Submitted")
        Create_Volunteer_Close_Screen.geometry("500x650")

        close_label = Label(Create_Volunteer_Close_Screen, text="Thank you for submitting a request to become a volunteer. \n The admin will review your request, and once approved you will be able to access our services.")
        close_label.pack()
        return_home_button = Button(Create_Volunteer_Close_Screen, text="Return to Homescreen", command=returnHome)
        return_home_button.pack()

    def returnHome():
        from LoginPage_v3_Arjun import loginPage
        loginPage()



    #Screen Setup

    def VolunteerEntryScreen(screen):
        global volunteer_entry_screen
        volunteer_entry_screen = Toplevel(screen)
        volunteer_entry_screen.geometry("500x600")
        volunteer_entry_screen.title("Volunteer Entry Screen")
        setupScreen()

        volunteer_entry_screen.mainloop()

    VolunteerEntryScreen(volunteer_screen)
