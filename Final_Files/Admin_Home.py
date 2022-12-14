#Import modules
from tkinter import *
import Login

#Define Functions
#Load Create new emergency
def adminHome():
    global admin_home
    def Create_Emergency():
        from Admin_Create_Plan import createnewemergencyPlan
        createnewemergencyPlan(admin_home)

    def Update_Emergency():
        from Admin_Update_Plan import updateexistingForm
        updateexistingForm(admin_home)

    def Manage_Volunteers():
        from Admin_Manage_Volunteers import manageVolunteers
        manageVolunteers(admin_home)

    def View_Camps():
        from Admin_View_Plan import viewexistingCamps
        viewexistingCamps()

    #Create main window of the application
    admin_home = Tk()
    admin_home.title("Admin Home Page")

    screen_width = admin_home.winfo_screenwidth()
    screen_height = admin_home.winfo_screenheight()
    window_height = screen_height
    window_width = 900

    center_x = int(screen_width / 2 - window_width / 2)
    center_y = int(screen_height / 2 - window_height / 2)
    admin_home.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

    Label(admin_home, text="LAMSA", font=("Avenir", 80, "bold")).pack()
    Label(admin_home, text="Welcome to the Admin Portal.\n", font=("Avenir", 24)).pack()


    #Add buttons to the window
    create_new_emergency_frame = Frame(admin_home)
    create_new_emergency_frame.pack()
    create_new_emergency_button = Button(create_new_emergency_frame, text="Create New Emergency", command=Create_Emergency, width=30, height=2)
    create_new_emergency_button.pack()
    update_emergency_frame = Frame(admin_home)
    update_emergency_frame.pack()
    update_emergency_button = Button(update_emergency_frame, text="Update an Emergency", command=Update_Emergency, width=30, height=2)
    update_emergency_button.pack()
    manage_volunteers_frame = Frame(admin_home)
    manage_volunteers_frame.pack()
    manage_volunteers_button = Button(manage_volunteers_frame, text="Manage Volunteers", command=Manage_Volunteers, width=30, height=2)
    manage_volunteers_button.pack()
    view_camps_button = Button(manage_volunteers_frame, text="Summary of Existing Camps", command=View_Camps, width=30, height=2)
    view_camps_button.pack()
    Label(admin_home, text="\n").pack()
    exit_button = Button(admin_home, text="Log Out", command=lambda: [admin_home.destroy(), Login.main()], width=30, height=2)
    exit_button.pack()


    admin_home.mainloop()

