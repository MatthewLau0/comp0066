#Import modules - is pip included in standard installers
from tkinter import *
import sys
import subprocess
subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'tkcalendar'])
from tkcalendar import Calendar

#Set up the required data structures
    #Open the emergency database file
emergency_database_file = open("Emergency_Database", "r")

    #Create a new emergency
new_emergency = ["NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA"]

    #Convert emergency database files into a list
emergency_database_list = []
for line in emergency_database_file:
    line_list = line.split(",")
    emergency_database_list.append(line_list)

    #Create the index number for the new emergency
if len(emergency_database_list) == 0:
    new_emergency[0] = "1"
elif len(emergency_database_list) >= 1:
    new_emergency[0] = str((int((emergency_database_list[-1])[0]) + 1))

    #Create a list for the camp names already in existence
camp_name_list = []
for i in range(0, len(emergency_database_list)):
    camp_name_list.append((emergency_database_list[i])[1])

#New Camp
def CreateNewCampScreen():
    global New_Camp_Screen
    global camp_name
    global new_emergency
    global index_number
    global emergency_type
    global emergency_description
    global area_affected
    global start_date
    global close_date
    global emergency_status
    global status_check_yes
    global status_check_no
    New_Camp_Screen = Toplevel(Create_New_Emergency_Home_Screen)
    New_Camp_Screen.title("Create a New Emergency")
    New_Camp_Screen.geometry("500x350")

    index_number = StringVar()
    camp_name = StringVar()
    emergency_type = StringVar()
    emergency_description = StringVar()
    area_affected = StringVar()
    start_date = StringVar()
    close_date = StringVar()
    emergency_status = StringVar()

    Label(New_Camp_Screen, text="You are going to make a new emergency plan. Please follow the below instructions").pack()
    Label(New_Camp_Screen, text="The index number for your camp is %s" %(new_emergency[0])).pack()

    camp_name_label = Label(New_Camp_Screen, text="Camp Name * ")
    camp_name_label.pack()
    camp_name_entry = Entry(New_Camp_Screen, textvariable=camp_name)
    camp_name_entry.pack()
    camp_name_verify(camp_name)

    emergency_type_label = Label(New_Camp_Screen, text="Select the type of emergency")
    emergency_type_label.pack()
    emergency_type_list = ["Flood", "Tsunami", "Earthquake", "Drought", "Other"]
    emergency_type.set(emergency_type_list[0])
    emergency_type_select = OptionMenu(New_Camp_Screen, emergency_type, *emergency_type_list)
    emergency_type_select.pack()

    if emergency_type_select == "Other":
        emergency_type_label_other = Label(New_Camp_Screen, text="Specify the type of emergency")
        emergency_type_label_other.pack()
        emergency_type_other = Entry(New_Camp_Screen, textvariable=emergency_type)
        emergency_type_other.pack()
        new_emergency[2] = emergency_type_other
    else:
        new_emergency[2] = emergency_type_select

    emergency_description_label = Label(New_Camp_Screen, text="Briefly describe the emergency")
    emergency_description_label.pack()
    emergency_description_entry = Entry(New_Camp_Screen, textvariable=emergency_description)
    emergency_description_entry.pack()
    new_emergency[3] = emergency_description_entry

    start_date_label = Label(New_Camp_Screen, text="Please select a start date for the emergency from the below calendar")
    start_date_label.pack()
    start_date_calendar = Calendar(New_Camp_Screen, selectmode='day')
    start_date_calendar.pack()

    status_label = Label(New_Camp_Screen, text="Has the emergency finished yet?")
    status_label.pack()
    status_check_yes = IntVar()
    status_check_button_yes = Checkbutton(New_Camp_Screen, variable=status_check_yes, onvalue=1, offvalue=2, text="Yes", command=New_Emergency_Status())
    status_check_button_yes.pack()

    status_check_no = IntVar()
    status_check_button_no = Checkbutton(New_Camp_Screen, variable=status_check_no, onvalue=1, offvalue=2, text="No", command=New_Emergency_Status())
    status_check_button_no.pack()

    submit_new_emergency_button = Button(New_Camp_Screen, text="Submit New Emergency")
    submit_new_emergency_button.pack()

def New_Emergency_Status():
    global status_check_yes
    global status_check_no
    global new_emergency
    global New_Camp_Screen
    if (status_check_yes.get() == 1) & (status_check_no.get() == 2):
        close_date_label = Label(New_Camp_Screen, text="Please select an end date for the emergency from the below calendar")
        close_date_label.pack()
        close_date_calendar = Calendar(New_Camp_Screen, selectmode='day')
        close_date_calendar.pack()
    elif (status_check_yes.get() == 2) & (status_check_no.get() == 1):
        new_emergency[6] = "NA"
        new_emergency[7] = "Active"
    elif (status_check_yes.get() == 1) & (status_check_no.get() == 1):
        status_check_error_label = Label(New_Camp_Screen, text="Please only select one checkbox", fg="#f00", bg="#fff")
        status_check_error_label.pack()




    #Button to run this and then implement into Create New Camp

#Processing of camp_name
def CreateNewCamp():
    pass



#Function for repeated camp namefcff
def camp_name_verify(camp_name):
    global new_emergency
    while camp_name in camp_name_list:
        camp_name_duplicate()
        camp_name_verify(camp_name_entry)
    else:
        new_emergency[1] = camp_name

def camp_name_duplicate():
    camp_name_duplicate_screen = Toplevel(New_Camp_Screen)
    camp_name_duplicate_screen.title("Camp Name Duplicate")
    camp_name_duplicate_screen.geometry("150 x 100")
    Label(camp_name_duplicate_screen, text="This camp name already exists in the database").pack()
    camp_name_entry = Entry(New_Camp_Screen, textvariable=camp_name)
    camp_name_entry.pack()
    return camp_name_entry




#Function for invalid date entry














#Set up the Create New Emergency Screen - ADD IN THIS
def Create_Emergency_Screen():
    global Create_New_Emergency_Home_Screen
    Create_New_Emergency_Home_Screen = Tk()
    Create_New_Emergency_Home_Screen.geometry("500x350")
    Create_New_Emergency_Home_Screen.title("Create New Emergency Main Screen")
    Create_New_Emergency_Button = Button(Create_New_Emergency_Home_Screen, text="Create a New Emergency", command=CreateNewCampScreen())
    Create_New_Emergency_Button.pack()
    Return_HomeScreen_Button = Button(Create_New_Emergency_Home_Screen, text="Return to the Homescreen")
    Return_HomeScreen_Button.pack()


    Create_New_Emergency_Home_Screen.mainloop()

Create_Emergency_Screen()
