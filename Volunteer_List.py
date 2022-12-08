#Import Files
from tkinter import *
from tkinter import ttk

def setupScreen():
    global new_volunteer
    global volunteer_name_list
    global emergency_database_list
    global camp_name_list

    volunteer_file = open("volunteers.txt", "r")
    new_volunteer = ["NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA"]

    current_volunteer_list = []
    for line in volunteer_file:
        line_list = line.split("%")
        current_volunteer_list.append(line_list)

    volunteer_file.close()

    #Create Volunteer Number
    if len(current_volunteer_list) == 0:
        new_volunteer[1] = "1"
    elif len(current_volunteer_list) >= 1:
        new_volunteer[1] = str((int((current_volunteer_list[-1])[0])+1))

    #Create name of current usernames
    volunteer_name_list = []
    for i in range(0, len(current_volunteer_list)):
        volunteer_name_list.append((current_volunteer_list[i])[0])

    #List of camp names
    emergency_database_file = open("Emergency_Database", "r")
    emergency_database_list = []
    for line in emergency_database_file:
        line_list = line.split("%")
        emergency_database_list.append(line_list)
    emergency_database_file.close()

    camp_name_list = []
    for i in range(0, len(emergency_database_list)):
        camp_name_list.append((emergency_database_list[i])[1])

    campTable()



def campTable():
    global select_camp_table
    global emergency_database_list
    global select_camp_table_label
    global select_camp_table_button
    global volunteer_entry_screen
    global emergency_database_list
    global camp_name_list

    select_camp_table_label = Label(volunteer_entry_screen, text="See below the respective locations of the available camps")
    select_camp_table_label.pack()

    select_camp_table_frame = Frame(volunteer_entry_screen)
    select_camp_table_frame.pack()

    select_camp_table = ttk.Treeview(volunteer_entry_screen)
    select_camp_table['columns'] = ("Camp Name", "Location")

    select_camp_table.column("#0", width=0, stretch=NO)
    select_camp_table.column("Camp Name", anchor=CENTER, width=100)
    select_camp_table.column("Location", anchor=CENTER, width=100)

    select_camp_table.heading("Camp Name", text="Camp Name", anchor=CENTER)
    select_camp_table.heading("Location", text="Location", anchor=CENTER)

    for i in range(0, len(emergency_database_list)):
        select_camp_table.insert(parent='', index=i, iid=i,
                                 values=(emergency_database_list[i][1], emergency_database_list[i][4]))
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
    global camp_name_list
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
    global select_camp

    select_camp = StringVar()
    username = StringVar()
    password = StringVar()
    email = StringVar()
    phone_area_code = StringVar()
    phone_number = StringVar()
    gender = StringVar()
    age = StringVar()
    volunteer_availability = StringVar()

    select_camp_label = Label(volunteer_entry_screen, text="Please select a camp")
    select_camp_label.pack()
    select_camp_select = OptionMenu(volunteer_entry_screen, select_camp, *camp_name_list)
    select_camp_select.pack()

    username_label = Label(volunteer_entry_screen, text="Please enter a username")
    username_label.pack()
    username_entry = Entry(volunteer_entry_screen, textvariable=username)
    username_entry.pack()

    password_label = Label(volunteer_entry_screen, text="Please enter a password")
    password_label.pack()
    password_entry = Entry(volunteer_entry_screen, textvariable=password)
    password_entry.pack()

    email_label = Label(volunteer_entry_screen, text="Please enter an email address")
    email_label.pack()
    email_entry = Entry(volunteer_entry_screen, textvariable=email)
    email_entry.pack()

    phone_number_label = Label(volunteer_entry_screen, text="Please enter a phone number")
    phone_number_label.pack()
    phone_number_area_code_entry = Entry(volunteer_entry_screen, textvariable=phone_area_code)
    phone_number_area_code_entry.pack()
    phone_number_entry = Entry(volunteer_entry_screen, textvariable=phone_number)
    phone_number_entry.pack()

    gender_label = Label(volunteer_entry_screen, text="Please enter the gender you identify with")
    gender_label.pack()
    gender_entry = Entry(volunteer_entry_screen, textvariable=gender)
    gender_entry.pack()

    age_label = Label(volunteer_entry_screen, text="Please enter your age in years")
    age_label.pack()
    age_entry = Entry(volunteer_entry_screen, textvariable=age)
    age_entry.pack()

    availability_label = Label(volunteer_entry_screen, text="Please enter your weekly availability")
    availability_label.pack()
    availability_entry = Entry(volunteer_entry_screen, textvariable=volunteer_availability)
    availability_entry.pack()

    emergency_submit_button = Button(volunteer_entry_screen, text="Submit", command=newvolunteerVerify)
    emergency_submit_button.pack()

#def selectCamp():
    #global select_camp
    #newvolunteerVerify()

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

    if username.get() in volunteer_name_list:
        username_label.config(text="This username already exists. Please enter another username", fg='#f00')
    if len(username.get()) == 0 or username.get() == ' ' or username.get().isalpha() != True:
        username_label.config(text="Please enter a valid username (no spaces, no numbers)", fg='#f00')
    if len(password.get()) == 0 or password.get() == ' ':
        password_label.config(text="Please enter a valid password", fg='#f00')
    if '@' not in email.get() or '.' not in email.get():
        email_label.config(text="Please enter a valid email address", fg='#f00')
    if '+' not in phone_area_code.get() or len(phone_area_code.get())>4:
        phone_number_label.config(text="Please enter a valid phone area code (including a + symbol) and a valid phone number", fg='#f00')
    if len(phone_number.get())>15 or len(phone_number.get()) < 7 or phone_number.get().isalpha() == True or phone_number.get().isalnum() != True:
        phone_number_label.config(text="Please enter a valid phone area code (including a + symbol) and a valid phone number", fg='#f00')
    if len(gender.get()) == 0 or gender.get() == ' ':
        gender_label.config(text="Please enter a gender. If you prefer not to specify a gender, enter n/a.", fg='#f00')
    if age.get().isalpha() == True or age.get().isalnum() != True:
        age_label.config(text="Please enter a valid age (numbers only).", fg='#f00')
    if len(volunteer_availability.get()) == 0 or (volunteer_availability.get() == ' '):
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

    phone_number_complete = ("%s%s"%(phone_area_code.get(), phone_number.get()))

    new_volunteer[1] = select_camp.get()
    new_volunteer[2] = username.get()
    new_volunteer[3] = password.get()
    new_volunteer[4] = email.get()
    new_volunteer[5] = phone_number_complete
    new_volunteer[6] = gender.get()
    new_volunteer[7] = age.get()
    new_volunteer[8] = volunteer_availability.get()

    new_volunteer_string = '%'.join(new_volunteer)

    volunteer_file_append = open("volunteers.txt", "a")
    volunteer_file_append.write("\n%s" %(new_volunteer_string))
    volunteer_file_append.close()


#Screen Setup

def VolunteerEntryScreen():
    global volunteer_entry_screen
    volunteer_entry_screen = Toplevel()
    volunteer_entry_screen.geometry("500x600")
    volunteer_entry_screen.title("Volunteer Entry Screen")
    setupScreen()

    volunteer_entry_screen.mainloop()

VolunteerEntryScreen()

