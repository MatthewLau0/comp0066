import tkinter
from tkinter import *
from tkinter import ttk

def viewexistingCamps():
    def viewcampsetUp():
        global view_camp_home_screen
        global emergency_database_list

        view_camp_screen = Toplevel(view_camp_home_screen)
        view_camp_screen.title("View Existing Camps")
        view_camp_screen.geometry("500x650")
        view_camp_screen_label = Label(view_camp_screen,
                                       text="Please see below a summary of all of the camps in the database")
        view_camp_screen_label.pack()

        emergency_database_file = open("Emergency_Database.txt", "r")
        emergency_database_list = []
        for line in emergency_database_file:
            line_list = line.split(",")
            emergency_database_list.append(line_list)
        emergency_database_file.close()

        viewTable()

    def viewTable():
        global emergency_database_list
        global view_camp_screen

        emergency_database_frame = Frame(view_camp_screen)
        emergency_database_frame.pack()

        emergency_database_table = ttk.Treeview(view_camp_screen)

        emergency_database_table['columns'] = (
        "Camp ID", "Camp Name", "Emergency Type", "Emergency Description", "Area Affected", "Start Date", "Close Date",
        "Status")

        emergency_database_table.column("#0", width=0, stretch=NO)
        emergency_database_table.column("Camp ID", anchor=CENTER, width=100)
        emergency_database_table.column("Camp Name", anchor=CENTER, width=100)
        emergency_database_table.column("Emergency Type", anchor=CENTER, width=100)
        emergency_database_table.column("Emergency Description", anchor=CENTER, width=100)
        emergency_database_table.column("Area Affected", anchor=CENTER, width=100)
        emergency_database_table.column("Start Date", anchor=CENTER, width=100)
        emergency_database_table.column("Close Date", anchor=CENTER, width=100)
        emergency_database_table.column("Status", anchor=CENTER, width=100)

        emergency_database_table.heading("Camp ID", text="Camp ID", anchor=CENTER)
        emergency_database_table.heading("Camp Name", text="Camp Name", anchor=CENTER)
        emergency_database_table.heading("Emergency Type", text="Emergency Type", anchor=CENTER)
        emergency_database_table.heading("Emergency Description", text="Emergency Description", anchor=CENTER)
        emergency_database_table.heading("Area Affected", text="Area Affected", anchor=CENTER)
        emergency_database_table.heading("Start Date", text="Start Date", anchor=CENTER)
        emergency_database_table.heading("Close Date", text="Close Date", anchor=CENTER)
        emergency_database_table.heading("Status", text="Status", anchor=CENTER)

        # https://pythonguides.com/python-tkinter-table-tutorial/
        for i in range(0, len(emergency_database_list)):
            emergency_database_table.insert(parent='', index=i, iid=i, values=(
            emergency_database_list[i][0], emergency_database_list[i][1], emergency_database_list[i][2],
            emergency_database_list[i][3], emergency_database_list[i][4], emergency_database_list[i][5],
            emergency_database_list[i][6], emergency_database_list[i][7]))
            i += 1

        emergency_database_table.pack()

        return_home_button = Button(view_camp_screen, text="Return to Homescreen", command=returnHome)
        return_home_button.pack()

    def selectLayoutCamp():
        global selected_camp_id
        global Layout_Screen


        Layout_Screen = Toplevel()
        Layout_Screen.title("View Camp Layout")
        Layout_Screen.geometry("500x600")

        emergency_database_file = open("Emergency_Database.txt", "r")
        emergency_database_list = []
        for line in emergency_database_file:
            line_list = line.split("%")
            emergency_database_list.append(line_list)
        emergency_database_file.close()

        camp_ID_list = []
        for i in range(0, len(emergency_database_list)):
            camp_ID_list.append(emergency_database_list[i][0])

        selected_camp_id = StringVar()
        select_camp_id_label = Label(Layout_Screen, text="Please select the camp ID that you would like to view")
        select_camp_id_label.pack()
        select_camp_id = OptionMenu(Layout_Screen, selected_camp_id, *camp_ID_list)
        select_camp_id.pack()
        select_camp_button = Button(Layout_Screen, text="Submit", command=layoutSetUp)
        select_camp_button.pack()


    def layoutSetUp():
        global selected_camp_id
        global Layout_Screen

        camp_id = selected_camp_id

        accommodation_file = open("accommodations.txt", "r")
        ration_file = open("ration_stall.txt", "r")
        toilet_file = open("toilets.txt", "r")
        medical_file = open("medical.txt", "r")
        volunteer_file = open("volunteers.txt", "r")
        refugee_file = open("refugee_database.txt", "r")

        accom_list = []
        for line1 in accommodation_file:
            list1 = line1.split(",")
            if list1[0] == str(camp_id):
                accom_list.append(list1)

        ration_list = []
        for line2 in ration_file:
            list2 = line2.split(",")
            if list2[0] == str(camp_id):
                ration_list.append(list2)

        toilet_list = []
        for line3 in toilet_file:
            list3 = line3.split(",")
            if list3[0] == str(camp_id):
                toilet_list.append(list3)

        medical_list = []
        for line4 in medical_file:
            list4 = line4.split(",")
            if list4[0] == str(camp_id):
                medical_list.append(list4)

        volunteer_list = []
        for line5 in volunteer_file:
            list5 = line5.split("%")
            if list5[0] == str(camp_id):
                volunteer_list.append(list5)

        refugee_list = []
        for line6 in refugee_file:
            list6 = line6.split("#")
            if list6[0] == str(camp_id):
                refugee_list.append(list6)

        accom_north = []
        ration_north = []
        toilet_north = []
        medical_north = []

        accom_east = []
        ration_east = []
        toilet_east = []
        medical_east = []

        accom_south = []
        ration_south = []
        toilet_south = []
        medical_south = []

        accom_west = []
        ration_west = []
        toilet_west = []
        medical_west = []

        for i in accom_list:
            if i[7] == "North Wing":
                accom_north.append(i)
            elif i[7] == "East Wing":
                accom_east.append(i)
            elif i[7] == "South Wing":
                accom_south.append(i)
            elif i[7] == "West Wing":
                accom_west.append(i)

        for i in ration_list:
            if i[7] == "North Wing":
                ration_north.append(i)
            elif i[7] == "East Wing":
                ration_east.append(i)
            elif i[7] == "South Wing":
                ration_south.append(i)
            elif i[7] == "West Wing":
                ration_west.append(i)

        for i in toilet_list:
            if i[7] == "North Wing":
                toilet_north.append(i)
            elif i[7] == "East Wing":
                toilet_east.append(i)
            elif i[7] == "South Wing":
                toilet_south.append(i)
            elif i[7] == "West Wing":
                toilet_west.append(i)

        for i in medical_list:
            if i[7] == "North Wing":
                medical_north.append(i)
            elif i[7] == "East Wing":
                medical_east.append(i)
            elif i[7] == "South Wing":
                medical_south.append(i)
            elif i[7] == "West Wing":
                medical_west.append(i)

        list_occ_north = []
        for i in accom_north:
            x = int(i[4])
            list_occ_north.append(x)
        refugee_north = sum(list_occ_north)

        list_occ_east = []
        for i in accom_east:
            x = int(i[4])
            list_occ_east.append(x)
        refugee_east = sum(list_occ_east)

        list_occ_south = []
        for i in accom_south:
            x = int(i[4])
            list_occ_south.append(x)
        refugee_south = sum(list_occ_south)

        list_occ_west = []
        for i in accom_west:
            x = int(i[4])
            list_occ_west.append(x)
        refugee_west = sum(list_occ_west)

        camp_summary_window = Toplevel(Layout_Screen)
        camp_summary_window.title("Camp Layout")

        screen_width = Layout_Screen.winfo_screenwidth()
        screen_height = Layout_Screen.winfo_screenheight()
        window_height = screen_height
        window_width = 1200

        center_x = int(screen_width / 2 - window_width / 2)
        center_y = int(screen_height / 2 - window_height / 2)
        camp_summary_window.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

        summary_frame = Frame(camp_summary_window, highlightbackground="purple", highlightthickness=3)
        summary_frame.pack()
        summary_frame.place(relx=0.88, rely=0.02, anchor=N)

        summary_label = Label(summary_frame, text="Camp Summary", font=("Avenir", 22, "bold", "underline"))
        summary_label.pack()

        volunteer_label = Label(summary_frame, text=f"No. of Volunteers at this camp: \n{len(volunteer_list)}")
        volunteer_label.pack()

        refugee_label = Label(summary_frame, text=f"No. of Refugees at this camp: \n{len(refugee_list)}")
        refugee_label.pack()

        north_frame = Frame(camp_summary_window, highlightbackground="orange", highlightthickness=3)
        north_frame.pack()
        north_frame.place(relx=0.12, rely=0.02, anchor=N)

        north_label = Label(north_frame, text="North Wing", font=("Avenir", 22, "bold", "underline"))
        north_label.pack()

        north_accom_label = Label(north_frame, text="Accommodation Blocks", font=("Avenir", 16, "bold", "underline"))
        north_accom_label.pack()

        for i in accom_north:
            accom_north_label = Label(north_frame, text=f"{i[2]} ({i[4]} occupants)")
            accom_north_label.pack()

        north_ration_label = Label(north_frame, text="Ration Stalls", font=("Avenir", 16, "bold", "underline"))
        north_ration_label.pack()

        for i in ration_north:
            ration_north_label = Label(north_frame, text=f"{i[2]}")
            ration_north_label.pack()

        north_toilet_label = Label(north_frame, text="Toilet Blocks", font=("Avenir", 16, "bold", "underline"))
        north_toilet_label.pack()

        for i in toilet_north:
            toilet_north_label = Label(north_frame, text=f"{i[2]}")
            toilet_north_label.pack()

        north_medical_label = Label(north_frame, text="Medical Dispensaries", font=("Avenir", 16, "bold", "underline"))
        north_medical_label.pack()

        for i in medical_north:
            medical_north_label = Label(north_frame, text=f"{i[2]}")
            medical_north_label.pack()

        north_summary_heading = Label(north_frame, text="\nNorth Wing Summary",
                                      font=("Avenir", 16, "bold", "underline"))
        north_summary_heading.pack()

        north_summary_label = Label(north_frame, text=
        f"""Accommodation Blocks: 
        {len(accom_north)}
        Ration Stalls: 
        {len(ration_north)}
        Toilet Blocks: 
        {len(toilet_north)}
        Medical Dispensaries: 
        {len(medical_north)}
        Refugees: 
        {str(refugee_north)}
        """)

        north_summary_label.pack()

        east_frame = Frame(camp_summary_window, highlightbackground="orange", highlightthickness=3)
        east_frame.pack()
        east_frame.place(relx=0.31, rely=0.02, anchor=N)

        east_label = Label(east_frame, text="East Wing", font=("Avenir", 22, "bold", "underline"))
        east_label.pack()

        east_accom_label = Label(east_frame, text="Accommodation Blocks", font=("Avenir", 16, "bold", "underline"))
        east_accom_label.pack()

        for x in accom_east:
            accom_east_label = Label(east_frame, text=f"{x[2]} ({x[4]} occupants)")
            accom_east_label.pack()

        east_ration_label = Label(east_frame, text="Ration Stalls", font=("Avenir", 16, "bold", "underline"))
        east_ration_label.pack()

        for x in ration_east:
            ration_east_label = Label(east_frame, text=f"{x[2]}")
            ration_east_label.pack()

        east_toilet_label = Label(east_frame, text="Toilet Blocks", font=("Avenir", 16, "bold", "underline"))
        east_toilet_label.pack()

        for x in toilet_east:
            toilet_east_label = Label(east_frame, text=f"{x[2]}")
            toilet_east_label.pack()

        east_medical_label = Label(east_frame, text="Medical Dispensaries", font=("Avenir", 16, "bold", "underline"))
        east_medical_label.pack()

        for x in medical_east:
            medical_east_label = Label(east_frame, text=f"{x[2]}")
            medical_east_label.pack()

        east_summary_heading = Label(east_frame, text="\nEast Wing Summary", font=("Avenir", 16, "bold", "underline"))
        east_summary_heading.pack()

        east_summary_label = Label(east_frame, text=
        f"""Accommodation Blocks: 
        {len(accom_east)}
        Ration Stalls: 
        {len(ration_east)}
        Toilet Blocks: 
        {len(toilet_east)}
        Medical Dispensaries: 
        {len(medical_east)}
        Refugees: 
        {str(refugee_east)}
        """)

        east_summary_label.pack()

        south_frame = Frame(camp_summary_window, highlightbackground="orange", highlightthickness=3)
        south_frame.pack()
        south_frame.place(relx=0.50, rely=0.02, anchor=N)

        south_label = Label(south_frame, text="South Wing", font=("Avenir", 22, "bold", "underline"))
        south_label.pack()

        south_accom_label = Label(south_frame, text="Accommodation Blocks", font=("Avenir", 16, "bold", "underline"))
        south_accom_label.pack()

        for y in accom_south:
            accom_south_label = Label(south_frame, text=f"{y[2]} ({y[4]} occupants)")
            accom_south_label.pack()

        south_ration_label = Label(south_frame, text="Ration Stalls", font=("Avenir", 16, "bold", "underline"))
        south_ration_label.pack()

        for y in ration_south:
            ration_south_label = Label(south_frame, text=f"{y[2]}")
            ration_south_label.pack()

        south_toilet_label = Label(south_frame, text="Toilet Blocks", font=("Avenir", 16, "bold", "underline"))
        south_toilet_label.pack()

        for y in toilet_south:
            toilet_south_label = Label(south_frame, text=f"{y[2]}")
            toilet_south_label.pack()

        south_medical_label = Label(south_frame, text="Medical Dispensaries", font=("Avenir", 16, "bold", "underline"))
        south_medical_label.pack()

        for y in medical_south:
            medical_south_label = Label(south_frame, text=f"{y[2]}")
            medical_south_label.pack()

        south_summary_heading = Label(south_frame, text="\nSouth Wing Summary",
                                      font=("Avenir", 16, "bold", "underline"))
        south_summary_heading.pack()

        south_summary_label = Label(south_frame, text=
        f"""Accommodation Blocks: 
        {len(accom_south)}
        Ration Stalls: 
        {len(ration_south)}
        Toilet Blocks: 
        {len(toilet_south)}
        Medical Dispensaries: 
        {len(medical_south)}
        Refugees: 
        {str(refugee_south)}
        """)

        south_summary_label.pack()

        west_frame = Frame(camp_summary_window, highlightbackground="orange", highlightthickness=3)
        west_frame.pack()
        west_frame.place(relx=0.69, rely=0.02, anchor=N)

        west_label = Label(west_frame, text="West Wing", font=("Avenir", 22, "bold", "underline"))
        west_label.pack()

        west_accom_label = Label(west_frame, text="Accommodation Blocks", font=("Avenir", 16, "bold", "underline"))
        west_accom_label.pack()

        for z in accom_west:
            accom_west_label = Label(west_frame, text=f"{z[2]} ({z[4]} occupants)")
            accom_west_label.pack()

        west_ration_label = Label(west_frame, text="Ration Stalls", font=("Avenir", 16, "bold", "underline"))
        west_ration_label.pack()

        for z in ration_west:
            ration_west_label = Label(west_frame, text=f"{z[2]}")
            ration_west_label.pack()

        west_toilet_label = Label(west_frame, text="Toilet Blocks", font=("Avenir", 16, "bold", "underline"))
        west_toilet_label.pack()

        for z in toilet_west:
            toilet_west_label = Label(west_frame, text=f"{z[2]}")
            toilet_west_label.pack()

        west_medical_label = Label(west_frame, text="Medical Dispensaries", font=("Avenir", 16, "bold", "underline"))
        west_medical_label.pack()

        for z in medical_west:
            medical_west_label = Label(west_frame, text=f"{z[2]}")
            medical_west_label.pack()

        west_summary_heading = Label(west_frame, text="\nWest Wing Summary", font=("Avenir", 16, "bold", "underline"))
        west_summary_heading.pack()

        west_summary_label = Label(west_frame, text=
        f"""Accommodation Blocks: 
        {len(accom_west)}
        Ration Stalls: 
        {len(ration_west)}
        Toilet Blocks: 
        {len(toilet_west)}
        Medical Dispensaries: 
        {len(medical_west)}
        Refugees: 
        {str(refugee_west)}
        """)

        west_summary_label.pack()

        camp_summary_window.mainloop()

        accommodation_file.close()
        ration_file.close()
        toilet_file.close()
        medical_file.close()
        volunteer_file.close()
        refugee_file.close()

    def viewRefugees():
        pass



    def returnHome():
        import Admin_HomePage


    def viewcampScreen():
        global view_camp_home_screen
        view_camp_home_screen = Toplevel()
        view_camp_home_screen.title("View Existing Camps")
        view_camp_home_screen.geometry("500x650")
        view_camp_home_screen_label = Label(view_camp_home_screen, text="Please select an option below")
        view_camp_home_screen_label.pack()
        view_camp_button = Button(view_camp_home_screen, text="View Existing Camps", command=viewcampsetUp)
        view_camp_button.pack()
        view_camp_layout_button = Button(view_camp_home_screen, text="View Layout of a Camp", command=selectLayoutCamp)
        view_camp_layout_button.pack()
        view_refugees_summary_button = Button(view_camp_home_screen, text="View Refugees", command=viewRefugees)
        view_refugees_summary_button.pack()


        view_camp_home_screen.mainloop()

    viewcampScreen()