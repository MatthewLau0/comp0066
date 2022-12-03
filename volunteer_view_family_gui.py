def table():
    import tkinter
    import tkinter.ttk
    import sys
    import subprocess
    from tkcalendar import Calendar

    subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'tkcalendar'])
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'tkintermapview'])


    volunteer_list_file = open("Volunteer_Database", "r")
    volunteer_database_list = []
    for line in volunteer_list_file:
        x = line.split("#")
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
        Update_Emergency_Screen.geometry("600x600")
        Update_Emergency_Screen.title("Table of Volunteers")

        emergency_database_label = tkinter.Label(Update_Emergency_Screen, text="Please use the below table to find the index number of the emergency you would like to update")
        emergency_database_label.pack()

        emergency_database_frame = tkinter.Frame(Update_Emergency_Screen)
        emergency_database_frame.pack()

        emergency_database_table = tkinter.ttk.Treeview(Update_Emergency_Screen)

        emergency_database_table['columns'] = ("Refugee ID", "Name", "Family members", "Date of Birth", "Age", "Sex", "Address", "Weight", "Height")

        emergency_database_table.column("#0", width=0, stretch=True)
        emergency_database_table.column("Refugee ID", anchor='center', width=100)
        emergency_database_table.column("Name", anchor='center', width=100)
        emergency_database_table.column("Family members", anchor='center', width=100)
        emergency_database_table.column("Date of Birth", anchor='center', width=100)
        emergency_database_table.column("Age", anchor='center', width=100)
        emergency_database_table.column("Sex", anchor='center', width=100)
        emergency_database_table.column("Address", anchor='center', width=300)
        emergency_database_table.column("Weight", anchor='center', width=100)
        emergency_database_table.column("Height", anchor='center', width=100)

        emergency_database_table.heading("Refugee ID", text="Refugee ID", anchor='center')
        emergency_database_table.heading("Name", text="Name", anchor='center')
        emergency_database_table.heading("Family members", text="Family members", anchor='center')
        emergency_database_table.heading("Date of Birth", text="Date of Birth", anchor='center')
        emergency_database_table.heading("Age", text="Age", anchor='center')
        emergency_database_table.heading("Sex", text="Sex", anchor='center')
        emergency_database_table.heading("Address", text="Address", anchor='center')
        emergency_database_table.heading("Weight", text="Weight", anchor='center')
        emergency_database_table.heading("Height", text="Height", anchor='center')

        #https://pythonguides.com/python-tkinter-table-tutorial/
        for i in range(0, len(volunteer_database_list)):
            emergency_database_table.insert(parent='', index=i, iid=i, values=(volunteer_database_list[i][0], str(volunteer_database_list[i][1]), volunteer_database_list[i][2], volunteer_database_list[i][3], volunteer_database_list[i][4], volunteer_database_list[i][5], volunteer_database_list[i][6], volunteer_database_list[i][7], volunteer_database_list[i][8]))
            i += 1

        emergency_database_table.pack()

        emergency_database_table_button = tkinter.Button(Update_Emergency_Screen, text="Continue", command=deleteTable)
        emergency_database_table_button.pack()

        Update_Emergency_Screen.mainloop()


    ViewTable()