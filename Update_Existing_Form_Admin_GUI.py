#NEED TO ADD AREA AFFECTED INFORMATION

#Import functions
from tkinter import *
from tkinter import ttk
import sys
import subprocess
import datetime
subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'tkcalendar'])
subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'tkintermapview'])
from tkcalendar import Calendar



def setupUpdate():
    global startDate
    global endDate
    global status
    global emergency_type_string
    global emergency_marker_country
    global emergency_database_list

    emergency_database_file = open("Emergency_Database", "r")
    emergency_database_list = []
    for line in emergency_database_file:
        line_list = line.split(",")
        emergency_database_list.append(line_list)
    emergency_database_file.close()
    UpdateEmergencyScreen()

    # Establish some variables
    startDate = "NA"
    endDate = "NA"
    status = "NA"
    emergency_type_string = "NA"
    emergency_marker_country = "NA"

def UpdateEmergencyScreen():
    global Update_Emergency_Home_Screen
    global Update_Emergency_Screen
    global emergency_database_list
    global View_Table_Yes
    Update_Emergency_Screen = Toplevel(Update_Emergency_Home_Screen)
    Update_Emergency_Screen.title("Update an existing emergency")
    Update_Emergency_Screen.geometry("500x600")

    Update_Emergency_Screen_Label = Label(Update_Emergency_Screen, text="You are going to update an existing emergency plan. Please follow the below instructions")
    Update_Emergency_Screen_Label.pack()

    View_Table_Label = Label(Update_Emergency_Screen, text="Would you like to view a summary of all of the projects currently in the database?")
    View_Table_Label.pack()

    View_Table_Yes = IntVar()
    View_Table_No = IntVar()

    view_table_check_yes = Checkbutton(Update_Emergency_Screen, variable=View_Table_Yes, onvalue=1, offvalue=2, text="Yes", command=ViewTable)
    view_table_check_yes.pack()

    view_table_check_no = Checkbutton(Update_Emergency_Screen, variable=View_Table_No, onvalue=1, offvalue=2, text="No", command=SelectIndex)
    view_table_check_no.pack()

def ViewTable():
    global Update_Emergency_Screen
    global emergency_database_list
    global View_Table_Yes
    global Index_Known_No
    global emergency_database_table

    emergency_database_label = Label(Update_Emergency_Screen, text="Please use the below table to find the index number of the emergency you would like to update")
    emergency_database_label.pack()

    emergency_database_frame = Frame(Update_Emergency_Screen)
    emergency_database_frame.pack()

    emergency_database_table = ttk.Treeview(emergency_database_frame)

    emergency_database_table['columns'] = ("Camp ID", "Camp Name", "Emergency Type", "Emergency Description", "Area Affected", "Start Date", "Close Date", "Status")

    emergency_database_table.column("#0", width=0, stretch=NO)
    emergency_database_table.column("Camp ID", anchor=CENTER, width=100)
    emergency_database_table.column("Camp Name", anchor=CENTER, width=100)
    emergency_database_table.column("Emergency Type", anchor=CENTER, width=100)
    emergency_database_table.column("Emergency Description", anchor=CENTER, width=100)
    emergency_database_table.column("Area Affected", anchor=CENTER, width=100)
    emergency_database_table.column("Start Date", anchor=CENTER, width=100)
    emergency_database_table.column("Close Date", anchor=CENTER, width=100)
    emergency_database_table.column("Status", anchor=CENTER, width=100)

    emergency_database_table.heading("Camp ID", text="Camp ID", anchor=CENTER)
    emergency_database_table.heading("Camp Name", text="Camp Name", anchor=CENTER)
    emergency_database_table.heading("Emergency Type", text="Emergency Type", anchor=CENTER)
    emergency_database_table.heading("Emergency Description", text="Emergency Description", anchor=CENTER)
    emergency_database_table.heading("Area Affected", text="Area Affected", anchor=CENTER)
    emergency_database_table.heading("Start Date", text="Start Date", anchor=CENTER)
    emergency_database_table.heading("Close Date", text="Close Date", anchor=CENTER)
    emergency_database_table.heading("Status", text="Status", anchor=CENTER)

    #https://pythonguides.com/python-tkinter-table-tutorial/
    for i in range(0, len(emergency_database_list)):
        emergency_database_table.insert(parent='', index=i, iid=i, values=(emergency_database_list[i][0], emergency_database_list[i][1], emergency_database_list[i][2], emergency_database_list[i][3], emergency_database_list[i][4], emergency_database_list[i][5], emergency_database_list[i][6], emergency_database_list[i][7]))
        i += 1

    emergency_database_table.pack()

    emergency_database_table_button = Button(Update_Emergency_Screen, text="Continue", command=deleteTable)
    emergency_database_table_button.pack()

