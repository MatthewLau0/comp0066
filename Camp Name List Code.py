#Import Files
from tkinter import *

#Open the emergency database file and import camp names into a list
def openFile():
    global camp_name_list
    emergency_database_file = open("Final_Files/Emergency_Database.txt", "r")
    emergency_database_list = []
    for line in emergency_database_file:
        line_list = line.split("%")
        emergency_database_list.append(line_list)
    emergency_database_file.close()

    camp_name_list = []
    for i in range (0, len(emergency_database_list)):
        camp_name_list.append((emergency_database_list[i])[1])

    campDropDown()

def campTable():
    global select_camp_table
    global emergency_database_list
    global select_camp_table_label
    global select_camp_table_button
    select_camp_table_label = Label(mock_screen, text="See below the respective locations of the available camps")
    select_camp_table_label.pack()

    select_camp_table_frame = Frame(mock_screen)
    select_camp_table_frame.pack()

    select_camp_table = ttk.Treeview(mock_screen)
    select_camp_table['columns'] = ("Camp Name", "Location")

    select_camp_table.column("#0", width=0, stretch=NO)
    select_camp_table.column("Camp Name", anchor=CENTER, width=100)
    select_camp_table.column("Location", anchor=CENTER, width=100)

    select_camp_table.heading("Camp Name", text="Camp Name", anchor=CENTER)
    select_camp_table_table.heading("Location", text="Location", anchor=CENTER)

    for i in range(0, len(emergency_database_list)):
        select_camp_table.insert(parent='', index=i, iid=i,
                                        values=(emergency_database_list[i][1], emergency_database_list[i][4]))
        i += 1

    select_camp_table.pack()

    select_camp_table_button = Button(mock_screen, text="Continue", command=deleteTable)
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
    global mock_screen


    select_camp = StringVar()
    username = StringVar()
    password = StringVar()
    email = StringVar()
    phone_area_code = StringVar()
    phone_number = StringVar()
    gender = StringVar()
    age = StringVar()
    availability = StringVar()


    select_camp_label = Label(mock_screen, text="Please select a camp")
    select_camp_label.pack()
    select_camp_select = OptionMenu(mock_screen, select_camp, *camp_name_list)
    select_camp_select.pack()

    username_label = Label(mock_screen, text="Please enter a username")
    username_label.pack()
    username_entry = Entry(mock_screen, textvariable=username)
    username_entry.pack()

    password_label = Label(mock_screen, text="Please enter a password")
    password_label.pack()
    password_entry = Entry(mock_screen, textvariable=password)
    password_entry.pack()

    email_label = Label(mock_screen, text="Please enter an email address")
    email_label.pack()
    email_entry = Entry(mock_screen, textvariable=email)
    email_entry.pack()

    phone_number_label = Label(mock_screen, text="Please enter a phone number")
    phone_number_label.pack()
    phone_number_area_code_entry = Entry(mock_screen, textvariable=phone_area_code)
    phone_number_area_code_entry.pack()
    phone_number_entry = Entry(mock_screen, textvariable=phone_number)
    phone_number_entry.pack()

    gender_label = Label(mock_screen, text="Please enter the gender you identify with")
    gender_label.pack()
    gender_entry = Entry(mock_screen, textvariable=gender)
    gender_entry.pack()

    age_label = Label(mock_screen, text="Please enter your age in years")
    age_label.pack()
    age_entry = Entry(mock_screen, textvariable=age)
    age_entry.pack()

    availability_label = Label(mock_screen, text="Please enter your weekly availability")
    availability_label.pack()
    availability_entry = Entry(mock_screen, textvariable=availability)
    availability_entry.pack()

    emergency_submit_button = Button(mock_screen, text="Submit", command=newvolunteerVerify)
    emergency_submit_button.pack()


def newvolunteerVerify():



#Status will be determined by the admin
def createvolunteerSubmit():
    global new_volunteer

    new_volunteer[1] = select_camp.get()
    new_volunteer[2] = username.get()
    new_volunteer[3] = password.get()



#Mock screen creation - CHANGE SCREEN NAME
def mockScreen():
    global mock_screen
    mock_screen = Tk()
    mock_screen.geometry("500x650")
    mock_screen.title("Mock Screen")
    openFile()
    mock_screen.mainloop()

mockScreen()