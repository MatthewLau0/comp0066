#Import functions
from tkinter import *
from tkinter import ttk
import sys
import subprocess
import datetime
subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'tkcalendar'])
subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'tkintermapview'])
import tkintermapview
from tkcalendar import Calendar

def updateexistingForm():
    def setupUpdate():
        global startDate
        global endDate
        global status
        global emergency_type_string
        global emergency_marker_country
        global emergency_database_list
        global camp_name_list

        emergency_database_file = open("Emergency_Database", "r")
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
        emergency_marker_country = "NA"

        camp_name_list = []
        for i in range(0, len(emergency_database_list)):
            camp_name_list.append((emergency_database_list[i])[1])

        UpdateEmergencyScreen()

    def UpdateEmergencyScreen():
        global Update_Emergency_Home_Screen
        global Update_Emergency_Screen
        global emergency_database_list
        global View_Table_Yes
        Update_Emergency_Screen = Toplevel(Update_Emergency_Home_Screen)
        Update_Emergency_Screen.title("Update an existing emergency")
        Update_Emergency_Screen.geometry("500x600")

        # #Create main frame
        # update_emergency_frame_scroll = Frame(Update_Emergency_Screen)
        # update_emergency_frame_scroll.pack(expand=1, fill=BOTH)
        #
        # #Create canvas
        # update_emergency_canvas = Canvas(update_emergency_frame_scroll)
        # update_emergency_canvas.pack(side=LEFT, expand=1, fill=BOTH)
        #
        # #Create scrollbar
        # update_emergency_scrollbar = Scrollbar(update_emergency_frame_scroll, orient=VERTICAL, command=update_emergency_canvas.yview)
        # update_emergency_scrollbar.pack(side=RIGHT, fill=Y)
        #
        # #Configure the canvas
        # update_emergency_canvas.configure(yscrollcommand=update_emergency_scrollbar.set)
        # update_emergency_canvas.bind('<Configure>', lambda e: update_emergency_canvas.configure(scrollregion=update_emergency_canvas.bbox("all")))
        #
        # #Create another frame inside the canvas
        # update_emergency_frame_two = Frame(update_emergency_canvas)
        #
        # #Add new frame to window in the canvas
        # update_emergency_canvas.create_window((0,0), window=update_emergency_frame_two, anchor="nw")

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
        global update_emergency_frame_two
        global Update_Emergency_Screen
        global emergency_database_list
        global select_index
        global index_updating_camp
        global emergency_database_list
        global updating_camp_list
        global camp_name
        global Update_Emergency_Entry_Screen

        if select_index.get() == '':
            invalid_select_index = Label(Update_Emergency_Screen, text="Invalid entry.")
            invalid_select_index.pack()
            SelectIndex()
        else:
            Update_Emergency_Entry_Screen = Toplevel(Update_Emergency_Screen)
            Update_Emergency_Entry_Screen.title("Update Existing Emergency")
            Update_Emergency_Entry_Screen.geometry("500x650")

            index_updating_camp_extract = select_index.get()
            index_updating_camp = int(index_updating_camp_extract) - 1

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
        global emergency_marker_country
        global map_confirm


        camp_name = StringVar()
        emergency_type = StringVar()
        emergency_description = StringVar()
        area_affected = StringVar()
        start_date = StringVar()
        close_date = StringVar()
        emergency_marker_country = StringVar()
        emergency_status = StringVar()

        Update_Emergency_Screen_Label = Label(Update_Emergency_Entry_Screen, text="You are updating an existing emergency. Please fill out the below.")
        Update_Emergency_Screen_Label.pack()

        Update_Emergency_Screen_Label_Index = Label(Update_Emergency_Entry_Screen, text="The index number for your camp is %s" %(updating_camp_list[0]))
        Update_Emergency_Screen_Label_Index.pack()

        camp_name_label = Label(Update_Emergency_Entry_Screen, text="Camp Name *")
        camp_name_label.pack()
        camp_name_label_instructions = Label(Update_Emergency_Entry_Screen,
                                             text="Camp Names must have no spaces and must only contain letters")
        camp_name_label_instructions.pack()
        camp_name_entry = Entry(Update_Emergency_Entry_Screen, textvariable=camp_name)
        camp_name_entry.pack()
        camp_name_entry.setvar(str(updating_camp_list[1]))

        emergency_type_frame = Frame(Update_Emergency_Entry_Screen)
        emergency_type_frame.pack()

        emergency_type_label = Label(Update_Emergency_Entry_Screen, text="Select the type of emergency")
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

        emergency_description_label = Label(Update_Emergency_Entry_Screen, text="Briefly describe the emergency")
        emergency_description_label.pack()
        emergency_description_entry = Entry(Update_Emergency_Entry_Screen, textvariable=emergency_description)
        emergency_description_entry.pack()
        emergency_description_entry.setvar(str(updating_camp_list[3]))

        def add_emergency_marker(coords):
            global emergency_marker
            global emergency_marker_country
            global emergency_map
            global emergency_marker_label
            if emergency_marker_country != "NA":
                emergency_marker_label.config(text="Please only select one marker", fg='#f00')
                mapReset()
            else:
                emergency_marker = emergency_map.set_marker(coords[0], coords[1], text="Emergency Marker")
                emergency_marker_country = tkintermapview.convert_coordinates_to_country(coords[0], coords[1])
                emergency_map.configure()
                return emergency_marker_country

        emergency_map = tkintermapview.TkinterMapView(Update_Emergency_Entry_Screen, width=150, height=150, corner_radius=0)
        emergency_map.set_zoom(2)
        emergency_map.pack()
        emergency_map.add_right_click_menu_command(label="Emergency Marker", command=add_emergency_marker, pass_coords=True)

        map_reset_button = Button(Update_Emergency_Entry_Screen, text="Reset Map", command=mapReset)
        map_reset_button.pack()
        map_confirm = IntVar()
        map_confirm_entry = Checkbutton(Update_Emergency_Entry_Screen, variable=map_confirm, onvalue=1, offvalue=0,
                                        text="Confirm Map Entry")
        map_confirm_entry.pack()

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

        status_label = Label(Update_Emergency_Entry_Screen, text="Is the emergency still active?")
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

        submit_updated_emergency_button = Button(Update_Emergency_Entry_Screen, text="Submit Updated Emergency", command=campnameVerify)
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

        if emergency_type_other.get() == 1:
            emergency_type_tsunami_check.config(state=DISABLED)
            emergency_type_earthquake_check.config(state=DISABLED)
            emergency_type_drought_check.config(state=DISABLED)
            emergency_type_flood_check.config(state=DISABLED)

            emergency_type_label_other = Label(emergency_type_frame, text="Specify the type of emergency")
            emergency_type_label_other.pack(anchor=CENTER)
            emergency_type_other = Entry(emergency_type_frame, textvariable=emergency_type)
            emergency_type_other.pack(anchor=CENTER)
            emergency_type_other_button = Button(emergency_type_frame, text="Confirm", command=OtherConfirm)
            emergency_type_other_button.pack(anchor=CENTER)


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
        global update_emergency_frame_two
        global startDate

        startDate = datetime.datetime.strptime(start_date_calendar.get_date(), "%d/%m/%Y").date()

        if status_check_no.get() == 1:
            close_date_label.configure(state=NORMAL)
            close_date_calendar.configure(state=NORMAL)
            close_date_calendar.configure(mindate=startDate)
            status = "Closed"

        if (status_check_yes.get() == 1):
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
        global emergency_marker_country
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

        if len(camp_name.get()) == 0 or camp_name.get() == ' ' or camp_name.get().count(" ") > 3 or camp_name.get().isalpha() != True:
            camp_name_label.config(text="Please enter a name for the new camp", fg='#f00')
        elif ((emergency_type_flood.get() != 1) and (emergency_type_drought.get() != 1) and (emergency_type_earthquake.get() != 1) and (emergency_type_tsunami.get() != 1) and (emergency_type_other.get() != 1)):
            emergency_type_label.config(text="Please enter an emergency type for the new camp", fg='#f00')
        elif len(emergency_description.get()) == 0:
            emergency_description_label.config(text="Please enter a description for the new emergency", fg='#f00')
        elif map_confirm.get() != 1:
            emergency_marker_label(text="Please enter an area for the emergency and click confirm.", fg='f00')
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

        Update_Camp_Summary_Screen = Toplevel(Update_Emergency_Screen)
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
                                            text="The country your emergency is in is: %s" % (emergency_marker_country))
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
        global emergency_marker_country

        updating_camp_list[1] = camp_name.get()
        updating_camp_list[2] = emergency_type_string
        updating_camp_list[3] = emergency_description.get()
        updating_camp_list[4] = emergency_marker_country
        updating_camp_list[5] = str(startDate)
        updating_camp_list[6] = str(endDate)
        updating_camp_list[7] = status

        emergency_database_list[(index_updating_camp)] = updating_camp_list
        emergency_database_file_write = open("Emergency_Database", "r+")
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

        Update_Camp_Close_Screen = Toplevel(Update_Emergency_Screen)
        Update_Camp_Close_Screen.title("Emergency successfully saved")
        Update_Camp_Close_Screen.geometry("500x350")

        Update_Emergency_Close_Screen_Label = Label(Update_Camp_Close_Screen,
                                                    text="Your updated emergency has been successfully saved.")
        Update_Emergency_Close_Screen_Label.pack()

        update_another_emergency_button = Button(Update_Camp_Close_Screen, text="Update another emergency", command=setupUpdate)
        update_another_emergency_button.pack()
        return_to_home_screen_button = Button(Update_Camp_Close_Screen, text="Return to homescreen", command=returnHome)
        return_to_home_screen_button.pack()

    def returnHome():
        import Admin_HomePage

    def campnameVerify():
        global camp_name
        global camp_name_list
        global camp_name
        global camp_name_verify
        global updating_camp_list
        global update_emergency_frame_two
        global camp_name_label

        camp_name_verify = camp_name.get()

        if (camp_name_verify != updating_camp_list[1]):
            if (camp_name_verify in camp_name_list):
                camp_name_label.config(text="This camp name already exists in the database. Please re-enter another camp-name below.", fg='#f00')
            else:
                UpdateCampVerify()
        else:
            generateEndDate()

    #Scroll bar creating
    #Create a main frame


    def destroyScreen():
        global Update_Emergency_Home_Screen
        Update_Emergency_Home_Screen.destroy()

    def UpdateEmergencyHomeScreen():
        global Update_Emergency_Home_Screen
        Update_Emergency_Home_Screen = Toplevel()
        Update_Emergency_Home_Screen.geometry("500x600")
        Update_Emergency_Home_Screen.title("Update Existing Emergency Home screen")
        Update_Emergency_Home_Screen_Button = Button(Update_Emergency_Home_Screen, text="Update Existing Emergency", command=setupUpdate)
        Update_Emergency_Home_Screen_Button.pack()
        Return_Homescreen_Button = Button(Update_Emergency_Home_Screen, text="Return to homepage", command=destroyScreen)
        Return_Homescreen_Button.pack()

        Update_Emergency_Home_Screen.mainloop()

    UpdateEmergencyHomeScreen()