def deleteTable():
    global emergency_database_table
    global View_Table_Yes
    global Index_Known_No
    emergency_database_table.destroy()
    if View_Table_Yes.get() == 1:
        IndexKnown()
    elif Index_Known_No.get() == 1:
        SelectIndex()
    else:
        IndexKnown()


def IndexKnown():
    global Update_Emergency_Screen
    global Index_Known_No

    Index_Known_Yes = IntVar()
    Index_Known_No = IntVar()

    Index_Known_Label = Label(Update_Emergency_Screen, text="Do you know the index number of the camp that you would like to update?")
    Index_Known_Label.pack()
    index_known_yes = Checkbutton(Update_Emergency_Screen, variable=Index_Known_Yes, onvalue=1, offvalue=2, text="Yes", command=SelectIndex)
    index_known_yes.pack()
    index_known_no = Checkbutton(Update_Emergency_Screen, variable=Index_Known_No, onvalue=1, offvalue=2, text="No", command=ViewTable)
    index_known_no.pack()

def SelectIndex():
    global Update_Emergency_Screen
    global emergency_database_list
    global select_index

    select_index = StringVar()

    emergency_database_list_index = []
    for i in range(0, len(emergency_database_list)):
        emergency_database_list_index.append((emergency_database_list[i])[0])
        i += 1

    select_index_label = Label(Update_Emergency_Screen, text="Please select the index number of the camp you would like to update")
    select_index_label.pack()

    select_index_select = OptionMenu(Update_Emergency_Screen, select_index, *emergency_database_list_index)
    select_index_select.pack()

    select_index_select_button = Button(Update_Emergency_Screen, text="Submit", command=printupdatingCamp)
    select_index_select_button.pack()


def printupdatingCamp():
    global Update_Emergency_Screen
    global emergency_database_list
    global select_index
    global index_updating_camp
    global emergency_database_list
    global updating_camp_list


    index_updating_camp = int(select_index.get())
    index_updating_camp = (index_updating_camp-1)

    updating_camp_list = []
    for i in range(0, len(emergency_database_list[index_updating_camp])):
        updating_camp_list.append((emergency_database_list[index_updating_camp])[i])
        i += 1

    index_select_label = Label(Update_Emergency_Screen, text="You are updating camp %d"%(index_updating_camp))
    index_select_label.pack()

    update_emergency_frame = Frame(Update_Emergency_Screen)
    update_emergency_frame.pack()

    update_emergency_table = ttk.Treeview(update_emergency_frame)

    update_emergency_table['columns'] = ("Camp ID", "Camp Name", "Emergency Type", "Emergency Description", "Area Affected", "Start Date", "Close Date", "Status")

    update_emergency_table.column("#0", width=0, stretch=NO)
    update_emergency_table.column("Camp ID", anchor=CENTER, width=100)
    update_emergency_table.column("Camp Name", anchor=CENTER, width=100)
    update_emergency_table.column("Emergency Type", anchor=CENTER, width=100)
    update_emergency_table.column("Emergency Description", anchor=CENTER, width=200)
    update_emergency_table.column("Area Affected", anchor=CENTER, width=100)
    update_emergency_table.column("Start Date", anchor=CENTER, width=100)
    update_emergency_table.column("Close Date", anchor=CENTER, width=100)
    update_emergency_table.column("Status", anchor=CENTER, width=100)

    update_emergency_table.heading("Camp ID", text="Camp ID", anchor=CENTER)
    update_emergency_table.heading("Camp Name", text="Camp Name", anchor=CENTER)
    update_emergency_table.heading("Emergency Type", text="Emergency Type", anchor=CENTER)
    update_emergency_table.heading("Emergency Description", text="Emergency Description", anchor=CENTER)
    update_emergency_table.heading("Area Affected", text="Area Affected", anchor=CENTER)
    update_emergency_table.heading("Start Date", text="Start Date", anchor=CENTER)
    update_emergency_table.heading("Close Date", text="Close Date", anchor=CENTER)
    update_emergency_table.heading("Status", text="Status", anchor=CENTER)


    update_emergency_table.insert(parent='', index=i, iid=i, values=(updating_camp_list[0], updating_camp_list[1], updating_camp_list[2], updating_camp_list[3], updating_camp_list[4], updating_camp_list[5], updating_camp_list[6], updating_camp_list[7]))

    update_emergency_table.pack()

    update_emergency_table_button = Button(Update_Emergency_Screen, text="Continue", command=updateemergencyEntry)
    update_emergency_table_button.pack()

