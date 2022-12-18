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
    emergency_database_table.heading("Ration", text="Medical", anchor='center')
    emergency_database_table.heading("Toilet", text="Toilet", anchor='center')
    emergency_database_table.heading("Medical", text="Rations", anchor='center')

    for i in range(0, len(refugee_database_list)):
        emergency_database_table.insert(parent='', index=i, iid=i, values=(
            str(refugee_database_list[i][0]), str(refugee_database_list[i][1]),
            refugee_database_list[i][2], refugee_database_list[i][3], str(refugee_database_list[i][4]),
            refugee_database_list[i][5], refugee_database_list[i][6], refugee_database_list[i][7],
            refugee_database_list[i][8], refugee_database_list[i][9], refugee_database_list[i][10],
            refugee_database_list[i][11], refugee_database_list[i][12], refugee_database_list[i][13], refugee_database_list[i][14]))

    emergency_database_table.pack(fill='both')

    def modify_family():
        update_family_screen_id = Toplevel()
        update_family_screen_id.title("Update ID Select")

        screen_width2 = update_family_screen_id.winfo_screenwidth()
        screen_height2 = update_family_screen_id.winfo_screenheight()
        window_height2 = 100
        window_width2 = 300

        center_x2 = int(screen_width2 / 2 - window_width2 / 2)
        center_y2 = int(screen_height2 / 2 - window_height2 / 2)
        update_family_screen_id.geometry(f'{window_width2}x{window_height2}+{center_x2}+{center_y2}')

        id_list = []

        for i in refugee_database_list:
            id_list.append(i[1])

        selected_refugee_id = StringVar()

        id_select_label = Label(update_family_screen_id, text="Please choose a block ID to update")
        id_select_label.pack()
        selected_refugee_id.set("Select ID")
        id_select_option = ttk.Combobox(update_family_screen_id, textvariable=selected_refugee_id, values=id_list)
        id_select_option.pack()

        def update_run():

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
            update_refugee_screen.title(f"Update Family {selected_refugee_id.get()}")

            current_updating_refugee = []
            for ref in refugee_database_list:
                if ref[1] == str(selected_refugee_id.get()):
                    current_updating_refugee.append(ref)

            refugee_date = current_updating_refugee[0][4].split("/")
            number = current_updating_refugee[0][7].split("#")
            address = current_updating_refugee[0][8].split(",")

            update_refugee_name = current_updating_refugee[0][2]
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
            update_refugee_family_health = current_updating_refugee[0][9]

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
                refugee_age = 10
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

        def run_the_update():
            if selected_refugee_id.get() not in id_list:
                id_select_label.config(fg="#f00")
            else:
                update_family_screen_id.destroy()
                update_run()

        id_done = Button(update_family_screen_id, text="Done", command=run_the_update)
        id_done.pack()


    update_a_family_button = Button(view_refugee_table, text="Update a Family", command=modify_family)
    update_a_family_button.pack()

    view_refugee_return_home_button = Button(view_refugee_table, text="Return Home", command=view_refugee_table.destroy)
    view_refugee_return_home_button.pack()

    view_refugee_table.mainloop()

table()