from tkinter import *
import Login
import Admin_Update_Plan
import Admin_View_Plan
import Admin_Update_Plan
import Admin_Manage_Volunteers
import Camp_Lead
import Volunteer_Create_Family
import Volunteer_View_Family
import Volunteer_Update_Family
import Volunteer_Settings

master_window = Tk()

def app_info():
    pass

signin = Button(master_window, text="Sign In", command=Login.main_signin_screen)
signin.pack()
info = Button(master_window, text="How to use this Application", command=app_info)
info.pack()

master_window.mainloop()

