def table():
    import tkinter
    import tkinter.ttk

    volunteer_list_file = open("refugee_database.txt", "r")
    volunteer_database_list = []
    for line in volunteer_list_file:
        x = line.split("%")
        volunteer_database_list.append(x)

    def deleteTable():
        Update_Emergency_Screen.destroy()

    def ViewTable():
        global Update_Emergency_Screen
        global emergency_database_list
        global View_Table_Yes
        global Index_Known_No
        global emergency_database_table
        global update_emergency_frame_two

        Update_Emergency_Screen = tkinter.Tk()
        Update_Emergency_Screen.geometry("1200x600")
        Update_Emergency_Screen.title("Table of Refugees")

        emergency_database_label = tkinter.Label(Update_Emergency_Screen, text="Please use the below table to view a full list of refugees")
        emergency_database_label.pack()

        emergency_database_frame = tkinter.Frame(Update_Emergency_Screen)
        emergency_database_frame.pack()

        emergency_database_table = tkinter.ttk.Treeview(Update_Emergency_Screen)

        emergency_database_table['columns'] = ("CampID", "ID", "Name", "Family size", "Date of Birth", "Age", "Sex", "Address", "Medical Conditions", "No. family with condition", "CampName", "Wing", "Accommodation", "Medical", "Toilet", "Ration")

        emergency_database_table.column("#0", width=0, stretch=True)
        emergency_database_table.column("CampID", anchor='center', width=50)
        emergency_database_table.column("ID", anchor='center', width=30)
        emergency_database_table.column("Name", anchor='center', width=80)
        emergency_database_table.column("Family size", anchor='center', width=60)
        emergency_database_table.column("Date of Birth", anchor='center', width=80)
        emergency_database_table.column("Age", anchor='center', width=40)
        emergency_database_table.column("Sex", anchor='center', width=80)
        emergency_database_table.column("Address", anchor='center', width=200)
        emergency_database_table.column("Medical Conditions", anchor='center', width=210)
        emergency_database_table.column("No. family with condition", anchor='center', width=85)
        emergency_database_table.column("CampName", anchor='center', width=100)
        emergency_database_table.column("Wing", anchor='center', width=85)
        emergency_database_table.column("Accommodation", anchor='center', width=80)
        emergency_database_table.column("Medical", anchor='center', width=80)
        emergency_database_table.column("Toilet", anchor='center', width=70)
        emergency_database_table.column("Ration", anchor='center', width=70)

        emergency_database_table.heading("CampID", text="Camp ID", anchor='center')
        emergency_database_table.heading("ID", text="ID", anchor='center')
        emergency_database_table.heading("Name", text="Name", anchor='center')
        emergency_database_table.heading("Family size", text="Family size", anchor='center')
        emergency_database_table.heading("Date of Birth", text="Date of Birth", anchor='center')
        emergency_database_table.heading("Age", text="Age", anchor='center')
        emergency_database_table.heading("Sex", text="Sex", anchor='center')
        emergency_database_table.heading("Address", text="Address", anchor='center')
        emergency_database_table.heading("Medical Conditions", text="Medical Conditions", anchor='center')
        emergency_database_table.heading("No. family with condition", text="No. w/ conditions", anchor='center')
        emergency_database_table.heading("CampName", text="Camp Name", anchor='center')
        emergency_database_table.heading("Wing", text="Wing", anchor='center')
        emergency_database_table.heading("Accommodation", text="Accom.", anchor='center')
        emergency_database_table.heading("Medical", text="Medical", anchor='center')
        emergency_database_table.heading("Toilet", text="Toilet", anchor='center')
        emergency_database_table.heading("Ration", text="Rations", anchor='center')


        #https://pythonguides.com/python-tkinter-table-tutorial/
        for i in range(0, len(volunteer_database_list)):
            emergency_database_table.insert(parent='', index=i, iid=i, values=(str(volunteer_database_list[i][0]), str(volunteer_database_list[i][1]), volunteer_database_list[i][2], volunteer_database_list[i][3], str(volunteer_database_list[i][4]), volunteer_database_list[i][5], volunteer_database_list[i][6], volunteer_database_list[i][7], volunteer_database_list[i][8], volunteer_database_list[i][9], volunteer_database_list[i][10], volunteer_database_list[i][11], volunteer_database_list[i][12], volunteer_database_list[i][13], volunteer_database_list[i][14], volunteer_database_list[i][15]))
            i += 1

        emergency_database_table.pack(fill='both')

        emergency_database_table_button = tkinter.Button(Update_Emergency_Screen, text="Continue", command=deleteTable)
        emergency_database_table_button.pack()

        Update_Emergency_Screen.mainloop()


    ViewTable()

