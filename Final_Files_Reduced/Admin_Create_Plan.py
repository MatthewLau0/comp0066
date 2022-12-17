#Import modules - is pip included in standard installers
from tkinter import *
from tkinter import ttk
import datetime
from country_list import countries_for_language



def createnewemergencyPlan(screen):
    global admin_home_screen
    admin_home_screen = screen

    def screenSetup():
        global new_emergency
        global emergency_database_list
        global camp_name_list
        global startDate
        global endDate
        global status
        global emergency_type_string
        global day_list
        global month_list
        global year_list

        emergency_database_file = open("emergency_database.txt", "r")

        new_emergency = ["NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA"]

        emergency_database_list = []
        for line in emergency_database_file:
            line_list = line.split("%")
            emergency_database_list.append(line_list)

        emergency_database_file.close()

        if len(emergency_database_list) == 0:
            new_emergency[0] = "1"
        elif len(emergency_database_list) >= 1:
            new_emergency[0] = str((int((emergency_database_list[-1])[0]) + 1))

        camp_name_list = []
        for i in range(0, len(emergency_database_list)):
            camp_name_list.append((emergency_database_list[i])[1])

        day_list = [str(i) for i in range(1, 32)]
        month_list = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October",
                      "November", "December"]
        year_list = [str(i) for i in range(2023, 1899, -1)]


        CreateNewCampScreen()


    #New Camp
    def CreateNewCampScreen():
        global camp_name
        global new_emergency
        global index_number
        global emergency_type
        global emergency_description
        global area_affected
        global startDate
        global endDate
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
        global emergency_type_frame
        global calendar_frame
        global close_date_label
        global close_date_calendar
        global emergency_type_label_other
        global emergency_type_other_entry
        global emergency_type_other_button
        global camp_name_label
        global emergency_type_label
        global emergency_description_label
        global emergency_marker_label
        global start_date_label
        global close_date_label
        global status_label
        global emergency_location_label
        global start_date_day
        global start_date_month
        global start_date_year
        global end_date_day
        global end_date_month
        global end_date_year
        global start_date_label
        global end_date_label

        index_number = StringVar()
        camp_name = StringVar()
        emergency_type = StringVar()
        emergency_description = StringVar()
        area_affected = StringVar()

        New_Camp_Screen_Label = Label(New_Camp_Screen, text="You are going to make a new emergency camp. Please follow the below instructions")
        New_Camp_Screen_Label.pack()
        New_Camp_Screen_Label_Index = Label(New_Camp_Screen, text="The index number for your camp is %s" %(new_emergency[0]))
        New_Camp_Screen_Label_Index.pack()

        camp_name_label = Label(New_Camp_Screen, text="Camp Name * ")
        camp_name_label.pack()
        camp_name_label_instructions = Label(New_Camp_Screen, text="Camp Names must have no spaces and must only contain letters", font=('.AppleSystemUIFont', 13, 'italic'))
        camp_name_label_instructions.pack()
        camp_name_entry = Entry(New_Camp_Screen, textvariable=camp_name)
        camp_name_entry.pack()


        emergency_type_label = Label(New_Camp_Screen, text="Enter the type of emergency")
        emergency_type_label.pack()
        emergency_type_entry = Entry(New_Camp_Screen, textvariable=emergency_type)
        emergency_type_entry.pack()

        emergency_description_label = Label(New_Camp_Screen, text="Briefly describe the emergency")
        emergency_description_label.pack()
        emergency_description_entry = Entry(New_Camp_Screen, textvariable=emergency_description)
        emergency_description_entry.pack()

        emergency_location_label = Label(New_Camp_Screen,
                                         text="Country Affected", font=('.AppleSystemUIFont', 13, 'bold'))
        emergency_location_label.pack()
        emergency_location_entry = Entry(New_Camp_Screen, textvariable=area_affected)
        emergency_location_entry.pack()


        start_date_day = StringVar()
        start_date_month = StringVar()
        start_date_year = StringVar()

        start_date_label = Label(New_Camp_Screen, text="Enter the start date for the emergency")
        start_date_label.pack()
        start_date_frame = Frame(New_Camp_Screen)
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

        end_date_label = Label(New_Camp_Screen, text="Enter the end date for the emergency")
        end_date_label.pack()
        end_date_frame = Frame(New_Camp_Screen)
        end_date_frame.pack()
        Label(New_Camp_Screen_Label, text="If the emergency has not finished yet, please leave the below boxes blank.", font=('.AppleSystemUIFont', 13, 'italic'))
        end_date_day_combobox = ttk.Combobox(end_date_frame, textvariable=end_date_day)
        end_date_day_combobox['values'] = day_list
        end_date_day_combobox.pack(side=LEFT)

        end_date_month_combobox = ttk.Combobox(end_date_frame, textvariable=end_date_month)
        end_date_month_combobox['values'] = month_list
        end_date_month_combobox.pack(side=LEFT)

        end_date_year_combobox = ttk.Combobox(end_date_frame, textvariable=end_date_year)
        end_date_year_combobox['values'] = year_list
        end_date_year_combobox.pack(side=LEFT)

        status_check_button = Button(New_Camp_Screen, text="Confirm", command=setactiveStatus)
        status_check_button.pack()

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
        global calendar_frame
        global start_date_label
        global start_date_calendar
        global close_date_label
        global endDate

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
        campnameVerify()

    def generateendDate():
        global endDate

        enddateComplete = ("%s-%s-%s" % (end_date_year.get(), end_date_month.get(), end_date_day.get()))
        endDate = datetime.datetime.strptime(enddateComplete, "%Y-%B-%d")
        generatestartDate()


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
        global emergency_type_flood
        global emergency_type_drought
        global emergency_type_earthquake
        global emergency_type_tsunami
        global emergency_type_other
        global startDate
        global status
        global emergency_marker_country
        global endDate
        global map_confirm
        global camp_name_label
        global emergency_type_label
        global emergency_description_label
        global start_date_label
        global close_date_label
        global status_label
        global area_affected
        global emergency_location_label
        global emergency_type_string


        camp_name_label.config(text="Camp Name *", fg='#000000')
        emergency_type_label.config(text="Enter the type of emergency", fg='#000000')
        emergency_description_label.config(text="Briefly describe the emergency", fg='#000000')
        start_date_label.config(text="Enter the start date for the emenrgency", fg='#000000')
        emergency_location_label.config(text="Country Affected", fg='#000000')

        countries = dict(countries_for_language('en'))
        countries_list = list(countries.values())

        today = datetime.datetime.today()

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
        elif len(start_date_day.get()) == 0 or len(start_date_month.get()) == 0 or len(start_date_year.get())  == 0:
            start_date_label.config(text="Please enter a value for the start date", fg='#f00')
        else:
            CreateNewCampSummary()

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
        global emergency_marker_country
        global New_Camp_Summary_Screen
        global area_affected

        New_Camp_Screen.destroy()
        New_Camp_Summary_Screen = Toplevel()
        New_Camp_Summary_Screen.title("Submit New Emergency")
        screen_width1 = New_Camp_Summary_Screen.winfo_screenwidth()
        screen_height1 = New_Camp_Summary_Screen.winfo_screenheight()
        window_height1 = screen_height1
        window_width1 = 900

        center_x1 = int(screen_width1 / 2 - window_width1 / 2)
        center_y1 = int(screen_height1 / 2 - window_height1 / 2)
        New_Camp_Summary_Screen.geometry(f'{window_width1}x{window_height1}+{center_x1}+{center_y1}')

        New_Camp_Summary_Screen_Label = Label(New_Camp_Summary_Screen, text="Please view below a summary of the camp that you are adding to the database")
        New_Camp_Summary_Screen_Label.pack()

        New_Camp_Name_Summary_Label = Label(New_Camp_Summary_Screen, text="The new camp name you are entering is: %s" %(camp_name.get()))
        New_Camp_Name_Summary_Label.pack()

        New_Camp_Type_Summary_Label = Label(New_Camp_Summary_Screen, text="The emergency type for the new camp is: %s" %(emergency_type.get()))
        New_Camp_Type_Summary_Label.pack()

        New_Camp_Description_Summary_Label = Label(New_Camp_Summary_Screen, text="Your description of the new emergency is: %s" %(emergency_description.get()))
        New_Camp_Description_Summary_Label.pack()

        New_Camp_Area_Summary_Label = Label(New_Camp_Summary_Screen, text="The country your emergency is in is: %s" %(area_affected.get()))
        New_Camp_Area_Summary_Label.pack()

        New_Camp_StartDate_Summary_Label = Label(New_Camp_Summary_Screen, text="The start date of the new emergency is: %s" %(startDate))
        New_Camp_StartDate_Summary_Label.pack()

        New_Camp_EndDate_Summary_Label = Label(New_Camp_Summary_Screen, text="The end date of the new emergency is: %s" %(endDate))
        New_Camp_EndDate_Summary_Label.pack()

        New_Camp_Status_Summary_Label = Label(New_Camp_Summary_Screen, text="The status of the new emergency is: %s" %(status))
        New_Camp_Status_Summary_Label.pack()

        New_Camp_Submission_Button = Button(New_Camp_Summary_Screen, text="Submit", command=SubmitEmergency)
        New_Camp_Submission_Button.pack()

        Go_Back_Button = Button(New_Camp_Summary_Screen, text="Go back", command=goBack)
        Go_Back_Button.pack()

    def goBack():
        New_Camp_Summary_Screen.destroy()
        Create_Emergency_Screen()

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
        global emergency_marker_country
        global emergency_type_string
        global New_Emergency_Close_Screen
        global New_Camp_Summary_Screen
        global New_Emergency_Close_Screen

        New_Camp_Summary_Screen.destroy()

        new_emergency[1] = camp_name.get()
        new_emergency[2] = emergency_type_string
        new_emergency[3] = emergency_description.get()
        new_emergency[4] = area_affected.get()
        new_emergency[5] = str(startDate)
        new_emergency[6] = str(endDate)
        new_emergency[7] = status

        new_emergency_string = '%'.join(new_emergency)

        emergency_database_file_append = open("emergency_database.txt", "a")
        emergency_database_file_append.write("\n%s" %(new_emergency_string))
        emergency_database_file_append.close()


    def campnameVerify():
        global camp_name
        global camp_name_list
        global camp_name
        global camp_name_verify
        global camp_name_label

        if len(camp_name.get()) == 0 or camp_name.get() == ' ' or camp_name.get().count(" ") > 3 or camp_name.get().isalpha() != True:
            camp_name_label.config(text="Please enter a name for the new camp.", fg='#f00')
        elif camp_name.get() in camp_name_list:
            camp_name_label.config(text="This camp name already exists in the database. Please re-enter another camp-name.", fg='#f00')
        else:
            NewCampVerify()

    def Create_Emergency_Screen():
        global New_Camp_Screen

        New_Camp_Screen = Toplevel(admin_home_screen)
        New_Camp_Screen.title("Create a New Emergency")
        screen_width1 = New_Camp_Screen.winfo_screenwidth()
        screen_height1 = New_Camp_Screen.winfo_screenheight()
        window_height1 = screen_height1
        window_width1 = 900

        center_x1 = int(screen_width1 / 2 - window_width1 / 2)
        center_y1 = int(screen_height1 / 2 - window_height1 / 2)
        New_Camp_Screen.geometry(f'{window_width1}x{window_height1}+{center_x1}+{center_y1}')
        screenSetup()


        New_Camp_Screen.mainloop()

    Create_Emergency_Screen()

createnewemergencyPlan(Tk())