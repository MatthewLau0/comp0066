def create_family():
    import tkinter
    import datetime
    import subprocess
    import sys
    import tkcalendar
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'tkcalendar'])
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'tkintermapview'])



    # Opening current database and reading it into a list
    volunteer_list_file = open("Volunteer_Database", "r")
    volunteer_database_list = []
    for line in volunteer_list_file:
        x = line.split("#")
        volunteer_database_list.append(x)

    # def age_status():
    #     date = refugee_dob.get()
    #
    #     if date == 0:
    #         refugee_age_status.config(text = "Please enter age in the box above")
    #
    #     else:
    #         refugee_age_status.config(text = "lolol")
    #
    #     return True

    country_list = ['Afghanistan', 'Aland Islands', 'Albania', 'Algeria', 'American Samoa', 'Andorra', 'Angola', 'Anguilla', 'Antarctica', 'Antigua and Barbuda', 'Argentina', 'Armenia', 'Aruba', 'Australia', 'Austria', 'Azerbaijan', 'Bahamas', 'Bahrain', 'Bangladesh', 'Barbados', 'Belarus', 'Belgium', 'Belize', 'Benin', 'Bermuda', 'Bhutan', 'Bolivia', 'Bosnia and Herzegovina', 'Botswana', 'Bouvet Island', 'Brazil', 'British Indian Ocean Territory', 'Brunei Darussalam', 'Bulgaria', 'Burkina Faso', 'Burundi', 'Cambodia', 'Cameroon', 'Canada', 'Cape Verde', 'Cayman Islands', 'Central African Republic', 'Chad', 'Chile', 'China', 'Christmas Island', 'Cocos (Keeling) Islands', 'Colombia', 'Comoros', 'Congo', 'The Democratic Republic of the Congo', 'Cook Islands', 'Costa Rica', "Côte d'Ivoire", 'Croatia', 'Cuba', 'Curaçao', 'Cyprus', 'Czech Republic', 'Denmark', 'Djibouti', 'Dominica', 'Dominican Republic', 'Ecuador', 'Egypt', 'El Salvador', 'Equatorial Guinea', 'Eritrea', 'Estonia', 'Ethiopia', 'Faroe Islands', 'Fiji', 'Finland', 'France', 'French Guiana', 'French Polynesia', 'French Southern Territories', 'Gabon', 'Gambia', 'Georgia', 'Germany', 'Ghana', 'Gibraltar', 'Greece', 'Greenland', 'Grenada', 'Guadeloupe', 'Guam', 'Guatemala', 'Guernsey', 'Guinea', 'Guinea-Bissau', 'Guyana', 'Haiti', 'Heard Island and McDonald Islands', 'Vatican City', 'Honduras', 'Hong Kong', 'Hungary', 'Iceland', 'India', 'Indonesia', 'Iran', 'Iraq', 'Ireland', 'Isle of Man', 'Israel', 'Italy', 'Jamaica', 'Japan', 'Jersey', 'Jordan', 'Kazakhstan', 'Kenya', 'Kiribati', 'Republic of Korea', 'Kuwait', 'Kyrgyzstan', "Laos", 'Latvia', 'Lebanon', 'Lesotho', 'Liberia', 'Libya', 'Liechtenstein', 'Lithuania', 'Luxembourg', 'Macao', 'Macedonia', 'Madagascar', 'Malawi', 'Malaysia', 'Maldives', 'Mali', 'Malta', 'Marshall Islands', 'Martinique', 'Mauritania', 'Mauritius', 'Mayotte', 'Mexico', 'Micronesia', 'Moldova', 'Monaco', 'Mongolia', 'Montenegro', 'Montserrat', 'Morocco', 'Mozambique', 'Myanmar', 'Namibia', 'Nauru', 'Nepal', 'Netherlands', 'New Caledonia', 'New Zealand', 'Nicaragua', 'Niger', 'Nigeria', 'Niue', 'Norfolk Island', 'Northern Mariana Islands', 'Norway', 'Oman', 'Pakistan', 'Palau', 'Palestinian Territory', 'Panama', 'Papua New Guinea', 'Paraguay', 'Peru', 'Philippines', 'Pitcairn', 'Poland', 'Portugal', 'Puerto Rico', 'Qatar', 'Réunion', 'Romania', 'Russia', 'Rwanda', 'Saint Lucia', 'Samoa', 'San Marino', 'Sao Tome and Principe', 'Saudi Arabia', 'Senegal', 'Serbia', 'Seychelles', 'Sierra Leone', 'Singapore', 'Slovakia', 'Slovenia', 'Solomon Islands', 'Somalia', 'South Africa', 'Spain', 'Sri Lanka', 'Sudan', 'Suriname', 'South Sudan', 'Svalbard', 'Swaziland', 'Sweden', 'Switzerland', 'Syrian Arab Republic', 'Taiwan', 'Tajikistan', 'Tanzania', 'Thailand', 'Timor-Leste', 'Togo', 'Tokelau', 'Tonga', 'Trinidad and Tobago', 'Tunisia', 'Turkey', 'Turkmenistan', 'Turks and Caicos Islands', 'Tuvalu', 'Uganda', 'Ukraine', 'United Arab Emirates', 'United Kingdom', 'United States', 'Uruguay', 'Uzbekistan', 'Vanuatu', 'Venezuela', 'Vietnam', 'Yemen', 'Zambia', 'Zimbabwe']


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

        #Check if there is no input in the required fields
        if name == "" or number == "" or sex == "":
            noinput_error()
            print("1")
            return

        #Check if name has errors
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


        #Check if number has error
        try:
            int(number)
        except ValueError:
            print("6")
            noinput_error()
            return

        if len(number)!=5:
            print("7")
            noinput_error()
            return

        if any(i.isalpha() for i in number):
            print("8")
            noinput_error()

            return

        if len(volunteer_database_list) == 0:
            pass
        else:
            for i in range(len(volunteer_database_list)):
                if number == volunteer_database_list[i][2]:
                    print("9")
                    noinput_error()
                    return



        #Checks for address line 1
        if first_address.isnumeric():
            print("10")
            noinput_error()
            return
        if len(first_address) > 100:
            print("11")
            noinput_error()
            return

        #Checks for city
        if city_address.count(" ") > 4:
            print("12")
            noinput_error()
            return

        if city_address.isnumeric():
            print("13")
            noinput_error()
            return

        #Checks for postcode
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


        #Checks for weight
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




        #Checks for height
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
        screen.destroy()

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
        name = refugee_name_entry.get()

        if len(name) == 0:
            namestatus.config(text = "Name cannot be 0")

        else:
            try:
                if len(name) <= 2:
                    namestatus.config(text = "Name too short!")

                elif any(i.isdigit() for i in name):
                    namestatus.config(text = "Name can't be numeric!")

                elif name.count(" ") > 3:
                    namestatus.config(text = "Please enter less than 4 separate names")

                else:
                    namestatus.config(text = "Valid :)")
            except:
                pass
        return True

    def number_validate():
        number = refugee_number.get()

        if len(number) == 0:
            numberstatus.config(text = "Number cannot be 0")

        else:
            try:
                if len(number) != 5:
                    numberstatus.config(text = "Number must be 5 digits long!")

                elif any(i.isalpha() for i in number):
                    numberstatus.config(text = "Number can't have alphabetical characters!")

                elif number.count(" ") > 1:
                    numberstatus.config(text = "Please enter it as a full number")

                elif number.count(".") > 1:
                    numberstatus.config(text = "The number can't be a decimal")

                elif number in volunteer_database_list:
                    numberstatus.config(text = "Number already exists!")

                else:
                    numberstatus.config(text = "Valid :)")
            except:
                pass
        return True

    def delete2():
        screen2.destroy()

    def noinput_error():
        global screen1
        screen1 = tkinter.Toplevel(screen)
        screen1.geometry("300x120")
        screen1.title("Warning!")
        noinput_error_text = tkinter.Label(screen1, text = "All fields required are marked with an *", fg = 'red')
        noinput_error_text.place(x = 40, y = 40)
        close_button = tkinter.Button(screen1, text = "I understand", command = delete1)
        close_button.place(x = 95, y = 80)
    def finish_message():
        global screen3
        screen3 = tkinter.Tk()
        screen3.geometry("300x120")
        screen3.title("Success!")
        finish_message_text = tkinter.Label(screen3, text = "Successfully added new refugee!", fg = 'green')
        finish_message_text.place(x = 40, y = 40)
        close_button = tkinter.Button(screen3, text = "I understand", command = delete3)
        close_button.place(x = 95, y = 80)

    def submit():
        print("1")
        # Creating new refugee
        new_refugee = [""] * 14

        # Finding index for new refugee
        if len(volunteer_database_list) == 0:
            new_refugee[0] = "1"
        elif len(volunteer_database_list) >= 1:
            new_refugee[0] = str((int((volunteer_database_list[-1])[0]) + 1))
        print("The index number for this emergency is ", new_refugee[0])

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
        volunteer_list_file_append = open("Volunteer_Database", "a")
        volunteer_list_file_append.write("\n%s" % (new_refugee_string))
        volunteer_list_file_append.close()

        delete2()
        finish_message()
        delete0()




    def success():
        global screen2
        screen2 = tkinter.Toplevel(screen)
        screen2.geometry("500x650")
        screen2.title("Confirm refugee submission")



        refugee_confirmation = tkinter.Label(screen2, text = "Please check the summary of details below to add to the database")
        refugee_confirmation.pack()

        name_confirmation = tkinter.Label(screen2, text = "The name you are entering is: %s" %(refugee_name.get()))
        name_confirmation.pack()

        number_confirmation = tkinter.Label(screen2, text = "The number you are entering is: %s" %refugee_number.get())
        number_confirmation.pack()

        sex_confirmation = tkinter.Label(screen2, text="The sex you are entering is: %s" %refugee_sex.get())
        sex_confirmation.pack()

        dob_confirmation = tkinter.Label(screen2, text="The date of birth you are entering is: %s" %str(refugee_dob.get()))
        dob_confirmation.pack()

        age_confirmation = tkinter.Label(screen2, text="This means their age is: %s" %str(calculate_age(str(refugee_dob.get()))))
        age_confirmation.pack()

        first_address = refugee_first_address.get()
        city_address = refugee_city_address.get()
        postcode_address = refugee_postcode_address.get()
        country_address = refugee_country_address.get()

        address_list = [first_address, city_address, postcode_address, country_address]
        address = ', '.join(address_list)

        address_confirmation = tkinter.Label(screen2, text="Their address is: %s" %address)
        address_confirmation.pack()

        weight_confirmation = tkinter.Label(screen2, text="Their weight is: %s kg" %refugee_weight.get())
        weight_confirmation.pack()

        height_confirmation = tkinter.Label(screen2, text="Their height is: %s cm" %refugee_height.get())
        height_confirmation.pack()

        submit_button = tkinter.Button(screen2, text="Submit", command=submit)
        submit_button.pack()
        update_refugee_button = tkinter.Button(screen2, text="Change details", command=delete2)
        update_refugee_button.pack()


    def refugee_text_on(self):
        if refugee_name_entry.get() == 'Enter refugee name...':
           refugee_name_entry.delete(0, "end") # delete all the text in the entry
           refugee_name_entry.insert(0, '') #Insert blank for user input
           refugee_name_entry.config(fg = 'black')
    def refugee_text_off(self):
        if refugee_name_entry.get() == '':
            refugee_name_entry.insert(0, 'Enter refugee name...')
            refugee_name_entry.config(fg = 'grey')

    def refugee_number_on(self):
        if refugee_number_entry.get() == 'Enter 5-digit number...':
           refugee_number_entry.delete(0, "end") # delete all the text in the entry
           refugee_number_entry.insert(0, '') #Insert blank for user input
           refugee_number_entry.config(fg = 'black')
    def refugee_number_off(self):
        if refugee_number_entry.get() == '':
            refugee_number_entry.insert(0, 'Enter 5-digit number...')
            refugee_number_entry.config(fg = 'grey')

    def refugee_first_address_on(self):
        if refugee_first_address_entry.get() == 'Address Line 1':
           refugee_first_address_entry.delete(0, "end") # delete all the text in the entry
           refugee_first_address_entry.insert(0, '') #Insert blank for user input
           refugee_first_address_entry.config(fg = 'black')
    def refugee_first_address_off(self):
        if refugee_first_address_entry.get() == '':
            refugee_first_address_entry.insert(0, 'Address Line 1')
            refugee_first_address_entry.config(fg = 'grey')

    def refugee_city_address_on(self):
        if refugee_city_address_entry.get() == 'Town/City':
           refugee_city_address_entry.delete(0, "end") # delete all the text in the entry
           refugee_city_address_entry.insert(0, '') #Insert blank for user input
           refugee_city_address_entry.config(fg = 'black')
    def refugee_city_address_off(self):
        if refugee_city_address_entry.get() == '':
            refugee_city_address_entry.insert(0, 'Town/City')
            refugee_city_address_entry.config(fg = 'grey')

    def refugee_postcode_address_on(self):
        if refugee_postcode_address_entry.get() == 'Postcode':
           refugee_postcode_address_entry.delete(0, "end") # delete all the text in the entry
           refugee_postcode_address_entry.insert(0, '') #Insert blank for user input
           refugee_postcode_address_entry.config(fg = 'black')
    def refugee_postcode_address_off(self):
        if refugee_postcode_address_entry.get() == '':
            refugee_postcode_address_entry.insert(0, 'Postcode')
            refugee_postcode_address_entry.config(fg = 'grey')


    def refugee_weight_on(self):
        if refugee_weight_entry.get() == 'Enter weight in kg...':
           refugee_weight_entry.delete(0, "end") # delete all the text in the entry
           refugee_weight_entry.insert(0, '') #Insert blank for user input
           refugee_weight_entry.config(fg = 'black')
    def refugee_weight_off(self):
        if refugee_weight_entry.get() == '':
            refugee_weight_entry.insert(0, 'Enter weight in kg...')
            refugee_weight_entry.config(fg = 'grey')

    def refugee_height_on(self):
        if refugee_height_entry.get() == 'Enter height in cm...':
           refugee_height_entry.delete(0, "end") # delete all the text in the entry
           refugee_height_entry.insert(0, '') #Insert blank for user input
           refugee_height_entry.config(fg = 'black')
    def refugee_height_off(self):
        if refugee_height_entry.get() == '':
            refugee_height_entry.insert(0, 'Enter height in cm...')
            refugee_height_entry.config(fg = 'grey')


    #define text file


    #Setting up the screen
    screen = tkinter.Toplevel()
    screen.geometry("500x1000")
    screen.title("Create Refugee Form")
    #screen.configure(background="#A1CDEC")

    #Title text
    intro_text = tkinter.Label(screen, text = "Use this section to create a refugee within this Database.", fg = 'Green', bg="Light Grey", width= 500)
    intro_text.pack

    #Input from user


    namestatus = tkinter.Label(screen, text = "")
    namestatus.place(x = 20, y = 70)

    refugee_name_text = tkinter.Label(screen, text = "Refugee name*: ")
    refugee_name_text.place(x = 20, y = 50)
    refugee_name = tkinter.StringVar()
    refugee_name_entry = tkinter.Entry(screen, validate = 'all', validatecommand = name_validate, textvariable=refugee_name)
    refugee_name_entry.insert(0, 'Enter refugee name...')
    refugee_name_entry.bind('<FocusIn>', refugee_text_on)
    refugee_name_entry.bind('<FocusOut>', refugee_text_off)
    refugee_name_entry.config(fg = 'grey')
    refugee_name_entry.place(x = 175, y = 50, width=300)



    numberstatus = tkinter.Label(screen, text = "")
    numberstatus.place(x = 20, y = 140)

    refugee_number_text = tkinter.Label(screen, text = "Refugee Number*: ")
    refugee_number_text.place(x = 20, y = 120)
    refugee_number = tkinter.StringVar()
    refugee_number_entry = tkinter.Entry(screen, textvariable=refugee_number, validate = 'all', validatecommand=number_validate)
    refugee_number_entry.insert(0, 'Enter 5-digit number...')
    refugee_number_entry.bind('<FocusIn>', refugee_number_on)
    refugee_number_entry.bind('<FocusOut>', refugee_number_off)
    refugee_number_entry.config(fg = 'grey')
    refugee_number_entry.place(x = 175, y = 120, width=300)



    refugee_sex_text = tkinter.Label(screen, text = "Sex*:")
    refugee_sex_text.place(x = 20, y = 190)
    refugee_sex = tkinter.StringVar()
    #refugee_sex_entry = Entry(textvariable=refugee_sex)
    #refugee_sex_entry.place(x = 175, y = 150, width=300)
    drop = tkinter.OptionMenu(screen, refugee_sex, "Male", "Female", "Prefer not to say")
    drop.place(x = 175, y = 190, width = 300)

    refugee_dob_text = tkinter.Label(screen, text = "Date of Birth*: ")
    refugee_dob_text.place(x = 20, y = 260)

    #refugee_dob_var= StringVar()
    # refugee_dob_entry = Entry(textvariable=refugee_dob)
    # refugee_dob_entry.place(x = 175, y = 200, width=300)

    today = datetime.date.today()

    refugee_dob = tkinter.StringVar()
    refugee_dob_calendar = tkcalendar.DateEntry(screen, textvariable = refugee_dob, date_pattern="d/m/y", selectmode='day')
    refugee_dob_calendar.place(x = 175, y = 260)

    #refugee_dob.trace('w', refugee_dob.get())
    calculate_refugee_dob = refugee_dob.get()


    #global refugee_age_status
    #refugee_age_text = Label(text = "Your age is:")
    #refugee_age_text.place(x = 20, y = 250)
    #refugee_age = StringVar()
    #refugee_age_status = Label(screen, text = str(calculate_age(refugee_dob.get())))
    #refugee_age_status.place(x = 175, y = 250, width=300)

    refugee_address_text = tkinter.Label(screen, text = "Address:")
    refugee_address_text.place(x = 20, y = 330)

    refugee_first_address = tkinter.StringVar()
    refugee_first_address_entry = tkinter.Entry(screen, textvariable=refugee_first_address)
    refugee_first_address_entry.insert(0, 'Address Line 1')
    refugee_first_address_entry.bind('<FocusIn>', refugee_first_address_on)
    refugee_first_address_entry.bind('<FocusOut>', refugee_first_address_off)
    refugee_first_address_entry.config(fg = 'grey')
    refugee_first_address_entry.place(x = 175, y = 330, width=300)

    refugee_city_address = tkinter.StringVar()
    refugee_city_address_entry = tkinter.Entry(screen, textvariable=refugee_city_address)
    refugee_city_address_entry.insert(0, 'Town/City')
    refugee_city_address_entry.bind('<FocusIn>', refugee_city_address_on)
    refugee_city_address_entry.bind('<FocusOut>', refugee_city_address_off)
    refugee_city_address_entry.config(fg = 'grey')
    refugee_city_address_entry.place(x = 175, y = 360, width=150)

    refugee_postcode_address = tkinter.StringVar()
    refugee_postcode_address_entry = tkinter.Entry(screen, textvariable=refugee_postcode_address)
    refugee_postcode_address_entry.insert(0, 'Postcode')
    refugee_postcode_address_entry.bind('<FocusIn>', refugee_postcode_address_on)
    refugee_postcode_address_entry.bind('<FocusOut>', refugee_postcode_address_off)
    refugee_postcode_address_entry.config(fg = 'grey')
    refugee_postcode_address_entry.place(x = 325, y = 360, width=150)

    refugee_country_address = tkinter.StringVar()
    refugee_country_address_entry = tkinter.OptionMenu(screen, refugee_country_address, *country_list)
    refugee_country_address_entry.place(x = 175, y = 390, width = 300)


    refugee_weight_text = tkinter.Label(screen, text = "Weight")
    refugee_weight_text.place(x = 20, y = 460)
    refugee_weight = tkinter.StringVar()
    refugee_weight_entry = tkinter.Entry(screen, textvariable=refugee_weight)
    refugee_weight_entry.insert(0, 'Enter weight in kg...')
    refugee_weight_entry.bind('<FocusIn>', refugee_weight_on)
    refugee_weight_entry.bind('<FocusOut>', refugee_weight_off)
    refugee_weight_entry.config(fg = 'grey')
    refugee_weight_entry.place(x = 175, y = 460, width=300)

    refugee_height_text = tkinter.Label(screen, text = "Height")
    refugee_height_text.place(x = 20, y = 530)
    refugee_height = tkinter.StringVar()
    refugee_height_entry = tkinter.Entry(screen, textvariable=refugee_height)
    refugee_height_entry.insert(0, 'Enter height in cm...')
    refugee_height_entry.bind('<FocusIn>', refugee_height_on)
    refugee_height_entry.bind('<FocusOut>', refugee_height_off)
    refugee_height_entry.config(fg = 'grey')
    refugee_height_entry.place(x = 175, y = 530, width=300)


    submit_button = tkinter.Button(screen, text = "Submit the form", width=30, command=save_to_file)
    submit_button.place(x = 100, y= 600)


    #click_me = Button(text = "Click me", fg = "red", height = 20, width = 20)
    #click_me.place(x = 10, y = 20)

    #name_storage = StringVar()
    #name = Entry(textvariable=name_storage)
    #name.pack()

    #tkinter.mainloop()
    screen.mainloop()

