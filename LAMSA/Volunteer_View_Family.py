from tkinter import *
from tkinter import ttk
import datetime

def table():
    camp_id_to_view = ""
    logins_file = open("successful_login.txt", "r")

    logins_list = []
    for line in logins_file:
        line_string = line.split("%")
        logins_list.append(line_string)
    logins_file.close()
    if len(logins_list) > 0:
        camp_id_to_view = logins_list[-1][0]

    refugee_list_file = open("refugee_database.txt", "r")
    refugee_database_list = []
    for line in refugee_list_file:
        x = line.split("%")
        if x[0] == camp_id_to_view:
            refugee_database_list.append(x)
    refugee_list_file.close()

    view_refugee_table = Toplevel()
    screen_width1 = view_refugee_table.winfo_screenwidth()
    screen_height1 = view_refugee_table.winfo_screenheight()
    window_height1 = screen_height1
    window_width1 = screen_width1 - 100

    center_x1 = int(screen_width1 / 2 - window_width1 / 2)
    center_y1 = int(screen_height1 / 2 - window_height1 / 2)
    view_refugee_table.geometry(f'{window_width1}x{window_height1}+{center_x1}+{center_y1}')
    view_refugee_table.title("Table of Refugees")

    emergency_database_label = Label(view_refugee_table,
                                     text="Please use the below table to view a full list of refugees")
    emergency_database_label.pack()

    emergency_database_frame = Frame(view_refugee_table)
    emergency_database_frame.pack()

    emergency_database_table = ttk.Treeview(view_refugee_table)

    emergency_database_table['columns'] = (
        "CampID", "ID", "Name", "Family size", "Date of Birth", "Age", "Gender", "Phone Number", "Address", "No. family with condition",
        "Medical Conditions", "Accommodation", "Ration", "Toilet", "Medical")

    emergency_database_table.column("#0", width=0, stretch=NO)
    emergency_database_table.column("CampID", anchor='center', width=50)
    emergency_database_table.column("ID", anchor='center', width=30)
    emergency_database_table.column("Name", anchor='center', width=80)
    emergency_database_table.column("Family size", anchor='center', width=60)
    emergency_database_table.column("Date of Birth", anchor='center', width=80)
    emergency_database_table.column("Age", anchor='center', width=40)
    emergency_database_table.column("Gender", anchor='center', width=80)
    emergency_database_table.column("Phone Number", anchor='center', width=120)
    emergency_database_table.column("Address", anchor='center', width=200)
    emergency_database_table.column("No. family with condition", anchor='center', width=85)
    emergency_database_table.column("Medical Conditions", anchor='center', width=210)
    emergency_database_table.column("Accommodation", anchor='center', width=80)
    emergency_database_table.column("Ration", anchor='center', width=80)
    emergency_database_table.column("Toilet", anchor='center', width=70)
    emergency_database_table.column("Medical", anchor='center', width=70)

    emergency_database_table.heading("CampID", text="Camp ID", anchor='center')
    emergency_database_table.heading("ID", text="ID", anchor='center')
    emergency_database_table.heading("Name", text="Name", anchor='center')
    emergency_database_table.heading("Family size", text="Family size", anchor='center')
    emergency_database_table.heading("Date of Birth", text="Date of Birth", anchor='center')
    emergency_database_table.heading("Age", text="Age", anchor='center')
    emergency_database_table.heading("Gender", text="Gender", anchor='center')
    emergency_database_table.heading("Phone Number", text="Phone Number", anchor='center')
    emergency_database_table.heading("Address", text="Address", anchor='center')
    emergency_database_table.heading("No. family with condition", text="No. w/ conditions", anchor='center')
    emergency_database_table.heading("Medical Conditions", text="Medical Conditions", anchor='center')
    emergency_database_table.heading("Accommodation", text="Accom.", anchor='center')
    emergency_database_table.heading("Ration", text="Rations", anchor='center')
    emergency_database_table.heading("Toilet", text="Toilet", anchor='center')
    emergency_database_table.heading("Medical", text="Medical", anchor='center')

    for i in range(0, len(refugee_database_list)):
        emergency_database_table.insert(parent='', index=i, iid=i, values=(
            str(refugee_database_list[i][0]), str(refugee_database_list[i][1]),
            refugee_database_list[i][2], refugee_database_list[i][3], str(refugee_database_list[i][4]),
            refugee_database_list[i][5], refugee_database_list[i][6], refugee_database_list[i][7],
            refugee_database_list[i][8], refugee_database_list[i][9], refugee_database_list[i][10],
            refugee_database_list[i][11], refugee_database_list[i][12], refugee_database_list[i][13], refugee_database_list[i][14]))

    emergency_database_table.pack(fill='both')

    def modify_family():
        update_family_screen_id_2 = Toplevel()
        update_family_screen_id_2.title("Update ID Select")

        screen_width4 = update_family_screen_id_2.winfo_screenwidth()
        screen_height4 = update_family_screen_id_2.winfo_screenheight()
        window_height4 = 110
        window_width4 = 300

        center_x4 = int(screen_width4 / 2 - window_width4 / 2)
        center_y4 = int(screen_height4 / 2 - window_height4 / 2)
        update_family_screen_id_2.geometry(f'{window_width4}x{window_height4}+{center_x4}+{center_y4}')

        id_list_2 = []

        for n in refugee_database_list:
            id_list_2.append(n[1])

        selected_refugee_id_2 = StringVar()

        id_select_label_2 = Label(update_family_screen_id_2, text="Please choose a Family ID to update")
        id_select_label_2.pack()
        selected_refugee_id_2.set("Select ID")
        id_select_option_2 = ttk.Combobox(update_family_screen_id_2, textvariable=selected_refugee_id_2, values=id_list_2)
        id_select_option_2.pack()

        def update_run():
            update_family_screen_id_2.destroy()

            country_list = ['Afghanistan', 'Aland Islands', 'Albania', 'Algeria', 'American Samoa', 'Andorra', 'Angola',
                            'Anguilla', 'Antarctica', 'Antigua and Barbuda', 'Argentina', 'Armenia', 'Aruba',
                            'Australia',
                            'Austria', 'Azerbaijan', 'Bahamas', 'Bahrain', 'Bangladesh', 'Barbados', 'Belarus',
                            'Belgium',
                            'Belize', 'Benin', 'Bermuda', 'Bhutan', 'Bolivia', 'Bosnia and Herzegovina', 'Botswana',
                            'Bouvet Island', 'Brazil', 'British Indian Ocean Territory', 'Brunei Darussalam',
                            'Bulgaria',
                            'Burkina Faso', 'Burundi', 'Cambodia', 'Cameroon', 'Canada', 'Cape Verde', 'Cayman Islands',
                            'Central African Republic', 'Chad', 'Chile', 'China', 'Christmas Island',
                            'Cocos (Keeling) Islands', 'Colombia', 'Comoros', 'Congo',
                            'The Democratic Republic of the Congo', 'Cook Islands', 'Costa Rica', "Côte d'Ivoire",
                            'Croatia', 'Cuba', 'Curaçao', 'Cyprus', 'Czech Republic', 'Denmark', 'Djibouti', 'Dominica',
                            'Dominican Republic', 'Ecuador', 'Egypt', 'El Salvador', 'Equatorial Guinea', 'Eritrea',
                            'Estonia', 'Ethiopia', 'Faroe Islands', 'Fiji', 'Finland', 'France', 'French Guiana',
                            'French Polynesia', 'French Southern Territories', 'Gabon', 'Gambia', 'Georgia', 'Germany',
                            'Ghana', 'Gibraltar', 'Greece', 'Greenland', 'Grenada', 'Guadeloupe', 'Guam', 'Guatemala',
                            'Guernsey', 'Guinea', 'Guinea-Bissau', 'Guyana', 'Haiti',
                            'Heard Island and McDonald Islands',
                            'Vatican City', 'Honduras', 'Hong Kong', 'Hungary', 'Iceland', 'India', 'Indonesia', 'Iran',
                            'Iraq', 'Ireland', 'Isle of Man', 'Israel', 'Italy', 'Jamaica', 'Japan', 'Jersey', 'Jordan',
                            'Kazakhstan', 'Kenya', 'Kiribati', 'Republic of Korea', 'Kuwait', 'Kyrgyzstan', "Laos",
                            'Latvia', 'Lebanon', 'Lesotho', 'Liberia', 'Libya', 'Liechtenstein', 'Lithuania',
                            'Luxembourg',
                            'Macao', 'Macedonia', 'Madagascar', 'Malawi', 'Malaysia', 'Maldives', 'Mali', 'Malta',
                            'Marshall Islands', 'Martinique', 'Mauritania', 'Mauritius', 'Mayotte', 'Mexico',
                            'Micronesia',
                            'Moldova', 'Monaco', 'Mongolia', 'Montenegro', 'Montserrat', 'Morocco', 'Mozambique',
                            'Myanmar',
                            'Namibia', 'Nauru', 'Nepal', 'Netherlands', 'New Caledonia', 'New Zealand', 'Nicaragua',
                            'Niger', 'Nigeria', 'Niue', 'Norfolk Island', 'Northern Mariana Islands', 'Norway', 'Oman',
                            'Pakistan', 'Palau', 'Palestinian Territory', 'Panama', 'Papua New Guinea', 'Paraguay',
                            'Peru',
                            'Philippines', 'Pitcairn', 'Poland', 'Portugal', 'Puerto Rico', 'Qatar', 'Réunion',
                            'Romania',
                            'Russia', 'Rwanda', 'Saint Lucia', 'Samoa', 'San Marino', 'Sao Tome and Principe',
                            'Saudi Arabia', 'Senegal', 'Serbia', 'Seychelles', 'Sierra Leone', 'Singapore', 'Slovakia',
                            'Slovenia', 'Solomon Islands', 'Somalia', 'South Africa', 'Spain', 'Sri Lanka', 'Sudan',
                            'Suriname', 'South Sudan', 'Svalbard', 'Swaziland', 'Sweden', 'Switzerland',
                            'Syrian Arab Republic', 'Taiwan', 'Tajikistan', 'Tanzania', 'Thailand', 'Timor-Leste',
                            'Togo',
                            'Tokelau', 'Tonga', 'Trinidad and Tobago', 'Tunisia', 'Turkey', 'Turkmenistan',
                            'Turks and Caicos Islands', 'Tuvalu', 'Uganda', 'Ukraine', 'United Arab Emirates',
                            'United Kingdom', 'United States', 'Uruguay', 'Uzbekistan', 'Vanuatu', 'Venezuela',
                            'Vietnam',
                            'Yemen', 'Zambia', 'Zimbabwe']

            update_refugee_screen = Toplevel()
            update_refugee_screen.title(f"Update Family {selected_refugee_id_2.get()}")

            screen_width2 = update_refugee_screen.winfo_screenwidth()
            screen_height2 = update_refugee_screen.winfo_screenheight()
            window_height2 = screen_height2
            window_width2 = 900

            center_x2 = int(screen_width2 / 2 - window_width2 / 2)
            center_y2 = int(screen_height2 / 2 - window_height2 / 2)
            update_refugee_screen.geometry(f'{window_width2}x{window_height2}+{center_x2}+{center_y2}')

            current_updating_refugee = []
            for ref in refugee_database_list:
                if ref[1] == str(selected_refugee_id_2.get()):
                    current_updating_refugee.append(ref)

            refugee_date = current_updating_refugee[0][4].split("/")
            number = current_updating_refugee[0][7].split("#")
            address = current_updating_refugee[0][8].replace(" ", "").split(",")

            updating_family_camp_id = current_updating_refugee[0][0]
            updating_family_id = current_updating_refugee[0][1]
            update_refugee_name = current_updating_refugee[0][2]
            updating_family_size = current_updating_refugee[0][3]
            update_refugee_date = refugee_date[0]
            update_refugee_month = refugee_date[1]
            update_refugee_year = refugee_date[2]
            update_refugee_gender = current_updating_refugee[0][6]
            update_phone_area_code = number[0]
            update_phone_number = number[1]
            update_refugee_address1 = address[0]
            update_refugee_address2 = address[1]
            update_refugee_address_city = address[2]
            update_refugee_address_post = address[3]
            update_refugee_address_country = address[4]
            updating_family_health_no = current_updating_refugee[0][9]
            update_refugee_family_health = current_updating_refugee[0][10]
            updating_refugee_accom = current_updating_refugee[0][11]
            updating_refugee_ration = current_updating_refugee[0][12]
            updating_refugee_toilet = current_updating_refugee[0][13]
            updating_refugee_medical = current_updating_refugee[0][14]
            updating_date_created = current_updating_refugee[0][15]

            refugee_name = StringVar()
            refugee_date = StringVar()
            refugee_month = StringVar()
            refugee_year = StringVar()
            refugee_gender = StringVar()
            phone_area_code = StringVar()
            phone_number = StringVar()
            refugee_address1 = StringVar()
            refugee_address2 = StringVar()
            refugee_address_city = StringVar()
            refugee_address_post = StringVar()
            refugee_address_country = StringVar()
            refugee_family_health = StringVar()

            Label(update_refugee_screen, text="To create a new Refugee Family, please fill in the form below.").pack()

            name_label = Label(update_refugee_screen, text="Full Name:")
            name_label.pack()
            name_entry = Entry(update_refugee_screen, textvariable=refugee_name)
            name_entry.insert(END, update_refugee_name)
            name_entry.pack()

            day_list = [str(i) for i in range(1, 32)]
            month_list = [str(i) for i in range(1, 13)]
            year_list = [str(i) for i in range(2023, 1899, -1)]

            dob_label = Label(update_refugee_screen, text="Enter the start date for the emergency")
            dob_label.pack()
            dob_frame = Frame(update_refugee_screen)
            dob_frame.pack()
            date_day_combobox = ttk.Combobox(dob_frame, textvariable=refugee_date, values=day_list)
            date_day_combobox.insert(END, update_refugee_date)
            date_day_combobox.pack(side=LEFT)
            date_month_combobox = ttk.Combobox(dob_frame, textvariable=refugee_month, values=month_list)
            date_month_combobox.insert(END, update_refugee_month)
            date_month_combobox.pack(side=LEFT)
            date_year_combobox = ttk.Combobox(dob_frame, textvariable=refugee_year, values=year_list)
            date_year_combobox.insert(END, update_refugee_year)
            date_year_combobox.pack(side=LEFT)

            def generate_dob():
                if len(refugee_date.get()) == 0 or len(refugee_month.get()) == 0 or len(refugee_year.get()) == 0:
                    return "empty"
                else:
                    try:
                        startdateComplete = ("%s-%s-%s" % (refugee_year.get(), refugee_month.get(), refugee_date.get()))
                        startDateTime = datetime.datetime.strptime(startdateComplete, "%Y-%m-%d")
                        startDate = datetime.datetime.date(startDateTime)
                        return startDate
                    except ValueError:
                        return "empty"

            def generate_age():
                today = datetime.datetime.today()
                x = generate_dob()
                if x == "empty":
                    pass
                else:
                    DOB = datetime.datetime.strptime(str(x), "%Y-%m-%d").date()
                    refugee_age = 0

                    if DOB.month < today.month and today.year > DOB.year:
                        refugee_age = today.year - DOB.year

                    elif DOB.month > DOB.month and today.year > DOB.year:
                        refugee_age = today.year - DOB.year - 1

                    elif DOB.month == today.month and today.year > DOB.year and today.day < DOB.day:
                        refugee_age = today.year - DOB.year - 1

                    elif DOB.month == today.month and today.year > DOB.year and today.day > DOB.day:
                        refugee_age = today.year - DOB.year
                    return refugee_age

            gender_list = ["Male", "Female", "Other", "Prefer not to say"]

            gender_label = Label(update_refugee_screen, text="Gender:")
            gender_label.pack()

            gender_entry = ttk.Combobox(update_refugee_screen, textvariable=refugee_gender, values=gender_list)
            gender_entry.insert(END, update_refugee_gender)
            gender_entry.pack()

            phone_number_label = Label(update_refugee_screen, text="Please enter a phone number")
            phone_number_label.pack()
            phone_frame = Frame(update_refugee_screen)
            phone_frame.pack()
            area_code_sign = Label(phone_frame, text="+")
            area_code_sign.pack(side=LEFT)
            phone_number_area_code_entry = Entry(phone_frame, textvariable=phone_area_code)
            phone_number_area_code_entry.insert(END, update_phone_area_code)
            phone_number_area_code_entry.pack(side=LEFT, ipadx=1)
            phone_number_entry = Entry(phone_frame, textvariable=phone_number)
            phone_number_entry.insert(END, update_phone_number)
            phone_number_entry.pack(side=LEFT)

            address1_label = Label(update_refugee_screen, text="Address Line 1:")
            address1_label.pack()
            address1_entry = Entry(update_refugee_screen, textvariable=refugee_address1)
            address1_entry.insert(END, update_refugee_address1)
            address1_entry.pack()

            address2_label = Label(update_refugee_screen, text="Address Line 2:")
            address2_label.pack()
            address2_entry = Entry(update_refugee_screen, textvariable=refugee_address2)
            address2_entry.insert(END, update_refugee_address2)
            address2_entry.pack()

            address3_label = Label(update_refugee_screen, text="City:")
            address3_label.pack()
            address3_entry = Entry(update_refugee_screen, textvariable=refugee_address_city)
            address3_entry.insert(END, update_refugee_address_city)
            address3_entry.pack()

            address4_label = Label(update_refugee_screen, text="Postcode:")
            address4_label.pack()
            address4_entry = Entry(update_refugee_screen, textvariable=refugee_address_post)
            address4_entry.insert(END, update_refugee_address_post)
            address4_entry.pack()

            address5_label = Label(update_refugee_screen, text="Country:")
            address5_label.pack()
            address5_entry = ttk.Combobox(update_refugee_screen, textvariable=refugee_address_country, values=country_list)
            address5_entry.insert(END, update_refugee_address_country)
            address5_entry.pack()

            health_label = Label(update_refugee_screen, text="Details of any health conditions within the family")
            health_label.pack()
            health_entry = Entry(update_refugee_screen, textvariable=refugee_family_health, width=40)
            health_entry.insert(END, update_refugee_family_health)
            health_entry.pack()

            def summary():

                refugee_summary = Toplevel()

                refugee_summary.title("Refugee Family Summary")

                label_1 = Label(refugee_summary, text="Please check that you are happy with the entry below:")
                label_1.pack()

                summary_label = Label(refugee_summary, text=
f"""Lead Member Name: \n{refugee_name.get()} 
Family Size: \n{updating_family_size} 
Lead Member DoB: \n{refugee_date.get()}/{refugee_month.get()}/{refugee_year.get()} (Age: {generate_age()})
Lead Member Gender: \n{refugee_gender.get()} 
Contact Number: \n+{phone_area_code.get()} {phone_number.get()}
Address: \n{refugee_address1.get()}, {refugee_address2.get()}, {refugee_address_city.get()}, {refugee_address_post.get()}, {refugee_address_country.get()} 
No. Members with Health Conditions: \n{updating_family_health_no}
Health Condition Details: \n{refugee_family_health.get()}\n\n
Accommodation: \n{updating_refugee_accom}
Ration Stall: \n{updating_refugee_ration}
Toilet Block: \n{updating_refugee_toilet}
Medical Dispensary: \n{updating_refugee_medical}\n""")
                summary_label.pack()

                def submit_command():
                    view_refugee_table.destroy()
                    phone_number_complete = ("%s#%s" % (phone_area_code.get(), phone_number.get()))

                    updated_family = ["NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA"]

                    updated_family[0] = str(updating_family_camp_id)
                    updated_family[1] = str(updating_family_id)
                    updated_family[2] = refugee_name.get()
                    updated_family[3] = str(updating_family_size)
                    updated_family[4] = f"{refugee_date.get()}/{refugee_month.get()}/{refugee_year.get()}"
                    updated_family[5] = str(generate_age())
                    updated_family[6] = refugee_gender.get()
                    updated_family[7] = phone_number_complete
                    updated_family[8] = f"{refugee_address1.get()}, {refugee_address2.get()}, {refugee_address_city.get()}, {refugee_address_post.get()}, {refugee_address_country.get()}"
                    updated_family[9] = str(updating_family_health_no)
                    updated_family[10] = refugee_family_health.get()
                    updated_family[11] = updating_refugee_accom
                    updated_family[12] = updating_refugee_ration
                    updated_family[13] = updating_refugee_toilet
                    updated_family[14] = updating_refugee_medical
                    updated_family[15] = updating_date_created

                    refugee_read = open("refugee_database.txt", "r")

                    refugee_list = []
                    for refugee_line in refugee_read:
                        line_string_1 = refugee_line.split("%")
                        refugee_list.append(line_string_1)

                    refugee_read.close()

                    refugee_list = [updated_family if num[1] == str(updating_family_id) else num for num in refugee_list]

                    clear_file = open("refugee_database.txt", "w")
                    clear_file.close()

                    for entry in refugee_list:
                        with open("refugee_database.txt", "a") as refugee_write:
                            updated_refugee_string = "%".join(entry)
                            refugee_write.write(updated_refugee_string)
                    refugee_write.close()

                    refugee_summary.destroy()
                    update_refugee_screen.destroy()

                edit_button = Button(refugee_summary, text="Cancel", command=refugee_summary.destroy)
                edit_button.pack()
                submit_button = Button(refugee_summary, text="Submit", command=submit_command)
                submit_button.pack()

                refugee_summary.mainloop()

            error_new_volunteer = []

            def check_block():

                name_label.config(text="Name entered", fg='green')
                dob_label.config(text="DoB entered", fg='green')
                gender_label.config(text="Gender entered", fg='green')
                phone_number_label.config(text="Phone Number is Valid!", fg="green")
                address1_label.config(text="Address Line 1 entered", fg='green')
                address2_label.config(text="Address Line 2 entered", fg='green')
                address3_label.config(text="City entered", fg='green')
                address4_label.config(text="Post Code entered", fg='green')
                address5_label.config(text="Country entered", fg='green')
                health_label.config(text="Health details entered", fg='green')

                error_new_volunteer.clear()

                if refugee_name.get().strip() == "":
                    name_label.config(text="Please enter a name", fg='#f00')
                    error_new_volunteer.append(1)
                if all(char.isalpha() for char in refugee_name.get().replace(" ", "")) is False:
                    name_label.config(text="Name can only contain alphabetical characters", fg='#f00')
                    error_new_volunteer.append(1.1)
                today = datetime.datetime.today()
                if generate_dob() == "empty":
                    dob_label.config(text="Please enter DoB", fg='#f00')
                    error_new_volunteer.append(5)
                if generate_dob() != "empty":
                    test_start_date = datetime.datetime.strptime(str(generate_dob()), "%Y-%m-%d")
                    if test_start_date > today:
                        dob_label.config(text="Please enter a valid DoB", fg='#f00')
                if len(phone_area_code.get()) > 4:
                    phone_number_label.config(
                        text="Please enter a valid phone area code and a valid phone number",
                        fg='#f00')
                    error_new_volunteer.append("e4")
                if len(phone_number.get()) > 15 or len(
                        phone_number.get()) < 7 or phone_number.get().isalnum() is not True:
                    phone_number_label.config(
                        text="Please enter a valid phone area code and a valid phone number",
                        fg='#f00')
                    error_new_volunteer.append("e5")
                if refugee_gender.get() not in gender_list:
                    gender_label.config(text="Please enter a gender from the provided list", fg='#f00')
                if refugee_address_country.get() not in country_list:
                    address5_label.config(text="Please enter a country from the list provided", fg='#f00')
                if refugee_address1.get().strip() == "":
                    address1_label.config(text="Please enter a valid Address Line 1", fg='#f00')
                if refugee_address_city.get().strip() == "":
                    address3_label.config(text="Please enter a valid City", fg='#f00')
                if refugee_address_post.get().strip() == "":
                    address4_label.config(text="Please enter a valid Postcode", fg='#f00')

                if len(error_new_volunteer) > 0:
                    pass
                else:
                    summary()

            button_block_done = Button(update_refugee_screen, text="Submit", command=check_block)
            button_block_done.pack()
            Button(update_refugee_screen, text="Cancel", command=update_refugee_screen.destroy).pack()

        def run_the_update():
            if selected_refugee_id_2.get() not in id_list_2:
                id_select_label_2.config(fg="#f00")
            else:
                update_family_screen_id_2.destroy()
                update_run()

        new_block_done = Button(update_family_screen_id_2, text="Select", command=run_the_update)
        new_block_done.pack()
        Button(update_family_screen_id_2, text="Close", command=update_family_screen_id_2.destroy).pack()

    def assign_to_unavailable():
        assign_id = Toplevel()
        assign_id.title("Update ID Select")

        screen_width3 = assign_id.winfo_screenwidth()
        screen_height3 = assign_id.winfo_screenheight()
        window_height3 = 110
        window_width3 = 500

        center_x3 = int(screen_width3 / 2 - window_width3 / 2)
        center_y3 = int(screen_height3 / 2 - window_height3 / 2)
        assign_id.geometry(f'{window_width3}x{window_height3}+{center_x3}+{center_y3}')

        unassigned_id_list = []

        for ref in refugee_database_list:
            if "Accommodation Unavailable" in ref or "Ration Unavailable" in ref or "Toilet Unavailable" in ref or "Medical Unavailable" in ref:
                unassigned_id_list.append(ref[1])

        selected_family_id = StringVar()

        select_label = Label(assign_id, text="Please choose a Family ID to assign amenities to")
        select_label.pack()
        selected_family_id.set("Select ID")
        select_option = ttk.Combobox(assign_id, textvariable=selected_family_id, values=unassigned_id_list)
        select_option.pack()

        def run_assignment():
            assign_id.destroy()

            current_family = []
            for z in refugee_database_list:
                if z[1] == selected_family_id.get():
                    current_family.append(z)

            camp_id = current_family[0][0]
            family_size = current_family[0][3]
            family_medical_size = current_family[0][9]

            open_accommodation_file = open("accommodation_database.txt", 'r')
            accommodation_database_list = []
            for line0 in open_accommodation_file:
                x = line0.split(",")
                if x[0] == str(camp_id):
                    accommodation_database_list.append(x)
            open_accommodation_file.close()

            open_medical_file = open("medical_database.txt", 'r')
            medical_database_list = []
            for line1 in open_medical_file:
                x = line1.split(",")
                if x[0] == str(camp_id):
                    medical_database_list.append(x)
            open_medical_file.close()

            open_toilet_file = open("toilet_database.txt", 'r')
            toilet_database_list = []
            for line2 in open_toilet_file:
                x = line2.split(",")
                if x[0] == str(camp_id):
                    toilet_database_list.append(x)
            open_toilet_file.close()

            open_ration_file = open("ration_database.txt", 'r')
            ration_database_list = []
            for line3 in open_ration_file:
                x = line3.split(",")
                if x[0] == str(camp_id):
                    ration_database_list.append(x)
            open_ration_file.close()

            accom_available = []
            for i in accommodation_database_list:
                if int(i[6]) >= int(family_size):
                    accom_available.append(f"{i[7]}, Block {i[1]}, {i[6]} Spaces")
            toilet_available = []
            for i in toilet_database_list:
                if int(i[6]) >= int(family_size):
                    toilet_available.append(f"{i[7]}, Toilet {i[1]}, {i[6]} Spaces")
            ration_available = []
            for i in ration_database_list:
                if int(i[6]) >= int(family_size):
                    ration_available.append(f"{i[7]}, Ration {i[1]}, {i[6]} Spaces")
            medical_available = []
            for i in medical_database_list:
                if int(i[6]) >= int(family_medical_size):
                    medical_available.append(f"{i[7]}, Medical {i[1]}, {i[6]} Spaces")

            if len(accom_available) == 0:
                accom_available.append("Accommodation Unavailable")
            if len(ration_available) == 0:
                ration_available.append("Ration Unavailable")
            if len(toilet_available) == 0:
                toilet_available.append("Toilet Unavailable")
            if len(medical_available) == 0:
                medical_available.append("Medical Unavailable")

            amenity_window = Toplevel()
            amenity_window.title("Allocate Amenities")

            screen_width4 = amenity_window.winfo_screenwidth()
            screen_height4 = amenity_window.winfo_screenheight()
            window_height4 = screen_height4
            window_width4 = 900

            center_x4 = int(screen_width4 / 2 - window_width4 / 2)
            center_y4 = int(screen_height4 / 2 - window_height4 / 2)
            amenity_window.geometry(f'{window_width4}x{window_height4}+{center_x4}+{center_y4}')

            Label(amenity_window, text="Please allocate amenities to this refugee family").pack()
            Label(amenity_window, text="Please try to pick amenities within the same wing").pack()

            refugee_accom = StringVar()
            refugee_ration = StringVar()
            refugee_toilet = StringVar()
            refugee_medical = StringVar()

            amenity_count = 0
            accom_count = 0
            toilet_count = 0
            ration_count = 0
            medical_count = 0

            accom_allocate = Label(amenity_window, text="Accommodation Block: ")
            accom_combo = ttk.Combobox(amenity_window, textvariable=refugee_accom, values=accom_available)
            if "Accommodation Unavailable" in current_family[0]:
                accom_allocate.pack()
                accom_combo.pack()
                amenity_count += 1
                accom_count += 1

            toilet_allocate = Label(amenity_window, text="Toilet Block: ")
            toilet_combo = ttk.Combobox(amenity_window, textvariable=refugee_toilet, values=toilet_available)
            if "Toilet Unavailable" in current_family[0]:
                toilet_allocate.pack()
                toilet_combo.pack()
                amenity_count += 1
                toilet_count += 1

            ration_allocate = Label(amenity_window, text="Ration Stall: ")
            ration_combo = ttk.Combobox(amenity_window, textvariable=refugee_ration, values=ration_available)
            if "Ration Unavailable" in current_family[0]:
                ration_allocate.pack()
                ration_combo.pack()
                amenity_count += 1
                ration_count += 1

            medical_allocate = Label(amenity_window, text="Medical Dispensary: ")
            med_combo = ttk.Combobox(amenity_window, textvariable=refugee_medical, values=medical_available)
            if "Medical Unavailable" in current_family[0]:
                medical_allocate.pack()
                med_combo.pack()
                amenity_count += 1
                medical_count += 1

            def submit_command():
                amenity_window.destroy()
                view_refugee_table.destroy()

                refugee_accom_save = ""
                refugee_toilet_save = ""
                refugee_ration_save = ""
                refugee_medical_save = ""

                if accom_count == 1:
                    if refugee_accom.get() != "Accommodation Unavailable":
                        refugee_accom_save = refugee_accom.get().split(",")
                        current_family[0][11] = refugee_accom_save[0] + refugee_accom_save[1]
                if toilet_count == 1:
                    if refugee_toilet.get() != "Toilet Unavailable":
                        refugee_toilet_save = refugee_toilet.get().split(",")
                        current_family[0][13] = refugee_toilet_save[0] + refugee_toilet_save[1]
                if ration_count == 1:
                    if refugee_ration.get() != "Ration Unavailable":
                        refugee_ration_save = refugee_ration.get().split(",")
                        current_family[0][12] = refugee_ration_save[0] + refugee_ration_save[1]
                if medical_count == 1:
                    if refugee_medical.get() != "Medical Unavailable":
                        refugee_medical_save = refugee_medical.get().split(",")
                        current_family[0][14] = refugee_medical_save[0] + refugee_medical_save[1]

                refugee_read = open("refugee_database.txt", "r")

                refugee_list = []
                for refugee_line in refugee_read:
                    line_string_1 = refugee_line.split("%")
                    refugee_list.append(line_string_1)

                refugee_read.close()

                refugee_list = [current_family[0] if num[1] == str(selected_family_id.get()) else num for num in refugee_list]

                clear_file = open("refugee_database.txt", "w")
                clear_file.close()

                for entry in refugee_list:
                    with open("refugee_database.txt", "a") as refugee_write:
                        updated_refugee_string = "%".join(entry)
                        refugee_write.write(updated_refugee_string)
                refugee_write.close()
                refugee_write.close()

                if refugee_accom.get() == "Accommodation Unavailable" or accom_count == 0:
                    pass
                else:
                    accom_id = refugee_accom_save[1][-1]
                    for acc in accommodation_database_list:
                        if acc[1] == accom_id:
                            acc[4] = str(int(acc[4]) + int(family_size))
                            acc[6] = str(int(acc[6]) - int(family_size))

                    clear_file = open("accommodation_database.txt", "w")
                    clear_file.close()

                    for entry in accommodation_database_list:
                        with open("accommodation_database.txt", "a") as accommodation_write:
                            updated_accommodation_string = ",".join(entry)
                            accommodation_write.write(updated_accommodation_string)
                    accommodation_write.close()

                if refugee_ration.get() == "Ration Unavailable"or ration_count == 0:
                    pass
                else:
                    ration_id = refugee_ration_save[1][-1]
                    for rat in ration_database_list:
                        if rat[1] == ration_id:
                            rat[4] = str(int(rat[4]) + int(family_size))
                            rat[6] = str(int(rat[6]) - int(family_size))

                    clear_file = open("ration_database.txt", "w")
                    clear_file.close()

                    for entry in ration_database_list:
                        with open("ration_database.txt", "a") as ration_write:
                            updated_ration_string = ",".join(entry)
                            ration_write.write(updated_ration_string)
                    ration_write.close()

                if refugee_toilet.get() == "Toilet Unavailable"or toilet_count == 0:
                    pass
                else:
                    toilet_id = refugee_toilet_save[1][-1]
                    for toi in toilet_database_list:
                        if toi[1] == toilet_id:
                            toi[4] = str(int(toi[4]) + int(family_size))
                            toi[6] = str(int(toi[6]) - int(family_size))

                    clear_file = open("toilet_database.txt", "w")
                    clear_file.close()

                    for entry in toilet_database_list:
                        with open("toilet_database.txt", "a") as toilet_write:
                            updated_toilet_string = ",".join(entry)
                            toilet_write.write(updated_toilet_string)
                    toilet_write.close()

                if refugee_medical.get() == "Medical Unavailable" or medical_count == 0:
                    pass
                else:
                    medical_id = refugee_medical_save[1][-1]
                    for med in medical_database_list:
                        if med[1] == medical_id:
                            med[4] = str(int(med[4]) + int(family_medical_size))
                            med[6] = str(int(med[6]) - int(family_medical_size))

                    clear_file = open("medical_database.txt", "w")
                    clear_file.close()

                    for entry in medical_database_list:
                        with open("medical_database.txt", "a") as medical_write:
                            updated_medical_string = ",".join(entry)
                            medical_write.write(updated_medical_string)
                    medical_write.close()

            allocation_errors = []

            def check_allocation():
                accom_allocate.config(text="Accommodation Allocated", fg='green')
                toilet_allocate.config(text="Toilet Allocated", fg='green')
                ration_allocate.config(text="Ration Stall Allocated", fg='green')
                medical_allocate.config(text="Medical Dispensary Allocated", fg='green')

                allocation_errors.clear()

                if refugee_accom.get() not in accom_available:
                    accom_allocate.config(text="Please choose from one of the available accommodations", fg='#f00')
                    allocation_errors.append(1)
                if refugee_toilet.get() not in toilet_available:
                    toilet_allocate.config(text="Please choose from one of the available toilet blocks", fg='#f00')
                    allocation_errors.append(2)
                if refugee_ration.get() not in ration_available:
                    ration_allocate.config(text="Please choose from one of the available ration stalls", fg='#f00')
                    allocation_errors.append(3)
                if refugee_medical.get() not in medical_available:
                    medical_allocate.config(text="Please choose from one of the available medical dispensaries",
                                            fg='#f00')
                    allocation_errors.append(4)

                if len(allocation_errors) <= (4-amenity_count):
                    submit_command()

            done_button = Button(amenity_window, text="Submit", command=check_allocation)
            done_button.pack()
            Button(amenity_window, text="Cancel", command=amenity_window.destroy).pack()

        def run_the_update():
            if selected_family_id.get() not in unassigned_id_list:
                select_label.config(fg="#f00")
            else:
                assign_id.destroy()
                run_assignment()

        Button(assign_id, text="Select", command=run_the_update).pack()
        Button(assign_id, text="Close", command=assign_id.destroy).pack()

    Button(view_refugee_table, text="Assign Amenities to Unassigned Families", command=assign_to_unavailable).pack()

    update_family_button = Button(view_refugee_table, text="Update a Family", command=modify_family)
    update_family_button.pack()

    view_refugee_return_home_button = Button(view_refugee_table, text="Return Home", command=view_refugee_table.destroy)
    view_refugee_return_home_button.pack()

    view_refugee_table.mainloop()

