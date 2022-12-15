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

    def userGuide():
        global admin_home

        app_info_screen = Toplevel(admin_home)
        app_info_screen.title("User Guide")
        app_info_screen.geometry("1200x750")


        Label(app_info_screen, text="\nHow to use the Admin Homepage", font=("Avenir", 44)).pack()

        Label(app_info_screen, text="\nCreate New Emergency Camp", font=("Avenir", 24, "bold")).pack()

        Label(app_info_screen, text="\nThis page can be used when a new emergency has occured, and you need to create a new camp for volunteers to assign refugees affected by the emergency. \nHere you can create a camp name, register the type of emergency, description of the emergency, area affected, start date and activation status.").pack()

        Label(app_info_screen, text="\nUpdate Existing Emergency Camp", font=("Avenir", 24, "bold")).pack()

        Label(app_info_screen, text="\nThis page can be used to update the details of an existing emergency camp. \nAll details (except for camp name and camp ID, which are unique to each camp) can be updated. \n Importantly, you can update the status to close the emergency if the situation has resolved.").pack()

        Label(app_info_screen, text="\nManage Volunteers", font=("Avenir", 24, "bold")).pack()

        Label(app_info_screen, text="\nThis page can be used to view all the volunteers currently in the LAMSA database across all camps.\n You can also use this page to activate, deactivate and delete volunteer accounts.").pack()

        Label(app_info_screen, text="\nSummary of Existing Camps", font=("Avenir", 24, "bold")).pack()

        Label(app_info_screen, text="\nThis page can be used to view all of the current camps that are in the LAMSA database, to view the layout of an individual camp \n(including medical supplies, rations, toilets and accommodation) and to view the refugees currently in the camp.\n\n").pack()

        back_button = Button(app_info_screen, text="Close", command=app_info_screen.destroy, width=30, height=2)
        back_button.pack()

    admin_home = Tk()
    admin_home.title("Admin Home Page")

    screen_width1 = admin_home.winfo_screenwidth()
    screen_height1 = admin_home.winfo_screenheight()
    window_height1 = screen_height1
    window_width1 = 900

    center_x1 = int(screen_width1 / 2 - window_width1 / 2)
    center_y1 = int(screen_height1 / 2 - window_height1 / 2)
    admin_home.geometry(f'{window_width1}x{window_height1}+{center_x1}+{center_y1}')
    Label(admin_home, text="LAMSA", font=("Avenir", 80, "bold")).pack()
    Label(admin_home, text="Welcome to the Admin Home Page", font=("Avenir", 18)).pack()

    create_new_emergency_frame = Frame(admin_home)
    create_new_emergency_frame.pack()
    create_new_emergency_button = Button(create_new_emergency_frame, text="Create New Emergency Camp", command=Create_Emergency, width=30, height=2)
    create_new_emergency_button.pack()
    update_emergency_frame = Frame(admin_home)
    update_emergency_frame.pack()
    update_emergency_button = Button(update_emergency_frame, text="Update Existing Emergency Camp", command=Update_Emergency, width=30, height=2)
    update_emergency_button.pack()
    manage_volunteers_frame = Frame(admin_home)
    manage_volunteers_frame.pack()
    manage_volunteers_button = Button(manage_volunteers_frame, text="Manage Volunteers", command=Manage_Volunteers, width=30, height=2)
    manage_volunteers_button.pack()
    view_camps_button = Button(manage_volunteers_frame, text="Summary of Existing Camps", command=View_Camps, width=30, height=2)
    view_camps_button.pack()
    user_guide_button = Button(manage_volunteers_frame, text="User Guide", command=userGuide, width=30, height=2)
    user_guide_button.pack()
    exit_button = Button(admin_home, text="Log Out", command=lambda: [admin_home.destroy(), Login.main()], width=30, height=2)
    exit_button.pack()


    admin_home.mainloop()

adminHome()