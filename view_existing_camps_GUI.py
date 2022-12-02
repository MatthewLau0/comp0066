import tkinter
from tkinter import *
from tkinter import ttk

def setUp():
    global emergency_database_list
    emergency_database_file = open("Emergency_Database", "r")
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




def returnHome():
    import Emergency_Plan_Form_Admin_GUI


def viewcampScreen():
    global view_camp_screen
    view_camp_screen = Toplevel()
    view_camp_screen.title("View Existing Camps")
    view_camp_screen.geometry("500x650")
    view_camp_screen_label = Label(view_camp_screen, text="Please see below a summary of all of the camps in the database")
    view_camp_screen_label.pack()
    setUp()

    view_camp_screen.mainloop()

viewcampScreen()