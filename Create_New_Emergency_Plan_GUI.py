#Import modules - is pip included in standard installers
from tkinter import *
import sys
import subprocess
subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'tkcalendar'])
from tkcalendar import Calendar
import datetime

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

emergency_database_file.close()

    #Create the index number for the new emergency
if len(emergency_database_list) == 0:
    new_emergency[0] = "1"
elif len(emergency_database_list) >= 1:
    new_emergency[0] = str((int((emergency_database_list[-1])[0]) + 1))

    #Create a list for the camp names already in existence
camp_name_list = []
for i in range(0, len(emergency_database_list)):
    camp_name_list.append((emergency_database_list[i])[1])

#Establish some variables
startDate = "NA"
endDate = "NA"

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
    global start_date_calendar
    New_Camp_Screen = Toplevel(Create_New_Emergency_Home_Screen)
    New_Camp_Screen.title("Create a New Emergency")
    New_Camp_Screen.geometry("500x600")

    index_number = StringVar()
    camp_name = StringVar()
    emergency_type = StringVar()
    emergency_description = StringVar()
    area_affected = StringVar()
    start_date = StringVar()
    close_date = StringVar()
    emergency_status = StringVar()

    New_Camp_Screen_Label = Label(New_Camp_Screen, text="You are going to make a new emergency plan. Please follow the below instructions")
    New_Camp_Screen_Label.pack()
    New_Camp_Screen_Label_Index = Label(New_Camp_Screen, text="The index number for your camp is %s" %(new_emergency[0]))
    New_Camp_Screen_Label_Index.pack()

    camp_name_label = Label(New_Camp_Screen, text="Camp Name * ")
    camp_name_label.pack()
    camp_name_entry = Entry(New_Camp_Screen, textvariable=camp_name)
    camp_name_entry.pack()

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

    emergency_description_label = Label(New_Camp_Screen, text="Briefly describe the emergency")
    emergency_description_label.pack()
    emergency_description_entry = Entry(New_Camp_Screen, textvariable=emergency_description)
    emergency_description_entry.pack()

    start_date_label = Label(New_Camp_Screen, text="Please select a start date for the emergency from the below calendar")
    start_date_label.pack()
    start_date_calendar = Calendar(New_Camp_Screen, date_pattern="d/m/y", selectmode='day')
    start_date_calendar.pack()

    status_label = Label(New_Camp_Screen, text="Has the emergency finished yet?")
    status_label.pack()

    status_check_yes = IntVar()
    status_check_button_yes = Checkbutton(New_Camp_Screen, variable=status_check_yes, onvalue=1, offvalue=2, text="Yes", command=setactiveStatus)
    status_check_button_yes.pack()

    status_check_no = IntVar()
    status_check_button_no = Checkbutton(New_Camp_Screen, variable=status_check_no, onvalue=1, offvalue=2, text="No")
    status_check_button_no.pack()

    submit_new_emergency_button = Button(New_Camp_Screen, text="Submit New Emergency")
    submit_new_emergency_button.pack()

    closedateSet()
    NewCampVerify()

def closedateSet():
    global status_check_yes
    global status_check_no
    global New_Camp_Screen
    global close_date_calendar
    global status
    global status_error_label
    global close_date_label

    while status_check_no.get() == 1:
        if status_check_yes.get() == 2:
            status_error_label.destroy()
            close_date_label = Label(New_Camp_Screen, text="Please select an end date for the emergency from the below calendar")
            close_date_label.pack()
            close_date_calendar = Calendar(New_Camp_Screen, date_pattern="d/m/y", selectmode='day')
            close_date_calendar.pack()
            status = "Closed"
            break
        elif status_check_yes.get() == 2:
            status_error_label = Label(New_Camp_Screen, text="Please only tick one checkbox.")
            status_error_label.pack()


def setactiveStatus():
    global status_check_yes
    global status_check_no
    global New_Camp_Screen
    global close_date_calendar
    global status
    global endDate
    global status_error_label
    global close_date_label

    if (status_check_no.get() == 1) and (status_check_yes.get() == 1):
        status_error_label = Label(New_Camp_Screen, text="Please only tick one checkbox.")
        status_error_label.pack()

    if (status_check_yes.get() == 1) and (status_check_no.get() == 2):
        status_error_label.destroy()
        close_date_calendar.destroy()
        close_date_label.destroy()
        endDate = "NA"
        status = "Active"


def NewCampVerify():
    global New_Camp_Screen
    global camp_name
    global new_emergency
    global index_number
    global emergency_type
    global emergency_description
    global area_affected
    global start_date_calendar
    global close_date_calendar
    global emergency_status
    global status_check_yes
    global status_check_no

    campnameVerify(camp_name)
    invalidDate()
    CreateNewCampSummary()


