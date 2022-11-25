#Import modules
from tkinter import *
from tkinter.ttk import *

#Define Functions
#Load Create new emergency
def Create_Emergency():
    import Create_New_Emergency_Plan_GUI

def Update_Emergency():
    import Update_Existing_Form_Admin_GUI

#Create main window of the application
admin_emergency = Tk()
admin_emergency.title("Admin Manage Emergencies")
admin_emergency_label = Label(admin_emergency, text="Use this section to Create or Update an Emergency within this Database.").pack()

#Add buttons to the window
create_new_emergency_frame = Frame(admin_emergency)
create_new_emergency_frame.pack()
create_new_emergency_button = Button(create_new_emergency_frame, text="Create New Emergency", command=Create_Emergency)
create_new_emergency_button.pack()
update_emergency_frame = Frame(admin_emergency)
update_emergency_frame.pack()
update_emergency_button = Button(update_emergency_frame, text="Update an Emergency", command=Update_Emergency())
update_emergency_button.pack()


admin_emergency.mainloop()
