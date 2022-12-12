#Import modules
from tkinter import *
import sys
import subprocess
import pycountry
subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'tkcalendar'])
subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'tkintermapview'])
import os
from tkcalendar import Calendar
import datetime

#Define Functions
#Load Create new emergency
def Create_Emergency():
    from Create_New_Emergency_Plan_GUI import createnewemergencyPlan
    createnewemergencyPlan()

def Update_Emergency():
    from Update_Existing_Form_Admin_GUI import updateexistingForm
    updateexistingForm()

def Manage_Volunteers():
    import volunteer_create_family_gui

def View_Camps():
    from view_existing_camps_GUI import viewexistingCamps
    viewexistingCamps()

#Create main window of the application
admin_home = Tk()
admin_home.geometry("500x650")
admin_home.title("Admin Home Page")
admin_home_label = Label(admin_home, text="Welcome to the admin homepage.")
admin_home_label.pack()

#Add buttons to the window
create_new_emergency_frame = Frame(admin_home)
create_new_emergency_frame.pack()
create_new_emergency_button = Button(create_new_emergency_frame, text="Create New Emergency", command=Create_Emergency)
create_new_emergency_button.pack()
update_emergency_frame = Frame(admin_home)
update_emergency_frame.pack()
update_emergency_button = Button(update_emergency_frame, text="Update an Emergency", command=Update_Emergency)
update_emergency_button.pack()
manage_volunteers_frame = Frame(admin_home)
manage_volunteers_frame.pack()
manage_volunteers_button = Button(manage_volunteers_frame, text="Manage Volunteers", command=Manage_Volunteers)
manage_volunteers_button.pack()
view_camps_button = Button(manage_volunteers_frame, text="Summary of Existing Camps", command=View_Camps)
view_camps_button.pack()
print(list(pycountry.countries))

admin_home.mainloop()


