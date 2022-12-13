#Import functions
from tkinter import *
from tkinter import ttk
import datetime

import tkintermapview
from tkcalendar import Calendar
from country_list import countries_for_language

def updateexistingForm(screen):
    global admin_home_screen
    admin_home_screen = screen

    def setupUpdate():
        global startDate
        global endDate
        global status
        global emergency_type_string
        global emergency_marker_country_update
        global emergency_database_list
        global camp_name_list

        emergency_database_file = open("emergency_database.txt", "r")
        emergency_database_list = []
        for line in emergency_database_file:
            line_list = line.split("%")
            emergency_database_list.append(line_list)
        emergency_database_file.close()

        # Establish some variables
        startDate = "NA"
        endDate = "NA"
        status = "NA"
        emergency_type_string = "NA"
        emergency_marker_country_update = "NA"

        camp_name_list = []
        for i in range(0, len(emergency_database_list)):
            camp_name_list.append((emergency_database_list[i])[1])

        UpdateEmergencyScreen()

    def UpdateEmergencyScreen():
        global Update_Emergency_Home_Screen
        global Update_Emergency_Screen
        global emergency_database_list
        global View_Table_Yes


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
        global update_emergency_frame_two

        emergency_database_label = Label(Update_Emergency_Screen, text="Please use the below table to find the index number of the emergency you would like to update")
        emergency_database_label.pack()

        emergency_database_frame = Frame(Update_Emergency_Screen)
        emergency_database_frame.pack()

        emergency_database_table = ttk.Treeview(Update_Emergency_Screen)

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

        emergency_database_table_button = Button(Update_Emergency_Screen, text="Continue", command=SelectIndex)
        emergency_database_table_button.pack()

    def SelectIndex():
        global Update_Emergency_Screen
        global emergency_database_list
        global select_index
        global select_index_label
        global emergency_database_list_index
        global select_index_enter
        global select_index_select_button

        select_index = IntVar()

        emergency_database_list_index = []
        for i in range(0, len(emergency_database_list)):
            emergency_database_list_index.append(int((emergency_database_list[i])[0]))
            i += 1


        select_index_label = Label(Update_Emergency_Screen, text="Please enter the index number of the camp you would like to update")
        select_index_label.pack()

        select_index_entry = ttk.Combobox(Update_Emergency_Screen, textvariable=select_index)
        select_index_entry['values'] = emergency_database_list_index
        select_index_entry.pack()

        select_index_select_button = Button(Update_Emergency_Screen, text="Submit", command=submitCampErrorCheck)
        select_index_select_button.pack()

    def submitCampErrorCheck():
        global select_index
        global emergency_database_list_index
        global select_index_label
        global select_index_enter
        global select_index_select_button

        select_index_label.config(text="Please enter the index number of the camp you would like to update.", fg='#000000')

        if select_index.get() in emergency_database_list_index:
            printupdatingCamp()
        else:
            select_index_label.config(text="Invalid entry.", fg='#f00')

    def printupdatingCamp():
        global update_emergency_frame_two
        global Update_Emergency_Screen
        global emergency_database_list
        global select_index
        global index_updating_camp
        global emergency_database_list
        global updating_camp_list
        global camp_name
        global Update_Emergency_Entry_Screen
        global select_index_label
        global update_emergency_table_button

        if select_index.get() == '':
            select_index_label.config(fg="#f00")
        else:
            Update_Emergency_Screen.destroy()
            Update_Emergency_Entry_Screen = Toplevel()
            Update_Emergency_Entry_Screen.title("Update Existing Emergency")
            Update_Emergency_Entry_Screen.geometry("500x650")

            index_updating_camp_extract = select_index.get()
            index_updating_camp = (index_updating_camp_extract - 1)

            updating_camp_list = []
            for i in range(0, len(emergency_database_list[index_updating_camp])):
                updating_camp_list.append((emergency_database_list[index_updating_camp])[i])
                i += 1

            index_select_label = Label(Update_Emergency_Entry_Screen,
                                       text="You are updating camp %d" % (int(index_updating_camp_extract)))
            index_select_label.pack()

            update_emergency_frame = Frame(Update_Emergency_Entry_Screen)
            update_emergency_frame.configure(height=20)
            update_emergency_frame.pack()

            update_emergency_table = ttk.Treeview(update_emergency_frame)

            update_emergency_table['columns'] = (
            "Camp ID", "Camp Name", "Emergency Type", "Emergency Description", "Area Affected", "Start Date", "Close Date",
            "Status")

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

            update_emergency_table.insert(parent='', index=i, iid=i, values=(
            updating_camp_list[0], updating_camp_list[1], updating_camp_list[2], updating_camp_list[3],
            updating_camp_list[4], updating_camp_list[5], updating_camp_list[6], updating_camp_list[7]))
            update_emergency_table.configure(height=2)
            update_emergency_table.pack()

            update_emergency_table_button = Button(Update_Emergency_Entry_Screen, text="Continue",
                                                   command=updateemergencyEntry)
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
        global updating_camp_list
        global camp_name
        global status_check_no
        global status_check_yes
        global emergency_description
        global startDate
        global update_emergency_frame_two
        global Update_Emergency_Entry_Screen
        global emergency_type_frame
        global close_date_calendar
        global close_date_label
        global emergency_marker_country_update
        global map_confirm
        global emergency_type_label_other
        global emergency_type_other_entry
        global emergency_type_other_button
        global emergency_marker_label
        global update_emergency_table_button
        global update_emergency_map
        global start_date_calendar
        global update_emergency_location_label
        global camp_name_label
        global emergency_type_label
        global emergency_description_label
        global status_label
        global area_affected
        global start_date_label

        update_emergency_table_button.destroy()

        camp_name = StringVar()
        emergency_type = StringVar()
        emergency_description = StringVar()
        area_affected = StringVar()
        start_date = StringVar()
        close_date = StringVar()
        emergency_status = StringVar()

        Update_Emergency_Screen_Label_Index = Label(Update_Emergency_Entry_Screen, text="The index number for your camp is %s" %(updating_camp_list[0]))
        Update_Emergency_Screen_Label_Index.pack()

        camp_name_label = Label(Update_Emergency_Entry_Screen, text="Camp Name * (Camp Names must have no spaces and must only contain letters)", state=DISABLED)
        camp_name_label.pack()
        camp_name_entry = Entry(Update_Emergency_Entry_Screen, textvariable=camp_name, state=DISABLED)
        camp_name_entry.insert(0, f"{updating_camp_list[1]}")
        camp_name_entry.pack()

        emergency_type_frame = Frame(Update_Emergency_Entry_Screen)
        emergency_type_frame.pack()

        emergency_type_label = Label(emergency_type_frame, text="Select the type of emergency")
        emergency_type_label.pack()
        emergency_type_flood = IntVar()
        emergency_type_tsunami = IntVar()
        emergency_type_earthquake = IntVar()
        emergency_type_drought = IntVar()
        emergency_type_other = IntVar()

        emergency_type_flood_check = Checkbutton(emergency_type_frame, variable=emergency_type_flood, onvalue=1, offvalue=0,
                                                 text="Flood", command=clickFlood)
        emergency_type_flood_check.pack(side=LEFT)
        emergency_type_tsunami_check = Checkbutton(emergency_type_frame, variable=emergency_type_tsunami, onvalue=1, offvalue=0,
                                                   text="Tsunami", command=clickTsunami)
        emergency_type_tsunami_check.pack(side=LEFT)
        emergency_type_earthquake_check = Checkbutton(emergency_type_frame, variable=emergency_type_earthquake, onvalue=1,
                                                      offvalue=0, text="Earthquake", command=clickEarthquake)
        emergency_type_earthquake_check.pack(side=LEFT)
        emergency_type_drought_check = Checkbutton(emergency_type_frame, variable=emergency_type_drought, onvalue=1, offvalue=0,
                                                   text="Drought", command=clickDrought)
        emergency_type_drought_check.pack(side=LEFT)
        emergency_type_other_check = Checkbutton(emergency_type_frame, variable=emergency_type_other, onvalue=1, offvalue=0,
                                                 text="Other", command=clickOther)
        emergency_type_other_check.pack(side=LEFT)

        emergency_type_label_other = Label(emergency_type_frame, text="Specify the type of emergency", state=DISABLED)
        emergency_type_label_other.pack(anchor=CENTER)
        emergency_type_other_entry = Entry(emergency_type_frame, textvariable=emergency_type, state=DISABLED)
        emergency_type_other_entry.pack(anchor=CENTER)
        emergency_type_other_button = Button(emergency_type_frame, text="Confirm", command=OtherConfirm, state=DISABLED)
        emergency_type_other_button.pack(side=BOTTOM, anchor=CENTER)

        emergency_description_label = Label(Update_Emergency_Entry_Screen, text="Briefly describe the emergency")
        emergency_description_label.pack()
        emergency_description_entry = Entry(Update_Emergency_Entry_Screen, textvariable=emergency_description)
        emergency_description_entry.insert(0, f"{updating_camp_list[3]}")
        emergency_description_entry.pack()

        update_emergency_location_label = Label(Update_Emergency_Entry_Screen, text="Please enter the country in whcih the emergency has occured")
        update_emergency_location_label.pack()
        update_emergency_location_entry = Entry(Update_Emergency_Entry_Screen, textvariable=area_affected)
        update_emergency_location_entry.insert(0, f"{updating_camp_list[4]}")
        update_emergency_location_entry.pack()

        calendar_frame_label = Frame(Update_Emergency_Entry_Screen)
        calendar_frame_label.pack()

        calendar_frame = Frame(Update_Emergency_Entry_Screen)
        calendar_frame.pack()

        from datetime import date
        today = date.today()

        start_date_label = Label(calendar_frame_label,
                                 text="Please select a start date for the emergency from the below calendar")
        start_date_label.pack(side=LEFT)
        start_date_calendar = Calendar(calendar_frame, date_pattern="d/m/y", selectmode='day', maxdate=today)
        start_date_calendar.pack(side=LEFT)
        close_date_label = Label(calendar_frame_label,
                                 text="Please select an end date for the emergency from the below calendar", state=DISABLED)
        close_date_label.pack(side=RIGHT)
        close_date_calendar = Calendar(calendar_frame, date_pattern="d/m/y", selectmode='day',
                                       state=DISABLED)
        close_date_calendar.pack(side=RIGHT)

        status_label = Label(Update_Emergency_Entry_Screen, text="Is the emergency still active? Please confirm your answer using the button below.")
        status_label.pack()

        def clickYes():
            global startDate
            startDate = datetime.datetime.strptime(start_date_calendar.get_date(), "%d/%m/%Y").date()
            if status_check_yes.get() == 1:
                status_check_button_no.config(state=DISABLED)
            else:
                status_check_button_no.config(state=NORMAL)

        def clickNo():
            global startDate
            startDate = datetime.datetime.strptime(start_date_calendar.get_date(), "%d/%m/%Y").date()
            if status_check_no.get() == 1:
                status_check_button_yes.config(state=DISABLED)
            else:
                status_check_button_yes.config(state=NORMAL)

        status_check_yes = IntVar()
        status_check_button_yes = Checkbutton(Update_Emergency_Entry_Screen, variable=status_check_yes, onvalue=1, offvalue=2, text="Yes",
                                              command=clickYes)
        status_check_button_yes.pack()

        status_check_no = IntVar()
        status_check_button_no = Checkbutton(Update_Emergency_Entry_Screen, variable=status_check_no, onvalue=1, offvalue=2, text="No",
                                             command=clickNo)
        status_check_button_no.pack()

        status_check_button = Button(Update_Emergency_Entry_Screen, text="Confirm", command=setactiveStatus)
        status_check_button.pack()

        def calendarReset():
            global start_date_label
            global start_date_calendar
            global close_date_label
            global close_date_calendar

            start_date_label.configure(state=NORMAL)
            start_date_calendar.configure(state=NORMAL)
            close_date_label.configure(state=DISABLED)
            close_date_calendar.configure(state=DISABLED)

        status_reset_button = Button(Update_Emergency_Entry_Screen, text="Reset Calendar", command=calendarReset)
        status_reset_button.pack()

        submit_updated_emergency_button = Button(Update_Emergency_Entry_Screen, text="Submit Updated Emergency", command=generateEndDate)
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
        global emergency_type_frame
        global emergency_type_label_other
        global emergency_type_other_entry
        global emergency_type_other_button

        if emergency_type_other.get() == 1:
            emergency_type_tsunami_check.config(state=DISABLED)
            emergency_type_earthquake_check.config(state=DISABLED)
            emergency_type_drought_check.config(state=DISABLED)
            emergency_type_flood_check.config(state=DISABLED)

            emergency_type_label_other.config(state=NORMAL)
            emergency_type_other_entry.config(state=NORMAL)
            emergency_type_other_button.config(state=NORMAL)


        else:
            emergency_type_label_other.config(state=DISABLED)
            emergency_type_other_entry.config(state=DISABLED)
            emergency_type_other_button.config(state=DISABLED)
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
        global update_emergency_frame_two
        global startDate

        startDate = datetime.datetime.strptime(start_date_calendar.get_date(), "%d/%m/%Y").date()

        if status_check_no.get() == 1:
            close_date_label.configure(state=NORMAL)
            close_date_calendar.configure(state=NORMAL)
            close_date_calendar.configure(mindate=startDate)
            status = "Closed"

        elif status_check_yes.get() == 1:
            endDate = "NA"
            status = "Active"

    def generateEndDate():
        global endDate

        if status_check_no.get() == 1:
            endDate = datetime.datetime.strptime(close_date_calendar.get_date(), "%d/%m/%Y").date()

        UpdateCampVerify()
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
        global emergency_marker_country_update
        global Update_Emergency_Screen
        global endDate
        global map_confirm
        global camp_name_label
        global emergency_type_label
        global emergency_description_label
        global emergency_marker_label
        global start_date_label
        global close_date_label
        global status_label
        global update_emergency_location_label
        global updating_camp_list

        camp_name_label.config(text="Please enter a name for the new camp.", fg='#000000')
        emergency_type_label.config(text="Please enter an emergency type for the new camp", fg='#000000')
        emergency_description_label.config(text="Please enter a description for the new emergency", fg='#000000')
        update_emergency_location_label.config(text="Please enter the country in which the emergency occured.", fg='#000000')
        status_label.config(text="Please select an activation status for the emergency.", fg='#000000')

        countries = dict(countries_for_language('en'))
        countries_list = list(countries.values())

        if ((emergency_type_flood.get() != 1) and (emergency_type_drought.get() != 1) and (emergency_type_earthquake.get() != 1) and (emergency_type_tsunami.get() != 1) and (emergency_type_other.get() != 1)):
            emergency_type_label.config(text="Please enter an emergency type for the new camp", fg='#f00')
        elif len(emergency_description.get()) == 0:
            emergency_description_label.config(text="Please enter a description for the new emergency", fg='#f00')
        elif area_affected.get() not in countries_list:
            update_emergency_location_label.config(text="Please enter an area for the emergency and click confirm.", fg='f00')
        elif status == "NA":
            if ((status_check_yes.get() != 1) and (status_check_no.get() != 1)):
                status_label.config(text="Please select an activation status for the emergency.", fg='#f00')
            else:
                status_label.config(text="Please tick confirm to commit your activation status answer",fg='#f00')
        else:
            UpdateCampSummary()

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
        global emergency_type_string
        global Update_Camp_Summary_Screen

        Update_Emergency_Entry_Screen.destroy()

        Update_Camp_Summary_Screen = Tk()
        Update_Camp_Summary_Screen.title("Update an Emergency")
        Update_Camp_Summary_Screen.geometry("500x350")

        Update_Camp_Summary_Screen_label = Label(Update_Camp_Summary_Screen, text="Please view below a summary of the camp that you are adding to the database")
        Update_Camp_Summary_Screen_label.pack()

        Update_Camp_Name_Summary_label = Label(Update_Camp_Summary_Screen, text="The updated camp name is: %s"%(camp_name.get()))
        Update_Camp_Name_Summary_label.pack()

        Update_Camp_Type_Summary_label = Label(Update_Camp_Summary_Screen,text="The type of emergency is: %s" % (emergency_type_string))
        Update_Camp_Type_Summary_label.pack()

        Update_Camp_Description_Summary_label = Label(Update_Camp_Summary_Screen, text="Your description of the emergency is: %s" % (emergency_description.get()))
        Update_Camp_Description_Summary_label.pack()

        Update_Camp_Area_Summary_Label = Label(Update_Camp_Summary_Screen,
                                            text="The country your emergency is in is: %s" % (area_affected.get()))
        Update_Camp_Area_Summary_Label.pack()

        Update_Camp_Start_Date_Summary_label = Label(Update_Camp_Summary_Screen, text="The start date of the emergency is: %s" % (startDate))
        Update_Camp_Start_Date_Summary_label.pack()

        Update_Camp_End_Date_Summary_label = Label(Update_Camp_Summary_Screen, text="The end date of the emergency is: %s" % (endDate))
        Update_Camp_End_Date_Summary_label.pack()

        Update_Camp_Status_Summary_label = Label(Update_Camp_Summary_Screen, text="The status of the emergency is: %s" %(status))
        Update_Camp_Status_Summary_label.pack()

        Update_Camp_Summission_Button = Button(Update_Camp_Summary_Screen, text="Update", command=UpdateEmergency)
        Update_Camp_Summission_Button.pack()

        Go_Back_Button = Button(Update_Camp_Summary_Screen, text="Go Back", command=goBack)
        Go_Back_Button.pack()

    def goBack():
        setupUpdate()

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
        global emergency_type_string
        global emergency_marker_country_update

        updating_camp_list[1] = camp_name.get()
        updating_camp_list[2] = emergency_type_string
        updating_camp_list[3] = emergency_description.get()
        updating_camp_list[4] = area_affected.get()
        updating_camp_list[5] = str(startDate)
        updating_camp_list[6] = str(endDate)
        updating_camp_list[7] = status

        emergency_database_list[(index_updating_camp)] = updating_camp_list
        emergency_database_file_write = open("emergency_database.txt", "r+")
        emergency_database_file_write.truncate(0)
        for i in range(0, len(emergency_database_list)):
            emergency_database_string = '%'.join(emergency_database_list[i])
            if i == index_updating_camp:
                emergency_database_file_write.write("%s\n" %(emergency_database_string))
            elif i != index_updating_camp:
                emergency_database_file_write.write(emergency_database_string)
            i += 1
        emergency_database_file_write.close()

        updatescreenClose()

    def updatescreenClose():
        global Update_Emergency_Screen
        global Update_Emergency_Close_Screen

        Update_Camp_Summary_Screen.destroy()
        Update_Camp_Close_Screen = Tk()
        Update_Camp_Close_Screen.title("Emergency successfully saved")
        Update_Camp_Close_Screen.geometry("500x350")

        Update_Emergency_Close_Screen_Label = Label(Update_Camp_Close_Screen,
                                                    text="Your updated emergency has been successfully saved.")
        Update_Emergency_Close_Screen_Label.pack()

        return_to_home_screen_button = Button(Update_Camp_Close_Screen, text="Return to homescreen", command=returnHome)
        return_to_home_screen_button.pack()

    def returnHome():
        global Update_Emergency_Close_Screen
        Update_Emergency_Close_Screen.destroy()


    #Scroll bar creating
    #Create a main frame


    def UpdateEmergencyHomeScreen():
        global Update_Emergency_Screen
        Update_Emergency_Screen = Toplevel(admin_home_screen)
        Update_Emergency_Screen.title("Update an existing emergency")
        Update_Emergency_Screen.geometry("650x600")
        setupUpdate()


        Update_Emergency_Screen.mainloop()

    UpdateEmergencyHomeScreen()
