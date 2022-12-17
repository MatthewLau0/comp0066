from tkinter import *
from tkinter import ttk
import datetime

camp_id = ""
user_id = ""

def camp_id_generate():
    global camp_id
    global user_id
    logins_file = open("successful_login.txt", "r")

    logins_list = []
    for line in logins_file:
        line_string = line.split("%")
        logins_list.append(line_string)
    logins_file.close()
    if len(logins_list) > 0:
        camp_id = logins_list[-1][0]
        user_id = logins_list[-1][1]
    else:
        pass

def add_calendar():
    camp_id_generate()

    availability_screen = Toplevel()
    availability_screen.title("Manage Availability")
    screen_width1 = availability_screen.winfo_screenwidth()
    screen_height1 = availability_screen.winfo_screenheight()
    window_height1 = screen_height1
    window_width1 = 900

    center_x1 = int(screen_width1 / 2 - window_width1 / 2)
    center_y1 = int(screen_height1 / 2 - window_height1 / 2)
    availability_screen.geometry(f'{window_width1}x{window_height1}+{center_x1}+{center_y1}')

    volunteer_list_file = open("volunteer_database.txt", "r")
    volunteer_database_list = []
    for line in volunteer_list_file:
        x = line.split("%")
        volunteer_database_list.append(x)

    volunteer_list_file.close()

    times = ["None", "M", "A", "E", "M+A", "M+E", "A+E", "M+A+E"]
    day_list = [str(i) for i in range(1, 32)]
    month_list = [str(i) for i in range(1, 13)]
    year_list = [str(i) for i in range(2023, 1899, -1)]

    volunteering_start_day = StringVar()
    volunteering_start_month = StringVar()
    volunteering_start_year = StringVar()
    volunteering_end_day = StringVar()
    volunteering_end_month = StringVar()
    volunteering_end_year = StringVar()
    volunteer_monday = StringVar()
    volunteer_tuesday = StringVar()
    volunteer_wednesday = StringVar()
    volunteer_thursday = StringVar()
    volunteer_friday = StringVar()
    volunteer_saturday = StringVar()
    volunteer_sunday = StringVar()

    start_date_label = Label(availability_screen, text="Please enter the date you would like to start volunteering")
    start_date_label.pack()
    start_date_frame = Frame(availability_screen)
    start_date_frame.pack()
    start_date_day_combobox = ttk.Combobox(start_date_frame, textvariable=volunteering_start_day, values=day_list)
    start_date_day_combobox.pack(side=LEFT)
    start_date_month_combobox = ttk.Combobox(start_date_frame, textvariable=volunteering_start_month, values=month_list)
    start_date_month_combobox.pack(side=LEFT)
    start_date_year_combobox = ttk.Combobox(start_date_frame, textvariable=volunteering_start_year, values=year_list)
    start_date_year_combobox.pack(side=LEFT)

    end_date_label = Label(availability_screen, text="Enter the end date for the emergency")
    end_date_label.pack()
    Label(availability_screen, text="Please enter the date you would like to ").pack()
    end_date_frame = Frame(availability_screen)
    end_date_frame.pack()
    end_date_day_combobox = ttk.Combobox(end_date_frame, textvariable=volunteering_end_day, values=day_list)
    end_date_day_combobox.pack(side=LEFT)
    end_date_month_combobox = ttk.Combobox(end_date_frame, textvariable=volunteering_end_month, values=month_list)
    end_date_month_combobox.pack(side=LEFT)
    end_date_year_combobox = ttk.Combobox(end_date_frame, textvariable=volunteering_end_year, values=year_list)
    end_date_year_combobox.pack(side=LEFT)

    days_choosing = Label(availability_screen, text="Please choose which shifts you can work on each of the days")
    days_choosing.pack()
    Label(availability_screen, text="M = Morning   A = Afternoon   E = Evening").pack()

    monday_frame = Frame(availability_screen)
    monday_frame.pack()
    Label(monday_frame, text="Monday: ").pack(side=LEFT)
    ttk.Combobox(monday_frame, textvariable=volunteer_monday, values=times).pack(side=LEFT)

    tuesday_frame = Frame(availability_screen)
    tuesday_frame.pack()
    Label(tuesday_frame, text="Tuesday: ").pack(side=LEFT)
    ttk.Combobox(tuesday_frame, textvariable=volunteer_tuesday, values=times).pack(side=LEFT)

    wednesday_frame = Frame(availability_screen)
    wednesday_frame.pack()
    Label(wednesday_frame, text="Wednesday: ").pack(side=LEFT)
    ttk.Combobox(wednesday_frame, textvariable=volunteer_wednesday, values=times).pack(side=LEFT)

    thursday_frame = Frame(availability_screen)
    thursday_frame.pack()
    Label(thursday_frame, text="Thursday: ").pack(side=LEFT)
    ttk.Combobox(thursday_frame, textvariable=volunteer_thursday, values=times).pack(side=LEFT)

    friday_frame = Frame(availability_screen)
    friday_frame.pack()
    Label(friday_frame, text="Friday: ").pack(side=LEFT)
    ttk.Combobox(friday_frame, textvariable=volunteer_friday, values=times).pack(side=LEFT)

    saturday_frame = Frame(availability_screen)
    saturday_frame.pack()
    Label(saturday_frame, text="Saturday: ").pack(side=LEFT)
    ttk.Combobox(saturday_frame, textvariable=volunteer_saturday, values=times).pack(side=LEFT)

    sunday_frame = Frame(availability_screen)
    sunday_frame.pack()
    Label(sunday_frame, text="Sunday: ").pack(side=LEFT)
    ttk.Combobox(sunday_frame, textvariable=volunteer_sunday, values=times).pack(side=LEFT)

    def generate_start_date():
        if len(volunteering_start_day.get()) == 0 or len(volunteering_start_month.get()) == 0 or len(volunteering_start_year.get()) == 0:
            return "empty"
        else:
            volunteer_from_date_string = f"{volunteering_start_day.get()}-{volunteering_start_month.get()}-{volunteering_start_year.get()}"
            volunteer_from_date_int = datetime.datetime.strptime(volunteer_from_date_string, "%d-%m-%Y")
            volunteer_from_date = datetime.datetime.date(volunteer_from_date_int)
            return volunteer_from_date

    def generate_end_date():
        if len(volunteering_end_day.get()) == 0 or len(volunteering_end_month.get()) == 0 or len(volunteering_end_year.get()) == 0:
            return "empty"
        else:
            volunteer_to_date_string = f"{volunteering_end_day.get()}-{volunteering_end_month.get()}-{volunteering_end_year.get()}"
            volunteer_to_date_int = datetime.datetime.strptime(volunteer_to_date_string, "%d-%m-%Y")
            volunteer_to_date = datetime.datetime.date(volunteer_to_date_int)
            return volunteer_to_date

    def availability_summary():

        availability_summary_screen = Toplevel()
        availability_summary_screen.title("Your Availability Summary")

        screen_width2 = availability_summary_screen.winfo_screenwidth()
        screen_height2 = availability_summary_screen.winfo_screenheight()
        window_height2 = screen_height2
        window_width2 = 900

        center_x2 = int(screen_width2 / 2 - window_width2 / 2)
        center_y2 = int(screen_height2 / 2 - window_height2 / 2)
        availability_summary_screen.geometry(f'{window_width2}x{window_height2}+{center_x2}+{center_y2}')

        availability_summary_screen_label = Label(availability_summary_screen, text="Please view below a summary of your chosen availability")
        availability_summary_screen_label.pack()

        Label(availability_summary_screen, text=f"You are available to start from: {generate_start_date()}").pack()
        Label(availability_summary_screen, text=f"You are available till: {generate_end_date()}").pack()
        Label(availability_summary_screen, text=f"You can volunteer in the following shifts:").pack()
        Label(availability_summary_screen, text=f"Monday: {volunteer_monday.get()}").pack()
        Label(availability_summary_screen, text=f"Tuesday: {volunteer_tuesday.get()}").pack()
        Label(availability_summary_screen, text=f"Wednesday: {volunteer_wednesday.get()}").pack()
        Label(availability_summary_screen, text=f"Thursday: {volunteer_thursday.get()}").pack()
        Label(availability_summary_screen, text=f"Friday: {volunteer_friday.get()}").pack()
        Label(availability_summary_screen, text=f"Saturday: {volunteer_saturday.get()}").pack()
        Label(availability_summary_screen, text=f"Sunday: {volunteer_sunday.get()}").pack()

        def submit_availability():
            availability_summary_screen.destroy()
            availability_screen.destroy()

            availability = ["", "", "", "", "", "", "", "", ""]

            availability[0] = str(generate_start_date())
            availability[1] = str(generate_end_date())
            availability[2] = volunteer_monday.get()
            availability[3] = volunteer_tuesday.get()
            availability[4] = volunteer_wednesday.get()
            availability[5] = volunteer_thursday.get()
            availability[6] = volunteer_friday.get()
            availability[7] = volunteer_saturday.get()
            availability[8] = volunteer_sunday.get()

            availability_string = "#".join(availability)

            volunteer_read = open("volunteer_database.txt", "r")

            volunteer_list = []
            for line in volunteer_read:
                line_string = line.split("%")
                volunteer_list.append(line_string)

            volunteer_read.close()

            for i in volunteer_list:
                if i[1] == str(user_id):
                    i[12] = availability_string

            clear_file = open("volunteer_database.txt", "w")
            clear_file.close()

            for entry in volunteer_list:
                with open("volunteer_database.txt", "a") as volunteer_write:
                    updated_volunteer_string = "%".join(entry)
                    volunteer_write.write(updated_volunteer_string)
            volunteer_write.close()

        Button(availability_summary_screen, text="Edit", command=availability_summary_screen.destroy).pack()
        Button(availability_summary_screen, text="Submit", command=submit_availability).pack()

    errors_availability = []

    def availability_verify():

        start_date_label.config(text="Start Date entered!", fg='green')
        end_date_label.config(text="End Date entered!", fg='green')
        days_choosing.config(text="All days filled!", fg='green')

        errors_availability.clear()

        today = datetime.datetime.today()

        days_chosen_list = [volunteer_monday.get(), volunteer_tuesday.get(), volunteer_wednesday.get(), volunteer_thursday.get(), volunteer_friday.get(), volunteer_saturday.get(), volunteer_sunday.get()]

        if generate_start_date() == "empty":
            start_date_label.config(text="Please enter a start date", fg='#f00')
            errors_availability.append(1)
        if generate_end_date() == "empty":
            end_date_label.config(text="Please enter an end date", fg='#f00')
            errors_availability.append(2)
        for i in days_chosen_list:
            if i not in times:
                days_choosing.config(text="Please enter availability for all days", fg='#f00')
                errors_availability.append(3)
        if generate_start_date() != "empty" and generate_end_date() != "empty":
            test_start_date = datetime.datetime.strptime(str(generate_start_date()), "%Y-%m-%d")
            test_end_date = datetime.datetime.strptime(str(generate_end_date()), "%Y-%m-%d")
            if test_start_date < today:
                start_date_label.config(text="Please enter a start date later than today.", fg='#f00')
                errors_availability.append(6)
            if test_end_date < test_start_date:
                end_date_label.config(text="Please enter an end date later than the start date.", fg='#f00')
                errors_availability.append(7)

        if len(errors_availability) > 0:
            pass
        else:
            availability_summary()

    done_button = Button(availability_screen, text="Submit", command=availability_verify)
    done_button.pack()

    availability_screen.mainloop()
