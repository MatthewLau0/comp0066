def create_family():
    import tkinter
    import datetime
    import subprocess
    import sys
    import tkcalendar
    import tkinter.messagebox
    #subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'tkcalendar'])
    #subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'tkintermapview'])


    # Opening current database and reading it into a list
    volunteer_list_file = open("Refugee_Database", "r")
    volunteer_database_list = []
    for line in volunteer_list_file:
        x = line.split("#")
        volunteer_database_list.append(x)
    volunteer_list_file.close()

    #CHECK THIS!!!!
    current_refugee_id = 1

    open_volunteer_file = open("volunteers.txt", 'r')
    volunteer_actual_database_list = []
    for line in open_volunteer_file:
        x = line.split("%")
        volunteer_actual_database_list.append(x)
    open_volunteer_file.close()

    open_camp_file = open("Emergency_Database.txt", 'r')
    camp_database_list = []
    for line in open_camp_file:
        x = line.split("%")
        camp_database_list.append(x)
    open_camp_file.close()

    open_accommodation_file = open("accommodations.txt", 'r')
    accommodation_database_list = []
    for line in open_accommodation_file:
        x = line.split(",")
        accommodation_database_list.append(x)
    open_accommodation_file.close()

    open_medical_file = open("medical.txt", 'r')
    medical_database_list = []
    for line in open_medical_file:
        x = line.split(",")
        medical_database_list.append(x)
    open_medical_file.close()

    open_toilet_file = open("toilets.txt", 'r')
    toilet_database_list = []
    for line in open_toilet_file:
        x = line.split(",")
        toilet_database_list.append(x)
    open_toilet_file.close()

    open_ration_file = open("ration_stall.txt", 'r')
    ration_database_list = []
    for line in open_ration_file:
        x = line.split(",")
        ration_database_list.append(x)
    open_ration_file.close()

    open_accommodation_write = open("accommodationstestlol.txt", "r")
    accommodation_write_list = []
    for line in open_accommodation_write:
        x = line.split(",")
        accommodation_write_list.append(x)
    open_accommodation_write.close()
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

        name = refugee_name.get().strip()
        number = refugee_number.get().strip()
        dob = refugee_dob_calendar.selection_get()
        age = str(calculate_age(datetime.datetime.strptime(refugee_dob_calendar.get_date(), "%d/%m/%Y")))
        sex = refugee_sex.get()

        first_address = refugee_first_address.get().strip()
        city_address = refugee_city_address.get().strip()
        postcode_address = refugee_postcode_address.get().strip()
        country_address = refugee_country_address.get().strip()



        conditions = refugee_height.get()
        no_fam_conditions = refugee_family_medical_no.get()

        #Check if there is no input in the required fields
        if name == "" or name == "Enter refugee name...":
            tkinter.messagebox.showerror(title = 'Error!', message = 'Name cannot be empty')
            return

        #Check if name has errors
        for i in name:
            if i.isnumeric() == True:
                tkinter.messagebox.showerror(title='Error!', message='Name cannot have numeric characters')
                return

            elif i.isalpha() != True and i != " ":
                tkinter.messagebox.showerror(title='Error!', message='Name cannot have special characters')
                return

        if len(name) == 0:
            tkinter.messagebox.showerror(title='Error!', message='Name cannot be empty')
            return

        if any(i.isdigit() for i in name):
            tkinter.messagebox.showerror(title='Error!', message='Name cannot have numeric characters')
            return

        if name.count(" ") > 3:
            tkinter.messagebox.showerror(title='Error!', message='Name cannot have more than 4 parts')
            return




        #Check if number has error

        if number == "":
            tkinter.messagebox.showerror(title='Error!', message='Number of family members cannot be empty')
            return

        try:
            int(number)
        except ValueError:
            tkinter.messagebox.showerror(title='Error!', message='No. of family members must be numeric')
            return

        if int(number) > 20:
            tkinter.messagebox.showerror(title='Error!', message='Maximum of 20 family members allowed')
            return

        if any(i.isalpha() for i in number):
            tkinter.messagebox.showerror(title='Error!', message='No. of family members cannot have alphabetical characters')
            return


        #Check for sex

        if sex == "":
            tkinter.messagebox.showerror(title='Error!', message='Sex cannot be empty')
            return

        #Checks for address line 1
        if first_address.isnumeric():
            tkinter.messagebox.showerror(title='Error!', message='Address cannot be fully numeric')
            return
        if len(first_address) > 100:
            tkinter.messagebox.showerror(title='Error!', message='Address must be shorter than 100 characters')
            return

        if first_address != "" or first_address != "Address Line 1":
            for i in first_address:
                if i.isalnum() != True and i != " ":
                    tkinter.messagebox.showerror(title='Error!', message='Unrecognised symbol in Address Line 1')
                    return

        #Checks for city
        if city_address.count(" ") > 3:
            tkinter.messagebox.showerror(title='Error!', message='City cannot have more than 3 words')
            return

        if city_address.isnumeric():
            tkinter.messagebox.showerror(title='Error!', message='City address cannot be numeric')
            return

        if any(i.isnumeric() for i in city_address):
            tkinter.messagebox.showerror(title='Error!', message='City cannot have numerical characters')
            return

        if city_address != "" or city_address != "Town/City":
            for i in city_address:
                if i.isalnum() != True and i != " " and i!= "/":
                    tkinter.messagebox.showerror(title='Error!', message='Unrecognised symbol in town/city')
                    return

        #Checks for postcode
        if len(postcode_address) > 10:
            tkinter.messagebox.showerror(title='Error!', message='Postcode cannot be longer than 10 characters')
            return

        if postcode_address != "" or postcode_address != "Postcode":
            for i in postcode_address:
                if i.isalnum() != True and i != " ":
                    tkinter.messagebox.showerror(title='Error!', message='Unrecognised symbol in postcode')
                    return

        address_list = [first_address, city_address, postcode_address, country_address]
        address = ', '.join(address_list)


        #Checks for conditions
        if len(conditions) > 300:
            tkinter.messagebox.showerror(title = 'Error!', message = 'Character length should be below 300!')
            return

        #Checks for family conditions




        add_camp()


    def delete1():
        screen1.destroy()

    def delete0():
        screen.destroy()

    def delete3():
        screen3.destroy()

    def calculate_age(birthdate):
        today = datetime.datetime.today()
        #x = lol.split("/")
        #birthyear = int(x[2])
        #birthmonth = int(x[1])
        #birthday = int(x[0])

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
    '''
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
    '''

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
        # Creating new refugee
        new_refugee = [""] * 9

        # Finding index for new refugee
        if len(volunteer_database_list) == 0:
            new_refugee[0] = "1"
        elif len(volunteer_database_list) >= 1:
            new_refugee[0] = str((int((volunteer_database_list[-1])[0]) + 1))


        name = refugee_name.get()
        number = refugee_number.get()
        dob = refugee_dob_calendar.get_date()
        age = str(calculate_age(datetime.datetime.strptime(refugee_dob_calendar.get_date(), "%d/%m/%Y")))
        sex = refugee_sex.get()
        conditions = refugee_height.get()
        no_fam_conditions = refugee_family_medical_no.get()



        first_address = refugee_first_address.get()
        if first_address == "Address Line 1":
            first_address = ''
        city_address = refugee_city_address.get()
        if city_address == "Town/City":
            city_address = ''
        postcode_address = refugee_postcode_address.get()
        if postcode_address == "Postcode":
            postcode_address = ''
        country_address = refugee_country_address.get()

        address_list = [first_address, city_address, postcode_address, country_address]
        address = ', '.join(address_list)

        if conditions == "Enter any medical conditions...":
            conditions = ''

        new_refugee[1] = name
        new_refugee[2] = number
        new_refugee[3] = dob
        new_refugee[4] = age
        new_refugee[5] = sex
        new_refugee[6] = address
        new_refugee[7] = conditions
        new_refugee[8] = str(no_fam_conditions)
        new_refugee_string = "#".join(new_refugee)
        volunteer_list_file.close()
        volunteer_list_file_append = open("Refugee_Database", "a")
        volunteer_list_file_append.write("\n%s" % (new_refugee_string))
        volunteer_list_file_append.close()

        delete2()
        finish_message()
        delete0()


    def add_camp():

        #Setting up the screen
        add_camp_screen = tkinter.Toplevel()
        add_camp_screen.geometry("500x1000")
        add_camp_screen.title("Enter refugee camp details")

        #CALENDAR TO CHOOSE ARRIVAL DATE
        refugee_arrival_date_text = tkinter.Label(add_camp_screen, text="Please select date of arrival if known:")
        refugee_arrival_date_text.pack()
        today = datetime.date.today()
        max = datetime.date(today.year + 2, today.month, today.day)
        min = datetime.date(today.year -2 ,today.month, today.day)
        # + or - 2 years
        refugee_arrival_calendar = tkcalendar.Calendar(add_camp_screen, date_pattern="d/m/y", selectmode='day', borderwidthint=400, foreground='black', maxdate=max, mindate=min)
        refugee_arrival_calendar.pack(pady = 30)

        #SELECT WHICH CAMP THEY WANT TO PUT REFUGEE IN

        #sees which camp the volunteer is currently assigned to
        volunteer_current_camp = int(volunteer_actual_database_list[current_refugee_id][0])

        #get list of only camp names
        camp_name_list = []
        for i in range(len(camp_database_list)):
            camp_name_list.append([camp_database_list[i][0], camp_database_list[i][1]])
        # label to get them to select which camp
        current_camp_name = ''
        for i in range(len(camp_name_list)):
            if int(camp_name_list[i][0]) == int(volunteer_current_camp):
                current_camp_name = camp_name_list[i][1]
                break

        volunteer_current_camp_label = tkinter.Label(add_camp_screen, text="Your refugee will be placed in your camp: %s" %current_camp_name)
        volunteer_current_camp_label.pack(pady=30)

        #ACCOMMODATION: get specific list with accommodation only for camp
        accommodation_specific_camp_list = []
        for i in range(len(accommodation_database_list)):
            if int(accommodation_database_list[i][0]) == int(volunteer_current_camp):
                accommodation_specific_camp_list.append(accommodation_database_list[i])


        #iterate through list to see which one is free
        refugee_assigned_accommodation = ''
        for i in range(len(accommodation_specific_camp_list)):
            if int(accommodation_specific_camp_list[i][6]) > (int(refugee_number.get())+1):
                refugee_assigned_accommodation = accommodation_specific_camp_list[i][2]
                refugee_assigned_block = accommodation_specific_camp_list[i][7]
                that_block_list = accommodation_specific_camp_list[i]
                xhaha = str(int(that_block_list[4]) + (int(refugee_number.get())+1))
                yhaha = str(int(that_block_list[6]) - (int(refugee_number.get())+1))
                print(xhaha)
                print(yhaha)
                that_block_list[4] = xhaha
                that_block_list[6] = yhaha
                print(that_block_list)



                for j in range(len(accommodation_database_list)):
                    if accommodation_database_list[j][0] == that_block_list[0] and accommodation_database_list[j][1] == that_block_list[1]:
                        accommodation_database_list[j] = that_block_list

                new_rewritten_database_temp = []
                for i in accommodation_database_list:
                    new_rewritten_database_temp.append(','.join(i))



                accommodations_write_new = open("accommodationstestlol.txt", "w")
                for i in range(len(new_rewritten_database_temp)):
                    accommodations_write_new.write(new_rewritten_database_temp[i])
                accommodations_write_new.close()

                break

        refugee_assigned_accommodation_label = tkinter.Label(add_camp_screen, text = 'Your refugee accommodation will be in: %s, %s' %(refugee_assigned_accommodation, refugee_assigned_block))
        refugee_assigned_accommodation_label.pack(pady = 10)

        #MEDICAL: get specific list with medical only for camp
        medical_specific_camp_list = []
        for i in range(len(medical_database_list)):
            if int(medical_database_list[i][0]) == int(volunteer_current_camp) and medical_database_list[i][7] == refugee_assigned_block:
                medical_specific_camp_list.append(medical_database_list[i])

        # iterate through list to see which one is free
        refugee_assigned_medical = 'No blocks available!'
        for i in range(len(medical_specific_camp_list)):
            if int(medical_specific_camp_list[i][6]) > int(refugee_family_medical_no.get()):
                refugee_assigned_medical = medical_specific_camp_list[i][2]
                break

        refugee_assigned_medical_label = tkinter.Label(add_camp_screen, text='Your refugee medical stall will be in: %s' % refugee_assigned_medical)
        refugee_assigned_medical_label.pack(pady=10)

        #TOILET: get specific list with toilets only for camp
        toilet_specific_camp_list = []

        for i in range(len(toilet_database_list)):
            if int(toilet_database_list[i][0]) == int(volunteer_current_camp) and toilet_database_list[i][7] == refugee_assigned_block:
                toilet_specific_camp_list.append(toilet_database_list[i])

        # iterate through list to see which one is free
        refugee_assigned_toilet = 'No toilets available!'
        for i in range(len(toilet_specific_camp_list)):
            if int(toilet_specific_camp_list[i][6]) > int(refugee_number.get()):
                refugee_assigned_toilet = toilet_specific_camp_list[i][2]
                break

        refugee_assigned_toilet_label = tkinter.Label(add_camp_screen, text='Your refugee toilet stall will be in: %s' % refugee_assigned_toilet)
        refugee_assigned_toilet_label.pack(pady=10)

        #RATIONS: get specific list with rations only for camp
        ration_specific_camp_list = []

        for i in range(len(ration_database_list)):
            if int(ration_database_list[i][0]) == int(volunteer_current_camp) and ration_database_list[i][7] == refugee_assigned_block:
                ration_specific_camp_list.append(ration_database_list[i])

        # iterate through list to see which one is free
        refugee_assigned_ration = 'No rations available!'
        for i in range(len(ration_specific_camp_list)):
            if int(ration_specific_camp_list[i][6]) > int(refugee_number.get()):
                refugee_assigned_ration = ration_specific_camp_list[i][2]
                break

        refugee_assigned_ration_label = tkinter.Label(add_camp_screen, text='Your refugee ration stall will be in: %s' % refugee_assigned_ration)
        refugee_assigned_ration_label.pack(pady=10)






        #function that runs when continue is clicked
        '''
        def output_camp():
            camp_name = volunteer_current_camp_var.get()
            index = camp_name_list.index(camp_name)

            #campID: THIS IS IDENTIFIER OF CAMP
            camp_id_pog = camp_database_list[index][0]

            #get a list of accommodations in that camp
            specific_accommodation_camp_list = []
            for i in range(len(accommodation_database_list)):
                if accommodation_database_list[i][0] == camp_id_pog:
                    specific_accommodation_camp_list.append(accommodation_database_list[i])

            print(specific_accommodation_camp_list)
        '''


        camp_submit_button = tkinter.Button(add_camp_screen, text="Submit the form", width=30, command=success)
        camp_submit_button.pack()







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

        dob_confirmation = tkinter.Label(screen2, text="The date of birth you are entering is: %s" %refugee_dob_calendar.get_date())
        dob_confirmation.pack()

        age_confirmation = tkinter.Label(screen2, text="This means their age is: %s" %str(calculate_age(datetime.datetime.strptime(refugee_dob_calendar.get_date(), "%d/%m/%Y"))))
        age_confirmation.pack()

        first_address = refugee_first_address.get()
        if first_address == "Address Line 1":
            first_address = ''
        city_address = refugee_city_address.get()
        if city_address == "Town/City":
            city_address = ''
        postcode_address = refugee_postcode_address.get()
        if postcode_address == "Postcode":
            postcode_address = ''
        country_address = refugee_country_address.get()

        address_list = [first_address, city_address, postcode_address, country_address]
        address = ', '.join(address_list)

        address_confirmation = tkinter.Label(screen2, text="Their address is: %s" %address)
        address_confirmation.pack()

        conditions = refugee_height.get()
        if conditions == 'Enter any medical conditions...':
            conditions = ''

        weight_confirmation = tkinter.Label(screen2, text="Your conditions are: %s" %conditions)
        weight_confirmation.pack()

        height_confirmation = tkinter.Label(screen2, text="Number of family members with conditions: %s" %str(refugee_family_medical_no.get()))
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
        if refugee_number_entry.get() == 'Enter no. of family members...':
           refugee_number_entry.delete(0, "end") # delete all the text in the entry
           refugee_number_entry.insert(0, '') #Insert blank for user input
           refugee_number_entry.config(fg = 'black')
    def refugee_number_off(self):
        if refugee_number_entry.get() == '':
            refugee_number_entry.insert(0, 'Enter no. of family members...')
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
        if refugee_height_entry.get() == 'Enter any medical conditions...':
           refugee_height_entry.delete(0, "end") # delete all the text in the entry
           refugee_height_entry.insert(0, '') #Insert blank for user input
           refugee_height_entry.config(fg = 'black')
    def refugee_height_off(self):
        if refugee_height_entry.get() == '':
            refugee_height_entry.insert(0, 'Enter any medical conditions...')
            refugee_height_entry.config(fg = 'grey')


    #define text file


    #Setting up the screen
    screen = tkinter.Toplevel()
    screen.geometry("500x1000")
    screen.title("Create Refugee Form")
    #screen.configure(background="#A1CDEC")

    #Title text
    intro_text = tkinter.Label(screen, text = "Use this section to create a refugee within this Database.", fg = 'Green', width= 300)
    intro_text.place(x = 20, y = 20)

    #Input from user


    namestatus = tkinter.Label(screen, text = "")
    namestatus.place(x = 20, y = 50)

    refugee_name_text = tkinter.Label(screen, text = "Refugee name*: ")
    refugee_name_text.place(x = 20, y = 30)
    refugee_name = tkinter.StringVar()
    refugee_name_entry = tkinter.Entry(screen, validate = 'all', validatecommand = name_validate, textvariable=refugee_name)
    refugee_name_entry.insert(0, 'Enter refugee name...')
    refugee_name_entry.bind('<FocusIn>', refugee_text_on)
    refugee_name_entry.bind('<FocusOut>', refugee_text_off)
    refugee_name_entry.config(fg = 'grey')
    refugee_name_entry.place(x = 175, y = 30, width=300)



    numberstatus = tkinter.Label(screen, text = "")
    numberstatus.place(x = 20, y = 120)

    refugee_number_text = tkinter.Label(screen, text = "No. of family members*: ")
    refugee_number_text.place(x = 20, y = 100)
    refugee_number = tkinter.StringVar()
    refugee_number_entry = tkinter.Spinbox(screen, textvariable = refugee_number, from_=0, to = 20)
    #refugee_number_entry.insert(0, 'Enter no. of family members...')
    #refugee_number_entry.bind('<FocusIn>', refugee_number_on)
    #refugee_number_entry.bind('<FocusOut>', refugee_number_off)
    #refugee_number_entry.config(fg = 'grey')
    refugee_number_entry.place(x = 175, y = 100, width=300)



    refugee_sex_text = tkinter.Label(screen, text = "Sex*:")
    refugee_sex_text.place(x = 20, y = 170)
    refugee_sex = tkinter.StringVar()
    #refugee_sex_entry = Entry(textvariable=refugee_sex)
    #refugee_sex_entry.place(x = 175, y = 150, width=300)
    drop = tkinter.OptionMenu(screen, refugee_sex, "Male", "Female", "Prefer not to say")
    drop.place(x = 175, y = 170, width = 300)

    refugee_dob_text = tkinter.Label(screen, text = "Date of Birth*: ")
    refugee_dob_text.place(x = 20, y = 220)

    #refugee_dob_var= StringVar()
    # refugee_dob_entry = Entry(textvariable=refugee_dob)
    # refugee_dob_entry.place(x = 175, y = 200, width=300)

    today = datetime.date.today()
    max = datetime.date(1904, 2, 11)
    #oldest person alive!


    #refugee_dob = tkinter.StringVar()
    refugee_dob_calendar = tkcalendar.Calendar(screen, date_pattern="d/m/y", selectmode='day', borderwidthint= 400, foreground = 'black', maxdate= today, mindate= max)
    refugee_dob_calendar.place(x = 175, y = 220)

    #refugee_dob.trace('w', refugee_dob.get())
    calculate_refugee_dob = refugee_dob_calendar.get_date()


    #global refugee_age_status
    #refugee_age_text = Label(text = "Your age is:")
    #refugee_age_text.place(x = 20, y = 250)
    #refugee_age = StringVar()
    #refugee_age_status = Label(screen, text = str(calculate_age(refugee_dob.get())))
    #refugee_age_status.place(x = 175, y = 250, width=300)

    refugee_address_text = tkinter.Label(screen, text = "Address:")
    refugee_address_text.place(x = 20, y = 400)

    refugee_first_address = tkinter.StringVar()
    refugee_first_address_entry = tkinter.Entry(screen, textvariable=refugee_first_address)
    refugee_first_address_entry.insert(0, 'Address Line 1')
    refugee_first_address_entry.bind('<FocusIn>', refugee_first_address_on)
    refugee_first_address_entry.bind('<FocusOut>', refugee_first_address_off)
    refugee_first_address_entry.config(fg = 'grey')
    refugee_first_address_entry.place(x = 175, y = 400, width=300)

    refugee_city_address = tkinter.StringVar()
    refugee_city_address_entry = tkinter.Entry(screen, textvariable=refugee_city_address)
    refugee_city_address_entry.insert(0, 'Town/City')
    refugee_city_address_entry.bind('<FocusIn>', refugee_city_address_on)
    refugee_city_address_entry.bind('<FocusOut>', refugee_city_address_off)
    refugee_city_address_entry.config(fg = 'grey')
    refugee_city_address_entry.place(x = 175, y = 430, width=150)

    refugee_postcode_address = tkinter.StringVar()
    refugee_postcode_address_entry = tkinter.Entry(screen, textvariable=refugee_postcode_address)
    refugee_postcode_address_entry.insert(0, 'Postcode')
    refugee_postcode_address_entry.bind('<FocusIn>', refugee_postcode_address_on)
    refugee_postcode_address_entry.bind('<FocusOut>', refugee_postcode_address_off)
    refugee_postcode_address_entry.config(fg = 'grey')
    refugee_postcode_address_entry.place(x = 325, y = 430, width=150)

    refugee_country_address = tkinter.StringVar()
    refugee_country_address_entry = tkinter.OptionMenu(screen, refugee_country_address, *country_list)
    refugee_country_address_entry.place(x = 175, y = 460, width = 300)

    def clickYes():
        global refugee_height
        global refugee_height_entry
        global refugee_family_medical_no
        refugee_height = tkinter.StringVar()
        refugee_family_medical_no = tkinter.StringVar(value=0)
        if refugee_weight.get() == 1:
            refugee_weight_entry_2.config(state='disabled')
            refugee_height_text = tkinter.Label(screen, text="Your conditions:")
            refugee_height_text.place(x=20, y=580)
            refugee_height_entry = tkinter.Entry(screen, textvariable=refugee_height)
            refugee_height_entry.insert(0, 'Enter any medical conditions...')
            refugee_height_entry.bind('<FocusIn>', refugee_height_on)
            refugee_height_entry.bind('<FocusOut>', refugee_height_off)
            refugee_height_entry.config(fg='grey')
            refugee_height_entry.place(x=175, y=580, width=300)
            refugee_family_medical_no_label = tkinter.Label(screen, text="How many family members have conditions")
            refugee_family_medical_no_label.place(x=20, y=650)

            refugee_family_num = []
            for i in range(0, int(refugee_number.get())+1):
                refugee_family_num.append(i)
            refugee_family_medical_no_option = tkinter.OptionMenu(screen, refugee_family_medical_no, *refugee_family_num)
            refugee_family_medical_no_option.place(x=300, y=650)

        else:
            refugee_height.set('Enter any medical conditions...')
            refugee_weight_entry_2.config(state='normal')
            hehe_label = tkinter.Label(screen, text='')
            hehe_label.place(x=15, y=580, width=800, height=40)
            hehe_label = tkinter.Label(screen, text='')
            hehe_label.place(x=15, y=650, width=800, height=40)

    def clickNo():
        global refugee_height
        refugee_height = tkinter.StringVar()
        global refugee_family_medical_no
        refugee_family_medical_no = tkinter.StringVar(value=0)
        if refugee_weight_2.get() == 1:
            refugee_height.set('Enter any medical conditions...')
            refugee_weight_entry.config(state='disabled')
            lol_label = tkinter.Label(screen, text = '')
            lol_label.place(x = 15, y = 580, width= 800, height = 40)
            lol_label = tkinter.Label(screen, text='')
            lol_label.place(x=15, y=650, width=800, height=40)
        else:
            refugee_height.set('Enter any medical conditions...')
            refugee_weight_entry.config(state='normal')

    #THIS IS REPLACED WITH MEDICAL CONDITION CHECKBOX
    refugee_weight_text = tkinter.Label(screen, text = "Do you or your family have\n any medical conditions?*")
    refugee_weight_text.place(x = 20, y = 510)
    refugee_weight = tkinter.IntVar()
    refugee_weight_2 = tkinter.IntVar()
    refugee_weight_entry = tkinter.Checkbutton(screen, variable = refugee_weight, onvalue=1, offvalue=2, text = "Yes", command = clickYes)
    refugee_weight_entry_2 = tkinter.Checkbutton(screen, variable = refugee_weight_2, onvalue=1, offvalue=2, text = "No", command = clickNo)
    #refugee_weight_entry.insert(0, 'Enter weight in kg...')
    #refugee_weight_entry.bind('<FocusIn>', refugee_weight_on)
    #refugee_weight_entry.bind('<FocusOut>', refugee_weight_off)
    #refugee_weight_entry.config(fg = 'grey')
    refugee_weight_entry.place(x = 300, y = 510)
    refugee_weight_entry_2.place(x = 300, y = 530)






    submit_button = tkinter.Button(screen, text = "Submit the form", width=30, command=save_to_file)
    submit_button.place(x = 100, y= 720)


    #click_me = Button(text = "Click me", fg = "red", height = 20, width = 20)
    #click_me.place(x = 10, y = 20)

    #name_storage = StringVar()
    #name = Entry(textvariable=name_storage)
    #name.pack()

    #tkinter.mainloop()
    screen.mainloop()

