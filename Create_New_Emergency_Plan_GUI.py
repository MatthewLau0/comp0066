#Import modules - is pip included in standard installers
from tkinter import *
import sys
import subprocess
subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'tkcalendar'])
from tkcalendar import Calendar
import datetime
import threading

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
status = "NA"
emergency_type_string = "NA"

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
    global camp_name_entry
    global emergency_type_flood
    global emergency_type_tsunami
    global emergency_type_earthquake
    global emergency_type_drought
    global emergency_type_other
    global emergency_type_flood_check
    global emergency_type_drought_check
    global emergency_type_earthquake_check
    global emergency_type_tsunami_check
    global emergency_type_other_check


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
    # emergency_type_list = ["Flood", "Tsunami", "Earthquake", "Drought", "Other"]
    # emergency_type.set(emergency_type_list[0])
    # emergency_type_select = OptionMenu(New_Camp_Screen, emergency_type, *emergency_type_list)
    # emergency_type_select.pack()

    emergency_type_flood = IntVar()
    emergency_type_tsunami = IntVar()
    emergency_type_earthquake = IntVar()
    emergency_type_drought = IntVar()
    emergency_type_other = IntVar()

    emergency_type_flood_check = Checkbutton(New_Camp_Screen, variable=emergency_type_flood, onvalue=1, offvalue=0, text="Flood", command=clickFlood)
    emergency_type_flood_check.pack()
    emergency_type_tsunami_check = Checkbutton(New_Camp_Screen, variable=emergency_type_tsunami, onvalue=1, offvalue=0, text="Tsunami", command=clickTsunami)
    emergency_type_tsunami_check.pack()
    emergency_type_earthquake_check = Checkbutton(New_Camp_Screen, variable=emergency_type_earthquake, onvalue=1, offvalue=0, text="Earthquake", command=clickEarthquake)
    emergency_type_earthquake_check.pack()
    emergency_type_drought_check = Checkbutton(New_Camp_Screen, variable=emergency_type_drought, onvalue=1, offvalue=0, text="Drought", command=clickDrought)
    emergency_type_drought_check.pack()
    emergency_type_other_check = Checkbutton(New_Camp_Screen, variable=emergency_type_other, onvalue=1, offvalue=0, text="Other", command=clickOther)
    emergency_type_other_check.pack()


    emergency_description_label = Label(New_Camp_Screen, text="Briefly describe the emergency")
    emergency_description_label.pack()
    emergency_description_entry = Entry(New_Camp_Screen, textvariable=emergency_description)
    emergency_description_entry.pack()

    start_date_label = Label(New_Camp_Screen, text="Please select a start date for the emergency from the below calendar")
    start_date_label.pack()
    start_date_calendar = Calendar(New_Camp_Screen, date_pattern="d/m/y", selectmode='day')
    start_date_calendar.pack()

    status_label = Label(New_Camp_Screen, text="Is the emergency active?")
    status_label.pack()

    def clickYes():
        if status_check_yes.get() == 1:
            status_check_button_no.config(state=DISABLED)
        else:
            status_check_button_no.config(state=NORMAL)

    def clickNo():
        if status_check_no.get() == 1:
            status_check_button_yes.config(state=DISABLED)
        else:
            status_check_button_yes.config(state=NORMAL)

    status_check_yes = IntVar()
    status_check_button_yes = Checkbutton(New_Camp_Screen, variable=status_check_yes, onvalue=1, offvalue=2, text="Yes", command=clickYes)
    status_check_button_yes.pack()


    status_check_no = IntVar()
    status_check_button_no = Checkbutton(New_Camp_Screen, variable=status_check_no, onvalue=1, offvalue=2, text="No", command=clickNo)
    status_check_button_no.pack()

    status_check_button = Button(New_Camp_Screen, text="Confirm", command=setactiveStatus)
    status_check_button.pack()

    submit_new_emergency_button = Button(New_Camp_Screen, text="Submit New Emergency", command=campnameVerify)
    submit_new_emergency_button.pack()




def clickFlood():
    global emergency_type
    global emergency_type_flood
    global emergency_type_flood_check
    global emergency_type_drought_check
    global emergency_type_earthquake_check
    global emergency_type_tsunami_check
    global emergency_type_other_check
    global emergency_type_string
    if emergency_type_flood.get() == 1:
        emergency_type_tsunami_check.config(state=DISABLED)
        emergency_type_earthquake_check.config(state=DISABLED)
        emergency_type_drought_check.config(state=DISABLED)
        emergency_type_other_check.config(state=DISABLED)
        emergency_type_string = "Flood"
    else:
        emergency_type_tsunami_check.config(state=NORMAL)
        emergency_type_earthquake_check.config(state=NORMAL)
        emergency_type_drought_check.config(state=NORMAL)
        emergency_type_other_check.config(state=NORMAL)