def updateemergencyEntry():
    global emergency_type
    global emergency_type_flood
    global emergency_type_drought
    global emergency_type_earthquake
    global emergency_type_tsunami
    global emergency_type_other
    global emergency_type_flood_check
    global emergency_type_drought_check
    global emergency_type_earthquake_check
    global emergency_type_tsunami_check
    global emergency_type_other_check
    global emergency_type_string


    camp_name = StringVar()
    emergency_type = StringVar()
    emergency_description = StringVar()
    area_affected = StringVar()
    start_date = StringVar()
    close_date = StringVar()
    emergency_marker_country = StringVar()
    emergency_status = StringVar()

    Update_Emergency_Screen_Label = Label(Update_Emergency_Screen, text="You are updating an existing emergency. Please fill out the below.")
    Update_Emergency_Screen_Label.pack()

    Update_Emergency_Screen_Label_Index = Label(Update_Emergency_Screen, text="The index number for your camp is %s" %(updating_camp_list[0]))
    Update_Emergency_Screen_Label_Index.pack()

    camp_name_label = Label(Update_Emergency_Screen, text="Camp Name *")
    camp_name_label.pack()
    camp_name_entry = Entry(Update_Emergency_Screen, textvariable=camp_name)
    camp_name_entry.pack()
    camp_name_entry.setvar(str(updating_camp_list[1]))

    emergency_type_label = Label(Update_Emergency_Screen, text="Select the type of emergency")
    emergency_type_label.pack()
    emergency_type_flood = IntVar()
    emergency_type_tsunami = IntVar()
    emergency_type_earthquake = IntVar()
    emergency_type_drought = IntVar()
    emergency_type_other = IntVar()

    emergency_type_flood_check = Checkbutton(Update_Emergency_Screen, variable=emergency_type_flood, onvalue=1, offvalue=0,
                                             text="Flood", command=clickFlood)
    emergency_type_flood_check.pack()
    emergency_type_tsunami_check = Checkbutton(Update_Emergency_Screen, variable=emergency_type_tsunami, onvalue=1, offvalue=0,
                                               text="Tsunami", command=clickTsunami)
    emergency_type_tsunami_check.pack()
    emergency_type_earthquake_check = Checkbutton(Update_Emergency_Screen, variable=emergency_type_earthquake, onvalue=1,
                                                  offvalue=0, text="Earthquake", command=clickEarthquake)
    emergency_type_earthquake_check.pack()
    emergency_type_drought_check = Checkbutton(Update_Emergency_Screen, variable=emergency_type_drought, onvalue=1, offvalue=0,
                                               text="Drought", command=clickDrought)
    emergency_type_drought_check.pack()
    emergency_type_other_check = Checkbutton(Update_Emergency_Screen, variable=emergency_type_other, onvalue=1, offvalue=0,
                                             text="Other", command=clickOther)
    emergency_type_other_check.pack()

    emergency_description_label = Label(Update_Emergency_Screen, text="Briefly describe the emergency")
    emergency_description_label.pack()
    emergency_description_entry = Entry(Update_Emergency_Screen, textvariable=emergency_description)
    emergency_description_entry.pack()
    emergency_description_entry.setvar(str(updating_camp_list[3]))

    from datetime import date
    today = date.today()

    start_date_label = Label(Update_Emergency_Screen,
                             text="Please select a start date for the emergency from the below calendar")
    start_date_label.pack()
    start_date_calendar = Calendar(Update_Emergency_Screen, date_pattern="d/m/y", selectmode='day', maxdate=today)
    start_date_calendar.pack()
    startDate = datetime.datetime.strptime(start_date_calendar.get_date(), "%d/%m/%Y").date()

    status_label = Label(Update_Emergency_Screen, text="Has the emergency finished yet?")
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
    status_check_button_yes = Checkbutton(Update_Emergency_Screen, variable=status_check_yes, onvalue=1, offvalue=2, text="Yes",
                                          command=clickYes)
    status_check_button_yes.pack()

    status_check_no = IntVar()
    status_check_button_no = Checkbutton(Update_Emergency_Screen, variable=status_check_no, onvalue=1, offvalue=2, text="No",
                                         command=clickNo)
    status_check_button_no.pack()

    status_check_button = Button(Update_Emergency_Screen, text="Confirm", command=setactiveStatus)
    status_check_button.pack()

    submit_updated_emergency_button = Button(Update_Emergency_Screen, text="Submit Updated Emergency", command=campnameVerify)
    submit_updated_emergency_button.pack()


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
    global startDate
    global endDate
    global status_error_label
    global close_date_label
    global Update_Emergency_Screen

    if status_check_no.get() == 1:
        close_date_label = Label(Update_Emergency_Screen, text="Please select an end date for the emergency from the below calendar")
        close_date_label.pack()
        close_date_calendar = Calendar(Update_Emergency_Screen, date_pattern="d/m/y", selectmode='day', mindate=startDate)
        close_date_calendar.pack()
        status = "Closed"

    if (status_check_yes.get() == 1):
        endDate = "NA"
        status = "Active"
