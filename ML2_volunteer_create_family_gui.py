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
    volunteer_list_file = open("Final_Files/refugee_database.txt", "r")
    volunteer_database_list = []
    for line in volunteer_list_file:
        x = line.split("#")
        volunteer_database_list.append(x)
    volunteer_list_file.close()

    #CHECK THIS!!!!
    current_refugee_id = 1

    open_volunteer_file = open("Final_Files/volunteer_database.txt", 'r')
    volunteer_actual_database_list = []
    for line in open_volunteer_file:
        x = line.split("%")
        volunteer_actual_database_list.append(x)
    open_volunteer_file.close()

    open_camp_file = open("Final_Files/emergency_database.txt", 'r')
    camp_database_list = []
    for line in open_camp_file:
        x = line.split("%")
        camp_database_list.append(x)
    open_camp_file.close()

    open_accommodation_file = open("Final_Files/accommodation_database.txt", 'r')
    accommodation_database_list = []
    for line in open_accommodation_file:
        x = line.split(",")
        accommodation_database_list.append(x)
    open_accommodation_file.close()

    open_medical_file = open("Final_Files/medical_database.txt", 'r')
    medical_database_list = []
    for line in open_medical_file:
        x = line.split(",")
        medical_database_list.append(x)
    open_medical_file.close()

    open_toilet_file = open("Final_Files/toilet_database.txt", 'r')
    toilet_database_list = []
    for line in open_toilet_file:
        x = line.split(",")
        toilet_database_list.append(x)
    open_toilet_file.close()

    open_ration_file = open("Final_Files/ration_database.txt", 'r')
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
    CAMP_COLUMN_NUM = 0
    CURRENT_VOLUNTEER_INDEX = 1
    print(volunteer_actual_database_list[CURRENT_VOLUNTEER_INDEX][2])
    def save_to_file():

        # GET ALL THE VALUES ENTERED ON THE FORM
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

        # CHECKING FOR ERRORS IN NAME
        if name == "" or name == "Enter refugee name...":
            tkinter.messagebox.showerror(title='Error!', message='Name cannot be empty')
            return

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

        # CHECKING FOR ERRORS IN NO. OF FAMILY MEMBERS

        if number == "" or number == "Enter no. of family members...":
            tkinter.messagebox.showerror(title='Error!', message='Number of family members cannot be empty')
            return

        if any(i.isalpha() for i in number):
            tkinter.messagebox.showerror(title='Error!',
                                         message='No. of family members cannot have alphabetical characters')
            return

        try:
            int(number)
        except ValueError:
            tkinter.messagebox.showerror(title='Error!',
                                         message='No. of family members cannot have special characters!')
            return

        if int(number) > 20:
            tkinter.messagebox.showerror(title='Error!', message='Maximum of 20 family members allowed')
            return
        if int(number) < 0:
            tkinter.messagebox.showerror(title='Error!', message='There is a minimum of value of 0')
            return

        # CHECK THAT SEX ISN'T EMPTY

        if sex == "":
            tkinter.messagebox.showerror(title='Error!', message='Sex cannot be empty')
            return

        # DOB CHECKS
        dob_datetime = datetime.datetime.strptime(refugee_dob_calendar.get_date(), "%d/%m/%Y")
        today_checktime = datetime.datetime.today()

        if today_checktime.year == dob_datetime.year and today_checktime.month == dob_datetime.month:
            if int(today_checktime.day - dob_datetime.day) < 6:
                tkinter.messagebox.showerror(title='Error!', message='Refugee must be more than 5 days old!')
                return

        # CHECKS ADDRESS LINE 1
        if first_address.isnumeric():
            tkinter.messagebox.showerror(title='Error!', message='Address cannot be fully numeric')
            return
        if len(first_address) > 100:
            tkinter.messagebox.showerror(title='Error!', message='Address must be shorter than 100 characters')
            return

        if first_address != "" or first_address != "Address Line 1":
            for i in first_address:
                if i.isalnum() != True and i != " ":
                    tkinter.messagebox.showerror(title='Error!',
                                                 message='Unrecognised symbol in Address Line 1')
                    return

        # CHECK FOR ERRORS IN CITY NAME
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
                if i.isalnum() != True and i != " " and i != "/":
                    tkinter.messagebox.showerror(title='Error!', message='Unrecognised symbol in town/city')
                    return

        # CHECKS FOR ERRORS IN POSTCODE
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

        # CHECK FOR ERRORS IN CHECKBOX
        check_box_1 = refugee_weight.get()
        check_box_2 = refugee_weight_2.get()
        if (check_box_1 == 0 and check_box_2 == 0) or (check_box_1 == 0 and check_box_2 == 2) or (
                check_box_1 == 2 and check_box_2 == 0) or (check_box_1 == 2 and check_box_2 == 2):
            tkinter.messagebox.showerror(title='Error!', message='You must select a medical conditions box')
            return

        # IF THEY TICK CONDITIONS
        # CHECKS FOR ERRORS IN CONDITIONS
        if check_box_1 == 1:
            if conditions == '' or conditions == 'Enter all relevant medical conditions...':
                tkinter.messagebox.showerror(title='Error!', message='Please specify your condition(s)')
                return
            if len(conditions) < 2:
                tkinter.messagebox.showerror(title='Error!', message='Too short, please add more detail')
                return
            if len(conditions) > 300:
                tkinter.messagebox.showerror(title='Error!',
                                             message='Condition list too long! Please shorten it')
                return
            if refugee_family_medical_no.get() == '':
                tkinter.messagebox.showerror(title='Error!',
                                             message='Please specify how many family members have conditions')
                return

        # CHECK IF THERE IS ENOUGH SPACE IN THE CAMP
        # KINDA SEPARATE SECTION BUT STILL IN THE VALIDATION PART

        # SEES WHICH CAMP THE VOLUNTEER IS CURRENTLY ASSIGNED TO
        volunteer_current_camp_id = int(volunteer_actual_database_list[CURRENT_VOLUNTEER_INDEX][CAMP_COLUMN_NUM])

        # ACCOMMODATION: GET SPECIFIC LIST WITH ONLY ACCOMMODATION IN VOLUNTEER CAMP
        accommodation_specific_camp_list_test = []
        for i in range(len(accommodation_database_list)):
            if int(accommodation_database_list[i][0]) == int(volunteer_current_camp_id):
                accommodation_specific_camp_list_test.append(accommodation_database_list[i])

        # MEDICAL: GET SPECIFIC LIST WITH ONLY MEDICAL IN VOLUNTEER CAMP
        medical_specific_camp_list_test = []
        for i in range(len(medical_database_list)):
            if int(medical_database_list[i][0]) == int(volunteer_current_camp_id):
                medical_specific_camp_list_test.append(medical_database_list[i])

        # TOILET: GET SPECIFIC LIST WITH ONLY TOILET IN VOLUNTEER CAMP
        toilet_specific_camp_list_test = []
        for i in range(len(toilet_database_list)):
            if int(toilet_database_list[i][0]) == int(volunteer_current_camp_id):
                toilet_specific_camp_list_test.append(toilet_database_list[i])

        # RATIONS: GET SPECIFIC LIST WITH ONLY RATIONS IN VOLUNTEER CAMP
        rations_specific_camp_list_test = []
        for i in range(len(ration_database_list)):
            if int(ration_database_list[i][0]) == int(volunteer_current_camp_id):
                rations_specific_camp_list_test.append(ration_database_list[i])

        print(accommodation_specific_camp_list_test)
        print(medical_specific_camp_list_test)
        print(toilet_specific_camp_list_test)
        print(rations_specific_camp_list_test)

        total_lol = int(number) + 1

        check_box_1 = refugee_weight.get()
        check_box_2 = refugee_weight_2.get()
        if (check_box_1 == 0 and check_box_2 == 1) or (check_box_1 == 2 and check_box_2 == 1):
            num_medical_check = 0
        else:
            num_medical_check = (int(refugee_family_medical_no.get()))

        # ITERATE THROUGH LIST AND SEE IF WE CAN ADD FAMILY TO CAMP
        # IF NOT, ERROR MESSAGE WILL POP UP AND SAY TO REDUCE FAM SIZE OR CONTACT ADMIN

        if len(accommodation_specific_camp_list_test) > 0:
            for i in range(len(accommodation_specific_camp_list_test)):
                if int(accommodation_specific_camp_list_test[i][6]) >= int(total_lol):
                    if int(medical_specific_camp_list_test[i][6]) >= (num_medical_check):
                        if int(toilet_specific_camp_list_test[i][6]) >= int(total_lol):
                            if int(rations_specific_camp_list_test[i][6]) >= int(total_lol):
                                break
                            else:
                                tkinter.messagebox.showerror(title='Error!',
                                                             message='Not enough space in this camp for rations! Change number of family members or contact the admin')
                                return
                        else:
                            tkinter.messagebox.showerror(title='Error!',
                                                         message='Not enough space in this camp for toilets! Change number of family members or contact the admin')
                            return

                    else:
                        tkinter.messagebox.showerror(title='Error!',
                                                     message='Not enough space in this camp for medical! Change number of family members with conditions or contact the admin')
                        return

                else:
                    tkinter.messagebox.showerror(title='Error!',
                                                 message='Not enough space in this camp for accommodation! Change number of family members or contact the admin')
                    return
        else:
            tkinter.messagebox.showerror(title='Error!',
                                         message='Not enough space in this camp for accommodation! Change number of family members or contact the admin')
            return
        success()



    def delete2():
        screen2.destroy()

    def delete0():
        screen.destroy()

    def delete3():
        screen3.destroy()

    def calculate_age(birthdate):

        today = datetime.datetime.today()
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

        if len(name) == 0 or name == "Enter refugee name...":
            namestatus.config(text="Name cannot be 0", font='Arial 12', fg='red')

        else:
            try:
                if len(name) <= 2:
                    namestatus.config(text="Name too short!", font='Arial 12', fg='red')

                elif any(i.isdigit() for i in name):
                    namestatus.config(text="Name can't be numeric!", font='Arial 12', fg='red')

                elif name.count(" ") > 3:
                    namestatus.config(text="Please enter less than 4 separate names", font='Arial 12', fg='red')

                else:
                    namestatus.config(text="Valid :)", font='Arial 12', fg='green')
            except:
                pass
        return True

    def finish_message():
        global screen3
        screen3 = tkinter.Tk()
        screen3.geometry("300x120")
        screen3.title("Success!")
        finish_message_text = tkinter.Label(screen3, text="Successfully added new refugee!", fg='green')
        finish_message_text.place(x=40, y=40)
        close_button = tkinter.Button(screen3, text="I understand", command=delete3)
        close_button.place(x=95, y=80)

    def submit():
        # Creating new refugee
        new_refugee = [""] * 16

        # Finding index for new refugee
        if len(volunteer_database_list) == 0:
            new_refugee[0] = "1"
        elif len(volunteer_database_list) >= 1:
            new_refugee[0] = str((int((volunteer_database_list[-1])[0]) + 1))

        # GET ALL VALUES
        name = refugee_name.get()
        number = refugee_number.get()
        dob = refugee_dob_calendar.get_date()
        age = str(calculate_age(datetime.datetime.strptime(refugee_dob_calendar.get_date(), "%d/%m/%Y")))
        sex = refugee_sex.get()
        num_of_fam = refugee_family_medical_no.get()
        if int(num_of_fam) == 0:
            num_of_fam = 'None'

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

        conditions = refugee_height.get()
        if conditions == 'Enter all relevant medical conditions...' or conditions == 'Enter any medical conditions...':
            conditions = 'None'

        new_rewritten_database_temp = return_list_for_database[0]
        new_rewritten_database_temp_medic = return_list_for_database[1]
        new_rewritten_database_temp_toilet = return_list_for_database[2]
        new_rewritten_database_temp_ration = return_list_for_database[3]

        accommodations_write_new = open("accommodationstestlol.txt", "w")
        for i in range(len(new_rewritten_database_temp)):
            accommodations_write_new.write(new_rewritten_database_temp[i])
        accommodations_write_new.close()

        medical_write_new = open("medical.txt", "w")
        for i in range(len(new_rewritten_database_temp_medic)):
            medical_write_new.write(new_rewritten_database_temp_medic[i])
        medical_write_new.close()

        toilets_write_new = open("toilets.txt", "w")
        for i in range(len(new_rewritten_database_temp_toilet)):
            toilets_write_new.write(new_rewritten_database_temp_toilet[i])
        toilets_write_new.close()

        rations_write_new = open("ration_stall.txt", "w")
        for i in range(len(new_rewritten_database_temp_ration)):
            rations_write_new.write(new_rewritten_database_temp_ration[i])
        rations_write_new.close()

        # STORE ALL VALUES INTO LIST
        new_refugee[1] = name
        new_refugee[2] = number
        new_refugee[3] = dob
        new_refugee[4] = age
        new_refugee[5] = sex
        new_refugee[6] = address
        new_refugee[7] = str(conditions)
        new_refugee[8] = str(num_of_fam)
        new_refugee[9] = str(return_list_for_database[4])
        new_refugee[10] = str(return_list_for_database[5])
        new_refugee[11] = str(return_list_for_database[6])
        new_refugee[12] = str(return_list_for_database[7])
        new_refugee[13] = str(return_list_for_database[8])
        new_refugee[14] = str(return_list_for_database[9])
        new_refugee[15] = str(return_list_for_database[10])
        new_refugee_string = "#".join(new_refugee)
        volunteer_list_file.close()
        volunteer_list_file_append = open("Refugee_Database", "a")
        volunteer_list_file_append.write("\n%s" % (new_refugee_string))
        volunteer_list_file_append.close()

        # DISPLAY FINISH MESSAGE AND DELETE SCREENS
        delete2()
        finish_message()
        delete0()

    def add_camp():
        # SEES WHICH CAMP THE VOLUNTEER IS CURRENTLY ASSIGNED TO
        volunteer_current_camp = int(volunteer_actual_database_list[CURRENT_VOLUNTEER_INDEX][0])

        # GET LIST OF ONLY CAMP NAMES FROM EMERGENCY DATABASE
        camp_name_list = []
        for i in range(len(camp_database_list)):
            camp_name_list.append([camp_database_list[i][0], camp_database_list[i][0]])

        # FUNCTION TO FIND WHICH THEIR CURRENT CAMP NAME IS
        # DO IT BY COMPARING CAMP ID IN EMERGENCY DATABASE TO CAMP ID IN VOLUNTEER FILE
        current_camp_name = ''
        for i in range(len(camp_name_list)):
            if int(camp_name_list[i][0]) == int(volunteer_current_camp):
                current_camp_name = camp_name_list[i][1]
                break

        # OUTPUTS WHICH CAMP THE REFUGEE IS PLACED IN
        volunteer_current_camp_label = tkinter.Label(screen2,
                                                     text="Your refugee will be placed in your camp: %s" % current_camp_name)
        volunteer_current_camp_label.pack()

        # ACCOMMODATION: GET SPECIFIC LIST WITH ONLY ACCOMMODATION
        accommodation_specific_camp_list = []
        for i in range(len(accommodation_database_list)):
            if int(accommodation_database_list[i][0]) == int(volunteer_current_camp):
                accommodation_specific_camp_list.append(accommodation_database_list[i])

        # ITERATE THROUGH LIST AND SEE WHICH ACCOMMODATION IS FREE
        refugee_assigned_accommodation = ''
        for i in range(len(accommodation_specific_camp_list)):
            # ONCE FREE ACCOMMODATION IDENTIFIED, ADD IT TO A LIST "THAT_BLOCK_LIST"
            if int(accommodation_specific_camp_list[i][6]) >= (int(refugee_number.get()) + 1):
                refugee_assigned_accommodation = accommodation_specific_camp_list[i][2]
                refugee_assigned_block = accommodation_specific_camp_list[i][7]
                that_block_list = accommodation_specific_camp_list[i]
                xhaha = str(int(that_block_list[4]) + (int(refugee_number.get()) + 1))
                yhaha = str(int(that_block_list[6]) - (int(refugee_number.get()) + 1))
                that_block_list[4] = xhaha
                that_block_list[6] = yhaha

                # FIND INDEX OF BLOCK IN ORIGINAL LIST AND UPDATE IT WITH NEW LIST WITH NEW VALUES
                for j in range(len(accommodation_database_list)):
                    if accommodation_database_list[j][0] == that_block_list[0] and \
                            accommodation_database_list[j][1] == that_block_list[1]:
                        accommodation_database_list[j] = that_block_list

                # CREATE LIST OF STRINGS FROM LIST OF LISTS
                new_rewritten_database_temp = []
                for i in accommodation_database_list:
                    new_rewritten_database_temp.append(','.join(i))

                # WRITE NEW LIST INTO ACCOMMODATION TEXT FILE

                break
        volunteer_current_wing_label = tkinter.Label(screen2,
                                                     text="Your refugee will be in the: %s" % that_block_list[
                                                         7])
        volunteer_current_wing_label.pack()
        # OUTPUT WHHICH BLOCK THEY ARE IN
        refugee_assigned_accommodation_label = tkinter.Label(screen2,
                                                             text='Your refugee accommodation will be in: %s' % (
                                                                 refugee_assigned_accommodation))
        refugee_assigned_accommodation_label.pack()

        # MEDICAL
        # CREATE LIST WITH MEDICAL STALLS THAT ARE IN THE SAME CAMP AND IN THE SAME WING
        medical_specific_camp_list = []
        for i in range(len(medical_database_list)):
            if int(medical_database_list[i][0]) == int(volunteer_current_camp) and medical_database_list[i][
                7] == refugee_assigned_block:
                medical_specific_camp_list.append(medical_database_list[i])

        # ITERATE THROUGH LIST TO SEE WHICH ONE IS FREE
        # IF NONE, IT WILL SAY "NO BLOCKS AVAILABLE"
        refugee_assigned_medical = 'No blocks available!'
        total_lol = int(refugee_number.get()) + 1

        check_box_1 = refugee_weight.get()
        check_box_2 = refugee_weight_2.get()
        if (check_box_1 == 0 and check_box_2 == 1) or (check_box_1 == 2 and check_box_2 == 1):
            num_medical_check = 0
        else:
            num_medical_check = (int(refugee_family_medical_no.get()))
        for i in range(len(medical_specific_camp_list)):

            # FIND MEDICAL STALL THAT IS GREATER THAN NO. OF PEOPLE IN FAMILY WITH MEDICAL CONDITIONS
            if int(medical_specific_camp_list[i][6]) >= num_medical_check:
                refugee_assigned_medical = medical_specific_camp_list[i][2]

                # CREATE NEW SPECIFIC LIST WITH NEW VALUES
                that_medic_list = medical_specific_camp_list[i]
                ahaha = str(int(that_medic_list[4]) + (int(refugee_family_medical_no.get())))
                bhaha = str(int(that_medic_list[6]) - (int(refugee_family_medical_no.get())))
                that_medic_list[4] = ahaha
                that_medic_list[6] = bhaha

                # APPEND NEW LIST INTO THE LIST OF LISTS (OF MEDICAL STALLS)
                for j in range(len(medical_database_list)):
                    if medical_database_list[j][0] == that_medic_list[0] and medical_database_list[j][1] == \
                            that_medic_list[1]:
                        medical_database_list[j] = that_medic_list

                # TURN LIST OF LISTS INTO LIST OF STRINGS
                new_rewritten_database_temp_medic = []
                for i in medical_database_list:
                    new_rewritten_database_temp_medic.append(','.join(i))

                # WRITE DATA INTO DATABASE

                break

        # OUTPUT WHICH MEDICAL STALL THEY WILL BE PUT INTO
        refugee_assigned_medical_label = tkinter.Label(screen2,
                                                       text='Your refugee medical stall will be in: %s' % refugee_assigned_medical)
        refugee_assigned_medical_label.pack()

        # TOILETS
        # CREATE LIST WITH TOILET STALLS SPECIFIC TO THE CAMP AND WING THEY ARE IN
        toilet_specific_camp_list = []
        for i in range(len(toilet_database_list)):
            if int(toilet_database_list[i][0]) == int(volunteer_current_camp) and toilet_database_list[i][
                7] == refugee_assigned_block:
                toilet_specific_camp_list.append(toilet_database_list[i])

        # ITERATE THROUGH LIST TO SEE WHICH ONE IS FREE
        # IF NONE, SAY "NO TOILETS AVAILABLE"
        refugee_assigned_toilet = 'No toilets available!'
        for i in range(len(toilet_specific_camp_list)):
            # CHECK IF TOILET SPACE IS GREATER THAN NO OF EXTRA FAMILY MEMBERS
            if int(toilet_specific_camp_list[i][6]) >= int(refugee_number.get()):
                refugee_assigned_toilet = toilet_specific_camp_list[i][2]
                that_toilet_list = toilet_specific_camp_list[i]
                chaha = str(int(that_toilet_list[4]) + (int(refugee_number.get()) + 1))
                dhaha = str(int(that_toilet_list[6]) - (int(refugee_number.get()) + 1))
                that_toilet_list[4] = chaha
                that_toilet_list[6] = dhaha
                print("toilet", that_toilet_list)

                # FIND ORIGINAL LINE IN LIST AND UPDATE IT WITH THE NEW LIST
                for j in range(len(toilet_database_list)):
                    if toilet_database_list[j][0] == that_toilet_list[0] and toilet_database_list[j][1] == \
                            that_toilet_list[1]:
                        toilet_database_list[j] = that_toilet_list

                # TURN LIST OF LISTS INTO LIST OF STRINGS
                new_rewritten_database_temp_toilet = []
                for i in toilet_database_list:
                    new_rewritten_database_temp_toilet.append(','.join(i))

                # WRITE UPDATED TO DATABASE

                break

        # PRINT WHAT TOILET STALL THEY WILL BE IN
        refugee_assigned_toilet_label = tkinter.Label(screen2,
                                                      text='Your refugee toilet stall will be in: %s' % refugee_assigned_toilet)
        refugee_assigned_toilet_label.pack()

        # RATIONS
        # GET SPECIFIC LIST OF RATIONS IN SAME CAMP AND SAME WING
        ration_specific_camp_list = []
        for i in range(len(ration_database_list)):
            if int(ration_database_list[i][0]) == int(volunteer_current_camp) and ration_database_list[i][
                7] == refugee_assigned_block:
                ration_specific_camp_list.append(ration_database_list[i])

        # ITERATE THROUGH LIST TO SEE WHICH ONES AVAILABLE
        # IF NONE AVAILABLE, SAY NO RATIONS AVAILABLE
        refugee_assigned_ration = 'No rations available!'
        for i in range(len(ration_specific_camp_list)):
            if int(ration_specific_camp_list[i][6]) >= int(refugee_number.get()):
                refugee_assigned_ration = ration_specific_camp_list[i][2]
                that_ration_list = ration_specific_camp_list[i]
                ehaha = str(int(that_ration_list[4]) + (int(refugee_number.get()) + 1))
                fhaha = str(int(that_ration_list[6]) - (int(refugee_number.get()) + 1))
                that_ration_list[4] = ehaha
                that_ration_list[6] = fhaha
                print("ration", that_ration_list)

                # FIND ORIGINAL LINE IN LIST AND UPDATE IT WITH THE NEW LIST
                for j in range(len(ration_database_list)):
                    if ration_database_list[j][0] == that_ration_list[0] and ration_database_list[j][1] == \
                            that_ration_list[1]:
                        ration_database_list[j] = that_ration_list

                # TURN LIST OF LISTS INTO LIST OF STRINGS
                new_rewritten_database_temp_ration = []
                for i in ration_database_list:
                    new_rewritten_database_temp_ration.append(','.join(i))

                # WRITE UPDATED TO DATABASE
                break

        # PRINT DESIGNATED LOCATION
        refugee_assigned_ration_label = tkinter.Label(screen2,
                                                      text='Your refugee ration stall will be in: %s' % refugee_assigned_ration)
        refugee_assigned_ration_label.pack()

        return [new_rewritten_database_temp, new_rewritten_database_temp_medic,
                new_rewritten_database_temp_toilet, new_rewritten_database_temp_ration, volunteer_current_camp,
                current_camp_name, that_block_list[7], refugee_assigned_accommodation, refugee_assigned_medical,
                refugee_assigned_toilet, refugee_assigned_ration]

    def success():
        global return_list_for_database
        # SETTING UP SCREEN
        global screen2
        screen2 = tkinter.Toplevel()
        screen2.geometry("500x650")
        screen2.title("Confirm refugee submission")

        # DISPLAYS SUMMED UP INFO
        refugee_confirmation = tkinter.Label(screen2,
                                             text="Please check the summary of details below to add to the database:",
                                             font=('Avenir', 14, 'bold', 'underline'))
        refugee_confirmation.pack(pady=30)

        name_confirmation = tkinter.Label(screen2,
                                          text="The name you are entering is: %s" % (refugee_name.get()))
        name_confirmation.pack()

        number_confirmation = tkinter.Label(screen2,
                                            text="The number of family members is: %s" % refugee_number.get())
        number_confirmation.pack()

        sex_confirmation = tkinter.Label(screen2, text="The sex you are entering is: %s" % refugee_sex.get())
        sex_confirmation.pack()

        dob_confirmation = tkinter.Label(screen2,
                                         text="The date of birth you are entering is: %s" % refugee_dob_calendar.get_date())
        dob_confirmation.pack()

        age_confirmation = tkinter.Label(screen2, text="This means their age is: %s" % str(
            calculate_age(datetime.datetime.strptime(refugee_dob_calendar.get_date(), "%d/%m/%Y"))))
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

        address_confirmation = tkinter.Label(screen2, text="Their address is: %s" % address)
        address_confirmation.pack()

        conditions = refugee_height.get()
        if conditions == 'Enter all relevant medical conditions...' or conditions == 'Enter any medical conditions...':
            conditions = 'None'

        weight_confirmation = tkinter.Label(screen2, text="Your conditions are: %s" % conditions)
        weight_confirmation.pack()

        num_of_fam = refugee_family_medical_no.get()
        if int(num_of_fam) == 0:
            num_of_fam = 'None'
        height_confirmation = tkinter.Label(screen2, text="Number of family members with conditions: %s" % str(
            num_of_fam))
        height_confirmation.pack()

        refugee_camp_confirmation = tkinter.Label(screen2,
                                                  text="Please check the allocations for the refugee below",
                                                  font=('Avenir', 14, 'bold', 'underline'))
        refugee_camp_confirmation.pack(pady=30)

        # RUNNING FUNCTION TO ALLOCATE PEOPLE TO THE CAMPS
        return_list_for_database = add_camp()

        # BUTTON TO SUBMIT
        submit_button = tkinter.Button(screen2, text="Submit", command=submit)
        submit_button.pack(pady=30)
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
        if refugee_number_entry.get() == 'Enter no. of family members...':
            refugee_number_entry.delete(0, "end")  # delete all the text in the entry
            refugee_number_entry.insert(0, '')  # Insert blank for user input
            refugee_number_entry.config(fg='black')

    def refugee_number_off(self):
        if refugee_number_entry.get() == '':
            refugee_number_entry.insert(0, 'Enter no. of family members...')
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
        if refugee_height_entry.get() == 'Enter all relevant medical conditions...':
            refugee_height_entry.delete(0, "end")  # delete all the text in the entry
            refugee_height_entry.insert(0, '')  # Insert blank for user input
            refugee_height_entry.config(fg='black')

    def refugee_height_off(self):
        if refugee_height_entry.get() == '':
            refugee_height_entry.insert(0, 'Enter all relevant medical conditions...')
            refugee_height_entry.config(fg='grey')

    screen = tkinter.Toplevel()
    screen.geometry("500x1000")
    screen.title("Create Refugee Form")
    # screen.configure(background="#A1CDEC")

    # Title text
    intro_text = tkinter.Label(screen, text="Use this section to create a refugee within this Database.", fg='Green',
                               width=300)
    intro_text.place(x=20, y=20)

    # Input from user

    # FORM THAT USER INPUTS
    namestatus = tkinter.Label(screen, text="")
    namestatus.place(x=20, y=50)

    # REFUGEE NAME STUFF
    refugee_name_text = tkinter.Label(screen, text="Refugee name*: ")
    refugee_name_text.place(x=20, y=30)
    refugee_name = tkinter.StringVar()
    refugee_name_entry = tkinter.Entry(screen, validate='all', validatecommand=name_validate,
                                       textvariable=refugee_name)
    refugee_name_entry.insert(0, 'Enter refugee name...')
    refugee_name_entry.bind('<FocusIn>', refugee_text_on)
    refugee_name_entry.bind('<FocusOut>', refugee_text_off)
    refugee_name_entry.config(fg='grey')

    refugee_name_entry.place(x=175, y=30, width=300)

    # REFUGEE NO. OF FAMILY MEMBERS STUFF
    numberstatus = tkinter.Label(screen, text="")
    numberstatus.place(x=20, y=120)
    refugee_number_text = tkinter.Label(screen, text="No. of family members*:")
    refugee_number_text.place(x=20, y=100)
    refugee_number_text_2 = tkinter.Label(screen, text="(Not including you)", font='Arial 12',
                                          fg='grey')
    refugee_number_text_2.place(x=20, y=120)
    refugee_number = tkinter.StringVar(value='')
    refugee_number_entry = tkinter.Spinbox(screen, textvariable=refugee_number)
    refugee_number_entry.insert(0, 'Enter no. of family members...')
    refugee_number_entry.bind('<FocusIn>', refugee_number_on)
    refugee_number_entry.bind('<FocusOut>', refugee_number_off)
    refugee_number_entry.config(fg='grey')
    refugee_number_entry.place(x=175, y=100, width=300)

    # REFUGEE SEX STUFF
    refugee_sex_text = tkinter.Label(screen, text="Sex*:")
    refugee_sex_text.place(x=20, y=170)
    refugee_sex = tkinter.StringVar()
    refugee_sex_entry = tkinter.Entry(textvariable=refugee_sex)
    refugee_sex_entry.place(x = 175, y = 170, width=300)
    drop = tkinter.OptionMenu(screen, refugee_sex, "Male", "Female", "Prefer not to say")
    drop.place(x=175, y=170, width=300)

    # REFUGEE DOB STUFF
    refugee_dob_text = tkinter.Label(screen, text="Date of Birth*: ")
    refugee_dob_text.place(x=20, y=220)
    today = datetime.date.today()
    max = datetime.date(1904, 2, 11)
    # max is oldest person alive!
    refugee_dob_calendar = tkcalendar.Calendar(screen, date_pattern="d/m/y", selectmode='day',
                                               font='Arial 12', foreground='black', maxdate=today,
                                               mindate=max)
    refugee_dob_calendar.place(x=190, y=220)

    # REFUGEE ADDRESS STUFF
    refugee_address_text = tkinter.Label(screen, text="Address:")
    refugee_address_text.place(x=20, y=420)
    refugee_address_text_2 = tkinter.Label(screen, text="(Not required)", font='Arial 12',
                                          fg='grey')
    refugee_address_text_2.place(x=20, y=440)


    refugee_first_address = tkinter.StringVar()
    refugee_first_address_entry = tkinter.Entry(screen, textvariable=refugee_first_address)
    refugee_first_address_entry.insert(0, 'Address Line 1')
    refugee_first_address_entry.bind('<FocusIn>', refugee_first_address_on)
    refugee_first_address_entry.bind('<FocusOut>', refugee_first_address_off)
    refugee_first_address_entry.config(fg='grey')
    refugee_first_address_entry.place(x=175, y=420, width=300)

    refugee_city_address = tkinter.StringVar()
    refugee_city_address_entry = tkinter.Entry(screen, textvariable=refugee_city_address)
    refugee_city_address_entry.insert(0, 'Town/City')
    refugee_city_address_entry.bind('<FocusIn>', refugee_city_address_on)
    refugee_city_address_entry.bind('<FocusOut>', refugee_city_address_off)
    refugee_city_address_entry.config(fg='grey')
    refugee_city_address_entry.place(x=175, y=450, width=150)

    refugee_postcode_address = tkinter.StringVar()
    refugee_postcode_address_entry = tkinter.Entry(screen, textvariable=refugee_postcode_address)
    refugee_postcode_address_entry.insert(0, 'Postcode')
    refugee_postcode_address_entry.bind('<FocusIn>', refugee_postcode_address_on)
    refugee_postcode_address_entry.bind('<FocusOut>', refugee_postcode_address_off)
    refugee_postcode_address_entry.config(fg='grey')
    refugee_postcode_address_entry.place(x=325, y=450, width=150)

    refugee_country_address = tkinter.StringVar()
    refugee_country_address_entry = tkinter.OptionMenu(screen, refugee_country_address, *country_list)
    refugee_country_address_entry.place(x=175, y=480, width=300)

    # FUNCTION TO DISPLAY INPUT BOX WHEN THEY CLICK YES TO MEDICAL CONDITIONS
    global refugee_height
    refugee_height = tkinter.StringVar(value=0)
    global refugee_family_medical_no
    refugee_family_medical_no = tkinter.StringVar(value=0)


    def clickYes():
        global refugee_height
        global refugee_height_entry
        global refugee_family_medical_no
        refugee_height = tkinter.StringVar()
        refugee_family_medical_no = tkinter.StringVar()
        refugee_fam_num = refugee_number.get()
        if refugee_fam_num == '' or refugee_fam_num == 'Enter no. of family members...':
            refugee_fam_num = 0
        else:
            try:
                refugee_fam_num = int(refugee_fam_num)
            except:
                tkinter.messagebox.showerror(title = 'Error!', message='Please ensure no. of family members is positive')
                return

        if refugee_weight.get() == 1:
            refugee_weight_entry_2.config(state='disabled')
            refugee_height_text = tkinter.Label(screen, text="Conditions:*")
            refugee_height_text.place(x=60, y=600)
            refugee_height_entry = tkinter.Entry(screen, textvariable=refugee_height)
            refugee_height_entry.insert(0, 'Enter all relevant medical conditions...')
            refugee_height_entry.bind('<FocusIn>', refugee_height_on)
            refugee_height_entry.bind('<FocusOut>', refugee_height_off)
            refugee_height_entry.config(fg='grey')
            refugee_height_entry.place(x=175, y=600, width=300)
            refugee_family_medical_no_label = tkinter.Label(screen, text="How many family members\n have conditions (inc. yourself):*")
            refugee_family_medical_no_label.place(x=20, y=640)


            refugee_family_num = []
            if int(refugee_fam_num) > 0:
                for i in range(0, int(refugee_fam_num) + 1):
                    refugee_family_num.append(i)
                refugee_family_medical_no_option = tkinter.OptionMenu(screen, refugee_family_medical_no,
                                                                      *refugee_family_num)
                refugee_family_medical_no_option.place(x=300, y=650)

            elif int(refugee_fam_num) == 0:
                refugee_fam_num = 1
                refugee_family_medical_no_option = tkinter.OptionMenu(screen, refugee_family_medical_no,
                                                                      int(refugee_fam_num))
                refugee_family_medical_no_option.place(x=300, y=650)

        else:
            refugee_height.set('Enter any medical conditions...')
            refugee_weight_entry_2.config(state='normal')
            hehe_label = tkinter.Label(screen, text='')
            hehe_label.place(x=15, y=580, width=800, height=40)
            hehe_label = tkinter.Label(screen, text='')
            hehe_label.place(x=15, y=620, width=800, height=100)

    # FUNCTION TO ERASE ANY INFO/DO NOTHING IF NO IS CLICKED
    def clickNo():
        global refugee_height
        refugee_height = tkinter.StringVar()
        global refugee_family_medical_no
        refugee_family_medical_no = tkinter.StringVar(value=0)
        if refugee_weight_2.get() == 1:
            refugee_height.set('Enter any medical conditions...')
            refugee_weight_entry.config(state='disabled')
            lol_label = tkinter.Label(screen, text='')
            lol_label.place(x=15, y=580, width=800, height=40)
            lol_label = tkinter.Label(screen, text='')
            lol_label.place(x=15, y=620, width=800, height=100)
        else:
            refugee_height.set('Enter any medical conditions...')
            refugee_weight_entry.config(state='normal')

    # MEDICAL CONDITIONS CHECKBOX
    refugee_weight_text = tkinter.Label(screen, text="Do you or your family have\n any medical conditions?*")
    refugee_weight_text.place(x=20, y=540)
    refugee_weight = tkinter.IntVar()
    refugee_weight_2 = tkinter.IntVar()

    refugee_weight_entry = tkinter.Checkbutton(screen, variable=refugee_weight, onvalue=1, offvalue=2,
                                               text="Yes", command=clickYes)
    refugee_weight_entry_2 = tkinter.Checkbutton(screen, variable=refugee_weight_2, onvalue=1,
                                                 offvalue=2,
                                                 text="No", command=clickNo)


    refugee_weight_entry.place(x=300, y=540)
    refugee_weight_entry_2.place(x=300, y=560)

    # BUTTON TO SUBMIT THE FORM
    submit_button = tkinter.Button(screen, text="Submit the form", width=30, command=save_to_file)
    submit_button.place(x=100, y=720)

    screen.mainloop()