def clickTsunami():
    global emergency_type
    global emergency_type_drought
    global emergency_type_flood_check
    global emergency_type_drought_check
    global emergency_type_earthquake_check
    global emergency_type_tsunami_check
    global emergency_type_other_check
    global emergency_type_string
    if emergency_type_tsunami.get() == 1:
        emergency_type_flood_check.config(state=DISABLED)
        emergency_type_earthquake_check.config(state=DISABLED)
        emergency_type_drought_check.config(state=DISABLED)
        emergency_type_other_check.config(state=DISABLED)
        emergency_type_string = "Tsunami"
    else:
        emergency_type_flood_check.config(state=NORMAL)
        emergency_type_earthquake_check.config(state=NORMAL)
        emergency_type_drought_check.config(state=NORMAL)
        emergency_type_other_check.config(state=NORMAL)


def clickEarthquake():
    global emergency_type
    global emergency_type_earthquake
    global emergency_type_flood_check
    global emergency_type_drought_check
    global emergency_type_earthquake_check
    global emergency_type_tsunami_check
    global emergency_type_other_check
    global emergency_type_string
    if emergency_type_earthquake.get() == 1:
        emergency_type_tsunami_check.config(state=DISABLED)
        emergency_type_flood_check.config(state=DISABLED)
        emergency_type_drought_check.config(state=DISABLED)
        emergency_type_other_check.config(state=DISABLED)
        emergency_type_string = "Earthquake"
    else:
        emergency_type_tsunami_check.config(state=NORMAL)
        emergency_type_flood_check.config(state=NORMAL)
        emergency_type_drought_check.config(state=NORMAL)
        emergency_type_other_check.config(state=NORMAL)


def clickDrought():
    global emergency_type
    global emergency_type_drought
    global emergency_type_flood_check
    global emergency_type_drought_check
    global emergency_type_earthquake_check
    global emergency_type_tsunami_check
    global emergency_type_other_check
    global emergency_type_string
    if emergency_type_drought.get() == 1:
        emergency_type_tsunami_check.config(state=DISABLED)
        emergency_type_earthquake_check.config(state=DISABLED)
        emergency_type_flood_check.config(state=DISABLED)
        emergency_type_other_check.config(state=DISABLED)
        emergency_type_string = "Drought"
    else:
        emergency_type_tsunami_check.config(state=NORMAL)
        emergency_type_earthquake_check.config(state=NORMAL)
        emergency_type_flood_check.config(state=NORMAL)
        emergency_type_other_check.config(state=NORMAL)


def clickOther():
    global emergency_type
    global emergency_type_other
    global emergency_type_flood_check
    global emergency_type_drought_check
    global emergency_type_earthquake_check
    global emergency_type_tsunami_check
    global emergency_type_other_check
    global emergency_type_string
    global emergency_type_entry

    if emergency_type_other.get() == 1:
        emergency_type_tsunami_check.config(state=DISABLED)
        emergency_type_earthquake_check.config(state=DISABLED)
        emergency_type_drought_check.config(state=DISABLED)
        emergency_type_flood_check.config(state=DISABLED)

        emergency_type_label_other = Label(New_Camp_Screen, text="Specify the type of emergency")
        emergency_type_label_other.pack()
        emergency_type_other = Entry(New_Camp_Screen, textvariable=emergency_type)
        emergency_type_other.pack()
        emergency_type_other_button = Button(New_Camp_Screen, text="Confirm", command=OtherConfirm)
        emergency_type_other_button.pack()


    else:
        emergency_type_tsunami_check.config(state=NORMAL)
        emergency_type_earthquake_check.config(state=NORMAL)
        emergency_type_drought_check.config(state=NORMAL)
        emergency_type_flood_check.config(state=NORMAL)

def OtherConfirm():
    global emergency_type
    global emergency_type_string

    emergency_type_string = emergency_type.get()


