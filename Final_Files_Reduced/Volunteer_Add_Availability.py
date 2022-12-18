from tkcalendar import Calendar
from tkinter import *
import datetime
import tkinter.messagebox
import Volunteer_Home

def add_calendar():
    #SETTING UP THE DEFAULT SCREEN
    availability_screen = Toplevel()
    availability_screen.geometry("500x1000")
    availability_screen.title("Manage availability")
    #screen.configure(background="#A1CDEC")

    #READING ALL VOLUNTEERS INTO A LIST
    volunteer_list_file = open("volunteer_database.txt", "r")
    volunteer_database_list = []
    for line in volunteer_list_file:
        x = line.split("%")
        volunteer_database_list.append(x)

    volunteer_list_file.close()

    volunteerID = Volunteer_Home.user_id


    #LIST WITH THE TIMINGS
    times = ['00:00', '00:15', '00:30', '00:45', '01:00', '01:15', '01:30', '01:45', '02:00', '02:15', '02:30', '02:45', '03:00', '03:15', '03:30', '03:45', '04:00', '04:15', '04:30', '04:45', '05:00', '05:15', '05:30', '05:45', '06:00', '06:15', '06:30' , '06:45' , '07:00', '07:15' , '07:30' , '07:45' , '08:00', '08:15' , '08:30' , '08:45' , '09:00', '09:15' , '09:30' , '09:45' , '10:00', '10:15' , '10:30' , '10:45' , '11:00', '11:15' , '11:30' , '11:45' , '12:00', '12:15' , '12:30' , '12:45' , '13:00', '13:15' , '13:30' , '13:45' , '14:00', '14:15' , '14:30' , '14:45' , '15:00', '15:15' , '15:30' , '15:45' , '16:00', '16:15' , '16:30' , '16:45' , '17:00', '17:15' , '17:30' , '17:45' , '18:00', '18:15' , '18:30' , '18:45' , '19:00', '19:15' , '19:30' , '19:45' , '20:00', '20:15' , '20:30' , '20:45' , '21:00', '21:15' , '21:30' , '21:45' , '22:00', '22:15' , '22:30' , '22:45' , '23:00', '23:15' , '23:30' , '23:45' ]

    def delete1():
        availability_screen.destroy()

    def delete2():
        final_calendar_screen.destroy()

    #SECOND SCREEN, ALLOWS USER TO SELECT THE END DATE OF THEIR VOLUNTEERING
    def final_calendar_lol():
        availability_screen.destroy()
        global final_calendar_screen
        global final_calendar
        global refugee_year_final
        global refugee_month_final
        global refugee_day_final
        today = datetime.date.today()

        final_calendar_screen = Toplevel()
        final_calendar_screen.geometry("500x1000")
        final_calendar_screen.title("Manage availability")

        #SETTING UP THE CALENDAR
        max = datetime.date(2024, today.month, today.day)
        final_text = Label(final_calendar_screen, text="Use this section to manage your availability\nPlease enter the range of days you will work as a volunteer", fg='Green', width=300)
        final_text.pack()
        final_calendar_label = Label(final_calendar_screen, text="Please enter the final date in the range:", font='Arial 18')
        final_calendar_label.pack(pady=50)

        refugee_year_final = StringVar()
        refugee_month_final = StringVar()
        refugee_day_final = StringVar()
        year_lolol = refugee_year.get()
        month_lolol = refugee_month.get()
        day_lolol = refugee_day.get()
        refugee_year_final.set(year_lolol)
        refugee_month_final.set(month_lolol)
        refugee_day_final.set(day_lolol)

        day_list = [d for d in range(1, 32)]
        month_list = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October",
                      "November", "December"]
        year_list = [m for m in range(int(year_lolol), int(year_lolol) + 3)]





        refugee_year_text = Label(final_calendar_screen, text='Year:')
        refugee_year_text.pack()
        refugee_year_combo = tkinter.ttk.Combobox(final_calendar_screen, textvariable=refugee_year_final, values=year_list)
        refugee_year_combo.pack()


        refugee_month_text = Label(final_calendar_screen, text='Month ')
        refugee_month_text.pack()
        refugee_month_combo = tkinter.ttk.Combobox(final_calendar_screen, textvariable=refugee_month_final, values=month_list)
        refugee_month_combo.pack()


        refugee_day_text = Label(final_calendar_screen, text='Day: ')
        refugee_day_text.pack()
        refugee_day_combo = tkinter.ttk.Combobox(final_calendar_screen, textvariable=refugee_day_final, values=day_list)
        refugee_day_combo.pack()


        #SUBMIT DATE RANGE
        final_calendar_button = Button(final_calendar_screen, text="Continue", width=30, command=validate_final)
        final_calendar_button.pack(pady = 75)
        final_calendar_back_button = Button(final_calendar_screen, text="Quit", width=30, command=delete2)
        final_calendar_back_button.pack()


    def validate_final():
        today = datetime.datetime.today()
        year = refugee_year_final.get()
        month = refugee_month_final.get().capitalize()
        day = refugee_day_final.get()

        day_list = [d for d in range(1, 32)]
        month_list = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October",
                      "November", "December"]
        year_list = [m for m in range(int(today.year), int(today.year) + 3)]

        try:
            year = int(year)
        except:
            tkinter.messagebox.showerror(title='Error!', message='Year must be numeric!')
            return

        try:
            day = int(day)
        except:
            tkinter.messagebox.showerror(title='Error!', message='Day must be numeric!')
            return

        if year not in year_list:
            tkinter.messagebox.showerror(title='Error!', message='Please select a valid year from list')
            return

        if month not in month_list:
            tkinter.messagebox.showerror(title='Error!', message='Please select a valid month from list')
            return

        if day not in day_list:
            tkinter.messagebox.showerror(title='Error!', message='Please select a valid day from list')
            return

        if int(year) == int(refugee_year.get()) and month_list.index(month) < month_list.index(refugee_month.get()):
            tkinter.messagebox.showerror(title='Error!', message='Final date must be after initial date!')
            return

        if int(year) == int(refugee_year.get()) and month_list.index(month) == month_list.index(refugee_month.get()) and int(day) < int(refugee_day.get()):
            tkinter.messagebox.showerror(title='Error!', message='Final date must be after initial date!')
            return




        choose_days()
    def validate_initial():
        today = datetime.datetime.today()
        year = refugee_year.get()
        month = refugee_month.get().capitalize()
        day = refugee_day.get()

        day_list = [d for d in range(1, 32)]
        month_list = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October",
                      "November", "December"]
        year_list = [m for m in range(int(today.year), int(today.year) + 3)]

        try:
            year = int(year)
        except:
            tkinter.messagebox.showerror(title='Error!', message='Year must be numeric!')
            return

        try:
            day = int(day)
        except:
            tkinter.messagebox.showerror(title='Error!', message='Day must be numeric!')
            return

        if year not in year_list:
            tkinter.messagebox.showerror(title='Error!', message='Please select a valid year from list')
            return

        if month not in month_list:
            tkinter.messagebox.showerror(title='Error!', message='Please select a valid month from list')
            return

        if day not in day_list:
            tkinter.messagebox.showerror(title='Error!', message='Please select a valid day from list')
            return


        final_calendar_lol()

    #INITIAL SCREEN, ALLOWS USER TO SELECT THE START DATE OF THEIR VOLUNTEERING
    def initial_calendar_lol():
        global refugee_year
        global refugee_month
        global refugee_day
        global initial_calendar_date
        global initial_calendar
        intro_text = Label(availability_screen, text = "Use this section to manage your availability\nPlease enter the range of days you will work as a volunteer", fg = 'Green', width= 300)
        intro_text.pack()
        today = datetime.date.today()
        max = datetime.date(2024, today.month, today.day)

        #SETTING UP THE CALENDAR
        initial_calendar_label = Label(availability_screen, text = "Please enter the inital date in the range:", font = 'Arial 18')
        initial_calendar_label.pack(pady = 50)
        day_list = [d for d in range(1, 32)]
        month_list = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October",
                      "November", "December"]
        year_list = [m for m in range(int(today.year), int(today.year) + 3)]


        refugee_year = StringVar()
        refugee_month = StringVar()
        refugee_day = StringVar()

        refugee_year_text = Label(availability_screen, text='Year:')
        refugee_year_text.pack()
        refugee_year_combo = tkinter.ttk.Combobox(availability_screen, textvariable=refugee_year, values=year_list)
        refugee_year_combo.pack()

        refugee_month_text = Label(availability_screen, text='Month ')
        refugee_month_text.pack()
        refugee_month_combo = tkinter.ttk.Combobox(availability_screen, textvariable=refugee_month, values=month_list)
        refugee_month_combo.pack()

        refugee_day_text = Label(availability_screen, text='Day: ')
        refugee_day_text.pack()
        refugee_day_combo = tkinter.ttk.Combobox(availability_screen, textvariable=refugee_day, values=day_list)
        refugee_day_combo.pack()

        #SETTING UP THE BUTTONS
        initial_calendar_button = Button(availability_screen, text = "Continue", width = 30, command = validate_initial)
        initial_calendar_button.pack(pady = 75)
        initial_calendar_quit_button = Button(availability_screen, text="Quit", width=30, command=delete1)
        initial_calendar_quit_button.pack()



    #THIS IS THE THIRD SCREEN TO OPEN, ALLOWS USER TO SELECT THE RANGE OF TIMES THEY'RE FREE
    def choose_days():
        global choose_days_screen
        final_calendar_screen.destroy()
        choose_days_screen = Toplevel()
        choose_days_screen.geometry("500x1000")
        choose_days_screen.title("Manage availability")

        #DISPLAY THEIR START AND END DATE
        range_confirmation_label = Label(choose_days_screen, text = "Please check the summary below to ensure these are your dates of volunteering")
        range_confirmation_label.pack()

        initial_dates_list = [refugee_day.get(), refugee_month.get(), refugee_year.get()]
        final_dates_list = [refugee_day_final.get(), refugee_month_final.get(), refugee_year_final.get()]
        initial_dates_string = ', '.join(initial_dates_list)
        final_dates_string = ', '.join(final_dates_list)

        start_date_confirmation = Label(choose_days_screen, text = "The start date of your volunteering is: %s" %initial_dates_string)
        start_date_confirmation.pack(pady = 20)

        end_date_confirmation = Label(choose_days_screen, text = "The end date of your volunteering is: %s" %final_dates_string)
        end_date_confirmation.pack(pady = 20)

        refugee_init_datetime = datetime.datetime.strptime(initial_dates_string, '%d, %B, %Y')
        refugee_final_datetime = datetime.datetime.strptime(final_dates_string, '%d, %B, %Y')
        x = str(refugee_final_datetime - refugee_init_datetime)
        y = x.split(',')


        #CALCULATES THE AMOUNT OF DAYS THEY WORK
        diff_confirmation = Label(choose_days_screen, text = "The total days you will be working is: %s" %str(y[0]))
        diff_confirmation.pack(pady = 20)

        #THIS PART IS TO CREATE BUTTONS AND ALLOW THEM TO CHOOSE THE DAYS THEY ARE FREE
        day_text = Label(choose_days_screen, text="Please select which days of the week you are available\nand add the hours you are available: ")
        day_text.pack(pady = 20)
        global monday_text
        global tuesday_text
        global wednesday_text
        global thursday_text
        global friday_text
        global saturday_text
        global sunday_text
        monday_text = IntVar()
        tuesday_text = IntVar()
        wednesday_text = IntVar()
        thursday_text = IntVar()
        friday_text = IntVar()
        saturday_text = IntVar()
        sunday_text = IntVar()

        #EACH INDIVIDUAL FUNCTION IS EACH DAY OF THE WEEK
        def mon():
            global monday_initial_time
            global monday_final_time
            monday_initial_time = StringVar()
            monday_final_time = StringVar()
            if monday_text.get() == 1:
                monday_initial_time_menu = OptionMenu(choose_days_screen, monday_initial_time, *times)
                monday_initial_time_menu.place(x = 180, y = 280, width = 100)

                monday_label = Label(choose_days_screen, text= "to")
                monday_label.place(x = 305, y = 280)


                monday_final_time_menu = OptionMenu(choose_days_screen, monday_final_time, *times)
                monday_final_time_menu.place(x=350, y=280, width=100)

            if monday_text.get() == 0:
                lol_label = Label(choose_days_screen, text='')
                lol_label.place(x=160, y=280, width=800, height=40)

        def tues():
            global tuesday_initial_time
            global tuesday_final_time
            if tuesday_text.get() == 2:
                tuesday_initial_time = StringVar()
                tuesday_initial_time_menu = OptionMenu(choose_days_screen, tuesday_initial_time, *times)
                tuesday_initial_time_menu.place(x = 180, y = 330, width = 100)

                tuesday_label = Label(choose_days_screen, text= "to")
                tuesday_label.place(x = 305, y = 330)

                tuesday_final_time = StringVar()
                tuesday_final_time_menu = OptionMenu(choose_days_screen, tuesday_final_time, *times)
                tuesday_final_time_menu.place(x=350, y=330, width=100)

            if tuesday_text.get() == 0:
                lol_label = Label(choose_days_screen, text='')
                lol_label.place(x=160, y=330, width=800, height=40)

        def wed():
            global wednesday_initial_time
            global wednesday_final_time
            if wednesday_text.get() == 3:
                wednesday_initial_time = StringVar()
                wednesday_initial_time_menu = OptionMenu(choose_days_screen, wednesday_initial_time, *times)
                wednesday_initial_time_menu.place(x = 180, y = 380, width = 100)

                wednesday_label = Label(choose_days_screen, text= "to")
                wednesday_label.place(x = 305, y = 380)

                wednesday_final_time = StringVar()
                wednesday_final_time_menu = OptionMenu(choose_days_screen, wednesday_final_time, *times)
                wednesday_final_time_menu.place(x=350, y=380, width=100)

            if wednesday_text.get() == 0:
                lol_label = Label(choose_days_screen, text='')
                lol_label.place(x=160, y=380, width=800, height=40)

        def thurs():
            global thursday_initial_time
            global thursday_final_time
            if thursday_text.get() == 4:
                thursday_initial_time = StringVar()
                thursday_initial_time_menu = OptionMenu(choose_days_screen, thursday_initial_time, *times)
                thursday_initial_time_menu.place(x = 180, y = 430, width = 100)

                thursday_label = Label(choose_days_screen, text= "to")
                thursday_label.place(x = 305, y = 430)

                thursday_final_time = StringVar()
                thursday_final_time_menu = OptionMenu(choose_days_screen, thursday_final_time, *times)
                thursday_final_time_menu.place(x=350, y=430, width=100)

            if thursday_text.get() == 0:
                lol_label = Label(choose_days_screen, text='')
                lol_label.place(x=160, y=430, width=800, height=40)

        def fri():
            global friday_initial_time
            global friday_final_time
            if friday_text.get() == 5:
                friday_initial_time = StringVar()
                friday_initial_time_menu = OptionMenu(choose_days_screen, friday_initial_time, *times)
                friday_initial_time_menu.place(x = 180, y = 480, width = 100)

                friday_label = Label(choose_days_screen, text= "to")
                friday_label.place(x = 305, y = 480)

                friday_final_time = StringVar()
                friday_final_time_menu = OptionMenu(choose_days_screen, friday_final_time, *times)
                friday_final_time_menu.place(x=350, y=480, width=100)

            if friday_text.get() == 0:
                lol_label = Label(choose_days_screen, text='')
                lol_label.place(x=160, y=480, width=800, height=40)


        def sat():
            global saturday_initial_time
            global saturday_final_time
            if saturday_text.get() == 6:
                saturday_initial_time = StringVar()
                saturday_initial_time_menu = OptionMenu(choose_days_screen, saturday_initial_time, *times)
                saturday_initial_time_menu.place(x = 180, y = 530, width = 100)

                saturday_label = Label(choose_days_screen, text= "to")
                saturday_label.place(x = 305, y = 530)

                saturday_final_time = StringVar()
                saturday_final_time_menu = OptionMenu(choose_days_screen, saturday_final_time, *times)
                saturday_final_time_menu.place(x=350, y=530, width=100)

            if saturday_text.get() == 0:
                lol_label = Label(choose_days_screen, text='')
                lol_label.place(x=160, y=530, width=800, height=40)


        def sun():
            global sunday_initial_time
            global sunday_final_time
            if sunday_text.get() == 7:
                sunday_initial_time = StringVar()
                sunday_initial_time_menu = OptionMenu(choose_days_screen, sunday_initial_time, *times)
                sunday_initial_time_menu.place(x = 180, y = 580, width = 100)

                sunday_label = Label(choose_days_screen, text= "to")
                sunday_label.place(x = 305, y = 580)

                sunday_final_time = StringVar()
                sunday_final_time_menu = OptionMenu(choose_days_screen, sunday_final_time, *times)
                sunday_final_time_menu.place(x=350, y=580, width=100)

            if sunday_text.get() == 0:
                lol_label = Label(choose_days_screen, text='')
                lol_label.place(x=160, y=580, width=800, height=40)

        #ALL THE CHECKBUTTON FUNCTIONALITY
        monday_entry = Checkbutton(choose_days_screen, variable=monday_text, onvalue=1, offvalue=0, text="Monday", command = mon)
        tuesday_entry = Checkbutton(choose_days_screen, variable=tuesday_text, onvalue=2, offvalue=0, text="Tuesday", command = tues)
        wednesday_entry = Checkbutton(choose_days_screen, variable=wednesday_text, onvalue=3, offvalue=0, text="Wednesday", command = wed)
        thursday_entry = Checkbutton(choose_days_screen, variable=thursday_text, onvalue=4, offvalue=0, text="Thursday", command = thurs)
        friday_entry = Checkbutton(choose_days_screen, variable=friday_text, onvalue=5, offvalue=0, text="Friday", command = fri)
        saturday_entry = Checkbutton(choose_days_screen, variable=saturday_text, onvalue=6, offvalue=0, text="Saturday", command = sat)
        sunday_entry = Checkbutton(choose_days_screen, variable=sunday_text, onvalue=7, offvalue=0, text="Sunday", command = sun)
        monday_entry.place(x = 20, y = 280)
        tuesday_entry.place(x = 20, y = 330)
        wednesday_entry.place(x = 20, y = 380)
        thursday_entry.place(x = 20, y = 430)
        friday_entry.place(x = 20, y = 480)
        saturday_entry.place(x = 20, y = 530)
        sunday_entry.place(x = 20, y = 580)

        #PROMPTS USER TO GO TO NEXT STAGE WITH BUTTON
        choose_days_button = Button(choose_days_screen, text="Continue", width=30, command=save_to_file_volunteer)
        choose_days_button.place(x = 115, y = 650)

        final_calendar_back_button = Button(choose_days_screen, text="Quit", width=30, command=delete3)
        final_calendar_back_button.place(x = 115, y = 680)

    def delete3():
        choose_days_screen.destroy()

    #THIS IS THE ERROR CHECKING FUNCTION. CHECKS TO SEE IF TIMES SUBMITTED ARE BEFORE EACH OTHER, ANY BLANK TABS ETC.
    def save_to_file_volunteer():


        #Check if one is bigger than the other
        if monday_text.get() == 1:
            monday_initial = monday_initial_time.get()
            monday_end = monday_final_time.get()
            try:
                index = times.index(monday_initial)
                index2 = times.index(monday_end)
                if index > index2:
                    tkinter.messagebox.showerror(title='Error!', message='Monday: The end time must be after the start time')
                    return

            except ValueError:
                tkinter.messagebox.showerror(title='Error!', message='Monday: Please make sure you have selected a time')
                return

            except:
                tkinter.messagebox.showerror(title = 'Error!', message='Monday: Please ensure input is correct')
                return



        if tuesday_text.get() == 2:
            tuesday_initial = tuesday_initial_time.get()
            tuesday_end = tuesday_final_time.get()
            try:
                index3 = times.index(tuesday_initial)
                index4 = times.index(tuesday_end)
                if index3 > index4:
                    tkinter.messagebox.showerror(title='Error!', message='Tuesday: The end time must be after the start time')
                    return
            except ValueError:
                tkinter.messagebox.showerror(title='Error!', message='Tuesday: Please make sure you have selected a time')
                return

            except:
                tkinter.messagebox.showerror(title='Error!', message='Tuesday: Please ensure input is correct')
                return

        if wednesday_text.get() == 3:
            wednesday_initial = wednesday_initial_time.get()
            wednesday_end = wednesday_final_time.get()
            try:
                index5 = times.index(wednesday_initial)
                index6 = times.index(wednesday_end)
                if index5 > index6:
                    tkinter.messagebox.showerror(title='Error!', message='Wednesday: The end time must be after the start time')
                    return
            except ValueError:
                tkinter.messagebox.showerror(title='Error!', message='Wednesday: Please make sure you have selected a time')
                return

            except:
                tkinter.messagebox.showerror(title='Error!', message='Wednesday: Please ensure input is correct')

        if thursday_text.get() == 4:
            thursday_initial = thursday_initial_time.get()
            thursday_end = thursday_final_time.get()
            try:
                index7 = times.index(thursday_initial)
                index8 = times.index(thursday_end)
                if index7 > index8:
                    tkinter.messagebox.showerror(title='Error!', message='Thursday: The end time must be after the start time')
                    return
            except ValueError:
                tkinter.messagebox.showerror(title='Error!', message='Thursday: Please make sure you have selected a time')
                return

            except:
                tkinter.messagebox.showerror(title='Error!', message='Thursday: Please ensure input is correct')
                return

        if friday_text.get() == 5:
            friday_initial = friday_initial_time.get()
            friday_end = friday_final_time.get()
            try:
                index9 = times.index(friday_initial)
                index10 = times.index(friday_end)
                if index9 > index10:
                    tkinter.messagebox.showerror(title='Error!', message='Friday: The end time must be after the start time')
                    return
            except ValueError:
                tkinter.messagebox.showerror(title='Error!', message='Friday: Please make sure you have selected a time')
                return

            except:
                tkinter.messagebox.showerror(title='Error!', message='Friday: Please ensure input is correct')
                return

        if saturday_text.get() == 6:
            saturday_initial = saturday_initial_time.get()
            saturday_end = saturday_final_time.get()
            try:
                index11 = times.index(saturday_initial)
                index12 = times.index(saturday_end)
                if index11 > index12:
                    tkinter.messagebox.showerror(title='Error!', message='Saturday: The end time must be after the start time')
                    return
            except ValueError:
                tkinter.messagebox.showerror(title='Error!', message='Saturday: Please make sure you have selected a time')
                return

            except:
                tkinter.messagebox.showerror(title='Error!', message='Saturday: Please ensure input is correct')
                return

        if sunday_text.get() == 7:
            sunday_initial = sunday_initial_time.get()
            sunday_end = sunday_final_time.get()
            try:
                index13 = times.index(sunday_initial)
                index14 = times.index(sunday_end)
                if index13 > index14:
                    tkinter.messagebox.showerror(title='Error!', message='Sunday: The end time must be after the start time')
                    return
            except ValueError:
                tkinter.messagebox.showerror(title='Error!', message='Sunday: Please make sure you have selected a time')
                return

            except:
                tkinter.messagebox.showerror(title='Error!', message='Sunday: Please ensure input is correct')
                return

        summary_page()

    #DISPLAYS A SUMMARY PAGE OF ALL THEIR INPUT
    def summary_page():
        global time_summary_page
        time_summary_page = Toplevel()
        time_summary_page.geometry("500x650")
        time_summary_page.title("Confirm hours submission")

        timings_confirmation = Label(time_summary_page, text = "Please check the summary of details below to add to the database")
        timings_confirmation.pack()

        start_confirmation = Label(time_summary_page, text = "The start date of your volunteering is: %s" %initial_calendar.get_date())
        start_confirmation.pack(pady = 30)

        end_confirmation = Label(time_summary_page, text = "The end date of your volunteering is: %s" %final_calendar.get_date())
        end_confirmation.pack(pady = 30)

        if monday_text.get() == 1:
            monday_summary_initial = monday_initial_time.get()
            monday_summary_final = monday_final_time.get()
            monday_confirmation = Label(time_summary_page, text = "On Monday: you are available from %s to %s" % (monday_summary_initial, monday_summary_final))
            monday_confirmation.pack(pady = 10)

        else:
            monday_no_confirmation = Label(time_summary_page, text = "On Monday: you are busy")
            monday_no_confirmation.pack(pady = 10)

        if tuesday_text.get() == 2:
            tuesday_summary_initial = tuesday_initial_time.get()
            tuesday_summary_final = tuesday_final_time.get()
            tuesday_confirmation = Label(time_summary_page, text = "On Tuesday: you are available from %s to %s" % (tuesday_summary_initial, tuesday_summary_final))
            tuesday_confirmation.pack(pady = 10)

        else:
            tuesday_no_confirmation = Label(time_summary_page, text = "On Tuesday: you are busy")
            tuesday_no_confirmation.pack(pady = 10)

        if wednesday_text.get() == 3:
            wednesday_summary_initial = wednesday_initial_time.get()
            wednesday_summary_final = wednesday_final_time.get()
            wednesday_confirmation = Label(time_summary_page, text = "On Wednesday: you are available from %s to %s" % (wednesday_summary_initial, wednesday_summary_final))
            wednesday_confirmation.pack(pady = 10)

        else:
            wednesday_no_confirmation = Label(time_summary_page, text = "On Wednesday: you are busy")
            wednesday_no_confirmation.pack(pady = 10)

        if thursday_text.get() == 4:
            thursday_summary_initial = thursday_initial_time.get()
            thursday_summary_final = thursday_final_time.get()
            thursday_confirmation = Label(time_summary_page, text = "On Thursday: you are available from %s to %s" % (thursday_summary_initial, thursday_summary_final))
            thursday_confirmation.pack(pady = 10)

        else:
            thursday_no_confirmation = Label(time_summary_page, text = "On Thursday: you are busy")
            thursday_no_confirmation.pack(pady = 10)

        if friday_text.get() == 5:
            friday_summary_initial = friday_initial_time.get()
            friday_summary_final = friday_final_time.get()
            friday_confirmation = Label(time_summary_page, text = "On Friday: you are available from %s to %s" % (friday_summary_initial, friday_summary_final))
            friday_confirmation.pack(pady = 10)

        else:
            friday_no_confirmation = Label(time_summary_page, text = "On Friday: you are busy")
            friday_no_confirmation.pack(pady = 10)

        if saturday_text.get() == 6:
            saturday_summary_initial = saturday_initial_time.get()
            saturday_summary_final = saturday_final_time.get()
            saturday_confirmation = Label(time_summary_page, text = "On Saturday: you are available from %s to %s" % (saturday_summary_initial, saturday_summary_final))
            saturday_confirmation.pack(pady = 10)

        else:
            saturday_no_confirmation = Label(time_summary_page, text = "On Saturday: you are busy")
            saturday_no_confirmation.pack(pady = 10)

        if sunday_text.get() == 7:
            sunday_summary_initial = sunday_initial_time.get()
            sunday_summary_final = sunday_final_time.get()
            sunday_confirmation = Label(time_summary_page, text = "On Sunday: you are available from %s to %s" % (sunday_summary_initial, sunday_summary_final))
            sunday_confirmation.pack(pady = 10)

        else:
            sunday_no_confirmation = Label(time_summary_page, text = "On Sunday: you are busy")
            sunday_no_confirmation.pack(pady = 10)

        summary_button = Button(time_summary_page, text="Submit", width=30, command=save_to_database)
        summary_button.pack(pady = 40)

        summary_button_no = Button(time_summary_page, text="Change details", width=30, command=no)
        summary_button_no.pack()


    def no():
        time_summary_page.destroy()

    #IF THEY SUBMIT, WILL CREATE A LIST OF [START DATE, END DATE, MONDAY INITIAL, MONDAY END, TUESDAY INITIAL, TUESDAY END...]
    def save_to_database():

        #GETTING ALL OF THE DATES
        volunteer_start_day = initial_calendar.get_date()
        volunteer_end_day = final_calendar.get_date()
        if monday_text.get() == 1:
            monday_summary_initial = monday_initial_time.get()
            monday_summary_final = monday_final_time.get()

        else:
            monday_summary_initial = 'Not Available'
            monday_summary_final = 'Not Available'

        if tuesday_text.get() == 2:
            tuesday_summary_initial = tuesday_initial_time.get()
            tuesday_summary_final = tuesday_final_time.get()

        else:
            tuesday_summary_initial = 'Not Available'
            tuesday_summary_final = 'Not Available'

        if wednesday_text.get() == 3:
            wednesday_summary_initial = wednesday_initial_time.get()
            wednesday_summary_final = wednesday_final_time.get()

        else:
            wednesday_summary_initial = 'Not Available'
            wednesday_summary_final = 'Not Available'

        if thursday_text.get() == 4:
            thursday_summary_initial = thursday_initial_time.get()
            thursday_summary_final = thursday_final_time.get()

        else:
            thursday_summary_initial = 'Not Available'
            thursday_summary_final = 'Not Available'

        if friday_text.get() == 5:
            friday_summary_initial = friday_initial_time.get()
            friday_summary_final = friday_final_time.get()
        else:
            friday_summary_initial = 'Not Available'
            friday_summary_final = 'Not Available'

        if saturday_text.get() == 6:
            saturday_summary_initial = saturday_initial_time.get()
            saturday_summary_final = saturday_final_time.get()
        else:
            saturday_summary_initial = 'Not Available'
            saturday_summary_final = 'Not Available'

        if sunday_text.get() == 7:
            sunday_summary_initial = sunday_initial_time.get()
            sunday_summary_final = sunday_final_time.get()
        else:
            sunday_summary_initial = 'Not Available'
            sunday_summary_final = 'Not Available'

        #CURRENTLY JUST OUTPUTS THE TIMINGS INFO
        timing_info = [volunteer_start_day, volunteer_end_day, monday_summary_initial, monday_summary_final, tuesday_summary_initial, tuesday_summary_final, wednesday_summary_initial, wednesday_summary_final, thursday_summary_initial, thursday_summary_final, friday_summary_initial, friday_summary_final, saturday_summary_initial, saturday_summary_final, sunday_summary_initial, sunday_summary_final,'\n']

        #COPYING THE OG VOLUNTEER INTO A TEMPORARY LIST
        for i in range(len(volunteer_database_list)):
            if int(volunteer_database_list[i][1]) == int(volunteerID):
                temp_volunteer_list = volunteer_database_list[i]
                break


        #USING ARBITRARY INDEX NUMBER RN
        index_num_of_timings = 12


        #ADDING TIMINGS TO THE ARBITRARY INDEX IN LIST
        temp_volunteer_list[index_num_of_timings] = ','.join(timing_info)


        #REPLACING OG VOLUNTEER WITH UPDATED VOLUNTEER AT SAME INDEX IN BIG LIST
        for j in range(len(volunteer_database_list)):
            if volunteer_database_list[j][1] == temp_volunteer_list[1] and volunteer_database_list[j][2] == temp_volunteer_list[2]:
                volunteer_database_list[j] = temp_volunteer_list

        #CREATING A LIST OF STRINGS
        new_rewritten_volunteer_temp = []
        for k in volunteer_database_list:
            new_rewritten_volunteer_temp.append('%'.join(k))



        #WRITING TO THE FILE
        volunteer_write_new = open("volunteer_database.txt", 'w')
        for i in range(len(new_rewritten_volunteer_temp)):
            volunteer_write_new.write(new_rewritten_volunteer_temp[i])
            print(new_rewritten_volunteer_temp[i])
        volunteer_write_new.close()







        time_summary_page.destroy()
        choose_days_screen.destroy()

    initial_calendar_lol()
    availability_screen.mainloop()

