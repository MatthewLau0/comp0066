from tkinter import *
import Login


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

    def userGuide():
        app_info_screen = Toplevel(admin_home)
        app_info_screen.title("User Guide")
        app_info_screen.geometry("1200x750")

        Label(app_info_screen, text="\nCreate New Emergency Camp").pack()

        Label(app_info_screen, text="\nThis page can be used when a new emergency has occured, and you need to create a new camp for volunteers to assign refugees affected by the emergency. \nHere you can create a camp name, register the type of emergency, description of the emergency, area affected, start date and activation status.").pack()

        Label(app_info_screen, text="\nUpdate Existing Emergency Camp").pack()

        Label(app_info_screen, text="\nThis page can be used to update the details of an existing emergency camp. \nAll details (except for camp name and camp ID, which are unique to each camp) can be updated. \n Importantly, you can update the status to close the emergency if the situation has resolved.").pack()

        Label(app_info_screen, text="\nManage Volunteers").pack()

        Label(app_info_screen, text="\nThis page can be used to view all the volunteers currently in the LAMSA database across all camps.\n You can also use this page to activate, deactivate and delete volunteer accounts.").pack()

        Label(app_info_screen, text="\nSummary of Existing Camps").pack()

        Label(app_info_screen, text="\nThis page can be used to view all of the current camps that are in the LAMSA database, to view the layout of an individual camp \n(including medical supplies, rations, toilets and accommodation) and to view the refugees currently in the camp.\n\n").pack()

        back_button = Button(app_info_screen, text="Close", command=app_info_screen.destroy)
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
    Label(admin_home, text="LAMSA", font=("TkDefaultFont", 80, "bold")).pack()
    Label(admin_home, text="Welcome to the Admin Home Page\n", font=("TkDefaultFont", 24)).pack()

    create_new_emergency_button = Button(admin_home, text="Create New Emergency Camp", command=Create_Emergency)
    create_new_emergency_button.pack()
    update_emergency_button = Button(admin_home, text="Update Existing Emergency Camp", command=Update_Emergency)
    update_emergency_button.pack()
    manage_volunteers_button = Button(admin_home, text="Manage Volunteers", command=Manage_Volunteers)
    manage_volunteers_button.pack()
    view_camps_button = Button(admin_home, text="Summary of Existing Camps", command=View_Camps)
    view_camps_button.pack()
    user_guide_button = Button(admin_home, text="User Guide", command=userGuide)
    user_guide_button.pack()

    def admin_home_destroy():
        admin_home.destroy()
        Login.main()
    exit_button = Button(admin_home, text="Log Out", command=admin_home_destroy)
    exit_button.pack()

    admin_home.mainloop()

adminHome()