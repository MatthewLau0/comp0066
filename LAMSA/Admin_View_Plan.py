from tkinter import *
from tkinter import ttk
def Update_Emergency():
    from Admin_Update_Plan import updateexistingForm
    updateexistingForm()
def viewexistingCamps():

    view_camp_home_screen = Tk()
    view_camp_home_screen.title("View Existing Camps")
    screen_width1 = view_camp_home_screen.winfo_screenwidth()
    screen_height1 = view_camp_home_screen.winfo_screenheight()
    window_height1 = screen_height1
    window_width1 = 900

    center_x1 = int(screen_width1 / 2 - window_width1 / 2)
    center_y1 = int(screen_height1 / 2 - window_height1 / 2)
    view_camp_home_screen.geometry(f'{window_width1}x{window_height1}+{center_x1}+{center_y1}')

    Label(view_camp_home_screen, text="\nPlease see below a summary of all LAMSA Camps\n").pack()

    emergency_database_file = open("emergency_database.txt", "r")
    emergency_database_list = []
    for line in emergency_database_file:
        line_list = line.split("%")
        emergency_database_list.append(line_list)
    emergency_database_file.close()

    emergency_database_frame = Frame(view_camp_home_screen)
    emergency_database_frame.pack()

    emergency_database_table = ttk.Treeview(view_camp_home_screen)

    emergency_database_table['columns'] = (
    "Camp ID", "Camp Name", "Emergency Type", "Emergency Description", "Area Affected", "Start Date", "Close Date",
    "Status")

    emergency_database_table.column("#0", width=0, stretch=NO)
    emergency_database_table.column("Camp ID", anchor=CENTER, width=100)
    emergency_database_table.column("Camp Name", anchor=CENTER, width=100)
    emergency_database_table.column("Emergency Type", anchor=CENTER, width=100)
    emergency_database_table.column("Emergency Description", anchor=CENTER, width=200)
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

    for f in range(0, len(emergency_database_list)):
        emergency_database_table.insert(parent='', index=f, iid=f, values=(
        emergency_database_list[f][0], emergency_database_list[f][1], emergency_database_list[f][2],
        emergency_database_list[f][3], emergency_database_list[f][4], emergency_database_list[f][5],
        emergency_database_list[f][6], emergency_database_list[f][7]))

    emergency_database_table.pack()


    def selectLayoutCamp():

        Layout_Screen = Toplevel()
        Layout_Screen.title("View Camp Layout")
        screen_width2 = Layout_Screen.winfo_screenwidth()
        screen_height2 = Layout_Screen.winfo_screenheight()
        window_height2 = 100
        window_width2 = 500

        center_x2 = int(screen_width2 / 2 - window_width2 / 2)
        center_y2 = int(screen_height2 / 2 - window_height2 / 2)
        Layout_Screen.geometry(f'{window_width2}x{window_height2}+{center_x2}+{center_y2}')

        emergency_database_file_1 = open("Emergency_Database.txt", "r")
        emergency_database_list_1 = []
        for line_1 in emergency_database_file_1:
            line_list_1 = line_1.split("%")
            emergency_database_list_1.append(line_list_1)
        emergency_database_file_1.close()

        camp_ID_list_1 = []
        for ids in range(0, len(emergency_database_list_1)):
            camp_ID_list_1.append(emergency_database_list_1[ids][0])

        selected_camp_id = IntVar()
        select_camp_id_label = Label(Layout_Screen, text="Please select the camp ID that you would like to view")
        select_camp_id_label.pack()
        selected_camp_id_entry = ttk.Combobox(Layout_Screen, textvariable=selected_camp_id, values=camp_ID_list_1)
        selected_camp_id_entry.pack()


        def layoutSetUp():

            camp_id = selected_camp_id.get()

            accommodation_file = open("accommodation_database.txt", "r")
            ration_file = open("ration_database.txt", "r")
            toilet_file = open("toilet_database.txt", "r")
            medical_file = open("medical_database.txt", "r")
            volunteer_file = open("volunteer_database.txt", "r")
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
                list6 = line6.split("%")
                if list6[0] == str(camp_id):
                    refugee_list.append(list6)

            accommodation_file.close()
            ration_file.close()
            toilet_file.close()
            medical_file.close()
            volunteer_file.close()
            refugee_file.close()

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

            for s in accom_list:
                if s[7] == "North Wing":
                    accom_north.append(s)
                elif s[7] == "East Wing":
                    accom_east.append(s)
                elif s[7] == "South Wing":
                    accom_south.append(s)
                elif s[7] == "West Wing":
                    accom_west.append(s)

            for j in ration_list:
                if j[7] == "North Wing":
                    ration_north.append(j)
                elif j[7] == "East Wing":
                    ration_east.append(j)
                elif j[7] == "South Wing":
                    ration_south.append(j)
                elif j[7] == "West Wing":
                    ration_west.append(j)

            for k in toilet_list:
                if k[7] == "North Wing":
                    toilet_north.append(k)
                elif k[7] == "East Wing":
                    toilet_east.append(k)
                elif k[7] == "South Wing":
                    toilet_south.append(k)
                elif k[7] == "West Wing":
                    toilet_west.append(k)

            for p in medical_list:
                if p[7] == "North Wing":
                    medical_north.append(p)
                elif p[7] == "East Wing":
                    medical_east.append(p)
                elif p[7] == "South Wing":
                    medical_south.append(p)
                elif p[7] == "West Wing":
                    medical_west.append(p)

            list_occ_north = []
            for l in accom_north:
                x = int(l[4])
                list_occ_north.append(x)
            refugee_north = sum(list_occ_north)

            list_occ_east = []
            for m in accom_east:
                x = int(m[4])
                list_occ_east.append(x)
            refugee_east = sum(list_occ_east)

            list_occ_south = []
            for n in accom_south:
                x = int(n[4])
                list_occ_south.append(x)
            refugee_south = sum(list_occ_south)

            list_occ_west = []
            for o in accom_west:
                x = int(o[4])
                list_occ_west.append(x)
            refugee_west = sum(list_occ_west)

            camp_summary_window = Toplevel()
            camp_summary_window.title("Camp Layout")

            screen_width = camp_summary_window.winfo_screenwidth()
            screen_height = camp_summary_window.winfo_screenheight()
            window_height = screen_height
            window_width = screen_width

            center_x = int(screen_width / 2 - window_width / 2)
            center_y = int(screen_height / 2 - window_height / 2)
            camp_summary_window.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

            summary_frame = Frame(camp_summary_window, highlightbackground="purple", highlightthickness=3)
            summary_frame.pack()
            summary_frame.place(relx=0.88, rely=0.02, anchor=N)

            summary_label = Label(summary_frame, text="Camp Summary", font=("TkDefaultFont", 22, "bold", "underline"))
            summary_label.pack()

            volunteer_label = Label(summary_frame, text=f"No. of Volunteers at this camp: \n{len(volunteer_list)}")
            volunteer_label.pack()

            refugee_total = 0
            for a in refugee_list:
                refugee_total += int(a[3])

            refugee_label = Label(summary_frame, text=f"No. of Refugees at this camp: \n{refugee_total}")
            refugee_label.pack()

            north_frame = Frame(camp_summary_window, highlightbackground="orange", highlightthickness=3)
            north_frame.pack()
            north_frame.place(relx=0.12, rely=0.02, anchor=N)

            north_label = Label(north_frame, text="North Wing", font=("TkDefaultFont", 22, "bold", "underline"))
            north_label.pack()

            north_accom_label = Label(north_frame, text="Accommodation Blocks",
                                      font=("TkDefaultFont", 16, "bold", "underline"))
            north_accom_label.pack()

            for b in accom_north:
                accom_north_label = Label(north_frame, text=f"Block {b[1]} ({b[4]} occupants)")
                accom_north_label.pack()

            north_ration_label = Label(north_frame, text="Ration Stalls",
                                       font=("TkDefaultFont", 16, "bold", "underline"))
            north_ration_label.pack()

            for c in ration_north:
                ration_north_label = Label(north_frame, text=f"Ration {c[1]}")
                ration_north_label.pack()

            north_toilet_label = Label(north_frame, text="Toilet Blocks",
                                       font=("TkDefaultFont", 16, "bold", "underline"))
            north_toilet_label.pack()

            for d in toilet_north:
                toilet_north_label = Label(north_frame, text=f"Toilet {d[1]}")
                toilet_north_label.pack()

            north_medical_label = Label(north_frame, text="Medical Dispensaries",
                                        font=("TkDefaultFont", 16, "bold", "underline"))
            north_medical_label.pack()

            for e in medical_north:
                medical_north_label = Label(north_frame, text=f"Medical {e[1]}")
                medical_north_label.pack()

            north_summary_heading = Label(north_frame, text="\nNorth Wing Summary",
                                          font=("TkDefaultFont", 16, "bold", "underline"))
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

            east_label = Label(east_frame, text="East Wing", font=("TkDefaultFont", 22, "bold", "underline"))
            east_label.pack()

            east_accom_label = Label(east_frame, text="Accommodation Blocks",
                                     font=("TkDefaultFont", 16, "bold", "underline"))
            east_accom_label.pack()

            for x in accom_east:
                accom_east_label = Label(east_frame, text=f"Block {x[1]} ({x[4]} occupants)")
                accom_east_label.pack()

            east_ration_label = Label(east_frame, text="Ration Stalls", font=("TkDefaultFont", 16, "bold", "underline"))
            east_ration_label.pack()

            for x in ration_east:
                ration_east_label = Label(east_frame, text=f"Ration {x[1]}")
                ration_east_label.pack()

            east_toilet_label = Label(east_frame, text="Toilet Blocks", font=("TkDefaultFont", 16, "bold", "underline"))
            east_toilet_label.pack()

            for x in toilet_east:
                toilet_east_label = Label(east_frame, text=f"Toilet {x[1]}")
                toilet_east_label.pack()

            east_medical_label = Label(east_frame, text="Medical Dispensaries",
                                       font=("TkDefaultFont", 16, "bold", "underline"))
            east_medical_label.pack()

            for x in medical_east:
                medical_east_label = Label(east_frame, text=f"Medical {x[1]}")
                medical_east_label.pack()

            east_summary_heading = Label(east_frame, text="\nEast Wing Summary",
                                         font=("TkDefaultFont", 16, "bold", "underline"))
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

            south_label = Label(south_frame, text="South Wing", font=("TkDefaultFont", 22, "bold", "underline"))
            south_label.pack()

            south_accom_label = Label(south_frame, text="Accommodation Blocks",
                                      font=("TkDefaultFont", 16, "bold", "underline"))
            south_accom_label.pack()

            for y in accom_south:
                accom_south_label = Label(south_frame, text=f"Block {y[1]} ({y[4]} occupants)")
                accom_south_label.pack()

            south_ration_label = Label(south_frame, text="Ration Stalls",
                                       font=("TkDefaultFont", 16, "bold", "underline"))
            south_ration_label.pack()

            for y in ration_south:
                ration_south_label = Label(south_frame, text=f"Ration {y[1]}")
                ration_south_label.pack()

            south_toilet_label = Label(south_frame, text="Toilet Blocks",
                                       font=("TkDefaultFont", 16, "bold", "underline"))
            south_toilet_label.pack()

            for y in toilet_south:
                toilet_south_label = Label(south_frame, text=f"Toilet {y[1]}")
                toilet_south_label.pack()

            south_medical_label = Label(south_frame, text="Medical Dispensaries",
                                        font=("TkDefaultFont", 16, "bold", "underline"))
            south_medical_label.pack()

            for y in medical_south:
                medical_south_label = Label(south_frame, text=f"Medical {y[1]}")
                medical_south_label.pack()

            south_summary_heading = Label(south_frame, text="\nSouth Wing Summary",
                                          font=("TkDefaultFont", 16, "bold", "underline"))
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

            west_label = Label(west_frame, text="West Wing", font=("TkDefaultFont", 22, "bold", "underline"))
            west_label.pack()

            west_accom_label = Label(west_frame, text="Accommodation Blocks",
                                     font=("TkDefaultFont", 16, "bold", "underline"))
            west_accom_label.pack()

            for z in accom_west:
                accom_west_label = Label(west_frame, text=f"Block {z[1]} ({z[4]} occupants)")
                accom_west_label.pack()

            west_ration_label = Label(west_frame, text="Ration Stalls", font=("TkDefaultFont", 16, "bold", "underline"))
            west_ration_label.pack()

            for z in ration_west:
                ration_west_label = Label(west_frame, text=f"Ration {z[1]}")
                ration_west_label.pack()

            west_toilet_label = Label(west_frame, text="Toilet Blocks", font=("TkDefaultFont", 16, "bold", "underline"))
            west_toilet_label.pack()

            for z in toilet_west:
                toilet_west_label = Label(west_frame, text=f"Toilet {z[1]}")
                toilet_west_label.pack()

            west_medical_label = Label(west_frame, text="Medical Dispensaries",
                                       font=("TkDefaultFont", 16, "bold", "underline"))
            west_medical_label.pack()

            for z in medical_west:
                medical_west_label = Label(west_frame, text=f"Medical {z[1]}")
                medical_west_label.pack()

            west_summary_heading = Label(west_frame, text="\nWest Wing Summary",
                                         font=("TkDefaultFont", 16, "bold", "underline"))
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
            Button(camp_summary_window, text="Close", command=camp_summary_window.destroy).pack(side=BOTTOM, pady=20)
            camp_summary_window.mainloop()

        def decide_to_open():
            try:
                if str(selected_camp_id.get()) not in camp_ID_list_1:
                    select_camp_id_label.config(text="Please choose a camp from the list below", fg="#f00")
                else:
                    Layout_Screen.destroy()
                    layoutSetUp()
            except TclError:
                pass

        select_camp_button = Button(Layout_Screen, text="Submit", command=decide_to_open)
        select_camp_button.pack()



    def viewRefugees():
        volunteer_list_file = open("refugee_database.txt", "r")
        volunteer_database_list = []
        for line2 in volunteer_list_file:
            x = line2.split("%")
            volunteer_database_list.append(x)
        volunteer_list_file.close()

        Update_Emergency_Screen = Tk()
        screen_width = Update_Emergency_Screen.winfo_screenwidth()
        screen_height = Update_Emergency_Screen.winfo_screenheight()
        window_height = screen_height
        window_width = screen_width

        center_x = int(screen_width / 2 - window_width / 2)
        center_y = int(screen_height / 2 - window_height / 2)
        Update_Emergency_Screen.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
        Update_Emergency_Screen.title("Table of Refugees")

        emergency_database_label = Label(Update_Emergency_Screen,
                                         text="\nPlease use the below table will Refugees at all LAMSA Camps\n")
        emergency_database_label.pack()

        emergency_database_frame_1 = Frame(Update_Emergency_Screen)
        emergency_database_frame_1.pack()

        emergency_database_table1 = ttk.Treeview(Update_Emergency_Screen)

        emergency_database_table1['columns'] = (
            "CampID", "Family ID", "Date Added", "Name", "Family size", "Date of Birth", "Age", "Gender", "Phone Number", "Address", "No. family with condition",
            "Medical Conditions", "Accommodation", "Medical", "Toilet", "Ration")

        emergency_database_table1.column("#0", width=0, stretch=NO)
        emergency_database_table1.column("CampID", anchor='center', width=50)
        emergency_database_table1.column("Family ID", anchor='center', width=50)
        emergency_database_table1.column("Date Added", anchor='center', width=90)
        emergency_database_table1.column("Name", anchor='center', width=100)
        emergency_database_table1.column("Family size", anchor='center', width=70)
        emergency_database_table1.column("Date of Birth", anchor='center', width=80)
        emergency_database_table1.column("Age", anchor='center', width=40)
        emergency_database_table1.column("Gender", anchor='center', width=90)
        emergency_database_table1.column("Address", anchor='center', width=200)
        emergency_database_table1.column("Phone Number", anchor='center', width=120)
        emergency_database_table1.column("No. family with condition", anchor='center', width=90)
        emergency_database_table1.column("Medical Conditions", anchor='center', width=210)
        emergency_database_table1.column("Accommodation", anchor='center', width=150)
        emergency_database_table1.column("Medical", anchor='center', width=150)
        emergency_database_table1.column("Toilet", anchor='center', width=150)
        emergency_database_table1.column("Ration", anchor='center', width=150)

        emergency_database_table1.heading("CampID", text="Camp ID", anchor='center')
        emergency_database_table1.heading("Family ID", text="Family ID", anchor='center')
        emergency_database_table1.heading("Date Added", text="Date Added", anchor='center')
        emergency_database_table1.heading("Name", text="Name", anchor='center')
        emergency_database_table1.heading("Family size", text="Family size", anchor='center')
        emergency_database_table1.heading("Date of Birth", text="Date of Birth", anchor='center')
        emergency_database_table1.heading("Age", text="Age", anchor='center')
        emergency_database_table1.heading("Gender", text="Sex", anchor='center')
        emergency_database_table1.heading("Address", text="Address", anchor='center')
        emergency_database_table1.heading("Phone Number", text="Phone Number", anchor='center')
        emergency_database_table1.heading("No. family with condition", text="No. w/ conditions", anchor='center')
        emergency_database_table1.heading("Medical Conditions", text="Medical Conditions", anchor='center')
        emergency_database_table1.heading("Accommodation", text="Accom.", anchor='center')
        emergency_database_table1.heading("Medical", text="Medical", anchor='center')
        emergency_database_table1.heading("Toilet", text="Toilet", anchor='center')
        emergency_database_table1.heading("Ration", text="Rations", anchor='center')

        for i in range(0, len(volunteer_database_list)):
            number = volunteer_database_list[i][7].split("#")
            emergency_database_table1.insert(parent='', index=i, iid=i, values=(
                str(volunteer_database_list[i][0]), str(volunteer_database_list[i][1]), str(volunteer_database_list[i][15]),
                volunteer_database_list[i][2], volunteer_database_list[i][3], str(volunteer_database_list[i][4]),
                volunteer_database_list[i][5], volunteer_database_list[i][6], f"+{number[0]} {number[1]}",
                volunteer_database_list[i][8], volunteer_database_list[i][9], volunteer_database_list[i][10],
                volunteer_database_list[i][11], volunteer_database_list[i][12], volunteer_database_list[i][13], volunteer_database_list[i][14]))

        emergency_database_table1.pack(fill='both')

        view_refugee_return_home_button = Button(Update_Emergency_Screen, text="Return Home",
                                                 command=Update_Emergency_Screen.destroy)
        view_refugee_return_home_button.pack()

    update_emergency_button = Button(view_camp_home_screen, text="Update Existing Emergency Camp", command=Update_Emergency)
    update_emergency_button.pack()
    view_camp_layout_button = Button(view_camp_home_screen, text="View Layout of a Camp", command=selectLayoutCamp)
    view_camp_layout_button.pack()
    view_refugees_summary_button = Button(view_camp_home_screen, text="View Refugees", command=viewRefugees)
    view_refugees_summary_button.pack()
    Button(view_camp_home_screen, text="Home", command=view_camp_home_screen.destroy).pack()


    view_camp_home_screen.mainloop()