def UpdateCampVerify():
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
    global emergency_type_flood
    global emergency_type_drought
    global emergency_type_earthquake
    global emergency_type_tsunami
    global emergency_type_other
    global startDate
    global status
    global emergency_marker_country
    global Update_Emergency_Screen

    if len(camp_name.get()) == 0:
        camp_name_reentry_label = Label(Update_Emergency_Screen, text="Please enter a name for the new camp", fg='#f00')
        camp_name_reentry_label.pack()
    if ((emergency_type_flood.get() != 1) and (emergency_type_drought.get() != 1) and (
            emergency_type_earthquake.get() != 1) and (emergency_type_tsunami.get() != 1) and (
            emergency_type_other.get() != 1)):
        emergency_type_reentry_label = Label(Update_Emergency_Screen, text="Please enter an emergency type for the new camp",
                                             fg='#f00')
        emergency_type_reentry_label.pack()
    if len(emergency_description.get()) == 0:
        emergency_description_reentry_label = Label(Update_Emergency_Screen,
                                                    text="Please enter a description for the new emergency", fg='#f00')
        emergency_description_reentry_label.pack()
    if emergency_marker_country == "NA":
        emergency_marker_reentry_label = Label(Update_Emergency_Screen, text="Please enter an area for the emergency",
                                               fg='#f00')
        emergency_marker_reentry_label.pack()
    if status == "NA":
        if ((status_check_yes.get() != 1) and (status_check_no.get() != 1)):
            status_check_reentry_label = Label(Update_Emergency_Screen,
                                               text="Please select an activation status for the emergency.", fg='#f00')
            status_check_reentry_label.pack()
        else:
            status_confirm_reentry_label = Label(Update_Emergency_Screen,
                                                 text="Please tick confirm to commit your activation status answer",
                                                 fg='#f00')
            status_confirm_reentry_label.pack()
    else:
        UpdateCampSummary

