#Import modules - is pip included in standard installers
from tkinter import *
import tkintermapview
from tkcalendar import Calendar
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
        global emergency_marker_country

        emergency_database_file = open("emergency_database.txt", "r")

        new_emergency = ["NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA"]

        emergency_database_list = []
        for line in emergency_database_file:
            line_list = line.split("%")
            emergency_database_list.append(line_list)

        emergency_database_file.close()

        # Create the index number for the new emergency
        if len(emergency_database_list) == 0:
            new_emergency[0] = "1"
        elif len(emergency_database_list) >= 1:
            new_emergency[0] = str((int((emergency_database_list[-1])[0]) + 1))

            # Create a list for the camp names already in existence
        camp_name_list = []
        for i in range(0, len(emergency_database_list)):
            camp_name_list.append((emergency_database_list[i])[1])

        #Establish some variables
        startDate = "NA"
        endDate = "NA"
        status = "NA"
        emergency_type_string = "NA"
        emergency_marker_country = "NA"

        CreateNewCampScreen()


    #New Camp
    def CreateNewCampScreen():
        global New_Camp_Screen
        global camp_name
        global new_emergency
        global index_number
        global emergency_type
        global emergency_description
        global area_affected
        global startDate
        global endDate
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
        global emergency_marker
        global emergency_marker_country
        global Create_New_Emergency_Home_Screen
        global emergency_map
        global emergency_type_frame
        global calendar_frame
        global close_date_label
        global close_date_calendar
        global emergency_type_label_other
        global emergency_type_other_entry
        global emergency_type_other_button
        global map_confirm
        global camp_name_label
        global emergency_type_label
        global emergency_description_label
        global emergency_marker_label
        global start_date_label
        global close_date_label
        global status_label
        global emergency_location_label

        index_number = StringVar()
        camp_name = StringVar()
        emergency_type = StringVar()
        emergency_description = StringVar()
        area_affected = StringVar()
        emergency_status = StringVar()

        New_Camp_Screen_Label = Label(New_Camp_Screen, text="You are going to make a new emergency plan. Please follow the below instructions")
        New_Camp_Screen_Label.pack()
        New_Camp_Screen_Label_Index = Label(New_Camp_Screen, text="The index number for your camp is %s" %(new_emergency[0]))
        New_Camp_Screen_Label_Index.pack()

        camp_name_label = Label(New_Camp_Screen, text="Camp Name * ")
        camp_name_label.pack()
        camp_name_label_instructions = Label(New_Camp_Screen, text="Camp Names must have no spaces and must only contain letters")
        camp_name_label_instructions.pack()
        camp_name_entry = Entry(New_Camp_Screen, textvariable=camp_name)
        camp_name_entry.pack()

        emergency_type_frame = Frame(New_Camp_Screen)
        emergency_type_frame.pack()

        emergency_type_label = Label(emergency_type_frame, text="Select the type of emergency")
        emergency_type_label.pack()

        emergency_type_flood = IntVar()
        emergency_type_tsunami = IntVar()
        emergency_type_earthquake = IntVar()
        emergency_type_drought = IntVar()
        emergency_type_other = IntVar()

        emergency_type_flood_check = Checkbutton(emergency_type_frame, variable=emergency_type_flood, onvalue=1, offvalue=0, text="Flood", command=clickFlood)
        emergency_type_flood_check.pack(side=LEFT)
        emergency_type_tsunami_check = Checkbutton(emergency_type_frame, variable=emergency_type_tsunami, onvalue=1, offvalue=0, text="Tsunami", command=clickTsunami)
        emergency_type_tsunami_check.pack(side=LEFT)
        emergency_type_earthquake_check = Checkbutton(emergency_type_frame, variable=emergency_type_earthquake, onvalue=1, offvalue=0, text="Earthquake", command=clickEarthquake)
        emergency_type_earthquake_check.pack(side=LEFT)
        emergency_type_drought_check = Checkbutton(emergency_type_frame, variable=emergency_type_drought, onvalue=1, offvalue=0, text="Drought", command=clickDrought)
        emergency_type_drought_check.pack(side=LEFT)
        emergency_type_other_check = Checkbutton(emergency_type_frame, variable=emergency_type_other, onvalue=1, offvalue=0, text="Other", command=clickOther)
        emergency_type_other_check.pack(side=LEFT)

        emergency_type_label_other = Label(emergency_type_frame, text="Specify the type of emergency", state=DISABLED)
        emergency_type_label_other.pack(anchor=CENTER)
        emergency_type_other_entry = Entry(emergency_type_frame, textvariable=emergency_type, state=DISABLED)
        emergency_type_other_entry.pack(anchor=CENTER)
        emergency_type_other_button = Button(emergency_type_frame, text="Confirm", command=OtherConfirm, state=DISABLED)
        emergency_type_other_button.pack(side=BOTTOM, anchor=CENTER)


        emergency_description_label = Label(New_Camp_Screen, text="Briefly describe the emergency")
        emergency_description_label.pack()
        emergency_description_entry = Entry(New_Camp_Screen, textvariable=emergency_description)
        emergency_description_entry.pack()

        emergency_location_label = Label(New_Camp_Screen,
                                         text="Please enter the country in which the emergency has occured")
        emergency_location_label.pack()
        emergency_location_entry = Entry(New_Camp_Screen, textvariable=area_affected)
        emergency_location_entry.pack()

        from datetime import date
        today = date.today()

        calendar_frame_label = Frame(New_Camp_Screen)
        calendar_frame_label.pack()

        calendar_frame = Frame(New_Camp_Screen)
        calendar_frame.pack()

        start_date_label = Label(calendar_frame_label, text="Start Date")
        start_date_label.pack(side=LEFT)
        close_date_label = Label(calendar_frame_label, text="Close Date", state=DISABLED)
        close_date_label.pack(side=RIGHT)
        start_date_calendar = Calendar(calendar_frame, date_pattern="d/m/y", selectmode='day', maxdate=today)
        start_date_calendar.pack(side=LEFT)
        close_date_calendar = Calendar(calendar_frame, date_pattern="d/m/y", selectmode='day', state=DISABLED)
        close_date_calendar.pack(side=RIGHT)

        status_label = Label(New_Camp_Screen, text="Is the emergency active? Please confirm your answer using the button below.")
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
        status_check_button_yes = Checkbutton(New_Camp_Screen, variable=status_check_yes, onvalue=1, offvalue=2, text="Yes", command=clickYes)
        status_check_button_yes.pack()

        status_check_no = IntVar()
        status_check_button_no = Checkbutton(New_Camp_Screen, variable=status_check_no, onvalue=1, offvalue=2, text="No", command=clickNo)
        status_check_button_no.pack()

        status_check_button = Button(New_Camp_Screen, text="Confirm", command=setactiveStatus)
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

        status_reset_button = Button(New_Camp_Screen, text="Reset Calendar", command=calendarReset)
        status_reset_button.pack()

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
        global calendar_frame
        global start_date_label
        global start_date_calendar
        global close_date_label

        global startDate
        startDate = datetime.datetime.strptime(start_date_calendar.get_date(), "%d/%m/%Y").date()

        if status_check_no.get() == 1:
            start_date_label.configure(state=DISABLED)
            start_date_calendar.configure(state=DISABLED)
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

        NewCampVerify()


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

        camp_name_label.config(text="Please enter a name for the new camp.", fg='#000000')
        emergency_type_label.config(text="Please enter an emergency type for the new camp", fg='#000000')
        emergency_description_label.config(text="Please enter a description for the new emergency", fg='#000000')
        emergency_location_label.config(text="Please enter the country in which the emergency occured.", fg='#000000')
        status_label.config(text="Please select an activation status for the emergency.", fg='#000000')

        countries = dict(countries_for_language('en'))
        countries_list = list(countries.values())



        if len(camp_name.get()) == 0 or camp_name.get() == ' ' or camp_name.get().count(" ") > 3 or camp_name.get().isalpha() != True:
            camp_name_label.config(text="Please enter a name for the new camp.", fg='#f00')
        elif ((emergency_type_flood.get() != 1) and (emergency_type_drought.get() != 1) and (emergency_type_earthquake.get() != 1) and (emergency_type_tsunami.get() != 1) and (emergency_type_other.get() !=1)):
            emergency_type_label.config(text="Please enter an emergency type for the new camp", fg='#f00')
        elif len(emergency_description.get()) == 0:
            emergency_description_label.config(text="Please enter a description for the new emergency", fg='#f00')
        elif area_affected.get() not in countries_list:
            emergency_location_label.config(text="Please enter the country where the emergency has occured", fg='#f00')
        elif status == "NA":
            if ((status_check_yes.get() != 1) and (status_check_no.get() != 1)):
                status_label.config(text="Please select an activation status for the emergency.", fg='#f00')
            else:
                status_label.config(text="Please tick confirm to commit your activation status answer", fg='#f00')
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
        New_Camp_Summary_Screen = Tk()
        New_Camp_Summary_Screen.title("Submit New Emergency")
        New_Camp_Summary_Screen.geometry("500x350")

        New_Camp_Summary_Screen_Label = Label(New_Camp_Summary_Screen, text="Please view below a summary of the camp that you are adding to the database")
        New_Camp_Summary_Screen_Label.pack()

        New_Camp_Name_Summary_Label = Label(New_Camp_Summary_Screen, text="The new camp name you are entering is: %s" %(camp_name.get()))
        New_Camp_Name_Summary_Label.pack()

        New_Camp_Type_Summary_Label = Label(New_Camp_Summary_Screen, text="The emergency type for the new camp is: %s" %(emergency_type_string))
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
        screenSetup()

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
        global emergency_marker_country
        global emergency_type_string
        global New_Emergency_Close_Screen

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

        New_Camp_Summary_Screen.destroy()
        New_Emergency_Close_Screen = Tk()
        New_Emergency_Close_Screen.title("Emergency Successfully Submitted")
        New_Emergency_Close_Screen.geometry("500x650")

        New_Emergency_Close_Screen_Label = Label(New_Emergency_Close_Screen, text="Your new emergency has been successfully saved. Would you like to submit another emergency, or return to homescreen.")
        New_Emergency_Close_Screen_Label.pack()

        Submit_Another_Emergency_Button = Button(New_Emergency_Close_Screen, text="Submit Another Emergency", command=Create_Emergency_Screen)
        Submit_Another_Emergency_Button.pack()
        Return_To_HomeScreen_Button = Button(New_Emergency_Close_Screen, text="Return to Homescreen", command=returnHome)
        Return_To_HomeScreen_Button.pack()

    def returnHome():
        import Admin_Home

    def campnameVerify():
        global camp_name
        global camp_name_list
        global camp_name
        global camp_name_verify
        global camp_name_label

        camp_name_verify = camp_name.get()
        if (camp_name_verify in camp_name_list):
            camp_name_label.config(text="This camp name already exists in the database. Please re-enter another camp-name.", fg='#f00')
        else:
            generateEndDate()

    def Create_Emergency_Screen():
        global New_Camp_Screen

        New_Camp_Screen = Toplevel(admin_home_screen)
        New_Camp_Screen.title("Create a New Emergency")
        New_Camp_Screen.geometry("500x600")
        screenSetup()


        New_Camp_Screen.mainloop()

    Create_Emergency_Screen()

createnewemergencyPlan(Tk())