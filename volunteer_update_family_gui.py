def ViewTable():
    global Update_Emergency_Screen
    global emergency_database_list
    global View_Table_Yes
    global Index_Known_No
    global emergency_database_table
    global update_emergency_frame_two

    emergency_database_label = Label(Update_Emergency_Screen, text="Please use the below table to find the index number of the emergency you would like to update")
    emergency_database_label.pack()

    emergency_database_frame = Frame(Update_Emergency_Screen)
    emergency_database_frame.pack()

    emergency_database_table = ttk.Treeview(Update_Emergency_Screen)

    emergency_database_table['columns'] = ("Camp ID", "Camp Name", "Emergency Type", "Emergency Description", "Area Affected", "Start Date", "Close Date", "Status")

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

    #https://pythonguides.com/python-tkinter-table-tutorial/
    for i in range(0, len(emergency_database_list)):
        emergency_database_table.insert(parent='', index=i, iid=i, values=(emergency_database_list[i][0], emergency_database_list[i][1], emergency_database_list[i][2], emergency_database_list[i][3], emergency_database_list[i][4], emergency_database_list[i][5], emergency_database_list[i][6], emergency_database_list[i][7]))
        i += 1

    emergency_database_table.pack()

    emergency_database_table_button = Button(Update_Emergency_Screen, text="Continue", command=deleteTable)
    emergency_database_table_button.pack()