#Processing of camp_name
def CreateNewCampSummary():
    global New_Camp_Screen
    global camp_name_entry
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
    global startDate
    global endDate
    global status
    New_Camp_Summary_Screen = Toplevel(Create_New_Emergency_Home_Screen)
    New_Camp_Summary_Screen.title("Create a New Emergency")
    New_Camp_Summary_Screen.geometry("500x350")

    New_Camp_Summary_Screen_Label = Label(New_Camp_Summary_Screen, text="Please view below a summary of the camp that you are adding to the database")
    New_Camp_Summary_Screen_Label.pack()

    New_Camp_Name_Summary_Label = Label(New_Camp_Summary_Screen, text="The new camp name you are entering is: %s" %(camp_name.get()))
    New_Camp_Name_Summary_Label.pack()

    New_Camp_Type_Summary_Label = Label(New_Camp_Summary_Screen, text="The emergency type for the new camp is: %s" %(emergency_type.get()))
    New_Camp_Type_Summary_Label.pack()

    New_Camp_Description_Summary_Label = Label(New_Camp_Summary_Screen, text="Your description of the new emergency is: %s" %(emergency_description.get()))
    New_Camp_Description_Summary_Label.pack()

    New_Camp_StartDate_Summary_Label = Label(New_Camp_Summary_Screen, text="The start date of the new emergency is: %s" %(startDate))
    New_Camp_StartDate_Summary_Label.pack()

    New_Camp_EndDate_Summary_Label = Label(New_Camp_Summary_Screen, text="The end date of the new emergency is: %s" %(endDate))
    New_Camp_EndDate_Summary_Label.pack()

    New_Camp_Status_Summary_Label = Label(New_Camp_Summary_Screen, text="The status of the new emergency is: %s" %(status))
    New_Camp_Status_Summary_Label.pack()

    New_Camp_Submission_Button = Button(New_Camp_Summary_Screen, text="Submit", command=SubmitEmergency)
    New_Camp_Submission_Button.pack()


def SubmitEmergency():
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
    global startDate
    global endDate
    global status

    new_emergency[1] = camp_name.get()
    new_emergency[2] = emergency_type.get()
    new_emergency[3] = emergency_description.get()
    new_emergency[5] = str(startDate)
    new_emergency[6] = str(endDate)
    new_emergency[7] = status

    new_emergency_string = ','.join(new_emergency)

    emergency_database_file_append = open("Emergency_Database", "a")
    emergency_database_file_append.write("\n%s" %(new_emergency_string))
    emergency_database_file_append.close()

    New_Emergency_Close_Screen_Label = Label(New_Emergency_Close_Screen, text="Your new emergency has been successfully saved.")
    New_Emergency_Close_Screen_Label.pack()



#Function for repeated camp namefcff
def campnameVerify(camp_name):
    global new_emergency
    while camp_name in camp_name_list:
        campnameDuplicate()
        campnameVerify(camp_name)

def campnameDuplicate():
    camp_name_duplicate_screen = Toplevel(New_Camp_Screen)
    camp_name_duplicate_screen.title("Camp Name Duplicate")
    camp_name_duplicate_screen.geometry("150 x 100")
    Label(camp_name_duplicate_screen, text="This camp name already exists in the database").pack()
    camp_name_entry = Entry(New_Camp_Screen, textvariable=camp_name)
    camp_name_entry.pack()
    return camp_name




#Function for invalid date entry

def invalidDate():
    global start_date_calendar
    global close_date_calendar
    global startdate
    global endDate
    global status
    global status_check_yes
    global status_check_no

    startDate = datetime.datetime.strptime(start_date_calendar.get_date(), "%d/%m/%Y").date()

    if ((status_check_yes == 2) and (status_check_no == 1)):
        endDate = datetime.datetime.strptime(close_date_calendar.get_date(), "%d/%m/%Y").date()
        while endDate < startDate:
            invalidDate_label = Label(New_Camp_Screen, text="The end date has to be after the start date. Please re-enter a close date below.")
            invalidDate_label.pack()
            close_date_label = Label(New_Camp_Screen, text="Please select an end date for the emergency from the below calendar")
            close_date_label.pack()
            close_date_calendar = Calendar(New_Camp_Screen, date_pattern="d/m/y", selectmode='day')
            close_date_calendar.pack()
            endDate = datetime.datetime.strptime(end_date_calendar.get_date(), "%d, %m, %Y").date()













#Set up the Create New Emergency Screen - ADD IN THIS
def Create_Emergency_Screen():
    global Create_New_Emergency_Home_Screen
    Create_New_Emergency_Home_Screen = Tk()
    Create_New_Emergency_Home_Screen.geometry("500x600")
    Create_New_Emergency_Home_Screen.title("Create New Emergency Main Screen")
    Create_New_Emergency_Button = Button(Create_New_Emergency_Home_Screen, text="Create a New Emergency", command=CreateNewCampScreen)
    Create_New_Emergency_Button.pack()
    Return_HomeScreen_Button = Button(Create_New_Emergency_Home_Screen, text="Return to the Homescreen")
    Return_HomeScreen_Button.pack()


    Create_New_Emergency_Home_Screen.mainloop()

Create_Emergency_Screen()
