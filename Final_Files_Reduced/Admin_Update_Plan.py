#Import functions
from tkinter import *
from tkinter import ttk
import datetime
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
        global emergency_database_list
        global camp_name_list
        global select_index_frame
        global day_list
        global month_list
        global year_list

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

        camp_name_list = []
        for i in range(0, len(emergency_database_list)):
            camp_name_list.append((emergency_database_list[i])[1])

        select_index_frame = Frame(Update_Emergency_Screen)
        select_index_frame.pack()

        day_list = [str(i) for i in range(1, 32)]
        month_list = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October",
                      "November", "December"]
        year_list = [str(i) for i in range(2023, 1899, -1)]

        UpdateEmergencyScreen()


    def UpdateEmergencyScreen():
        global Update_Emergency_Home_Screen
        global Update_Emergency_Screen
        global emergency_database_list
        global View_Table_Yes


        Update_Emergency_Screen_Label = Label(Update_Emergency_Screen, text="You are going to update an existing emergency camp. Please follow the below instructions")
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
        global select_index_frame


        select_index = IntVar()

        emergency_database_list_index = []
        for i in range(0, len(emergency_database_list)):
            emergency_database_list_index.append(int((emergency_database_list[i])[0]))
            i += 1

        for widget in select_index_frame.winfo_children():
            widget.destroy()


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
            screen_width1 = Update_Emergency_Entry_Screen.winfo_screenwidth()
            screen_height1 = Update_Emergency_Entry_Screen.winfo_screenheight()
            window_height1 = screen_height1
            window_width1 = 900

            center_x1 = int(screen_width1 / 2 - window_width1 / 2)
            center_y1 = int(screen_height1 / 2 - window_height1 / 2)
            Update_Emergency_Entry_Screen.geometry(f'{window_width1}x{window_height1}+{center_x1}+{center_y1}')

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
        global start_date_day
        global start_date_month
        global start_date_year
        global end_date_day
        global end_date_month
        global end_date_year


        update_emergency_table_button.destroy()

        camp_name = StringVar()
        emergency_type = StringVar()
        emergency_description = StringVar()
        area_affected = StringVar()

        Update_Emergency_Screen_Label_Index = Label(Update_Emergency_Entry_Screen, text="The index number for your camp is %s" %(updating_camp_list[0]))
        Update_Emergency_Screen_Label_Index.pack()

        camp_name_label = Label(Update_Emergency_Entry_Screen, text="Camp Name* ")
        camp_name_label.pack()
        camp_name_instructions_label = Label(Update_Emergency_Entry_Screen, text="Camp Names must have no spaces and must only contain letters")
        camp_name_instructions_label.pack()
        camp_name_entry = Entry(Update_Emergency_Entry_Screen, textvariable=camp_name, state=DISABLED)
        camp_name_entry.insert(0, f"{updating_camp_list[1]}")
        camp_name_entry.pack()

        emergency_type_label = Label(Update_Emergency_Entry_Screen, text="Enter the type of emergency")
        emergency_type_label.pack()
        emergency_type_entry = Entry(Update_Emergency_Entry_Screen, textvariable=emergency_type)
        emergency_type_entry.insert(0, f"{updating_camp_list[2]}")
        emergency_type_entry.pack()

        emergency_description_label = Label(Update_Emergency_Entry_Screen, text="Briefly describe the emergency", font=('.AppleSystemUIFont', 13, 'bold'))
        emergency_description_label.pack()
        emergency_description_entry = Entry(Update_Emergency_Entry_Screen, textvariable=emergency_description)
        emergency_description_entry.insert(0, f"{updating_camp_list[3]}")
        emergency_description_entry.pack()

        update_emergency_location_label = Label(Update_Emergency_Entry_Screen, text="Country Affected", font=('.AppleSystemUIFont', 13, 'bold'))
        update_emergency_location_label.pack()
        update_emergency_location_entry = Entry(Update_Emergency_Entry_Screen, textvariable=area_affected)
        update_emergency_location_entry.insert(0, f"{updating_camp_list[4]}")
        update_emergency_location_entry.pack()

        start_date_day = StringVar()
        start_date_month = StringVar()
        start_date_year = StringVar()

        start_date_label = Label(Update_Emergency_Entry_Screen, text="Enter the start date for the emergency")
        start_date_label.pack()
        start_date_frame = Frame(Update_Emergency_Entry_Screen)
        start_date_frame.pack()
        start_date_day_combobox = ttk.Combobox(start_date_frame, textvariable=start_date_day)
        start_date_day_combobox['values'] = day_list
        start_date_day_combobox.pack(side=LEFT)

        start_date_month_combobox = ttk.Combobox(start_date_frame, textvariable=start_date_month)
        start_date_month_combobox['values'] = month_list
        start_date_month_combobox.pack(side=LEFT)

        start_date_year_combobox = ttk.Combobox(start_date_frame, textvariable=start_date_year)
        start_date_year_combobox['values'] = year_list
        start_date_year_combobox.pack(side=LEFT)

        end_date_day = StringVar()
        end_date_month = StringVar()
        end_date_year = StringVar()

        end_date_label = Label(Update_Emergency_Entry_Screen, text="Enter the end date for the emergency")
        end_date_label.pack()
        Label(Update_Emergency_Entry_Screen, text="If the emergency has not finished yet, please leave the below boxes blank.",
              font=('.AppleSystemUIFont', 13, 'italic'))
        end_date_frame = Frame(Update_Emergency_Entry_Screen)
        end_date_frame.pack()
        end_date_day_combobox = ttk.Combobox(end_date_frame, textvariable=end_date_day)
        end_date_day_combobox['values'] = day_list
        end_date_day_combobox.pack(side=LEFT)

        end_date_month_combobox = ttk.Combobox(end_date_frame, textvariable=end_date_month)
        end_date_month_combobox['values'] = month_list
        end_date_month_combobox.pack(side=LEFT)

        end_date_year_combobox = ttk.Combobox(end_date_frame, textvariable=end_date_year)
        end_date_year_combobox['values'] = year_list
        end_date_year_combobox.pack(side=LEFT)

        submit_updated_emergency_button = Button(Update_Emergency_Entry_Screen, text="Submit Updated Emergency", command=setactiveStatus())
        submit_updated_emergency_button.pack()

        Button(Update_Emergency_Entry_Screen, text="Return Home", command=Update_Emergency_Entry_Screen.destroy)

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

        if len(end_date_day.get()) == 0 or len(end_date_month.get()) == 0 or len(end_date_year.get()) == 0:
            status = "Closed"
            endDate = "NA"
            generatestartDate()
        else:
            status = "Active"
            generateendDate()

    def generatestartDate():
        global startDate

        startdateComplete = ("%s-%s-%s" % (start_date_year.get(), start_date_month.get(), start_date_day.get()))
        startDate = datetime.datetime.strptime(startdateComplete, "%Y-%B-%d")
        UpdateCampVerify()

    def generateendDate():
        global endDate

        enddateComplete = ("%s-%s-%s" % (end_date_year.get(), end_date_month.get(), end_date_day.get()))
        endDate = datetime.datetime.strptime(enddateComplete, "%Y-%B-%d")
        generatestartDate()
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
        global emergency_type_string

        camp_name_label.config(text="Camp Name *", fg='#000000')
        emergency_type_label.config(text="Select the type of emergency", fg='#000000')
        emergency_description_label.config(text="Briefly describe the emergency", fg='#000000')
        update_emergency_location_label.config(text="Country Affected", fg='#000000')
        start_date_label.config(text="Enter the start date for the emergency")

        countries = dict(countries_for_language('en'))
        countries_list = list(countries.values())

        if len(emergency_type.get()) == 0 or emergency_type.get() == ' ':
            emergency_type_label.config(text="Please enter an emergency type for the new camp", fg='#f00')
        elif len(emergency_description.get()) == 0:
            emergency_description_label.config(text="Please enter a description for the new emergency", fg='#f00')
        elif area_affected.get() not in countries_list:
            emergency_location_label.config(text="Please enter the country where the emergency has occurred", fg='#f00')
        elif startDate > today:
            start_date_label.config(text="Please enter a start date later than today.", fg='#f00')
        elif endDate != "NA":
            if endDate < startDate:
                end_date_label.config(text="Please enter an end date later than the start date.", fg='#f00')
            else:
                pass
        elif len(start_date_day.get()) == 0 or len(start_date_month.get()) == 0 or len(start_date_year.get()) == 0:
            start_date_label.config(text="Please enter a value for the start date", fg='#f00')
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

        Update_Camp_Summary_Screen = Toplevel()
        Update_Camp_Summary_Screen.title("Update an Emergency")
        screen_width1 = Update_Camp_Summary_Screen.winfo_screenwidth()
        screen_height1 = Update_Camp_Summary_Screen.winfo_screenheight()
        window_height1 = screen_height1
        window_width1 = 900

        center_x1 = int(screen_width1 / 2 - window_width1 / 2)
        center_y1 = int(screen_height1 / 2 - window_height1 / 2)
        Update_Camp_Summary_Screen.geometry(f'{window_width1}x{window_height1}+{center_x1}+{center_y1}')

        Update_Camp_Summary_Screen_label = Label(Update_Camp_Summary_Screen, text="Please view below a summary of the camp that you are adding to the database")
        Update_Camp_Summary_Screen_label.pack()

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

        Update_Camp_Summary_Screen.destroy()



    def UpdateEmergencyHomeScreen():
        global Update_Emergency_Screen
        Update_Emergency_Screen = Toplevel(admin_home_screen)
        Update_Emergency_Screen.title("Update an existing emergency")
        screen_width1 = Update_Emergency_Screen.winfo_screenwidth()
        screen_height1 = Update_Emergency_Screen.winfo_screenheight()
        window_height1 = screen_height1
        window_width1 = 900

        center_x1 = int(screen_width1 / 2 - window_width1 / 2)
        center_y1 = int(screen_height1 / 2 - window_height1 / 2)
        Update_Emergency_Screen.geometry(f'{window_width1}x{window_height1}+{center_x1}+{center_y1}')
        setupUpdate()


        Update_Emergency_Screen.mainloop()

    UpdateEmergencyHomeScreen()
