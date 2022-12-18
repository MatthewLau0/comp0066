from tkinter import *
from tkinter import ttk
import datetime


def updateexistingForm():
    emergency_database_file = open("emergency_database.txt", "r")

    emergency_database_list = []
    for line in emergency_database_file:
        line_list = line.split("%")
        emergency_database_list.append(line_list)

    emergency_database_file.close()

    update_block_screen_id = Toplevel()
    update_block_screen_id.title("Update ID Select")

    screen_width1 = update_block_screen_id.winfo_screenwidth()
    screen_height1 = update_block_screen_id.winfo_screenheight()
    window_height1 = 100
    window_width1 = 300

    center_x1 = int(screen_width1 / 2 - window_width1 / 2)
    center_y1 = int(screen_height1 / 2 - window_height1 / 2)
    update_block_screen_id.geometry(f'{window_width1}x{window_height1}+{center_x1}+{center_y1}')

    id_list = []

    for i in emergency_database_list:
        id_list.append(i[0])

    selected_camp_id = StringVar()
    camp_name = StringVar()
    emergency_type = StringVar()
    emergency_description = StringVar()
    area_affected = StringVar()
    start_date_day = StringVar()
    start_date_month = StringVar()
    start_date_year = StringVar()
    end_date_day = StringVar()
    end_date_month = StringVar()
    end_date_year = StringVar()

    id_select_label = Label(update_block_screen_id, text="Please choose a block ID to update")
    id_select_label.pack()
    selected_camp_id.set("Select ID")
    id_select_option = ttk.Combobox(update_block_screen_id, textvariable=selected_camp_id, values=id_list)
    id_select_option.pack()

    def update_run():

        day_list = [str(i) for i in range(1, 32)]
        month_list = [str(i) for i in range(1, 13)]
        year_list = [str(i) for i in range(2023, 1899, -1)]

        update_block_screen = Toplevel()
        update_block_screen.title("Update Block")

        screen_width2 = update_block_screen.winfo_screenwidth()
        screen_height2 = update_block_screen.winfo_screenheight()
        window_height2 = screen_height2
        window_width2 = 900

        center_x2 = int(screen_width2 / 2 - window_width2 / 2)
        center_y2 = int(screen_height2 / 2 - window_height2 / 2)
        update_block_screen.geometry(f'{window_width2}x{window_height2}+{center_x2}+{center_y2}')

        id = int(selected_camp_id.get())
        x = id - 1

        update_emergency = [emergency_database_list[x][0], emergency_database_list[x][1], emergency_database_list[x][2], emergency_database_list[x][3], emergency_database_list[x][4], emergency_database_list[x][5], emergency_database_list[x][6], emergency_database_list[x][7], "\n"]

        New_Camp_Screen_Label = Label(update_block_screen, text="You are going to make a new emergency camp. Please follow the below instructions")
        New_Camp_Screen_Label.pack()
        New_Camp_Screen_Label_Index = Label(update_block_screen, text="The index number for your camp is %s" % (update_emergency[0]))
        New_Camp_Screen_Label_Index.pack()

        camp_name_label = Label(update_block_screen, text="Camp Name")
        camp_name_label.pack()
        camp_name_label_instructions = Label(update_block_screen, text="Camp Names must have no spaces and must only contain letters")
        camp_name_label_instructions.pack()
        camp_name_entry = Entry(update_block_screen, textvariable=camp_name)
        camp_name_entry.insert(END, f"{update_emergency[1]}")
        camp_name_entry.pack()

        emergency_type_label = Label(update_block_screen, text="Enter the type of emergency")
        emergency_type_label.pack()
        emergency_type_entry = ttk.Combobox(update_block_screen, textvariable=emergency_type,
                                            values=["Earthquake", "Tsunami", "Flood", "Drought", "Cyclone", "Hurricane",
                                                    "Climate Change", "Food Shortage", "Health Epidemic", "War",
                                                    "Industrial Accident", "Other: "])
        emergency_type_entry.insert(END, f"{update_emergency[2]}")
        emergency_type_entry.pack()

        emergency_description_label = Label(update_block_screen, text="Briefly describe the emergency")
        emergency_description_label.pack()
        emergency_description_entry = Entry(update_block_screen, textvariable=emergency_description)
        emergency_description_entry.insert(END, f"{update_emergency[3]}")
        emergency_description_entry.pack()

        country_list = ['Afghanistan', 'Aland Islands', 'Albania', 'Algeria', 'American Samoa', 'Andorra', 'Angola',
                        'Anguilla', 'Antarctica', 'Antigua and Barbuda', 'Argentina', 'Armenia', 'Aruba', 'Australia',
                        'Austria', 'Azerbaijan', 'Bahamas', 'Bahrain', 'Bangladesh', 'Barbados', 'Belarus', 'Belgium',
                        'Belize', 'Benin', 'Bermuda', 'Bhutan', 'Bolivia', 'Bosnia and Herzegovina', 'Botswana',
                        'Bouvet Island', 'Brazil', 'British Indian Ocean Territory', 'Brunei Darussalam', 'Bulgaria',
                        'Burkina Faso', 'Burundi', 'Cambodia', 'Cameroon', 'Canada', 'Cape Verde', 'Cayman Islands',
                        'Central African Republic', 'Chad', 'Chile', 'China', 'Christmas Island',
                        'Cocos (Keeling) Islands',
                        'Colombia', 'Comoros', 'Congo', 'The Democratic Republic of the Congo', 'Cook Islands',
                        'Costa Rica', "Côte d'Ivoire", 'Croatia', 'Cuba', 'Curaçao', 'Cyprus', 'Czech Republic',
                        'Denmark',
                        'Djibouti', 'Dominica', 'Dominican Republic', 'Ecuador', 'Egypt', 'El Salvador',
                        'Equatorial Guinea', 'Eritrea', 'Estonia', 'Ethiopia', 'Faroe Islands', 'Fiji', 'Finland',
                        'France',
                        'French Guiana', 'French Polynesia', 'French Southern Territories', 'Gabon', 'Gambia',
                        'Georgia',
                        'Germany', 'Ghana', 'Gibraltar', 'Greece', 'Greenland', 'Grenada', 'Guadeloupe', 'Guam',
                        'Guatemala', 'Guernsey', 'Guinea', 'Guinea-Bissau', 'Guyana', 'Haiti',
                        'Heard Island and McDonald Islands', 'Vatican City', 'Honduras', 'Hong Kong', 'Hungary',
                        'Iceland',
                        'India', 'Indonesia', 'Iran', 'Iraq', 'Ireland', 'Isle of Man', 'Israel', 'Italy', 'Jamaica',
                        'Japan', 'Jersey', 'Jordan', 'Kazakhstan', 'Kenya', 'Kiribati', 'Republic of Korea', 'Kuwait',
                        'Kyrgyzstan', "Laos", 'Latvia', 'Lebanon', 'Lesotho', 'Liberia', 'Libya', 'Liechtenstein',
                        'Lithuania', 'Luxembourg', 'Macao', 'Macedonia', 'Madagascar', 'Malawi', 'Malaysia', 'Maldives',
                        'Mali', 'Malta', 'Marshall Islands', 'Martinique', 'Mauritania', 'Mauritius', 'Mayotte',
                        'Mexico',
                        'Micronesia', 'Moldova', 'Monaco', 'Mongolia', 'Montenegro', 'Montserrat', 'Morocco',
                        'Mozambique',
                        'Myanmar', 'Namibia', 'Nauru', 'Nepal', 'Netherlands', 'New Caledonia', 'New Zealand',
                        'Nicaragua',
                        'Niger', 'Nigeria', 'Niue', 'Norfolk Island', 'Northern Mariana Islands', 'Norway', 'Oman',
                        'Pakistan', 'Palau', 'Palestinian Territory', 'Panama', 'Papua New Guinea', 'Paraguay', 'Peru',
                        'Philippines', 'Pitcairn', 'Poland', 'Portugal', 'Puerto Rico', 'Qatar', 'Réunion', 'Romania',
                        'Russia', 'Rwanda', 'Saint Lucia', 'Samoa', 'San Marino', 'Sao Tome and Principe',
                        'Saudi Arabia',
                        'Senegal', 'Serbia', 'Seychelles', 'Sierra Leone', 'Singapore', 'Slovakia', 'Slovenia',
                        'Solomon Islands', 'Somalia', 'South Africa', 'Spain', 'Sri Lanka', 'Sudan', 'Suriname',
                        'South Sudan', 'Svalbard', 'Swaziland', 'Sweden', 'Switzerland', 'Syrian Arab Republic',
                        'Taiwan',
                        'Tajikistan', 'Tanzania', 'Thailand', 'Timor-Leste', 'Togo', 'Tokelau', 'Tonga',
                        'Trinidad and Tobago', 'Tunisia', 'Turkey', 'Turkmenistan', 'Turks and Caicos Islands',
                        'Tuvalu',
                        'Uganda', 'Ukraine', 'United Arab Emirates', 'United Kingdom', 'United States', 'Uruguay',
                        'Uzbekistan', 'Vanuatu', 'Venezuela', 'Vietnam', 'Yemen', 'Zambia', 'Zimbabwe']

        emergency_location_label = Label(update_block_screen, text="Country Affected")
        emergency_location_label.pack()
        emergency_location_entry = ttk.Combobox(update_block_screen, textvariable=area_affected, values=country_list)
        emergency_location_entry.insert(END, f"{update_emergency[4]}")
        emergency_location_entry.pack()

        start_date_label = Label(update_block_screen, text="Enter the start date for the emergency")
        start_date_label.pack()
        start_date_frame = Frame(update_block_screen)
        start_date_frame.pack()
        start_date_day_combobox = ttk.Combobox(start_date_frame, textvariable=start_date_day, values=day_list)
        start_date_day_combobox.insert(END, f"{update_emergency[5][8:10]}")
        start_date_day_combobox.pack(side=LEFT)
        start_date_month_combobox = ttk.Combobox(start_date_frame, textvariable=start_date_month, values=month_list)
        start_date_month_combobox.insert(END, f"{update_emergency[5][5:7]}")
        start_date_month_combobox.pack(side=LEFT)
        start_date_year_combobox = ttk.Combobox(start_date_frame, textvariable=start_date_year, values=year_list)
        start_date_year_combobox.insert(END, f"{update_emergency[5][0:4]}")
        start_date_year_combobox.pack(side=LEFT)

        end_date_label = Label(update_block_screen, text="Enter the end date for the emergency")
        end_date_label.pack()
        Label(update_block_screen, text="If the emergency has not finished yet, please leave the below boxes blank.").pack()
        end_date_frame = Frame(update_block_screen)
        end_date_frame.pack()
        end_date_day_combobox = ttk.Combobox(end_date_frame, textvariable=end_date_day, values=day_list)
        end_date_month_combobox = ttk.Combobox(end_date_frame, textvariable=end_date_month, values=month_list)
        end_date_year_combobox = ttk.Combobox(end_date_frame, textvariable=end_date_year, values=year_list)
        if update_emergency[6][8:10] != "00" and update_emergency[6][5:7] != "00" and update_emergency[6][0:4] != "0000":
            end_date_day_combobox.insert(END, f"{update_emergency[6][8:10]}")
            end_date_month_combobox.insert(END, f"{update_emergency[6][5:7]}")
            end_date_year_combobox.insert(END, f"{update_emergency[6][0:4]}")
        end_date_day_combobox.pack(side=LEFT)
        end_date_month_combobox.pack(side=LEFT)
        end_date_year_combobox.pack(side=LEFT)

        def generate_start_date():
            if len(start_date_day.get()) == 0 and len(start_date_month.get()) == 0 and len(start_date_year.get()) == 0:
                return "0000-00-00"
            elif len(start_date_day.get()) == 0 or len(start_date_month.get()) == 0 or len(start_date_year.get()) == 0:
                start_date_label.config(text="Please enter a day, month and year.", fg='#f00')
            else:
                try:
                    startdateComplete = ("%s-%s-%s" % (start_date_year.get(), start_date_month.get(), start_date_day.get()))
                    startDateTime = datetime.datetime.strptime(startdateComplete, "%Y-%m-%d")
                    startDate = datetime.datetime.date(startDateTime)
                    return startDate
                except TclError:
                    return "0000-00-00"
                except ValueError:
                    return "0000-00-00"

        def generate_end_date():
            if len(end_date_day.get()) == 0 and len(end_date_month.get()) == 0 and len(end_date_year.get()) == 0:
                return "0000-00-00"
            elif len(end_date_day.get()) == 0 or len(end_date_month.get()) == 0 or len(end_date_year.get()) == 0:
                end_date_label.config(text="Please enter a day, month and year, or leave end date blank", fg='#f00')
            else:
                try:
                    enddateComplete = ("%s-%s-%s" % (end_date_year.get(), end_date_month.get(), end_date_day.get()))
                    endDateTime = datetime.datetime.strptime(enddateComplete, "%Y-%m-%d")
                    endDate = datetime.datetime.date(endDateTime)
                    return endDate
                except TclError:
                    return "0000-00-00"
                except ValueError:
                    return "0000-00-00"

        def generate_status():
            if generate_end_date() != "0000-00-00":
                status = "Closed"
            else:
                status = "Active"
            return status

        def CreateNewCampSummary():

            New_Camp_Summary_Screen = Toplevel()
            New_Camp_Summary_Screen.title("Submit New Emergency")

            screen_width2 = New_Camp_Summary_Screen.winfo_screenwidth()
            screen_height2 = New_Camp_Summary_Screen.winfo_screenheight()
            window_height2 = screen_height2
            window_width2 = 900

            center_x2 = int(screen_width2 / 2 - window_width2 / 2)
            center_y2 = int(screen_height2 / 2 - window_height2 / 2)
            New_Camp_Summary_Screen.geometry(f'{window_width2}x{window_height2}+{center_x2}+{center_y2}')

            New_Camp_Summary_Screen_Label = Label(New_Camp_Summary_Screen,
                                                  text="Please view below a summary of the camp that you are adding to the database")
            New_Camp_Summary_Screen_Label.pack()

            New_Camp_Name_Summary_Label = Label(New_Camp_Summary_Screen,
                                                text="The new camp name you are entering is: %s" % (camp_name.get()))
            New_Camp_Name_Summary_Label.pack()

            New_Camp_Type_Summary_Label = Label(New_Camp_Summary_Screen,
                                                text="The emergency type for the new camp is: %s" % (
                                                    emergency_type.get()))
            New_Camp_Type_Summary_Label.pack()

            New_Camp_Description_Summary_Label = Label(New_Camp_Summary_Screen,
                                                       text="Your description of the new emergency is: %s" % (
                                                           emergency_description.get()))
            New_Camp_Description_Summary_Label.pack()

            New_Camp_Area_Summary_Label = Label(New_Camp_Summary_Screen,
                                                text="The country your emergency is in is: %s" % (area_affected.get()))
            New_Camp_Area_Summary_Label.pack()

            New_Camp_StartDate_Summary_Label = Label(New_Camp_Summary_Screen,
                                                     text="The start date of the new emergency is: %s" % (
                                                         generate_start_date()))
            New_Camp_StartDate_Summary_Label.pack()

            if generate_end_date() == "0000-00-00":
                end_date_display = "NA"
            else:
                end_date_display = generate_end_date()

            New_Camp_EndDate_Summary_Label = Label(New_Camp_Summary_Screen,
                                                   text="The end date of the new emergency is: %s" % (
                                                       end_date_display))
            New_Camp_EndDate_Summary_Label.pack()

            New_Camp_Status_Summary_Label = Label(New_Camp_Summary_Screen,
                                                  text="The status of the new emergency is: %s" % (generate_status()))
            New_Camp_Status_Summary_Label.pack()

            def SubmitEmergency():
                New_Camp_Summary_Screen.destroy()
                update_block_screen.destroy()

                update_emergency[1] = camp_name.get()
                update_emergency[2] = emergency_type.get()
                update_emergency[3] = emergency_description.get()
                update_emergency[4] = area_affected.get()
                update_emergency[5] = str(generate_start_date())
                update_emergency[6] = str(generate_end_date())
                update_emergency[7] = generate_status()

                emergency_read = open("emergency_database.txt", "r")

                emergency_list = []
                for line in emergency_read:
                    line_string = line.split("%")
                    emergency_list.append(line_string)

                emergency_read.close()

                emergency_list = [update_emergency if i[0] == str(selected_camp_id.get()) else i for i in emergency_list]

                clear_file = open("emergency_database.txt", "w")
                clear_file.close()

                for entry in emergency_list:
                    with open("emergency_database.txt", "a") as emergency_write:
                        updated_camp_string = "%".join(entry)
                        emergency_write.write(updated_camp_string)
                emergency_write.close()

            Go_Back_Button = Button(New_Camp_Summary_Screen, text="Edit", command=New_Camp_Summary_Screen.destroy)
            Go_Back_Button.pack()

            New_Camp_Submission_Button = Button(New_Camp_Summary_Screen, text="Submit", command=SubmitEmergency)
            New_Camp_Submission_Button.pack()

        errors_new_camp = []

        def NewCampVerify():

            camp_name_label.config(text="Camp Name entered!", fg='green')
            emergency_type_label.config(text="Emergency Type entered!", fg='green')
            emergency_description_label.config(text="Description entered!", fg='green')
            start_date_label.config(text="Start date entered!", fg='green')
            if generate_end_date() == "0000-00-00":
                end_date_label.config(text="Emergency still active!", fg='green')
            else:
                end_date_label.config(text="End date entered!", fg='green')
            emergency_location_label.config(text="Country specified!", fg='green')

            errors_new_camp.clear()

            today = datetime.datetime.today()

            if len(camp_name.get()) == 0 or camp_name.get() == "":
                camp_name_label.config(text="Please enter a name for the new camp.", fg='#f00')
                errors_new_camp.append(1)
            if len(start_date_day.get()) == 0 or len(start_date_month.get()) == 0 or len(start_date_year.get()) == 0:
                start_date_label.config(text="Please enter a start date", fg='#f00')
            if len(emergency_type.get()) == 0 or emergency_type.get() == ' ':
                emergency_type_label.config(text="Please enter an emergency type for the new camp", fg='#f00')
                errors_new_camp.append(2)
            if len(emergency_description.get()) == 0:
                emergency_description_label.config(text="Please enter a description for the new emergency", fg='#f00')
                errors_new_camp.append(3)
            if len(area_affected.get()) == 0:
                emergency_location_label.config(text="Please enter the country where the emergency has occurred",
                                                fg='#f00')
                errors_new_camp.append(4)
            if generate_start_date() == "0000-00-00":
                start_date_label.config(text="Please enter a start date.", fg='#f00')
                errors_new_camp.append(5)
            elif generate_start_date() != "0000-00-00" and generate_end_date() != "0000-00-00":
                test_start_date = datetime.datetime.strptime(str(generate_start_date()), "%Y-%m-%d")
                test_end_date = datetime.datetime.strptime(str(generate_end_date()), "%Y-%m-%d")
                if test_start_date > today:
                    start_date_label.config(text="Please enter a start date later than today.", fg='#f00')
                    errors_new_camp.append(6)
                if test_end_date < test_start_date:
                    end_date_label.config(text="Please enter an end date later than the start date.", fg='#f00')
                    errors_new_camp.append(7)
            elif generate_start_date() != "0000-00-00" and generate_end_date() == "0000-00-00":
                test_start_date = datetime.datetime.strptime(str(generate_start_date()), "%Y-%m-%d")
                if test_start_date > today:
                    start_date_label.config(text="Please enter a start date later than today.", fg='#f00')
                    errors_new_camp.append(8)
            name_list = []
            for n in range(0, len(emergency_database_list)):
                name_list.append(emergency_database_list[n][1])
            name_list.remove(emergency_database_list[x][1])
            if camp_name.get() in name_list:
                camp_name_label.config(
                    text="This camp name already exists in the database. Please re-enter another camp-name.", fg='#f00')
                errors_new_camp.append(8)
            if area_affected.get() not in country_list:
                emergency_location_label.config(text="Please enter a valid country where the emergency has occurred", fg="#f00")
                errors_new_camp.append(9)

            if len(errors_new_camp) > 0:
                pass
            else:
                CreateNewCampSummary()

        done_button = Button(update_block_screen, text="Submit", command=NewCampVerify)
        done_button.pack()

        update_block_screen.mainloop()

    def run_the_update():
        if selected_camp_id.get() not in id_list:
            id_select_label.config(fg="#f00")
        else:
            update_block_screen_id.destroy()
            update_run()


    id_done = Button(update_block_screen_id, text="Done", command=run_the_update)
    id_done.pack()

    update_block_screen_id.mainloop()
