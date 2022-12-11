#Import modules
from tkinter import *

#Define Functions
#Load Create new emergency
def adminHome():
    def Create_Emergency():
        from Admin_Create_Plan import createnewemergencyPlan
        createnewemergencyPlan()

    def Update_Emergency():
        from Admin_Update_Plan import updateexistingForm
        updateexistingForm()

    def Manage_Volunteers():
        from Admin_Manage_Volunteers import manageVolunteers
        manageVolunteers()

    def View_Camps():
        from Admin_View_Plan import viewexistingCamps
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


    admin_home.mainloop()

