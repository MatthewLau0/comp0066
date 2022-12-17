from tkinter import *
from tkinter import ttk
import datetime

camp_id = ""


def camp_id_generate():
    global camp_id
    logins_file = open("successful_login.txt", "r")

    logins_list = []
    for line in logins_file:
        line_string = line.split("%")
        logins_list.append(line_string)
    logins_file.close()
    if len(logins_list) > 0:
        camp_id = logins_list[-1][0]
    else:
        pass


def create_family():
    camp_id_generate()

    country_list = ['Afghanistan', 'Aland Islands', 'Albania', 'Algeria', 'American Samoa', 'Andorra', 'Angola',
                    'Anguilla', 'Antarctica', 'Antigua and Barbuda', 'Argentina', 'Armenia', 'Aruba', 'Australia',
                    'Austria', 'Azerbaijan', 'Bahamas', 'Bahrain', 'Bangladesh', 'Barbados', 'Belarus', 'Belgium',
                    'Belize', 'Benin', 'Bermuda', 'Bhutan', 'Bolivia', 'Bosnia and Herzegovina', 'Botswana',
                    'Bouvet Island', 'Brazil', 'British Indian Ocean Territory', 'Brunei Darussalam', 'Bulgaria',
                    'Burkina Faso', 'Burundi', 'Cambodia', 'Cameroon', 'Canada', 'Cape Verde', 'Cayman Islands',
                    'Central African Republic', 'Chad', 'Chile', 'China', 'Christmas Island',
                    'Cocos (Keeling) Islands', 'Colombia', 'Comoros', 'Congo',
                    'The Democratic Republic of the Congo', 'Cook Islands', 'Costa Rica', "Côte d'Ivoire",
                    'Croatia', 'Cuba', 'Curaçao', 'Cyprus', 'Czech Republic', 'Denmark', 'Djibouti', 'Dominica',
                    'Dominican Republic', 'Ecuador', 'Egypt', 'El Salvador', 'Equatorial Guinea', 'Eritrea',
                    'Estonia', 'Ethiopia', 'Faroe Islands', 'Fiji', 'Finland', 'France', 'French Guiana',
                    'French Polynesia', 'French Southern Territories', 'Gabon', 'Gambia', 'Georgia', 'Germany',
                    'Ghana', 'Gibraltar', 'Greece', 'Greenland', 'Grenada', 'Guadeloupe', 'Guam', 'Guatemala',
                    'Guernsey', 'Guinea', 'Guinea-Bissau', 'Guyana', 'Haiti', 'Heard Island and McDonald Islands',
                    'Vatican City', 'Honduras', 'Hong Kong', 'Hungary', 'Iceland', 'India', 'Indonesia', 'Iran',
                    'Iraq', 'Ireland', 'Isle of Man', 'Israel', 'Italy', 'Jamaica', 'Japan', 'Jersey', 'Jordan',
                    'Kazakhstan', 'Kenya', 'Kiribati', 'Republic of Korea', 'Kuwait', 'Kyrgyzstan', "Laos",
                    'Latvia', 'Lebanon', 'Lesotho', 'Liberia', 'Libya', 'Liechtenstein', 'Lithuania', 'Luxembourg',
                    'Macao', 'Macedonia', 'Madagascar', 'Malawi', 'Malaysia', 'Maldives', 'Mali', 'Malta',
                    'Marshall Islands', 'Martinique', 'Mauritania', 'Mauritius', 'Mayotte', 'Mexico', 'Micronesia',
                    'Moldova', 'Monaco', 'Mongolia', 'Montenegro', 'Montserrat', 'Morocco', 'Mozambique', 'Myanmar',
                    'Namibia', 'Nauru', 'Nepal', 'Netherlands', 'New Caledonia', 'New Zealand', 'Nicaragua',
                    'Niger', 'Nigeria', 'Niue', 'Norfolk Island', 'Northern Mariana Islands', 'Norway', 'Oman',
                    'Pakistan', 'Palau', 'Palestinian Territory', 'Panama', 'Papua New Guinea', 'Paraguay', 'Peru',
                    'Philippines', 'Pitcairn', 'Poland', 'Portugal', 'Puerto Rico', 'Qatar', 'Réunion', 'Romania',
                    'Russia', 'Rwanda', 'Saint Lucia', 'Samoa', 'San Marino', 'Sao Tome and Principe',
                    'Saudi Arabia', 'Senegal', 'Serbia', 'Seychelles', 'Sierra Leone', 'Singapore', 'Slovakia',
                    'Slovenia', 'Solomon Islands', 'Somalia', 'South Africa', 'Spain', 'Sri Lanka', 'Sudan',
                    'Suriname', 'South Sudan', 'Svalbard', 'Swaziland', 'Sweden', 'Switzerland',
                    'Syrian Arab Republic', 'Taiwan', 'Tajikistan', 'Tanzania', 'Thailand', 'Timor-Leste', 'Togo',
                    'Tokelau', 'Tonga', 'Trinidad and Tobago', 'Tunisia', 'Turkey', 'Turkmenistan',
                    'Turks and Caicos Islands', 'Tuvalu', 'Uganda', 'Ukraine', 'United Arab Emirates',
                    'United Kingdom', 'United States', 'Uruguay', 'Uzbekistan', 'Vanuatu', 'Venezuela', 'Vietnam',
                    'Yemen', 'Zambia', 'Zimbabwe']

    refugee_file = open("refugee_database.txt", "r")

    refugee_list = []
    for line in refugee_file:
        line_string = line.split("%")
        refugee_list.append(line_string)

    refugee_file.close()

    new_refugee = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    new_refugee_screen = Toplevel()
    new_refugee_screen.title("Add New Family")

    refugee_camp_id = str(camp_id)

    refugee_id = ""

    if len(refugee_list) == 0:
        refugee_id = "1"
    elif len(refugee_list) >= 1:
        refugee_id = str((int((refugee_list[-1])[1]) + 1))

    refugee_name = StringVar()
    refugee_family_size = StringVar()
    refugee_date = StringVar()
    refugee_month = StringVar()
    refugee_year = StringVar()
    refugee_gender = StringVar()
    refugee_address1 = StringVar()
    refugee_address2 = StringVar()
    refugee_address_city = StringVar()
    refugee_address_post = StringVar()
    refugee_address_country = StringVar()
    refugee_family_health_no = StringVar()
    refugee_family_health = StringVar()

    Label(new_refugee_screen, text="To create a new Refugee Family, please fill in the form below.").pack()
    Label(new_refugee_screen, text=f"Your Refugee ID is {refugee_id}").pack()
    Label(new_refugee_screen, text=f"You are in Camp {refugee_camp_id}").pack()

    name_frame = Frame(new_refugee_screen)
    name_frame.pack()

    name_label = Label(name_frame, text="Full Name:                                ")
    name_label.pack(side="left")
    name_entry = Entry(name_frame, textvariable=refugee_name)
    name_entry.pack(side="left")

    size_frame = Frame(new_refugee_screen)
    size_frame.pack()

    size_label = Label(size_frame, text="No. of Total Family Members: ")
    size_label.pack(side="left")
    size_entry = Entry(size_frame, textvariable=refugee_family_size)
    size_entry.pack(side="left")

    dob_frame = Frame(new_refugee_screen)
    dob_frame.pack()

    dob_label = Label(dob_frame, text="Date of Birth (dd/mm/yyyy):   ")
    dob_label.pack(side="left")
    dob1_entry = Entry(dob_frame, textvariable=refugee_date, width=5)
    dob1_entry.pack(side="left")
    dob2_entry = Entry(dob_frame, textvariable=refugee_month, width=5)
    dob2_entry.pack(side="left")
    dob3_entry = Entry(dob_frame, textvariable=refugee_year, width=7)
    dob3_entry.pack(side="left")

    gender_frame = Frame(new_refugee_screen)
    gender_frame.pack()

    gender_label = Label(gender_frame, text="Gender:                                 ")
    gender_label.pack(side="left")
    gender_entry = ttk.Combobox(gender_frame, textvariable=refugee_gender, values=["Male", "Female", "Other", "Prefer not to say"])
    gender_entry.pack(side="left")

    address_frame = Frame(new_refugee_screen)
    address_frame.pack()

    address1_label = Label(address_frame, text="Address Line 1:                         ")
    address1_label.pack(side="left")
    address1_entry = Entry(address_frame, textvariable=refugee_address1)
    address1_entry.pack(side="left")

    address_frame2 = Frame(new_refugee_screen)
    address_frame2.pack()

    address2_label = Label(address_frame2, text="Address Line 2:                         ")
    address2_label.pack(side="left")
    address2_entry = Entry(address_frame2, textvariable=refugee_address2)
    address2_entry.pack(side="left")

    address_frame3 = Frame(new_refugee_screen)
    address_frame3.pack()

    address3_label = Label(address_frame3, text="City:                                           ")
    address3_label.pack(side="left")
    address3_entry = Entry(address_frame3, textvariable=refugee_address_city)
    address3_entry.pack(side="left")

    address_frame4 = Frame(new_refugee_screen)
    address_frame4.pack()

    address4_label = Label(address_frame4, text="Postcode:                                 ")
    address4_label.pack(side="left")
    address4_entry = Entry(address_frame4, textvariable=refugee_address_post)
    address4_entry.pack(side="left")

    address_frame5 = Frame(new_refugee_screen)
    address_frame5.pack()

    address5_label = Label(address_frame5, text="Country:                               ")
    address5_label.pack(side="left")
    address5_entry = ttk.Combobox(address_frame5, textvariable=refugee_address_country, values=country_list)
    address5_entry.pack(side="left")

    health_frame1 = Frame(new_refugee_screen)
    health_frame1.pack()

    health_number = Label(health_frame1, text="Total number of family members with any health conditions")
    health_number.pack()
    health_number_entry = Entry(health_frame1, textvariable=refugee_family_health_no, width=5)
    health_number_entry.pack()

    health_frame2 = Frame(new_refugee_screen)
    health_frame2.pack()

    health_label = Label(health_frame2, text="Details of any health conditions within the family")
    health_label.pack()
    health_entry = Entry(health_frame2, textvariable=refugee_family_health, width=40)
    health_entry.pack()

    refugee_age = 0
    if refugee_year.get() != "":
        refugee_age = datetime.datetime.now().year - int(refugee_year.get())

    refugee_wing = ""
    refugee_accom = ""
    refugee_ration = ""
    refugee_toilet = ""
    refugee_medical = ""

    def summary():

        refugee_summary = Toplevel()

        refugee_summary.title("Refugee Family Summary")

        label_1 = Label(refugee_summary, text="Please check that you are happy with the entry below:")
        label_1.pack()

        summary_label = Label(refugee_summary, text=f"""
        Lead Member Name: {refugee_name.get()} \n 
        Family Size: {refugee_family_size.get()} \n
        Lead Member DoB: {refugee_date.get()}/{refugee_month.get()}/{refugee_year.get()}
        Lead Member Age: {refugee_age} 
        Lead Member Gender: {refugee_gender.get()} \n 
        Address: {refugee_address1.get()}, {refugee_address2.get()}, {refugee_address_city.get()} \n{refugee_address_post.get()}, {refugee_address_country.get()} \n
        No. Members with Health Conditions: {refugee_family_health_no.get()}\n
        Health Condition Details: {refugee_family_health.get()}""")
        summary_label.pack()

        def edit_command():
            refugee_summary.destroy()

        def submit_command():

            new_refugee[0] = refugee_camp_id
            new_refugee[1] = refugee_id
            new_refugee[2] = refugee_name.get()
            new_refugee[3] = refugee_family_size.get()
            new_refugee[4] = f"{refugee_date}/{refugee_month}/{refugee_year}"
            new_refugee[5] = refugee_age
            new_refugee[6] = refugee_gender.get()
            new_refugee[7] = f"{refugee_address1.get()}, {refugee_address2.get()}, {refugee_address_city.get()}, {refugee_address_post.get()}, {refugee_address_country.get()}"
            new_refugee[8] = refugee_family_health_no.get()
            new_refugee[9] = refugee_family_health.get()
            new_refugee[10] = refugee_wing
            new_refugee[11] = refugee_accom
            new_refugee[12] = refugee_ration
            new_refugee[13] = refugee_toilet
            new_refugee[14] = refugee_medical

            new_refugee_string = '%'.join(new_refugee)

            refugee_append = open("refugee_database.txt", "a")
            refugee_append.write(new_refugee_string + "\n")
            refugee_append.close()

            refugee_summary.destroy()
            new_refugee_screen.destroy()

        edit_button = Button(refugee_summary, text="Edit", command=edit_command, width=30, height=2)
        edit_button.pack()
        submit_button = Button(refugee_summary, text="Submit", command=submit_command, width=30, height=2)
        submit_button.pack()

        refugee_summary.mainloop()

    error_window = Toplevel()
    error_frame = Frame(error_window)

    def check_block():

        for widget in error_frame.winfo_children():
            widget.destroy()

        check_status = ["0", "1", "0", "0", "0", "0"]

        def name_check():
            if refugee_name.get().strip() == "":
                new_block_name_reentry_1 = Label(error_frame, text="Please enter a Refugee Name")
                new_block_name_reentry_1.pack()
            else:
                check_status[0] = "1"

        name_check()

        def cap_check():
            try:
                int(refugee_family_size.get())
                check_status[2] = "1"
            except ValueError:
                new_block_capacity_reentry = Label(error_frame, text="Please enter an integer for family size")
                new_block_capacity_reentry.pack()

        cap_check()

        def occ_check():
            try:
                int(refugee_family_health_no.get())
                check_status[3] = "1"
            except ValueError:
                new_block_occupancy_reentry_1 = Label(error_frame, text="Please enter an integer for medical")
                new_block_occupancy_reentry_1.pack()
            if check_status[3] == "1" and check_status[1] == "1":
                try:
                    if int(refugee_family_health_no.get()) <= int(refugee_family_size.get()):
                        print(refugee_family_health_no.get())
                        print(refugee_family_size)
                        check_status[4] = "1"
                    else:
                        new_block_occupancy_reentry_2 = Label(error_frame, text="Please enter an medical lower than size")
                        new_block_occupancy_reentry_2.pack()
                except ValueError:
                    pass

        occ_check()

        def location_check():
            if refugee_date.get() == 0 or refugee_month.get() == 0 or refugee_year.get() == 0:
                new_block_location_reentry = Label(error_frame, text="Please choose a DoB")
                new_block_location_reentry.pack()
            else:
                check_status[5] = "1"

        location_check()

        if "0" in check_status:
            error_frame.pack()
            close_button = Button(error_window, text="Close", command=error_window.destroy, width=10, height=1)
            close_button.pack()
            error_window.mainloop()
        else:
            summary()

    new_block_done = Button(new_refugee_screen, text="Done", command=check_block, width=30, height=2)
    new_block_done.pack()

    new_refugee_screen.mainloop()


create_family()