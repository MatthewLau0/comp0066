#Import Files
from tkinter import *

#Open the emergency database file and import camp names into a list
def openFile():
    global camp_name_list
    emergency_database_file = open("Emergency_Database", "r")
    emergency_database_list = []
    for line in emergency_database_file:
        line_list = line.split("%")
        emergency_database_list.append(line_list)
    emergency_database_file.close()

    camp_name_list = []
    for i in range (0, len(emergency_database_list)):
        camp_name_list.append((emergency_database_list[i])[1])

    campDropDown()

def campDropDown():
    global camp_name_list
    select_camp = StringVar()
    select_camp_label = Label(mock_screen, text="Please select a camp")
    select_camp_label.pack()
    select_camp_select = OptionMenu(mock_screen, select_camp, *camp_name_list)
    select_camp_select.pack()


#Mock screen creation - CHANGE SCREEN NAME
def mockScreen():
    global mock_screen
    mock_screen = Tk()
    mock_screen.geometry("500x650")
    mock_screen.title("Mock Screen")
    openFile()
    mock_screen.mainloop()

mockScreen()