def UpdateCampSummary():
    global Update_Emergency_Screen
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

    Update_Camp_Summary_Screen = TopLevel(Update_Emergency_Screen)
    Update_Camp_Summary_Screen.title("Update an Emergency")
    Update_Camp_Summary_Screen.geometry("500x350")

    Update_Camp_Summary_Screen_label = Label(Update_Emergency_Screen, text="Please view below a summary of the camp that you are adding to the database")
    Update_Camp_Summary_Screen_label.pack()

    Update_Camp_Name_Summary_label = Label(Update_Emergency_Screen, text="The updated camp name is: %s"%(camp_name.get()))
    Update_Camp_Name_Summary_label.pack()

    Update_Camp_Type_Summary_label = Label(Update_Emergency_Screen,text="The type of emergency is: %s" % (emergency_type.get()))
    Update_Camp_Type_Summary_label.pack()

    Update_Camp_Description_Summary_label = Label(Update_Emergency_Screen, text="Your description of the emergency is: %s" % (emergency_description.get()))
    Update_Camp_Description_Summary_label.pack()

    Update_Camp_Start_Date_Summary_label = Label(Update_Emergency_Screen,text="The start date of the emergency is: %s" % (startDate))
    Update_Camp_Start_Date_Summary_label.pack()

    Update_Camp_End_Date_Summary_label = Label(Update_Emergency_Screen, text="The end date of the emergency is: %s" % (endDate))
    Update_Camp_End_Date_Summary_label.pack()

    Update_Camp_Summission_Button = Button(Update_Emergency_Screen, text="Update", command=UpdateEmergency)
    Update_Camp_Summission_Button.pack()

def UpdateEmergency():
    global Update_Emergency_Screen
    global camp_name
    global updating_camp_list
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
    global emergency_database_list
    global index_updating_camp

    updating_camp_list[1] = camp_name.get()
    updating_camp_list[2] = emergency_type.get()
    updating_camp_list[3] = emergency_description.get()
    updating_camp_list[5] = str(startDate)
    updating_camp_list[6] = str(endDate)
    updating_camp_list[7] = status

    emergency_database_list[(index_updating_camp-1)] = updating_camp_list
    emergency_database_file_write = open("Emergency_Database", "r+")
    for i in range(0, len(emergency_database_list)):
        emergency_database_string = ','.join(emergency_database_list[i])
        emergency_database_file_write.write(emergency_database_string)
        i += 1
    emergency_database_file_write.close()

    Update_Emergency_Close_Screen_Label = Label(Update_Emergency_Screen, text="Your updated emergency has been successfully saved.")
    Update_Emergency_Close_Screen_Label.pack()


def campnameVerify():
    global camp_name
    global camp_name_list
    global camp_name
    global camp_name_verify

    camp_name_verify = camp_name.get()
    if (camp_name_verify in camp_name_list):
        camp_name_reentry_Label = Label(Update_Emergency_Screen,
                                        text="This camp name already exists in the database. Please re-enter another camp-name below.", fg='#f00')
        camp_name_reentry_Label.pack()
    else:
        UpdateCampVerify()
























def UpdateEmergencyHomeScreen():
    global Update_Emergency_Home_Screen
    Update_Emergency_Home_Screen = Tk()
    Update_Emergency_Home_Screen.geometry("500x600")
    Update_Emergency_Home_Screen.title("Update Existing Emergency Home screen")
    Update_Emergency_Home_Screen_Button = Button(Update_Emergency_Home_Screen, text="Update Existing Emergency", command=setupUpdate)
    Update_Emergency_Home_Screen_Button.pack()
    Return_Homescreen_Button = Button(Update_Emergency_Home_Screen, text="Return to homepage")
    Return_Homescreen_Button.pack()

    Update_Emergency_Home_Screen.mainloop()

UpdateEmergencyHomeScreen()