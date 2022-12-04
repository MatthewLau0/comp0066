import volunteer_view_family_gui
import tkinter
import datetime
import subprocess
import sys
import tkcalendar
subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'tkcalendar'])
subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'tkintermapview'])

def delete1():
    screen1.destroy()
def error_one():
    global screen1
    screen1 = tkinter.Toplevel(update_screen)
    screen1.geometry("300x120")
    screen1.title("Warning!")
    noinput_error_text = tkinter.Label(screen1, text="Please select an index!", fg='red')
    noinput_error_text.place(x=80, y=30)
    close_button = tkinter.Button(screen1, text="I understand", command=delete1)
    close_button.place(x=95, y=80)
def confirm_update():
    if refugee_button.get() == '':
        error_one()
        return
    else:
        update_current_refugee = tkinter.Toplevel(update_screen)
        update_current_refugee.title("Updating refugee")
        update_current_refugee.geometry("500x1000")

        refugee_index_var = refugee_button.get()
        refugee_index = int(refugee_index_var) - 1




# Opening current database and reading it into a list
volunteer_list_file = open("Volunteer_Database", "r")
volunteer_database_list = []
for line in volunteer_list_file:
    x = line.split("#")
    volunteer_database_list.append(x)

volunteer_database_list_index = []
for i in range(0, len(volunteer_database_list)):
    volunteer_database_list_index.append((volunteer_database_list[i])[0])
    i += 1

update_screen = tkinter.Toplevel()
update_screen.geometry("500x1000")
update_screen.title("Update Refugee Information")

update_refugee_label = tkinter.Label(update_screen, text = "You are going to update a refugee")
update_refugee_label.pack()

global Update_Emergency_Screen
global emergency_database_list
global View_Table_Yes
global Index_Known_No
global emergency_database_table
global update_emergency_frame_two

emergency_database_label = tkinter.Label(update_screen, text="Please use the below table to find the Refugee ID")
emergency_database_label.pack()

emergency_database_frame = tkinter.Frame(update_screen)
emergency_database_frame.pack()

emergency_database_table = tkinter.ttk.Treeview(update_screen)

emergency_database_table['columns'] = ("Refugee ID", "Name", "Family members", "Date of Birth", "Age", "Sex", "Address", "Weight", "Height")

emergency_database_table.column("#0", width=0, stretch='NO')
emergency_database_table.column("Refugee ID", anchor='center', width=70)
emergency_database_table.column("Name", anchor='center', width=100)
emergency_database_table.column("Family members", anchor='center', width=100)
emergency_database_table.column("Date of Birth", anchor='center', width=100)
emergency_database_table.column("Age", anchor='center', width=30)
emergency_database_table.column("Sex", anchor='center', width=70)
emergency_database_table.column("Address", anchor='center', width=300)
emergency_database_table.column("Weight", anchor='center', width=60)
emergency_database_table.column("Height", anchor='center', width=60)

emergency_database_table.heading("Refugee ID", text="Refugee ID", anchor='center')
emergency_database_table.heading("Name", text="Name", anchor='center')
emergency_database_table.heading("Family members", text="Family members", anchor='center')
emergency_database_table.heading("Date of Birth", text="Date of Birth", anchor='center')
emergency_database_table.heading("Age", text="Age", anchor='center')
emergency_database_table.heading("Sex", text="Sex", anchor='center')
emergency_database_table.heading("Address", text="Address", anchor='center')
emergency_database_table.heading("Weight", text="Weight", anchor='center')
emergency_database_table.heading("Height", text="Height", anchor='center')



emergency_database_table.pack(pady = 20)

for i in range(0, len(volunteer_database_list)):
    emergency_database_table.insert(parent='', index=i, iid=i, values=(
    volunteer_database_list[i][0], str(volunteer_database_list[i][1]), volunteer_database_list[i][2],
    volunteer_database_list[i][3], volunteer_database_list[i][4], volunteer_database_list[i][5],
    volunteer_database_list[i][6], volunteer_database_list[i][7], volunteer_database_list[i][8]))
    i += 1




choose_refugee_label = tkinter.Label(update_screen, text = 'Please enter the ID of the refugee to update: ')
choose_refugee_label.pack(pady = 20)

refugee_button = tkinter.StringVar()
choose_refugee_button = tkinter.OptionMenu(update_screen, refugee_button, *volunteer_database_list_index)
choose_refugee_button.pack()

confirm_refugee_button = tkinter.Button(update_screen, text = "Submit", command = confirm_update)
confirm_refugee_button.pack()


update_screen.mainloop()