def setactiveStatus():
    global status_check_yes
    global status_check_no
    global New_Camp_Screen
    global close_date_calendar
    global status
    global endDate
    global status_error_label
    global close_date_label

    if status_check_no.get() == 1:
        close_date_label = Label(New_Camp_Screen, text="Please select an end date for the emergency from the below calendar")
        close_date_label.pack()
        close_date_calendar = Calendar(New_Camp_Screen, date_pattern="d/m/y", selectmode='day')
        close_date_calendar.pack()
        status = "Closed"

    if (status_check_yes.get() == 1):
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
    global camp_name

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
    global camp_name
    global emergency_type_string
    global emergency_type_other
    global emergency_type_entry

    New_Camp_Summary_Screen = Toplevel(Create_New_Emergency_Home_Screen)
    New_Camp_Summary_Screen.title("Create a New Emergency")
    New_Camp_Summary_Screen.geometry("500x350")

    New_Camp_Summary_Screen_Label = Label(New_Camp_Summary_Screen, text="Please view below a summary of the camp that you are adding to the database")
    New_Camp_Summary_Screen_Label.pack()

    New_Camp_Name_Summary_Label = Label(New_Camp_Summary_Screen, text="The new camp name you are entering is: %s" %(camp_name.get()))
    New_Camp_Name_Summary_Label.pack()

    New_Camp_Type_Summary_Label = Label(New_Camp_Summary_Screen, text="The emergency type for the new camp is: %s" %(emergency_type_string))
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
    global Create_New_Emergency_Home_Screen

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

    New_Emergency_Close_Screen = TopLevel(Create_New_Emergency_Home_Screen)
    New_Emergency_Close_Screen.title("Emergency Successfully Submitted")
    New_Emergency_Close_Screen.geometry("500x650")

    New_Emergency_Close_Screen_Label = Label(New_Emergency_Close_Screen, text="Your new emergency has been successfully saved. Would you like to submit another emergency, or return to homescreen.")
    New_Emergency_Close_Screen_Label.pack()

    Submit_Another_Emergency_Button = Button(New_Emergency_Close_Screen, text="Submit Another Emergency", command=CreateNewCampScreen)
    Submit_Another_Emergency_Button.pack()
    Return_To_HomeScreen_Button = Button(New_Emergency_Close_Screen, text="Return to Homescreen")
    Return_To_HomeScreen_Button.pack()








#Function for repeated camp namefcff
def campnameVerify():
    global camp_name
    global camp_name_list
    global camp_name
    global camp_name_verify

    # if (camp_name_verify in camp_name_list):
    #     camp_name_reentry_Label = Label(New_Camp_Screen,
    #                                     text="This camp name already exists in the database. Please re-enter another camp-name below.",
    #                                     bg='#fff', fg='#f00')
    #     camp_name_reentry_Label.pack()
    #     camp_name_entry.delete(0, END)
    #     camp_name_reentry_button = Button(New_Camp_Screen, text="Resubmit", command=NewCampVerify)
    #     camp_name_reentry_button.pack()
    #     campnameVerify()

    # def campnameverifyLoop():
    #     global camp_name
    #     global camp_name_list
    #     global camp_name_verify
    #
    #     while camp_name_verify in camp_name_list:
    #         camp_name_reentry_Label = Label(New_Camp_Screen,
    #                                             text="This camp name already exists in the database. Please re-enter another camp-name below.",
    #                                             bg='#fff', fg='#f00')
    #         camp_name_reentry_Label.pack()
    #         camp_name_entry.delete(0, END)
    #         camp_name_verify = camp_name.get()
    #         camp_name_reentry_button = Button(New_Camp_Screen, text="Resubmit", command=NewCampVerify)
    #         camp_name_reentry_button.pack()

    camp_name_verify = camp_name.get()
    while (camp_name_verify in camp_name_list):
        camp_name_reentry_Label = Label(New_Camp_Screen,
                                        text="This camp name already exists in the database. Please re-enter another camp-name below.",
                                        bg='#fff', fg='#f00')
        camp_name_reentry_Label.pack()
        camp_name_entry.delete(0, END)
        camp_name_reentry_button = Button(New_Camp_Screen, text="Resubmit", command=campnameVerify)
        camp_name_reentry_button.pack()
        camp_name_verify = camp_name.get()
    else:
        NewCampVerify()











def campnameDuplicate():
    global camp_name

    camp_name_reentry_Label = Label(New_Camp_Screen, text="This camp name already exists in the database. Please re-enter another camp-name below.", bg='#fff', fg='#f00')
    camp_name_reentry_Label.pack()
    camp_name_reentry = Entry(New_Camp_Screen, textvariable=camp_name)
    camp_name_reentry.setvar(" ")
    camp_name_reentry.pack()
    camp_name_reentry_button = Button(New_Camp_Screen, text="Resubmit", command=campnameVerify)
    camp_name_reentry_button.pack()
    campnameVerify()




#Function for invalid date entry

def invalidDate():
    global start_date_calendar
    global close_date_calendar
    global startDate
    global endDate
    global status
    global status_check_yes
    global status_check_no

    startDate = datetime.datetime.strptime(start_date_calendar.get_date(), "%d/%m/%Y").date()

    if status_check_no.get() == 1:
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
