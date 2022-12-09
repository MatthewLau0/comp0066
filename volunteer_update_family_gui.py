def modify_family():
    import volunteer_view_family_gui
    import tkinter
    import subprocess
    import sys
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'tkcalendar'])
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'tkintermapview'])
    import tkinter.ttk
    import datetime
    import tkcalendar

    def delete_update_screen():
        update_screen.destroy()
    def delete1():
        screen1.destroy()
    def error_one():
        global screen1
        screen1 = tkinter.Toplevel(update_screen)
        screen1.geometry("300x120")
        screen1.title("Warning!")
        noinput_error_text = tkinter.Label(screen1, text="Please select an index!", fg='red')
        noinput_error_text.place(x=80, y=30)
        close_button = tkinter.Button(screen1, text="I understand", command=delete1)
        close_button.place(x=95, y=80)

    def confirm_update():
        if refugee_button.get() == '':
            error_one()
            return
        else:
            delete_update_screen()
            update_current_refugee = tkinter.Toplevel()
            update_current_refugee.title("Updating refugee")
            update_current_refugee.geometry("500x1000")

            refugee_index_var = refugee_button.get()
            refugee_index = int(refugee_index_var) - 1
            updating_refugee_list = []
            for i in range(0, len(volunteer_database_list[refugee_index])):
                updating_refugee_list.append(str(volunteer_database_list[refugee_index][i]))

            refugee_select_label = tkinter.Label(update_current_refugee, text = "You are updating refugee %d" % int(refugee_index_var))
            refugee_select_label.pack()


            update_refugee_table = tkinter.ttk.Treeview(update_current_refugee)

            update_refugee_table['columns'] = (
            "Refugee ID", "Name", "Family members", "Date of Birth", "Age", "Sex", "Address", "Weight", "Height")

            update_refugee_table.column("#0", width=0, stretch='NO')
            update_refugee_table.column("Refugee ID", anchor='center', width=100)
            update_refugee_table.column("Name", anchor='center', width=100)
            update_refugee_table.column("Family members", anchor='center', width=100)
            update_refugee_table.column("Date of Birth", anchor='center', width=100)
            update_refugee_table.column("Age", anchor='center', width=100)
            update_refugee_table.column("Sex", anchor='center', width=100)
            update_refugee_table.column("Address", anchor='center', width=300)
            update_refugee_table.column("Weight", anchor='center', width=100)
            update_refugee_table.column("Height", anchor='center', width=100)

            update_refugee_table.heading("Refugee ID", text="Refugee ID", anchor='center')
            update_refugee_table.heading("Name", text="Name", anchor='center')
            update_refugee_table.heading("Family members", text="Family members", anchor='center')
            update_refugee_table.heading("Date of Birth", text="Date of Birth", anchor='center')
            update_refugee_table.heading("Age", text="Age", anchor='center')
            update_refugee_table.heading("Sex", text="Sex", anchor='center')
            update_refugee_table.heading("Address", text="Address", anchor='center')
            update_refugee_table.heading("Weight", text="Weight", anchor='center')
            update_refugee_table.heading("Height", text="Height", anchor='center')

            # https://pythonguides.com/python-tkinter-table-tutorial/
            update_refugee_table.insert(parent='', index=i, iid=i, values=(
            updating_refugee_list[0], str(updating_refugee_list[1]), updating_refugee_list[2],
            updating_refugee_list[3], updating_refugee_list[4], updating_refugee_list[5],
            updating_refugee_list[6], updating_refugee_list[7], updating_refugee_list[8]))
            update_refugee_table.configure(height = 2)
            update_refugee_table.pack(pady = 20)


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

            def save_to_file():

                name = refugee_name.get()
                number = refugee_number.get()
                dob = refugee_dob.get()
                age = str(calculate_age(dob))
                sex = refugee_sex.get()

                first_address = refugee_first_address.get()
                city_address = refugee_city_address.get()
                postcode_address = refugee_postcode_address.get()
                country_address = refugee_country_address.get()

                weight = refugee_weight.get()
                height = refugee_height.get()

                # Check if there is no input in the required fields
                if name == "" or number == "" or sex == "":
                    noinput_error()
                    print("1")
                    return

                # Check if name has errors
                for i in name:
                    if i.isalpha() != True and i != " ":
                        print("2")
                        noinput_error()
                        return

                if len(name) == 0:
                    noinput_error()
                    print("3")
                    return

                if any(i.isdigit() for i in name):
                    print("4")
                    noinput_error()
                    return

                if name.count(" ") > 3:
                    print("5")
                    noinput_error()
                    return

                # Check if number has error
                try:
                    int(number)
                except ValueError:
                    print("6")
                    noinput_error()
                    return

                if len(number) != 5:
                    print("7")
                    noinput_error()
                    return

                if any(i.isalpha() for i in number):
                    print("8")
                    noinput_error()

                    return



                # Checks for address line 1
                if first_address.isnumeric():
                    print("10")
                    noinput_error()
                    return
                if len(first_address) > 100:
                    print("11")
                    noinput_error()
                    return

                # Checks for city
                if city_address.count(" ") > 4:
                    print("12")
                    noinput_error()
                    return

                if city_address.isnumeric():
                    print("13")
                    noinput_error()
                    return

                # Checks for postcode
                if len(postcode_address) > 10:
                    print("14")
                    noinput_error()
                    return

                for i in postcode_address:
                    if i.isalnum() != True and i != " ":
                        print("14.5")
                        noinput_error()
                        return

                address_list = [first_address, city_address, postcode_address, country_address]
                address = ', '.join(address_list)

                # Checks for weight
                try:
                    float(weight)
                except ValueError:
                    print("15")
                    noinput_error()
                    return

                if float(weight) > 400 or float(weight) < 1:
                    print("16")
                    noinput_error()
                    return

                # Checks for height
                try:
                    float(height)
                except ValueError:
                    print("18")
                    noinput_error()
                    return

                if float(height) > 230 or float(height) < 30:
                    print("19")
                    noinput_error()
                    return

                success()

            def delete1():
                screen1.destroy()

            def delete0():
                update_current_refugee.destroy()

            def delete3():
                screen3.destroy()

            def calculate_age(lol):
                today = datetime.date.today()
                x = lol.split("/")
                birthyear = int(x[2])
                birthmonth = int(x[1])
                birthday = int(x[0])

                birthdate = datetime.date(birthyear, birthmonth, birthday)
                age = 0

                if birthdate.month < today.month and today.year > birthdate.year:
                    age = today.year - birthdate.year

                elif birthdate.month > today.month and today.year > birthdate.year:
                    age = today.year - birthdate.year - 1

                elif birthdate.month == today.month and today.year > birthdate.year and today.day < birthdate.day:
                    age = today.year - birthdate.year - 1

                elif birthdate.month == today.month and today.year > birthdate.year and today.day > birthdate.day:
                    age = today.year - birthdate.year

                return age

            def name_validate():
                name = refugee_name.get()

                if len(name) == 0:
                    namestatus.config(text="Name cannot be 0")

                else:
                    try:
                        if len(name) <= 2:
                            namestatus.config(text="Name too short!")

                        elif any(i.isdigit() for i in name):
                            namestatus.config(text="Name can't be numeric!")

                        elif name.count(" ") > 3:
                            namestatus.config(text="Please enter less than 4 separate names")

                        else:
                            namestatus.config(text="Valid :)")
                    except:
                        pass
                return True

            def number_validate():
                number = refugee_number.get()

                if len(number) == 0:
                    numberstatus.config(text="Number cannot be 0")

                else:
                    try:
                        if len(number) != 5:
                            numberstatus.config(text="Number must be 5 digits long!")

                        elif any(i.isalpha() for i in number):
                            numberstatus.config(text="Number can't have alphabetical characters!")

                        elif number.count(" ") > 1:
                            numberstatus.config(text="Please enter it as a full number")

                        elif number.count(".") > 1:
                            numberstatus.config(text="The number can't be a decimal")

                        elif number in volunteer_database_list:
                            numberstatus.config(text="Number already exists!")

                        else:
                            numberstatus.config(text="Valid :)")
                    except:
                        pass
                return True

            def delete2():
                screen2.destroy()

            def noinput_error():
                global screen1
                screen1 = tkinter.Toplevel()
                screen1.geometry("300x120")
                screen1.title("Warning!")
                noinput_error_text = tkinter.Label(screen1, text="All fields required are marked with an *", fg='red')
                noinput_error_text.place(x=40, y=40)
                close_button = tkinter.Button(screen1, text="I understand", command=delete1)
                close_button.place(x=95, y=80)

            def finish_message():
                global screen3
                screen3 = tkinter.Tk()
                screen3.geometry("300x120")
                screen3.title("Success!")
                finish_message_text = tkinter.Label(screen3, text="Successfully updated refugee!", fg='green')
                finish_message_text.place(x=40, y=40)
                close_button = tkinter.Button(screen3, text="I understand", command=delete3)
                close_button.place(x=95, y=80)

            def submit():
                print("1")
                # Creating new refugee
                new_refugee = [""] * 9

                '''
                # Finding index for new refugee
                if len(volunteer_database_list) == 0:
                    new_refugee[0] = "1"
                elif len(volunteer_database_list) >= 1:
                    new_refugee[0] = str((int((volunteer_database_list[-1])[0]) + 1))
                print("The index number for this emergency is ", new_refugee[0])
                '''
                id = refugee_id.get()
                name = refugee_name.get()
                number = refugee_number.get()
                dob = refugee_dob.get()
                age = str(calculate_age(dob))
                sex = refugee_sex.get()
                weight = refugee_weight.get()
                height = refugee_height.get()

                print("2")

                first_address = refugee_first_address.get()
                city_address = refugee_city_address.get()
                postcode_address = refugee_postcode_address.get()
                country_address = refugee_country_address.get()

                address_list = [first_address, city_address, postcode_address, country_address]
                address = ', '.join(address_list)

                new_refugee[0] = id
                new_refugee[1] = name
                new_refugee[2] = number
                new_refugee[3] = dob
                new_refugee[4] = age
                new_refugee[5] = sex
                new_refugee[6] = address
                new_refugee[7] = weight
                new_refugee[8] = height
                print("3")
                new_refugee_string = "#".join(new_refugee)
                volunteer_list_file.close()
                for i in range(0, len(volunteer_database_list)):
                    if volunteer_database_list[i][0] == new_refugee[0]:
                        volunteer_database_list[i] = new_refugee
                print(volunteer_database_list)
                for j in range(len(volunteer_database_list)):
                    volunteer_database_list[j] = "#".join(volunteer_database_list[j])

                print(volunteer_database_list)


                volunteer_list_file_append = open("Refugee_Database", "w")
                for item in volunteer_database_list:
                    volunteer_list_file_append.write(f'{item}')

                volunteer_list_file_append.close()

                '''
                volunteer_list_file_append = open("Refugee_Database", "w")
                volunteer_list_file_append.write("%s\n" %(new_refugee_string))
                volunteer_list_file_append.close()
                '''

                delete2()
                finish_message()
                delete0()

            def success():
                global screen2
                screen2 = tkinter.Toplevel(update_current_refugee)
                screen2.geometry("500x650")
                screen2.title("Confirm refugee edits")

                refugee_confirmation = tkinter.Label(screen2,
                                                     text="Please check the summary of your edits below to add to the database")
                refugee_confirmation.pack()

                name_confirmation = tkinter.Label(screen2, text="The name you are entering is: %s" % (refugee_name.get()))
                name_confirmation.pack()

                number_confirmation = tkinter.Label(screen2,
                                                    text="The number you are entering is: %s" % refugee_number.get())
                number_confirmation.pack()

                sex_confirmation = tkinter.Label(screen2, text="The sex you are entering is: %s" % refugee_sex.get())
                sex_confirmation.pack()

                dob_confirmation = tkinter.Label(screen2,
                                                 text="The date of birth you are entering is: %s" % str(refugee_dob.get()))
                dob_confirmation.pack()

                age_confirmation = tkinter.Label(screen2, text="This means their age is: %s" % str(
                    calculate_age(str(refugee_dob.get()))))
                age_confirmation.pack()

                first_address = refugee_first_address.get()
                city_address = refugee_city_address.get()
                postcode_address = refugee_postcode_address.get()
                country_address = refugee_country_address.get()

                address_list = [first_address, city_address, postcode_address, country_address]
                address = ', '.join(address_list)

                address_confirmation = tkinter.Label(screen2, text="Their address is: %s" % address)
                address_confirmation.pack()

                weight_confirmation = tkinter.Label(screen2, text="Their weight is: %s kg" % refugee_weight.get())
                weight_confirmation.pack()

                height_confirmation = tkinter.Label(screen2, text="Their height is: %s cm" % refugee_height.get())
                height_confirmation.pack()

                submit_button = tkinter.Button(screen2, text="Submit", command=submit)
                submit_button.pack()
                update_refugee_button = tkinter.Button(screen2, text="Change details", command=delete2)
                update_refugee_button.pack()

            def refugee_text_on(self):
                if refugee_name_entry.get() == 'Enter refugee name...':
                    refugee_name_entry.delete(0, "end")  # delete all the text in the entry
                    refugee_name_entry.insert(0, '')  # Insert blank for user input
                    refugee_name_entry.config(fg='black')

            def refugee_text_off(self):
                if refugee_name_entry.get() == '':
                    refugee_name_entry.insert(0, 'Enter refugee name...')
                    refugee_name_entry.config(fg='grey')

            def refugee_number_on(self):
                if refugee_number_entry.get() == 'Enter 5-digit number...':
                    refugee_number_entry.delete(0, "end")  # delete all the text in the entry
                    refugee_number_entry.insert(0, '')  # Insert blank for user input
                    refugee_number_entry.config(fg='black')

            def refugee_number_off(self):
                if refugee_number_entry.get() == '':
                    refugee_number_entry.insert(0, 'Enter 5-digit number...')
                    refugee_number_entry.config(fg='grey')

            def refugee_first_address_on(self):
                if refugee_first_address_entry.get() == 'Address Line 1':
                    refugee_first_address_entry.delete(0, "end")  # delete all the text in the entry
                    refugee_first_address_entry.insert(0, '')  # Insert blank for user input
                    refugee_first_address_entry.config(fg='black')

            def refugee_first_address_off(self):
                if refugee_first_address_entry.get() == '':
                    refugee_first_address_entry.insert(0, 'Address Line 1')
                    refugee_first_address_entry.config(fg='grey')

            def refugee_city_address_on(self):
                if refugee_city_address_entry.get() == 'Town/City':
                    refugee_city_address_entry.delete(0, "end")  # delete all the text in the entry
                    refugee_city_address_entry.insert(0, '')  # Insert blank for user input
                    refugee_city_address_entry.config(fg='black')

            def refugee_city_address_off(self):
                if refugee_city_address_entry.get() == '':
                    refugee_city_address_entry.insert(0, 'Town/City')
                    refugee_city_address_entry.config(fg='grey')

            def refugee_postcode_address_on(self):
                if refugee_postcode_address_entry.get() == 'Postcode':
                    refugee_postcode_address_entry.delete(0, "end")  # delete all the text in the entry
                    refugee_postcode_address_entry.insert(0, '')  # Insert blank for user input
                    refugee_postcode_address_entry.config(fg='black')

            def refugee_postcode_address_off(self):
                if refugee_postcode_address_entry.get() == '':
                    refugee_postcode_address_entry.insert(0, 'Postcode')
                    refugee_postcode_address_entry.config(fg='grey')

            def refugee_weight_on(self):
                if refugee_weight_entry.get() == 'Enter weight in kg...':
                    refugee_weight_entry.delete(0, "end")  # delete all the text in the entry
                    refugee_weight_entry.insert(0, '')  # Insert blank for user input
                    refugee_weight_entry.config(fg='black')

            def refugee_weight_off(self):
                if refugee_weight_entry.get() == '':
                    refugee_weight_entry.insert(0, 'Enter weight in kg...')
                    refugee_weight_entry.config(fg='grey')

            def refugee_height_on(self):
                if refugee_height_entry.get() == 'Enter height in cm...':
                    refugee_height_entry.delete(0, "end")  # delete all the text in the entry
                    refugee_height_entry.insert(0, '')  # Insert blank for user input
                    refugee_height_entry.config(fg='black')

            def refugee_height_off(self):
                if refugee_height_entry.get() == '':
                    refugee_height_entry.insert(0, 'Enter height in cm...')
                    refugee_height_entry.config(fg='grey')

            # define text file
            '''
            # Setting up the screen
            screen = tkinter.Toplevel()
            screen.geometry("500x1000")
            screen.title("Create Refugee Form")
            # screen.configure(background="#A1CDEC")
            
            # Title text
            intro_text = tkinter.Label(update_current_refugee, text="Use this section to create a refugee within this Database.",
                                       fg='Green', bg="Light Grey", width=500)
            intro_text.pack
            '''
            # Input from user

            namestatus = tkinter.Label(update_current_refugee, text="")
            namestatus.place(x=20, y=120)

            refugee_id = tkinter.StringVar(value = updating_refugee_list[0])

            refugee_name_text = tkinter.Label(update_current_refugee, text="Refugee name*: ")
            refugee_name_text.place(x=20, y=100)
            refugee_name = tkinter.StringVar(value = updating_refugee_list[1])
            global refugee_name_entry
            refugee_name_entry = tkinter.Entry(update_current_refugee, validate='all', validatecommand=name_validate,
                                               textvariable=refugee_name)
            #refugee_name_entry.insert(0, textvariable = refugee_name)
            refugee_name_entry.bind('<FocusIn>', refugee_text_on)
            refugee_name_entry.bind('<FocusOut>', refugee_text_off)
            #refugee_name_entry.config(fg='grey')
            refugee_name_entry.place(x=175, y=100, width=300)

            numberstatus = tkinter.Label(update_current_refugee, text="")
            numberstatus.place(x=20, y=190)

            refugee_number_text = tkinter.Label(update_current_refugee, text="Refugee Number*: ")
            refugee_number_text.place(x=20, y=170)
            refugee_number = tkinter.StringVar(value = updating_refugee_list[2])
            refugee_number_entry = tkinter.Entry(update_current_refugee, textvariable=refugee_number, validate='all',
                                                 validatecommand=number_validate)
            #print(update_current_refugee[2])
            #lol = str(update_current_refugee[2])
            #refugee_number_entry.insert(0, "pog")
            refugee_number_entry.bind('<FocusIn>', refugee_number_on)
            refugee_number_entry.bind('<FocusOut>', refugee_number_off)
            #refugee_number_entry.config(fg='grey')
            refugee_number_entry.place(x=175, y=170, width=300)

            refugee_sex_text = tkinter.Label(update_current_refugee, text="Sex*:")
            refugee_sex_text.place(x=20, y=240)
            refugee_sex = tkinter.StringVar(value = updating_refugee_list[5])
            # refugee_sex_entry = Entry(textvariable=refugee_sex)
            # refugee_sex_entry.place(x = 175, y = 150, width=300)
            drop = tkinter.OptionMenu(update_current_refugee, refugee_sex, "Male", "Female", "Prefer not to say")
            drop.place(x=175, y=240, width=300)

            refugee_dob_text = tkinter.Label(update_current_refugee, text="Date of Birth*: ")
            refugee_dob_text.place(x=20, y=290)

            # refugee_dob_var= StringVar()
            # refugee_dob_entry = Entry(textvariable=refugee_dob)
            # refugee_dob_entry.place(x = 175, y = 200, width=300)

            today = datetime.date.today()

            refugee_dob = tkinter.StringVar()
            refugee_dob_calendar = tkcalendar.DateEntry(update_current_refugee, textvariable=refugee_dob, date_pattern="d/m/y",
                                                        selectmode='day')
            refugee_dob_calendar.set_date(datetime.datetime.strptime(updating_refugee_list[3], '%d/%m/%Y'))
            refugee_dob_calendar.place(x=175, y=290)

            # refugee_dob.trace('w', refugee_dob.get())
            calculate_refugee_dob = refugee_dob.get()

            # global refugee_age_status
            # refugee_age_text = Label(text = "Your age is:")
            # refugee_age_text.place(x = 20, y = 250)
            # refugee_age = StringVar()
            # refugee_age_status = Label(screen, text = str(calculate_age(refugee_dob.get())))
            # refugee_age_status.place(x = 175, y = 250, width=300)
            refugee_address = updating_refugee_list[6].split(",")

            refugee_address_text = tkinter.Label(update_current_refugee, text="Address:")
            refugee_address_text.place(x=20, y=380)

            refugee_first_address = tkinter.StringVar(value = refugee_address[0])
            refugee_first_address_entry = tkinter.Entry(update_current_refugee, textvariable=refugee_first_address)
            #refugee_first_address_entry.insert(0, 'Address Line 1')
            refugee_first_address_entry.bind('<FocusIn>', refugee_first_address_on)
            refugee_first_address_entry.bind('<FocusOut>', refugee_first_address_off)
            #refugee_first_address_entry.config(fg='grey')
            refugee_first_address_entry.place(x=175, y=380, width=300)

            refugee_city_address = tkinter.StringVar(value = refugee_address[1])
            refugee_city_address_entry = tkinter.Entry(update_current_refugee, textvariable=refugee_city_address)
            #refugee_city_address_entry.insert(0, 'Town/City')
            refugee_city_address_entry.bind('<FocusIn>', refugee_city_address_on)
            refugee_city_address_entry.bind('<FocusOut>', refugee_city_address_off)
            #refugee_city_address_entry.config(fg='grey')
            refugee_city_address_entry.place(x=175, y=410, width=150)

            refugee_postcode_address = tkinter.StringVar(value = refugee_address[2])
            refugee_postcode_address_entry = tkinter.Entry(update_current_refugee, textvariable=refugee_postcode_address)
            #refugee_postcode_address_entry.insert(0, 'Postcode')
            refugee_postcode_address_entry.bind('<FocusIn>', refugee_postcode_address_on)
            refugee_postcode_address_entry.bind('<FocusOut>', refugee_postcode_address_off)
            #refugee_postcode_address_entry.config(fg='grey')
            refugee_postcode_address_entry.place(x=325, y=410, width=150)

            refugee_country_address = tkinter.StringVar(value = refugee_address[3])
            refugee_country_address_entry = tkinter.OptionMenu(update_current_refugee, refugee_country_address, *country_list)
            refugee_country_address_entry.place(x=175, y=440, width=300)

            refugee_weight_text = tkinter.Label(update_current_refugee, text="Weight")
            refugee_weight_text.place(x=20, y=510)
            refugee_weight = tkinter.StringVar(value = updating_refugee_list[7])
            refugee_weight_entry = tkinter.Entry(update_current_refugee, textvariable=refugee_weight)
            #refugee_weight_entry.insert(0, str(update_current_refugee[7]))
            refugee_weight_entry.bind('<FocusIn>', refugee_weight_on)
            refugee_weight_entry.bind('<FocusOut>', refugee_weight_off)
            #refugee_weight_entry.config(fg='grey')
            refugee_weight_entry.place(x=175, y=510, width=300)

            refugee_height_text = tkinter.Label(update_current_refugee, text="Height")
            refugee_height_text.place(x=20, y=580)
            refugee_height = tkinter.StringVar(value = updating_refugee_list[8])
            refugee_height_entry = tkinter.Entry(update_current_refugee, textvariable=refugee_height)
            #refugee_height_entry.insert(0, 'Enter height in cm...')
            refugee_height_entry.bind('<FocusIn>', refugee_height_on)
            refugee_height_entry.bind('<FocusOut>', refugee_height_off)
            #refugee_height_entry.config(fg='grey')
            refugee_height_entry.place(x=175, y=580, width=300)

            submit_button = tkinter.Button(update_current_refugee, text="Submit the form", width=30, command=save_to_file)
            submit_button.place(x=100, y=650)

            # click_me = Button(text = "Click me", fg = "red", height = 20, width = 20)
            # click_me.place(x = 10, y = 20)

            # name_storage = StringVar()
            # name = Entry(textvariable=name_storage)
            # name.pack()



    # Opening current database and reading it into a list
    volunteer_list_file = open("Refugee_Database", "r")
    volunteer_database_list = []
    for line in volunteer_list_file:
        x = line.split("#")
        volunteer_database_list.append(x)

    volunteer_database_list_index = []
    for i in range(0, len(volunteer_database_list)):
        volunteer_database_list_index.append((volunteer_database_list[i])[0])
        i += 1

    update_screen = tkinter.Toplevel()
    update_screen.geometry("500x1000")
    update_screen.title("Update Refugee Information")

    update_refugee_label = tkinter.Label(update_screen, text = "You are going to update a refugee")
    update_refugee_label.pack()

    global Update_Emergency_Screen
    global emergency_database_list
    global View_Table_Yes
    global Index_Known_No
    global emergency_database_table
    global update_emergency_frame_two

    emergency_database_label = tkinter.Label(update_screen, text="Please use the below table to find the Refugee ID")
    emergency_database_label.pack()

    emergency_database_frame = tkinter.Frame(update_screen)
    emergency_database_frame.pack()

    emergency_database_table = tkinter.ttk.Treeview(update_screen)

    emergency_database_table['columns'] = ("Refugee ID", "Name", "Family members", "Date of Birth", "Age", "Sex", "Address", "Weight", "Height")

    emergency_database_table.column("#0", width=0, stretch='NO')
    emergency_database_table.column("Refugee ID", anchor='center', width=70)
    emergency_database_table.column("Name", anchor='center', width=100)
    emergency_database_table.column("Family members", anchor='center', width=100)
    emergency_database_table.column("Date of Birth", anchor='center', width=100)
    emergency_database_table.column("Age", anchor='center', width=30)
    emergency_database_table.column("Sex", anchor='center', width=70)
    emergency_database_table.column("Address", anchor='center', width=300)
    emergency_database_table.column("Weight", anchor='center', width=60)
    emergency_database_table.column("Height", anchor='center', width=60)

    emergency_database_table.heading("Refugee ID", text="Refugee ID", anchor='center')
    emergency_database_table.heading("Name", text="Name", anchor='center')
    emergency_database_table.heading("Family members", text="Family members", anchor='center')
    emergency_database_table.heading("Date of Birth", text="Date of Birth", anchor='center')
    emergency_database_table.heading("Age", text="Age", anchor='center')
    emergency_database_table.heading("Sex", text="Sex", anchor='center')
    emergency_database_table.heading("Address", text="Address", anchor='center')
    emergency_database_table.heading("Weight", text="Weight", anchor='center')
    emergency_database_table.heading("Height", text="Height", anchor='center')



    emergency_database_table.pack(pady = 20)

    for i in range(0, len(volunteer_database_list)):
        emergency_database_table.insert(parent='', index=i, iid=i, values=(
        volunteer_database_list[i][0], str(volunteer_database_list[i][1]), volunteer_database_list[i][2],
        volunteer_database_list[i][3], volunteer_database_list[i][4], volunteer_database_list[i][5],
        volunteer_database_list[i][6], volunteer_database_list[i][7], volunteer_database_list[i][8]))
        i += 1




    choose_refugee_label = tkinter.Label(update_screen, text = 'Please enter the ID of the refugee to update: ')
    choose_refugee_label.pack(pady = 20)

    refugee_button = tkinter.StringVar()
    choose_refugee_button = tkinter.OptionMenu(update_screen, refugee_button, *volunteer_database_list_index)
    choose_refugee_button.pack()

    confirm_refugee_button = tkinter.Button(update_screen, text = "Submit", command = confirm_update)
    confirm_refugee_button.pack()


    update_screen.mainloop()


