from tkinter import *
import datetime
import tkcalendar
import tkinter.messagebox
import tkinter.ttk


def create_family():
    import Volunteer_Home
    # Opening current database and reading it into a list
    volunteer_list_file = open("refugee_database.txt", "r")
    volunteer_database_list = []
    for line in volunteer_list_file:
        x = line.split("%")
        volunteer_database_list.append(x)
    volunteer_list_file.close()


    open_volunteer_file = open("volunteer_database.txt", 'r')
    volunteer_actual_database_list = []
    for line in open_volunteer_file:
        x = line.split("%")
        volunteer_actual_database_list.append(x)
    open_volunteer_file.close()

    open_camp_file = open("emergency_database.txt", 'r')
    camp_database_list = []
    for line in open_camp_file:
        x = line.split("%")
        camp_database_list.append(x)
    open_camp_file.close()

    open_accommodation_file = open("accommodation_database.txt", 'r')
    accommodation_database_list = []
    for line in open_accommodation_file:
        x = line.split(",")
        accommodation_database_list.append(x)
    open_accommodation_file.close()

    open_medical_file = open("medical_database.txt", 'r')
    medical_database_list = []
    for line in open_medical_file:
        x = line.split(",")
        medical_database_list.append(x)
    open_medical_file.close()

    open_toilet_file = open("toilet_database.txt", 'r')
    toilet_database_list = []
    for line in open_toilet_file:
        x = line.split(",")
        toilet_database_list.append(x)
    open_toilet_file.close()

    open_ration_file = open("ration_database.txt", 'r')
    ration_database_list = []
    for line in open_ration_file:
        x = line.split(",")
        ration_database_list.append(x)
    open_ration_file.close()

    open_accommodation_write = open("accommodation_database.txt", "r")
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
    def save_to_file():

        # GET ALL THE VALUES ENTERED ON THE FORM
        name = refugee_name.get().strip()
        number = refugee_number.get().strip()
        sex = refugee_sex.get()

        ref_year = refugee_year.get()
        ref_month = refugee_month.get()
        ref_day = refugee_day.get()

        try:
            ref_year = int(ref_year)
        except:
            tkinter.messagebox.showerror(title='Error!', message='Year must be numeric!')
            return
        try:
            ref_day = int(ref_day)
        except:
            tkinter.messagebox.showerror(title='Error!', message='Day must be numeric!')
            return

        today_checktime = datetime.datetime.today()


        if ref_year not in year_list:
            tkinter.messagebox.showerror(title='Error!', message='Please select valid year')
            return
        if ref_month not in month_list:
            tkinter.messagebox.showerror(title='Error!', message='Please select valid month')
            return
        if ref_day not in day_list:
            tkinter.messagebox.showerror(title='Error!', message='Please select valid day')
            return



        ref_dob_list = ','.join([str(ref_day), str(ref_month), str(ref_year)])
        refugee_dob_calendar = datetime.datetime.strptime(ref_dob_list, '%d,%B,%Y')

        dob_datetime = refugee_dob_calendar

        if today_checktime.year == dob_datetime.year and today_checktime.month == dob_datetime.month:
            if int(today_checktime.day - dob_datetime.day) < 6:
                tkinter.messagebox.showerror(title='Error!', message='Refugee must be more than 5 days old!')
                return

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

        if sex == "" or sex == "Select or type your sex...":
            tkinter.messagebox.showerror(title='Error!', message='Sex cannot be empty')
            return

        if sex != "Male" and sex != "Female" and sex != "Prefer not to say":
            tkinter.messagebox.showerror(title='Error!', message='Sex must be "Male", "Female", or "Prefer not to say"')
            return

        # DOB CHECKS

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

        #CHECK FOR ERRORS IN COUNTRY
        if country_address != "" and country_address != "Use dropdown or type to select country...":
            if country_address.count(" ") > 3:
                tkinter.messagebox.showerror(title='Error!', message='Country cannot have more than 3 words')
                return

            if country_address.isnumeric():
                tkinter.messagebox.showerror(title='Error!', message='Country address cannot be numeric')
                return

            if any(i.isnumeric() for i in country_address):
                tkinter.messagebox.showerror(title='Error!', message='Country cannot have numerical characters')
                return


            for i in country_address:
                if i.isalnum() != True and i != " " and i != ".":
                    tkinter.messagebox.showerror(title='Error!', message='Unrecognised symbol in country')
                    return

            country_address = country_address.lower()
            country_address = country_address.capitalize()

            if country_address not in country_list:
                tkinter.messagebox.showerror(title='Error!', message='Country not in list! Please use dropdown menu to select')
                return

        address_list = [first_address, city_address, postcode_address, country_address]


        # CHECK FOR ERRORS IN CHECKBOX


        # IF THEY TICK CONDITIONS
        # CHECKS FOR ERRORS IN CONDITIONS

        if conditions != '' and conditions != 'Enter all relevant medical conditions...':

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



        if no_fam_conditions != "":

            if any(i.isalpha() for i in no_fam_conditions):
                tkinter.messagebox.showerror(title='Error!',
                                             message='No. of family members with conditions cannot have alphabetical characters')
                return

            try:
                int(no_fam_conditions)
            except ValueError:
                tkinter.messagebox.showerror(title='Error!',
                                             message='No. of family members with conditions cannot have special characters!')
                return


            if int(no_fam_conditions) < 1:
                tkinter.messagebox.showerror(title='Error!', message='There is a minimum of value of 1!')
                return

            if int(no_fam_conditions) > 20:
                tkinter.messagebox.showerror(title='Error!', message='There is a maximum of value of 20!')
                return

            if int(no_fam_conditions) > (int(number) + 1):
                tkinter.messagebox.showerror(title='Error!', message='Number of people with conditions cannot be greater than total number of people!')
                return



        # CHECK IF THERE IS ENOUGH SPACE IN THE CAMP
        # KINDA SEPARATE SECTION BUT STILL IN THE VALIDATION PART

        # SEES WHICH CAMP THE VOLUNTEER IS CURRENTLY ASSIGNED TO
        volunteer_current_camp_id = int(volunteer_actual_database_list[int(Volunteer_Home.user_id) - 1][CAMP_COLUMN_NUM])

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



        try:
            int(refugee_family_medical_no.get())
            num_medical_check = int(refugee_family_medical_no.get())
        except:
            num_medical_check = 0

        # ITERATE THROUGH LIST AND SEE IF WE CAN ADD FAMILY TO CAMP
        # IF NOT, ERROR MESSAGE WILL POP UP AND SAY TO REDUCE FAM SIZE OR CONTACT ADMIN


        var_accom_counter = 0
        var_medical_counter = 0
        var_toilet_counter = 0
        var_ration_counter = 0
        total_lol = int(refugee_number.get())+1

        if len(accommodation_specific_camp_list_test) > 0:
            for i in range(len(accommodation_specific_camp_list_test)):
                if int(accommodation_specific_camp_list_test[i][6]) >= int(total_lol):
                    var_accom_counter = var_accom_counter + 1

            for i in range(len(medical_specific_camp_list_test)):
                if int(medical_specific_camp_list_test[i][6]) >= (num_medical_check):
                    var_medical_counter = var_medical_counter + 1

            for i in range(len(toilet_specific_camp_list_test)):
                if int(toilet_specific_camp_list_test[i][6]) >= int(total_lol):
                    var_toilet_counter = var_toilet_counter + 1

            for i in range(len(rations_specific_camp_list_test)):
                if int(rations_specific_camp_list_test[i][6]) >= int(total_lol):
                    var_ration_counter = var_ration_counter + 1

            if var_accom_counter < 1:
                tkinter.messagebox.showerror(title='Error!',
                                             message='Not enough space in this camp for accommodation! Change number of family members or contact the admin')
                return

            if var_medical_counter < 1:
                tkinter.messagebox.showerror(title='Error!',
                                             message='Not enough space in this camp for medical! Change number of family members with conditions or contact the admin')
                return

            if var_toilet_counter < 1:
                tkinter.messagebox.showerror(title='Error!',
                                             message='Not enough space in this camp for toilets! Change number of family members or contact the admin')
                return

            if var_ration_counter < 1:
                tkinter.messagebox.showerror(title='Error!',
                                             message='Not enough space in this camp for rations! Change number of family members or contact the admin')
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
        screen3 = Tk()
        screen3.geometry("300x120")
        screen3.title("Success!")
        finish_message_text = Label(screen3, text="Successfully added new refugee!", fg='green')
        finish_message_text.place(x=40, y=40)
        close_button = Button(screen3, text="I understand", command=delete3)
        close_button.place(x=95, y=80)

    def submit():
        # Creating new refugee
        new_refugee = [""] * 18

        # Finding index for new refugee
        if len(volunteer_database_list) == 0:
            new_refugee[1] = "1"
        elif len(volunteer_database_list) >= 1:
            new_refugee[1] = str((int((volunteer_database_list[-1])[1]) + 1))
        name = refugee_name.get().strip()
        number = refugee_number.get().strip()
        sex = refugee_sex.get()

        ref_year = refugee_year.get()
        ref_month = refugee_month.get()
        ref_day = refugee_day.get()

        ref_year = int(ref_year)
        ref_day = int(ref_day)

        ref_dob_list = ','.join([str(ref_day), str(ref_month), str(ref_year)])
        refugee_dob_calendar = datetime.datetime.strptime(ref_dob_list, '%d,%B,%Y')
        refugee_dob_calendar_string = refugee_dob_calendar.strftime("%d,%m,%Y")

        # GET ALL VALUES
        name = refugee_name.get()
        number = refugee_number.get()
        dob = refugee_dob_calendar_string
        age = str(calculate_age(refugee_dob_calendar))
        sex = refugee_sex.get()

        try:
            num_of_fam = refugee_family_medical_no.get()
            num_of_fam = int(num_of_fam)
        except:
            num_of_fam = 0

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
        if country_address == 'Use dropdown or type to select country...':
            country_address = ''

        address_list = [first_address, city_address, postcode_address, country_address]
        address = ', '.join(address_list)

        conditions = refugee_height.get()
        if conditions == 'Enter all relevant medical conditions...' or conditions == 'Enter any medical conditions...':
            conditions = 'None'

        new_rewritten_database_temp = return_list_for_database[0]
        new_rewritten_database_temp_medic = return_list_for_database[1]
        new_rewritten_database_temp_toilet = return_list_for_database[2]
        new_rewritten_database_temp_ration = return_list_for_database[3]

        accommodations_write_new = open("accommodation_database.txt", "w")
        for i in range(len(new_rewritten_database_temp)):
            accommodations_write_new.write(new_rewritten_database_temp[i])
        accommodations_write_new.close()

        medical_write_new = open("medical_database.txt", "w")
        for i in range(len(new_rewritten_database_temp_medic)):
            medical_write_new.write(new_rewritten_database_temp_medic[i])
        medical_write_new.close()

        toilets_write_new = open("toilet_database.txt", "w")
        for i in range(len(new_rewritten_database_temp_toilet)):
            toilets_write_new.write(new_rewritten_database_temp_toilet[i])
        toilets_write_new.close()

        rations_write_new = open("ration_database.txt", "w")
        for i in range(len(new_rewritten_database_temp_ration)):
            rations_write_new.write(new_rewritten_database_temp_ration[i])
        rations_write_new.close()

        # STORE ALL VALUES INTO LIST
        new_refugee[0] = str(return_list_for_database[4])
        new_refugee[2] = name
        new_refugee[3] = number
        new_refugee[4] = dob
        new_refugee[5] = age
        new_refugee[6] = sex
        new_refugee[7] = address
        new_refugee[8] = str(conditions)
        new_refugee[9] = str(num_of_fam)
        new_refugee[10] = str(return_list_for_database[5])
        new_refugee[11] = str(return_list_for_database[6])
        new_refugee[12] = str(return_list_for_database[7])
        new_refugee[13] = str(return_list_for_database[8])
        new_refugee[14] = str(return_list_for_database[9])
        new_refugee[15] = str(return_list_for_database[10])
        new_refugee[16] = str(return_list_for_database[11])
        new_refugee[17] = '\n'
        new_refugee_string = "%".join(new_refugee)
        volunteer_list_file_append = open("refugee_database.txt", "a")
        volunteer_list_file_append.write("%s" % (new_refugee_string))
        volunteer_list_file_append.close()

        # DISPLAY FINISH MESSAGE AND DELETE SCREENS
        delete2()
        finish_message()
        delete0()

    def add_camp():
        # SEES WHICH CAMP THE VOLUNTEER IS CURRENTLY ASSIGNED TO
        volunteer_current_camp = int(Volunteer_Home.user_camp_id)

        # GET LIST OF ONLY CAMP NAMES FROM EMERGENCY DATABASE
        camp_name_list = []
        for i in range(len(camp_database_list)):
            camp_name_list.append([camp_database_list[i][0], camp_database_list[i][1]])

        # FUNCTION TO FIND WHICH THEIR CURRENT CAMP NAME IS
        # DO IT BY COMPARING CAMP ID IN EMERGENCY DATABASE TO CAMP ID IN VOLUNTEER FILE
        current_camp_name = ''
        for i in range(len(camp_name_list)):
            if int(camp_name_list[i][0]) == int(volunteer_current_camp):
                current_camp_name = camp_name_list[i][1]
                break

        # OUTPUTS WHICH CAMP THE REFUGEE IS PLACED IN
        volunteer_current_camp_label = Label(screen2,
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
                for s in accommodation_database_list:
                    new_rewritten_database_temp.append(','.join(s))

                # WRITE NEW LIST INTO ACCOMMODATION TEXT FILE

                break
        volunteer_current_wing_label = Label(screen2,
                                                     text="Your refugee will be in the: %s" % that_block_list[
                                                         7])
        volunteer_current_wing_label.pack()
        # OUTPUT WHHICH BLOCK THEY ARE IN
        refugee_assigned_accommodation_label = Label(screen2,
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




        if refugee_family_medical_no.get() == '':
            num_medical_check = 0
        else:
            num_medical_check = int(refugee_family_medical_no.get())

        for i in range(len(medical_specific_camp_list)):

            # FIND MEDICAL STALL THAT IS GREATER THAN NO. OF PEOPLE IN FAMILY WITH MEDICAL CONDITIONS
            if int(medical_specific_camp_list[i][6]) >= num_medical_check:
                refugee_assigned_medical = medical_specific_camp_list[i][2]

                # CREATE NEW SPECIFIC LIST WITH NEW VALUES
                that_medic_list = medical_specific_camp_list[i]
                ahaha = str(int(that_medic_list[4]) + (int(num_medical_check)))
                bhaha = str(int(that_medic_list[6]) - (int(num_medical_check)))
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
        refugee_assigned_medical_label = Label(screen2,
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
        refugee_assigned_toilet_label = Label(screen2,
                                                      text='Your refugee toilet stall will be in: %s' % refugee_assigned_toilet)
        refugee_assigned_toilet_label.pack()

        # RATIONS
        # GET SPECIFIC LIST OF RATIONS IN SAME CAMP AND SAME WING
        ration_specific_camp_list = []
        for i in range(len(ration_database_list)):
            if int(ration_database_list[i][0]) == int(volunteer_current_camp) and ration_database_list[i][7] == refugee_assigned_block:
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
        refugee_assigned_ration_label = Label(screen2,
                                                      text='Your refugee ration stall will be in: %s' % refugee_assigned_ration)
        refugee_assigned_ration_label.pack()

        return [new_rewritten_database_temp, new_rewritten_database_temp_medic,
                new_rewritten_database_temp_toilet, new_rewritten_database_temp_ration, volunteer_current_camp,
                current_camp_name, that_block_list[7], refugee_assigned_accommodation, refugee_assigned_medical,
                refugee_assigned_toilet, refugee_assigned_ration, that_block_list[1]]

    def success():
        global return_list_for_database
        # SETTING UP SCREEN
        global screen2
        screen2 = tkinter.Toplevel()
        screen2.geometry("500x650")
        screen2.title("Confirm refugee submission")

        ref_year = refugee_year.get()
        ref_month = refugee_month.get()
        ref_day = refugee_day.get()

        ref_year = int(ref_year)
        ref_day = int(ref_day)

        ref_dob_list = ','.join([str(ref_day), str(ref_month), str(ref_year)])
        refugee_dob_calendar = datetime.datetime.strptime(ref_dob_list, '%d,%B,%Y')
        refugee_dob_calendar_string = refugee_dob_calendar.strftime("%d,%m,%Y")

        # DISPLAYS SUMMED UP INFO
        refugee_confirmation = Label(screen2,
                                             text="Please check the summary of details below to add to the database:",
                                             font=('Avenir', 14, 'bold', 'underline'))
        refugee_confirmation.pack(pady=30)

        name_confirmation = Label(screen2,
                                          text="The name you are entering is: %s" % (refugee_name.get()))
        name_confirmation.pack()

        number_confirmation = Label(screen2,
                                            text="The number of family members is: %s" % refugee_number.get())
        number_confirmation.pack()

        sex_confirmation = Label(screen2, text="The sex you are entering is: %s" % refugee_sex.get())
        sex_confirmation.pack()

        dob_confirmation = Label(screen2,
                                         text="The date of birth you are entering is: %s" % refugee_dob_calendar_string)
        dob_confirmation.pack()

        age_confirmation = Label(screen2, text="This means their age is: %s" % str(
            calculate_age(refugee_dob_calendar)))
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
        if country_address == "Use dropdown or type to select country...":
            country_address = ''
        address_list = [first_address, city_address, postcode_address, country_address]
        address = ', '.join(address_list)

        address_confirmation = Label(screen2, text="Their address is: %s" % address)
        address_confirmation.pack()

        conditions = refugee_height.get()
        if conditions == 'Enter all relevant medical conditions...' or conditions == 'Enter any medical conditions...':
            conditions = 'None'

        weight_confirmation = Label(screen2, text="Your conditions are: %s" % conditions)
        weight_confirmation.pack()

        num_of_fam = refugee_family_medical_no.get()
        try:
            num_of_fam = int(num_of_fam)
        except:
            if num_of_fam == '':
                num_of_fam = 'None'

        num_of_fam = str(num_of_fam)
        height_confirmation = Label(screen2, text="Number of family members with conditions: %s" % str(
            num_of_fam))
        height_confirmation.pack()

        refugee_camp_confirmation = Label(screen2,
                                                  text="Please check the allocations for the refugee below",
                                                  font=('Avenir', 14, 'bold', 'underline'))
        refugee_camp_confirmation.pack(pady=30)

        # RUNNING FUNCTION TO ALLOCATE PEOPLE TO THE CAMPS
        return_list_for_database = add_camp()

        # BUTTON TO SUBMIT
        submit_button = Button(screen2, text="Submit", command=submit)
        submit_button.pack(pady=30)
        update_refugee_button = Button(screen2, text="Change details", command=delete2)
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

    def refugee_sex_on(self):
        if refugee_sex_entry.get() == 'Select or type your sex...':
            refugee_sex_entry.delete(0, "end")  # delete all the text in the entry
            refugee_sex_entry.insert(0, '')  # Insert blank for user input
            refugee_sex_entry.config(foreground='black')

    def refugee_sex_off(self):
        if refugee_sex_entry.get() == '':
            refugee_sex_entry.insert(0, 'Select or type your sex...')
            refugee_sex_entry.config(foreground='grey')

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

    def refugee_country_address_on(self):
        if refugee_country_address_entry.get() == 'Use dropdown or type to select country...':
            refugee_country_address_entry.delete(0, "end")  # delete all the text in the entry
            refugee_country_address_entry.insert(0, '')  # Insert blank for user input
            refugee_country_address_entry.config(foreground='black')

    def refugee_country_address_off(self):
        if refugee_country_address_entry.get() == '':
            refugee_country_address_entry.insert(0, 'Use dropdown or type to select country...')
            refugee_country_address_entry.config(foreground='grey')

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
    intro_text = Label(screen, text="Use this section to create a refugee within this Database.", fg='Green',
                               width=300)
    intro_text.place(x=20, y=20)

    # Input from user

    # FORM THAT USER INPUTS
    namestatus = Label(screen, text="")
    namestatus.place(x=20, y=50)

    # REFUGEE NAME STUFF
    refugee_name_text = Label(screen, text="Refugee name*: ")
    refugee_name_text.place(x=20, y=30)
    refugee_name = StringVar()
    refugee_name_entry = Entry(screen, validate='all', validatecommand=name_validate,
                                       textvariable=refugee_name)
    refugee_name_entry.insert(0, 'Enter refugee name...')
    refugee_name_entry.bind('<FocusIn>', refugee_text_on)
    refugee_name_entry.bind('<FocusOut>', refugee_text_off)
    refugee_name_entry.config(fg='grey')

    refugee_name_entry.place(x=175, y=30, width=300)

    # REFUGEE NO. OF FAMILY MEMBERS STUFF
    numberstatus = Label(screen, text="")
    numberstatus.place(x=20, y=120)
    refugee_number_text = Label(screen, text="No. of family members*:")
    refugee_number_text.place(x=20, y=100)
    refugee_number_text_2 = Label(screen, text="(Not including you)", font='Arial 12',
                                          fg='grey')
    refugee_number_text_2.place(x=20, y=120)
    refugee_number = StringVar(value='')
    refugee_number_entry = Spinbox(screen, textvariable=refugee_number)
    refugee_number_entry.insert(0, 'Enter no. of family members...')
    refugee_number_entry.bind('<FocusIn>', refugee_number_on)
    refugee_number_entry.bind('<FocusOut>', refugee_number_off)
    refugee_number_entry.config(fg='grey')
    refugee_number_entry.place(x=175, y=100, width=300)

    # REFUGEE SEX STUFF
    refugee_sex_text = Label(screen, text="Sex*:")
    refugee_sex_text.place(x=20, y=170)
    refugee_sex = StringVar()
    refugee_sex_entry = tkinter.ttk.Combobox(screen, textvariable=refugee_sex, values = ["Male", "Female", "Prefer not to say"])
    refugee_sex_entry.insert(0, 'Select or type your sex...')
    refugee_sex_entry.bind('<FocusIn>', refugee_sex_on)
    refugee_sex_entry.bind('<FocusOut>', refugee_sex_off)
    refugee_sex_entry.config(foreground='grey')
    refugee_sex_entry.place(x=175, y=170, width=300)

    # REFUGEE DOB STUFF
    refugee_dob_text = Label(screen, text="Date of Birth*: ")
    refugee_dob_text.place(x=20, y=220)
    today = datetime.date.today()
    '''
    max = datetime.date(1904, 2, 11)
    
    # max is oldest person alive!
    refugee_dob_calendar = tkcalendar.Calendar(screen, date_pattern="d/m/y", selectmode='day',
                                               font='Arial 12', foreground='black', maxdate=today,
                                               mindate=max)
    refugee_dob_calendar.place(x=190, y=220)
    '''
    day_list = [d for d in range(1,32)]
    month_list = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    year_list = [m for m in range(1900, 2023)]
    year_list.reverse()

    refugee_year = StringVar()
    refugee_month = StringVar()
    refugee_day = StringVar()

    refugee_year_text = Label(screen, text='Year:')
    refugee_year_text.place(x=175, y=220)
    refugee_year_combo = tkinter.ttk.Combobox(screen, textvariable=refugee_year, values=year_list)
    refugee_year_combo.place(x=300, y=220, width=100)

    refugee_month_text = Label(screen, text='Month ')
    refugee_month_text.place(x=175, y=280)
    refugee_month_combo = tkinter.ttk.Combobox(screen, textvariable=refugee_month, values=month_list)
    refugee_month_combo.place(x=300, y=280, width=100)

    refugee_day_text = Label(screen, text='Day: ')
    refugee_day_text.place(x=175, y=340)
    refugee_day_combo = tkinter.ttk.Combobox(screen, textvariable=refugee_day, values=day_list)
    refugee_day_combo.place(x=300, y=340, width=100)



    # REFUGEE ADDRESS STUFF
    refugee_address_text = Label(screen, text="Address:")
    refugee_address_text.place(x=20, y=420)
    refugee_address_text_2 = Label(screen, text="(Not required)", font='Arial 12',
                                          fg='grey')
    refugee_address_text_2.place(x=20, y=440)


    refugee_first_address = StringVar()
    refugee_first_address_entry = Entry(screen, textvariable=refugee_first_address)
    refugee_first_address_entry.insert(0, 'Address Line 1')
    refugee_first_address_entry.bind('<FocusIn>', refugee_first_address_on)
    refugee_first_address_entry.bind('<FocusOut>', refugee_first_address_off)
    refugee_first_address_entry.config(fg='grey')
    refugee_first_address_entry.place(x=175, y=420, width=300)

    refugee_city_address = StringVar()
    refugee_city_address_entry = Entry(screen, textvariable=refugee_city_address)
    refugee_city_address_entry.insert(0, 'Town/City')
    refugee_city_address_entry.bind('<FocusIn>', refugee_city_address_on)
    refugee_city_address_entry.bind('<FocusOut>', refugee_city_address_off)
    refugee_city_address_entry.config(fg='grey')
    refugee_city_address_entry.place(x=175, y=450, width=150)

    refugee_postcode_address = StringVar()
    refugee_postcode_address_entry = Entry(screen, textvariable=refugee_postcode_address)
    refugee_postcode_address_entry.insert(0, 'Postcode')
    refugee_postcode_address_entry.bind('<FocusIn>', refugee_postcode_address_on)
    refugee_postcode_address_entry.bind('<FocusOut>', refugee_postcode_address_off)
    refugee_postcode_address_entry.config(fg='grey')
    refugee_postcode_address_entry.place(x=325, y=450, width=150)

    refugee_country_address = StringVar()
    refugee_country_address_entry = tkinter.ttk.Combobox(screen, textvariable=refugee_country_address, values = country_list)
    refugee_country_address_entry.insert(0, 'Use dropdown or type to select country...')
    refugee_country_address_entry.bind('<FocusIn>', refugee_country_address_on)
    refugee_country_address_entry.bind('<FocusOut>', refugee_country_address_off)
    refugee_country_address_entry.config(foreground='grey')
    refugee_country_address_entry.place(x=175, y=480, width=300)

    # FUNCTION TO DISPLAY INPUT BOX WHEN THEY CLICK YES TO MEDICAL CONDITIONS
    global refugee_height
    refugee_height = StringVar()
    global refugee_family_medical_no
    refugee_family_medical_no = StringVar(value=0)

    refugee_height_text = Label(screen, text="Conditions:")
    refugee_height_text.place(x=60, y=540)
    refugee_height_entry = Entry(screen, textvariable=refugee_height)
    refugee_height_entry.insert(0, 'Enter all relevant medical conditions...')
    refugee_height_entry.bind('<FocusIn>', refugee_height_on)
    refugee_height_entry.bind('<FocusOut>', refugee_height_off)
    refugee_height_entry.config(fg='grey')
    refugee_height_entry.place(x=175, y=540, width=300)
    refugee_family_medical_no_label = Label(screen,
                                            text="How many family members\n have conditions (inc. yourself):")
    refugee_family_medical_no_label.place(x=20, y=600)

    refugee_family_medical_no = StringVar()
    total_list = []
    for m in range(1,21):
        total_list.append(m)

    refugee_family_medical_no_option = tkinter.ttk.Combobox(screen, textvariable=refugee_family_medical_no,
                                                            values= total_list)
    refugee_family_medical_no_option.place(x=300, y=600, width=50)


    # BUTTON TO SUBMIT THE FORM
    submit_button = Button(screen, text="Submit the form", width=30, command=save_to_file)
    submit_button.place(x=100, y=660)

    screen.mainloop()

create_family()