from tkcalendar import calendar_
from tkcalendar import *

import tkinter
import datetime
import subprocess
import sys
import tkinter.messagebox
subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'tkcalendar'])


def add_calendar():

    #Setting up the screen
    availability_screen = tkinter.Toplevel()
    availability_screen.geometry("500x1000")
    availability_screen.title("Manage availability")
    #screen.configure(background="#A1CDEC")


    volunteer_list_file = open("Final_Files/volunteer_database.txt", "r")
    volunteer_database_list = []
    for line in volunteer_list_file:
        x = line.split("%")
        volunteer_database_list.append(x)

    times = ['00:00', '00:15', '00:30', '00:45', '01:00', '01:15', '01:30', '01:45', '02:00', '02:15', '02:30', '02:45', '03:00', '03:15', '03:30', '03:45', '04:00', '04:15', '04:30', '04:45', '05:00', '05:15', '05:30', '05:45', '06:00', '06:15', '06:30' , '06:45' , '07:00', '07:15' , '07:30' , '07:45' , '08:00', '08:15' , '08:30' , '08:45' , '09:00', '09:15' , '09:30' , '09:45' , '10:00', '10:15' , '10:30' , '10:45' , '11:00', '11:15' , '11:30' , '11:45' , '12:00', '12:15' , '12:30' , '12:45' , '13:00', '13:15' , '13:30' , '13:45' , '14:00', '14:15' , '14:30' , '14:45' , '15:00', '15:15' , '15:30' , '15:45' , '16:00', '16:15' , '16:30' , '16:45' , '17:00', '17:15' , '17:30' , '17:45' , '18:00', '18:15' , '18:30' , '18:45' , '19:00', '19:15' , '19:30' , '19:45' , '20:00', '20:15' , '20:30' , '20:45' , '21:00', '21:15' , '21:30' , '21:45' , '22:00', '22:15' , '22:30' , '22:45' , '23:00', '23:15' , '23:30' , '23:45' ]

    def delete1():
        availability_screen.destroy()

    def delete2():
        final_calendar_screen.destroy()

    def final_calendar_lol():
        availability_screen.destroy()
        global final_calendar_screen
        global final_calendar
        today = datetime.date.today()

        final_calendar_screen = tkinter.Toplevel()
        final_calendar_screen.geometry("500x1000")
        final_calendar_screen.title("Manage availability")

        max = datetime.date(2024, today.month, today.day)

        final_calendar_label = tkinter.Label(final_calendar_screen, text="Please enter the final date in the range:", font='Arial 18')
        final_calendar_label.pack(pady=50)
        initial_calendar_date = initial_calendar.selection_get()
        final_calendar = Calendar(final_calendar_screen, font = 'Arial 14', date_pattern="d/m/y", selectmode='day', foreground = 'black', mindate= initial_calendar_date, maxdate= max)
        final_calendar.pack(pady = 50)

        final_calendar_button = tkinter.Button(final_calendar_screen, text="Continue", width=30, command=choose_days)
        final_calendar_button.pack()
        final_calendar_back_button = tkinter.Button(final_calendar_screen, text="Quit", width=30, command=delete2)
        final_calendar_back_button.pack()

    global initial_calendar_date
    global initial_calendar
    intro_text = tkinter.Label(availability_screen, text = "Use this section to manage your availability\nPlease enter the range of days you will work as a volunteer", fg = 'Green', width= 300)
    intro_text.pack()
    today = datetime.date.today()
    max = datetime.date(2024, today.month, today.day)

    initial_calendar_label = tkinter.Label(availability_screen, text = "Please enter the inital date in the range:", font = 'Arial 18')
    initial_calendar_label.pack(pady = 50)
    initial_calendar = Calendar(availability_screen, font = 'Arial 14', date_pattern="d/m/y", selectmode='day', foreground = 'black', mindate= today, maxdate= max)
    initial_calendar.pack()

    initial_calendar_button = tkinter.Button(availability_screen, text = "Continue", width = 30, command = final_calendar_lol)
    initial_calendar_button.pack(pady = 20)
    initial_calendar_quit_button = tkinter.Button(availability_screen, text="Quit", width=30, command=delete1)
    initial_calendar_quit_button.pack()


    #Title text


    def choose_days():
        global choose_days_screen
        final_calendar_screen.destroy()
        choose_days_screen = tkinter.Toplevel()
        choose_days_screen.geometry("500x1000")
        choose_days_screen.title("Manage availability")

        range_confirmation_label = tkinter.Label(choose_days_screen, text = "Please check the summary below to ensure these are your dates of volunteering")
        range_confirmation_label.pack()

        start_date_confirmation = tkinter.Label(choose_days_screen, text = "The start date of your volunteering is: %s" %initial_calendar.get_date())
        start_date_confirmation.pack(pady = 20)

        end_date_confirmation = tkinter.Label(choose_days_screen, text = "The end date of your volunteering is: %s" %final_calendar.get_date())
        end_date_confirmation.pack(pady = 20)

        x = str(final_calendar.selection_get() - initial_calendar.selection_get())
        y = x.split(',')

        diff_confirmation = tkinter.Label(choose_days_screen, text = "The total days you will be working is: %s" %str(y[0]))
        diff_confirmation.pack(pady = 20)

        day_text = tkinter.Label(choose_days_screen, text="Please select which days of the week you are available\nand add the hours you are available: ")
        day_text.pack(pady = 20)
        global monday_text
        global tuesday_text
        global wednesday_text
        global thursday_text
        global friday_text
        global saturday_text
        global sunday_text
        monday_text = tkinter.IntVar()
        tuesday_text = tkinter.IntVar()
        wednesday_text = tkinter.IntVar()
        thursday_text = tkinter.IntVar()
        friday_text = tkinter.IntVar()
        saturday_text = tkinter.IntVar()
        sunday_text = tkinter.IntVar()

        def mon():
            global monday_initial_time
            global monday_final_time
            monday_initial_time = tkinter.StringVar()
            monday_final_time = tkinter.StringVar()
            if monday_text.get() == 1:
                monday_initial_time_menu = tkinter.OptionMenu(choose_days_screen, monday_initial_time, *times)
                monday_initial_time_menu.place(x = 180, y = 280, width = 100)

                monday_label = tkinter.Label(choose_days_screen, text= "to")
                monday_label.place(x = 305, y = 280)


                monday_final_time_menu = tkinter.OptionMenu(choose_days_screen, monday_final_time, *times)
                monday_final_time_menu.place(x=350, y=280, width=100)

            if monday_text.get() == 0:
                lol_label = tkinter.Label(choose_days_screen, text='')
                lol_label.place(x=160, y=280, width=800, height=40)

        def tues():
            global tuesday_initial_time
            global tuesday_final_time
            if tuesday_text.get() == 2:
                tuesday_initial_time = tkinter.StringVar()
                tuesday_initial_time_menu = tkinter.OptionMenu(choose_days_screen, tuesday_initial_time, *times)
                tuesday_initial_time_menu.place(x = 180, y = 330, width = 100)

                tuesday_label = tkinter.Label(choose_days_screen, text= "to")
                tuesday_label.place(x = 305, y = 330)

                tuesday_final_time = tkinter.StringVar()
                tuesday_final_time_menu = tkinter.OptionMenu(choose_days_screen, tuesday_final_time, *times)
                tuesday_final_time_menu.place(x=350, y=330, width=100)

            if tuesday_text.get() == 0:
                lol_label = tkinter.Label(choose_days_screen, text='')
                lol_label.place(x=160, y=330, width=800, height=40)

        def wed():
            global wednesday_initial_time
            global wednesday_final_time
            if wednesday_text.get() == 3:
                wednesday_initial_time = tkinter.StringVar()
                wednesday_initial_time_menu = tkinter.OptionMenu(choose_days_screen, wednesday_initial_time, *times)
                wednesday_initial_time_menu.place(x = 180, y = 380, width = 100)

                wednesday_label = tkinter.Label(choose_days_screen, text= "to")
                wednesday_label.place(x = 305, y = 380)

                wednesday_final_time = tkinter.StringVar()
                wednesday_final_time_menu = tkinter.OptionMenu(choose_days_screen, wednesday_final_time, *times)
                wednesday_final_time_menu.place(x=350, y=380, width=100)

            if wednesday_text.get() == 0:
                lol_label = tkinter.Label(choose_days_screen, text='')
                lol_label.place(x=160, y=380, width=800, height=40)

        def thurs():
            global thursday_initial_time
            global thursday_final_time
            if thursday_text.get() == 4:
                thursday_initial_time = tkinter.StringVar()
                thursday_initial_time_menu = tkinter.OptionMenu(choose_days_screen, thursday_initial_time, *times)
                thursday_initial_time_menu.place(x = 180, y = 430, width = 100)

                thursday_label = tkinter.Label(choose_days_screen, text= "to")
                thursday_label.place(x = 305, y = 430)

                thursday_final_time = tkinter.StringVar()
                thursday_final_time_menu = tkinter.OptionMenu(choose_days_screen, thursday_final_time, *times)
                thursday_final_time_menu.place(x=350, y=430, width=100)

            if thursday_text.get() == 0:
                lol_label = tkinter.Label(choose_days_screen, text='')
                lol_label.place(x=160, y=430, width=800, height=40)

        def fri():
            global friday_initial_time
            global friday_final_time
            if friday_text.get() == 5:
                friday_initial_time = tkinter.StringVar()
                friday_initial_time_menu = tkinter.OptionMenu(choose_days_screen, friday_initial_time, *times)
                friday_initial_time_menu.place(x = 180, y = 480, width = 100)

                friday_label = tkinter.Label(choose_days_screen, text= "to")
                friday_label.place(x = 305, y = 480)

                friday_final_time = tkinter.StringVar()
                friday_final_time_menu = tkinter.OptionMenu(choose_days_screen, friday_final_time, *times)
                friday_final_time_menu.place(x=350, y=480, width=100)

            if friday_text.get() == 0:
                lol_label = tkinter.Label(choose_days_screen, text='')
                lol_label.place(x=160, y=480, width=800, height=40)


        def sat():
            global saturday_initial_time
            global saturday_final_time
            if saturday_text.get() == 6:
                saturday_initial_time = tkinter.StringVar()
                saturday_initial_time_menu = tkinter.OptionMenu(choose_days_screen, saturday_initial_time, *times)
                saturday_initial_time_menu.place(x = 180, y = 530, width = 100)

                saturday_label = tkinter.Label(choose_days_screen, text= "to")
                saturday_label.place(x = 305, y = 530)

                saturday_final_time = tkinter.StringVar()
                saturday_final_time_menu = tkinter.OptionMenu(choose_days_screen, saturday_final_time, *times)
                saturday_final_time_menu.place(x=350, y=530, width=100)

            if saturday_text.get() == 0:
                lol_label = tkinter.Label(choose_days_screen, text='')
                lol_label.place(x=160, y=530, width=800, height=40)


        def sun():
            global sunday_initial_time
            global sunday_final_time
            if sunday_text.get() == 7:
                sunday_initial_time = tkinter.StringVar()
                sunday_initial_time_menu = tkinter.OptionMenu(choose_days_screen, sunday_initial_time, *times)
                sunday_initial_time_menu.place(x = 180, y = 580, width = 100)

                sunday_label = tkinter.Label(choose_days_screen, text= "to")
                sunday_label.place(x = 305, y = 580)

                sunday_final_time = tkinter.StringVar()
                sunday_final_time_menu = tkinter.OptionMenu(choose_days_screen, sunday_final_time, *times)
                sunday_final_time_menu.place(x=350, y=580, width=100)

            if sunday_text.get() == 0:
                lol_label = tkinter.Label(choose_days_screen, text='')
                lol_label.place(x=160, y=580, width=800, height=40)

        monday_entry = tkinter.Checkbutton(choose_days_screen, variable=monday_text, onvalue=1, offvalue=0, text="Monday", command = mon)
        tuesday_entry = tkinter.Checkbutton(choose_days_screen, variable=tuesday_text, onvalue=2, offvalue=0, text="Tuesday", command = tues)
        wednesday_entry = tkinter.Checkbutton(choose_days_screen, variable=wednesday_text, onvalue=3, offvalue=0, text="Wednesday", command = wed)
        thursday_entry = tkinter.Checkbutton(choose_days_screen, variable=thursday_text, onvalue=4, offvalue=0, text="Thursday", command = thurs)
        friday_entry = tkinter.Checkbutton(choose_days_screen, variable=friday_text, onvalue=5, offvalue=0, text="Friday", command = fri)
        saturday_entry = tkinter.Checkbutton(choose_days_screen, variable=saturday_text, onvalue=6, offvalue=0, text="Saturday", command = sat)
        sunday_entry = tkinter.Checkbutton(choose_days_screen, variable=sunday_text, onvalue=7, offvalue=0, text="Sunday", command = sun)
        monday_entry.place(x = 20, y = 280)
        tuesday_entry.place(x = 20, y = 330)
        wednesday_entry.place(x = 20, y = 380)
        thursday_entry.place(x = 20, y = 430)
        friday_entry.place(x = 20, y = 480)
        saturday_entry.place(x = 20, y = 530)
        sunday_entry.place(x = 20, y = 580)

        choose_days_button = tkinter.Button(choose_days_screen, text="Continue", width=30, command=save_to_file_volunteer)
        choose_days_button.place(x = 115, y = 650)

        final_calendar_back_button = tkinter.Button(choose_days_screen, text="Quit", width=30, command=delete3)
        final_calendar_back_button.place(x = 115, y = 680)

    def delete3():
        choose_days_screen.destroy()
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

    def summary_page():
        global time_summary_page
        time_summary_page = tkinter.Toplevel()
        time_summary_page.geometry("500x650")
        time_summary_page.title("Confirm hours submission")

        timings_confirmation = tkinter.Label(time_summary_page, text = "Please check the summary of details below to add to the database")
        timings_confirmation.pack()

        start_confirmation = tkinter.Label(time_summary_page, text = "The start date of your volunteering is: %s" %initial_calendar.get_date())
        start_confirmation.pack(pady = 30)

        end_confirmation = tkinter.Label(time_summary_page, text = "The end date of your volunteering is: %s" %final_calendar.get_date())
        end_confirmation.pack(pady = 30)

        if monday_text.get() == 1:
            monday_summary_initial = monday_initial_time.get()
            monday_summary_final = monday_final_time.get()
            monday_confirmation = tkinter.Label(time_summary_page, text = "On Monday: you are available from %s to %s" % (monday_summary_initial, monday_summary_final))
            monday_confirmation.pack(pady = 10)

        else:
            monday_no_confirmation = tkinter.Label(time_summary_page, text = "On Monday: you are busy")
            monday_no_confirmation.pack(pady = 10)

        if tuesday_text.get() == 2:
            tuesday_summary_initial = tuesday_initial_time.get()
            tuesday_summary_final = tuesday_final_time.get()
            tuesday_confirmation = tkinter.Label(time_summary_page, text = "On Tuesday: you are available from %s to %s" % (tuesday_summary_initial, tuesday_summary_final))
            tuesday_confirmation.pack(pady = 10)

        else:
            tuesday_no_confirmation = tkinter.Label(time_summary_page, text = "On Tuesday: you are busy")
            tuesday_no_confirmation.pack(pady = 10)

        if wednesday_text.get() == 3:
            wednesday_summary_initial = wednesday_initial_time.get()
            wednesday_summary_final = wednesday_final_time.get()
            wednesday_confirmation = tkinter.Label(time_summary_page, text = "On Wednesday: you are available from %s to %s" % (wednesday_summary_initial, wednesday_summary_final))
            wednesday_confirmation.pack(pady = 10)

        else:
            wednesday_no_confirmation = tkinter.Label(time_summary_page, text = "On Wednesday: you are busy")
            wednesday_no_confirmation.pack(pady = 10)

        if thursday_text.get() == 4:
            thursday_summary_initial = thursday_initial_time.get()
            thursday_summary_final = thursday_final_time.get()
            thursday_confirmation = tkinter.Label(time_summary_page, text = "On Thursday: you are available from %s to %s" % (thursday_summary_initial, thursday_summary_final))
            thursday_confirmation.pack(pady = 10)

        else:
            thursday_no_confirmation = tkinter.Label(time_summary_page, text = "On Thursday: you are busy")
            thursday_no_confirmation.pack(pady = 10)

        if friday_text.get() == 5:
            friday_summary_initial = friday_initial_time.get()
            friday_summary_final = friday_final_time.get()
            friday_confirmation = tkinter.Label(time_summary_page, text = "On Friday: you are available from %s to %s" % (friday_summary_initial, friday_summary_final))
            friday_confirmation.pack(pady = 10)

        else:
            friday_no_confirmation = tkinter.Label(time_summary_page, text = "On Friday: you are busy")
            friday_no_confirmation.pack(pady = 10)

        if saturday_text.get() == 6:
            saturday_summary_initial = saturday_initial_time.get()
            saturday_summary_final = saturday_final_time.get()
            saturday_confirmation = tkinter.Label(time_summary_page, text = "On Saturday: you are available from %s to %s" % (saturday_summary_initial, saturday_summary_final))
            saturday_confirmation.pack(pady = 10)

        else:
            saturday_no_confirmation = tkinter.Label(time_summary_page, text = "On Saturday: you are busy")
            saturday_no_confirmation.pack(pady = 10)

        if sunday_text.get() == 7:
            sunday_summary_initial = sunday_initial_time.get()
            sunday_summary_final = sunday_final_time.get()
            sunday_confirmation = tkinter.Label(time_summary_page, text = "On Sunday: you are available from %s to %s" % (sunday_summary_initial, sunday_summary_final))
            sunday_confirmation.pack(pady = 10)

        else:
            sunday_no_confirmation = tkinter.Label(time_summary_page, text = "On Sunday: you are busy")
            sunday_no_confirmation.pack(pady = 10)

        summary_button = tkinter.Button(time_summary_page, text="Submit", width=30, command=save_to_database)
        summary_button.pack(pady = 40)

        summary_button_no = tkinter.Button(time_summary_page, text="Change details", width=30, command=no)
        summary_button_no.pack()


    def no():
        time_summary_page.destroy()

    def save_to_database():

        volunteer_start_day = initial_calendar.get_date()
        volunteer_end_day = final_calendar.get_date()
        if monday_text.get() == 1:
            monday_summary_initial = monday_initial_time.get()
            monday_summary_final = monday_final_time.get()
            monday_summary = [monday_summary_initial, monday_summary_final]
        else:
            monday_summary = "NA"

        if tuesday_text.get() == 2:
            tuesday_summary_initial = tuesday_initial_time.get()
            tuesday_summary_final = tuesday_final_time.get()
            tuesday_summary = [tuesday_summary_initial, tuesday_summary_final]
        else:
            tuesday_summary = "NA"

        if wednesday_text.get() == 3:
            wednesday_summary_initial = wednesday_initial_time.get()
            wednesday_summary_final = wednesday_final_time.get()
            wednesday_summary = [wednesday_summary_initial, wednesday_summary_final]
        else:
            wednesday_summary = "NA"

        if thursday_text.get() == 4:
            thursday_summary_initial = thursday_initial_time.get()
            thursday_summary_final = thursday_final_time.get()
            thursday_summary = [thursday_summary_initial, thursday_summary_final]
        else:
            thursday_summary = "NA"

        if friday_text.get() == 5:
            friday_summary_initial = friday_initial_time.get()
            friday_summary_final = friday_final_time.get()
            friday_summary = [friday_summary_initial, friday_summary_final]
        else:
            friday_summary = "NA"

        if saturday_text.get() == 6:
            saturday_summary_initial = saturday_initial_time.get()
            saturday_summary_final = saturday_final_time.get()
            saturday_summary = [saturday_summary_initial, saturday_summary_final]
        else:
            saturday_summary = "NA"

        if sunday_text.get() == 7:
            sunday_summary_initial = sunday_initial_time.get()
            sunday_summary_final = sunday_final_time.get()
            sunday_summary = [sunday_summary_initial, sunday_summary_final]
        else:
            sunday_summary = "NA"

        timing_info = [volunteer_start_day, volunteer_end_day, monday_summary, tuesday_summary, wednesday_summary, thursday_summary, friday_summary, saturday_summary, sunday_summary]
        print(timing_info)

        time_summary_page.destroy()
        choose_days_screen.destroy()


    availability_screen.mainloop()

