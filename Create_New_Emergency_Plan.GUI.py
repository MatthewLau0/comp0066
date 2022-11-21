#Import modules
from tkinter import *

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
def CreateNewCamp(new_emergency):
    global New_Camp_Screen
    global camp_name
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
    camp_name_verify(camp_name_label)


#Function for repeated camp name
def camp_name_verify(camp_name):
    while camp_name in camp_name_list:
        camp_name_duplicate()
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
















#Set up the Create New Emergency Screen
def Create_Emergency_Screen():
    global Create_New_Emergency_Home_Screen
    Create_New_Emergency_Home_Screen = Tk()
    Create_New_Emergency_Home_Screen.geometry("500x350")
    Create_New_Emergency_Home_Screen.title("Create New Emergency Main Screen")
    Create_New_Emergency_Button = Button(Create_New_Emergency_Home_Screen, text="Create a New Emergency", command=CreateNewCamp())
    Create_New_Emergency_Button.pack()
    Return_HomeScreen_Button = Button(Create_New_Emergency_Home_Screen, text="Return to the Homescreen")
    Return_HomeScreen_Button.pack()


    Create_New_Emergency_Home_Screen.mainloop()

Create_Emergency_Screen()
