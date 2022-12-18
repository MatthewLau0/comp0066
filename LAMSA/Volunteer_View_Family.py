from tkinter import *
from tkinter import ttk

camp_id_to_view = ""


def camp_id_generate():
    global camp_id_to_view
    logins_file = open("successful_login.txt", "r")

    logins_list = []
    for line in logins_file:
        line_string = line.split("%")
        logins_list.append(line_string)
    logins_file.close()
    if len(logins_list) > 0:
        camp_id_to_view = logins_list[-1][0]
    else:
        pass

def table():
    camp_id_generate()
    volunteer_list_file = open("refugee_database.txt", "r")
    volunteer_database_list = []
    for line in volunteer_list_file:
        x = line.split("%")
        if x[0] == camp_id_to_view:
            volunteer_database_list.append(x)
    volunteer_list_file.close()

    view_refugee_table = Toplevel()
    screen_width1 = view_refugee_table.winfo_screenwidth()
    screen_height1 = view_refugee_table.winfo_screenheight()
    window_height1 = screen_height1
    window_width1 = screen_width1 - 100

    center_x1 = int(screen_width1 / 2 - window_width1 / 2)
    center_y1 = int(screen_height1 / 2 - window_height1 / 2)
    view_refugee_table.geometry(f'{window_width1}x{window_height1}+{center_x1}+{center_y1}')
    view_refugee_table.title("Table of Refugees")

    emergency_database_label = Label(view_refugee_table,
                                     text="Please use the below table to view a full list of refugees")
    emergency_database_label.pack()

    emergency_database_frame = Frame(view_refugee_table)
    emergency_database_frame.pack()

    emergency_database_table = ttk.Treeview(view_refugee_table)

    emergency_database_table['columns'] = (
        "CampID", "ID", "Name", "Family size", "Date of Birth", "Age", "Sex", "Address", "No. family with condition",
        "Medical Conditions", "Accommodation", "Medical", "Toilet", "Ration")

    emergency_database_table.column("#0", width=0, stretch=NO)
    emergency_database_table.column("CampID", anchor='center', width=50)
    emergency_database_table.column("ID", anchor='center', width=30)
    emergency_database_table.column("Name", anchor='center', width=80)
    emergency_database_table.column("Family size", anchor='center', width=60)
    emergency_database_table.column("Date of Birth", anchor='center', width=80)
    emergency_database_table.column("Age", anchor='center', width=40)
    emergency_database_table.column("Sex", anchor='center', width=80)
    emergency_database_table.column("Address", anchor='center', width=200)
    emergency_database_table.column("No. family with condition", anchor='center', width=85)
    emergency_database_table.column("Medical Conditions", anchor='center', width=210)
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
    emergency_database_table.heading("No. family with condition", text="No. w/ conditions", anchor='center')
    emergency_database_table.heading("Medical Conditions", text="Medical Conditions", anchor='center')
    emergency_database_table.heading("Accommodation", text="Accom.", anchor='center')
    emergency_database_table.heading("Medical", text="Medical", anchor='center')
    emergency_database_table.heading("Toilet", text="Toilet", anchor='center')
    emergency_database_table.heading("Ration", text="Rations", anchor='center')

    for i in range(0, len(volunteer_database_list)):
        emergency_database_table.insert(parent='', index=i, iid=i, values=(
            str(volunteer_database_list[i][0]), str(volunteer_database_list[i][1]),
            volunteer_database_list[i][2], volunteer_database_list[i][3], str(volunteer_database_list[i][4]),
            volunteer_database_list[i][5], volunteer_database_list[i][6], volunteer_database_list[i][7],
            volunteer_database_list[i][8], volunteer_database_list[i][9], volunteer_database_list[i][10],
            volunteer_database_list[i][11], volunteer_database_list[i][12], volunteer_database_list[i][13]))

    emergency_database_table.pack(fill='both')

    def modify_family():
        pass


    update_a_family_button = Button(view_refugee_table, text="Update a Family", command=modify_family)
    update_a_family_button.pack()

    view_refugee_return_home_button = Button(view_refugee_table, text="Return Home", command=view_refugee_table.destroy)
    view_refugee_return_home_button.pack()

    view_refugee_table.mainloop()

table()