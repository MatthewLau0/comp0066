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

    new_refugee = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

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

    day_list = [str(i) for i in range(1, 32)]
    month_list = [str(i) for i in range(1, 13)]
    year_list = [str(i) for i in range(2023, 1899, -1)]

    dob_label = Label(new_refugee_screen, text="Enter the start date for the emergency")
    dob_label.pack()
    dob_frame = Frame(new_refugee_screen)
    dob_frame.pack()
    date_day_combobox = ttk.Combobox(dob_frame, textvariable=refugee_date, values=day_list)
    date_day_combobox.pack(side=LEFT)
    date_month_combobox = ttk.Combobox(dob_frame, textvariable=refugee_month, values=month_list)
    date_month_combobox.pack(side=LEFT)
    date_year_combobox = ttk.Combobox(dob_frame, textvariable=refugee_year, values=year_list)
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

    gender_frame = Frame(new_refugee_screen)
    gender_frame.pack()

    gender_label = Label(gender_frame, text="Gender:                                 ")
    gender_label.pack(side="left")
    gender_entry = ttk.Combobox(gender_frame, textvariable=refugee_gender, values=gender_list)
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


    def allocate_blocks():

        new_refugee_screen.destroy()

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
            if int(i[6]) >= int(refugee_family_size.get()):
                accom_available.append(f"{i[7]}, Block {i[1]}, {i[6]} Spaces")
        toilet_available = []
        for i in toilet_database_list:
            if int(i[6]) >= int(refugee_family_size.get()):
                toilet_available.append(f"{i[7]}, Toilet {i[1]}, {i[6]} Spaces")
        ration_available = []
        for i in ration_database_list:
            if int(i[6]) >= int(refugee_family_size.get()):
                ration_available.append(f"{i[7]}, Ration {i[1]}, {i[6]} Spaces")
        medical_available = []
        for i in medical_database_list:
            if int(i[6]) >= int(refugee_family_health_no.get()):
                medical_available.append(f"{i[7]}, Medical {i[1]}, {i[6]} Spaces")

        if len(accom_available) == 0:
            accom_available.append("Accommodation Unavailable,")
        if len(ration_available) == 0:
            ration_available.append("Ration Unavailable,")
        if len(toilet_available) == 0:
            toilet_available.append("Toilet Unavailable,")
        if len(medical_available) == 0:
            medical_available.append("Medical Unavailable,")

        amenity_window = Toplevel()
        amenity_window.title("Allocate Amenities")

        Label(amenity_window, text="Please allocate amenities to this refugee family").pack()
        Label(amenity_window, text="Please try to pick amenities within the same wing").pack()

        refugee_accom = StringVar()
        refugee_ration = StringVar()
        refugee_toilet = StringVar()
        refugee_medical = StringVar()

        accom_allocate = Label(amenity_window, text="Accommodation Block: ")
        accom_allocate.pack()
        ttk.Combobox(amenity_window, textvariable=refugee_accom, values=accom_available).pack()

        toilet_allocate = Label(amenity_window, text="Toilet Block: ")
        toilet_allocate.pack()
        ttk.Combobox(amenity_window, textvariable=refugee_toilet, values=toilet_available).pack()

        ration_allocate = Label(amenity_window, text="Ration Stall: ")
        ration_allocate.pack()
        ttk.Combobox(amenity_window, textvariable=refugee_ration, values=ration_available).pack()

        medical_allocate = Label(amenity_window, text="Medical Dispensary: ")
        medical_allocate.pack()
        ttk.Combobox(amenity_window, textvariable=refugee_medical, values=medical_available).pack()

        allocation_errors = []

        def summary():
            amenity_window.destroy()

            refugee_summary = Toplevel()

            refugee_summary.title("Refugee Family Summary")

            label_1 = Label(refugee_summary, text="Please check that you are happy with the entry below:")
            label_1.pack()

            summary_label = Label(refugee_summary, text=f"""
            Lead Member Name: {refugee_name.get()} \n 
            Family Size: {refugee_family_size.get()} \n
            Lead Member DoB: {refugee_date.get()}/{refugee_month.get()}/{refugee_year.get()}
            Lead Member Age: {generate_age()} 
            Lead Member Gender: {refugee_gender.get()} \n 
            Address: {refugee_address1.get()}, {refugee_address2.get()}, {refugee_address_city.get()} \n{refugee_address_post.get()}, {refugee_address_country.get()} \n
            No. Members with Health Conditions: {refugee_family_health_no.get()}\n
            Health Condition Details: {refugee_family_health.get()}""")
            summary_label.pack()

            def submit_command():
                refugee_accom_save = refugee_accom.get().split(",")
                refugee_ration_save = refugee_ration.get().split(",")
                refugee_toilet_save = refugee_toilet.get().split(",")
                refugee_medical_save = refugee_medical.get().split(",")
                new_refugee[0] = str(refugee_camp_id)
                new_refugee[1] = str(refugee_id)
                new_refugee[2] = refugee_name.get()
                new_refugee[3] = str(refugee_family_size.get())
                new_refugee[4] = f"{refugee_date.get()}/{refugee_month.get()}/{refugee_year.get()}"
                new_refugee[5] = str(generate_age())
                new_refugee[6] = refugee_gender.get()
                new_refugee[7] = f"{refugee_address1.get()}, {refugee_address2.get()}, {refugee_address_city.get()}, {refugee_address_post.get()}, {refugee_address_country.get()}"
                new_refugee[8] = str(refugee_family_health_no.get())
                new_refugee[9] = refugee_family_health.get()
                new_refugee[10] = refugee_accom_save[0] + refugee_accom_save[1]
                new_refugee[11] = refugee_ration_save[0] + refugee_ration_save[1]
                new_refugee[12] = refugee_toilet_save[0] + refugee_toilet_save[1]
                new_refugee[13] = refugee_medical_save[0] + refugee_medical_save[1]

                new_refugee_string = '%'.join(new_refugee)

                refugee_append = open("refugee_database.txt", "a")
                refugee_append.write(new_refugee_string + "\n")
                refugee_append.close()

                accom_id = refugee_accom_save[1][-1]
                ration_id = refugee_ration_save[1][-1]
                toilet_id = refugee_toilet_save[1][-1]
                medical_id = refugee_medical_save[1][-1]

                for acc in accommodation_database_list:
                    if acc[1] == accom_id:
                        acc[4] = str(int(acc[4]) + int(refugee_family_size.get()))
                        acc[6] = str(int(acc[6]) - int(refugee_family_size.get()))

                clear_file = open("accommodation_database.txt", "w")
                clear_file.close()

                for entry in accommodation_database_list:
                    with open("accommodation_database.txt", "a") as accommodation_write:
                        updated_accommodation_string = ",".join(entry)
                        accommodation_write.write(updated_accommodation_string)
                accommodation_write.close()

                for rat in ration_database_list:
                    if rat[1] == ration_id:
                        rat[4] = str(int(rat[4]) + int(refugee_family_size.get()))
                        rat[6] = str(int(rat[6]) - int(refugee_family_size.get()))

                clear_file = open("ration_database.txt", "w")
                clear_file.close()

                for entry in ration_database_list:
                    with open("ration_database.txt", "a") as ration_write:
                        updated_ration_string = ",".join(entry)
                        ration_write.write(updated_ration_string)
                ration_write.close()

                for toi in toilet_database_list:
                    if toi[1] == toilet_id:
                        toi[4] = str(int(toi[4]) + int(refugee_family_size.get()))
                        toi[6] = str(int(toi[6]) - int(refugee_family_size.get()))

                clear_file = open("toilet_database.txt", "w")
                clear_file.close()

                for entry in toilet_database_list:
                    with open("toilet_database.txt", "a") as toilet_write:
                        updated_toilet_string = ",".join(entry)
                        toilet_write.write(updated_toilet_string)
                toilet_write.close()

                for med in medical_database_list:
                    if med[1] == toilet_id:
                        med[4] = str(int(med[4]) + int(refugee_family_health_no.get()))
                        med[6] = str(int(med[6]) - int(refugee_family_health_no.get()))

                clear_file = open("medical_database.txt", "w")
                clear_file.close()

                for entry in medical_database_list:
                    with open("medical_database.txt", "a") as medical_write:
                        updated_medical_string = ",".join(entry)
                        medical_write.write(updated_medical_string)
                medical_write.close()

                refugee_summary.destroy()
                new_refugee_screen.destroy()

            edit_button = Button(refugee_summary, text="Cancel", command=refugee_summary.destroy, width=30, height=2)
            edit_button.pack()
            submit_button = Button(refugee_summary, text="Submit", command=submit_command, width=30, height=2)
            submit_button.pack()

            refugee_summary.mainloop()

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
                medical_allocate.config(text="Please choose from one of the available medical dispensaries", fg='#f00')
                allocation_errors.append(4)

            if len(allocation_errors) > 0:
                pass
            else:
                summary()

        Button(amenity_window, text="Done", command=check_allocation).pack()


    error_new_volunteer = []

    def check_block():

        name_label.config(text="Name entered", fg='green')
        size_label.config(text="Family size entered", fg='green')
        dob_label.config(text="DoB entered", fg='green')
        gender_label.config(text="Gender entered", fg='green')
        address1_label.config(text="Address Line 1 entered", fg='green')
        address2_label.config(text="Address Line 2 entered", fg='green')
        address3_label.config(text="City entered", fg='green')
        address4_label.config(text="Post Code entered", fg='green')
        address5_label.config(text="Country entered", fg='green')
        health_number.config(text="No. with health conditions entered", fg='green')
        health_label.config(text="Health details entered", fg='green')

        error_new_volunteer.clear()

        if refugee_name.get().strip() == "":
            name_label.config(text="Please enter a name", fg='#f00')
            error_new_volunteer.append(1)
        if all(char.isalpha() for char in refugee_name.get().replace(" ", "")) is False:
            name_label.config(text="Name can only contain alphabetical characters", fg='#f00')
            error_new_volunteer.append(1.1)
        try:
            int(refugee_family_size.get())
            if int(refugee_family_size.get()) == 0:
                size_label.config(text="Minimum family size is 1", fg='#f00')
                error_new_volunteer.append(2.1)
        except ValueError:
            size_label.config(text="Please enter an integer for family size", fg='#f00')
            error_new_volunteer.append(2)
        try:
            int(refugee_family_health_no.get())
        except ValueError:
            health_number.config(text="Please enter an integer for medical", fg='#f00')
            error_new_volunteer.append(3)
        if 2 not in error_new_volunteer and 3 not in error_new_volunteer:
            try:
                if int(refugee_family_health_no.get()) > int(refugee_family_size.get()):
                    health_number.config(text="Please enter an medical lower than size", fg='#f00')
                    error_new_volunteer.append(4)
            except ValueError:
                pass
        today = datetime.datetime.today()
        if generate_dob() == "empty":
            dob_label.config(text="Please enter DoB", fg='#f00')
            error_new_volunteer.append(5)
        if generate_dob() != "empty":
            test_start_date = datetime.datetime.strptime(str(generate_dob()), "%Y-%m-%d")
            if test_start_date > today:
                dob_label.config(text="Please enter a valid DoB", fg='#f00')

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
            allocate_blocks()

    new_block_done = Button(new_refugee_screen, text="Done", command=check_block, width=30, height=2)
    new_block_done.pack()

    new_refugee_screen.mainloop()
