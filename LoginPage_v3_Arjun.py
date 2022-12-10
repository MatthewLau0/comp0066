# import modules

from distutils.command.config import config
from textwrap import wrap
from tkinter import *
from tkinter import messagebox
import hashlib
import volunteer_home_page_gui

from distutils.command.config import config
from tkinter import *
from tkinter import messagebox
import hashlib


# Functionality of user regi stration
def loginPage():
    def register_user():
        new_user = ["NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA"]
        # Gets user info from UI
        username_info_entry = username.get().encode()
        password_info_entry = password.get().encode()

        # Creating hashing object
        secret_username_info = hashlib.sha3_256(username_info_entry)
        secret_password_info = hashlib.sha3_256(password_info_entry)

        # getting binary hash from object
        username_hash = secret_username_info.hexdigest()
        password_hash = secret_password_info.hexdigest()


        file = open("volunteers.txt", "r")
        current_volunteer_list_1 = []
        for line in file:
            line_list = line.split("%")
            current_volunteer_list_1.append(line_list)

        if len(current_volunteer_list_1) == 0:
            new_user[1] = "1"
        elif len(current_volunteer_list_1) >= 1:
            new_user[1] = str((int((current_volunteer_list_1[-1])[1]) + 1))

        new_user[3] = username_hash
        new_user[4] = password_hash

        file.close()

        new_user_string = "%".join(new_user)

        volunteer_append = open("volunteers.txt", "a")

        volunteer_append.write("%s" %(new_user_string))
        volunteer_append.close()

        # Cleaning
        username_entry.delete(0, END)
        password_entry.delete(0, END)

        # Success message
        Label(register_screen, text="Registration Successful", fg="green", font=("calibri", 12)).pack()
        from Volunteer_List import volunteerList
        volunteerList(register_screen)

    # Functionality of user login
    def login_verify():
        # Gets username and password from UI
        username_string = username = username_verify.get()
        username = username_verify.get().encode()
        password = password_verify.get().encode()

        # Cleaning
        username_login_entry.delete(0, END)
        password_entry.delete(0, END)

        # Creating hashing object
        username_hash_obj = hashlib.sha3_256(username)
        password_hash_obj = hashlib.sha3_256(password)

        # getting binary hash from object
        username_hash = username_hash_obj.hexdigest()
        password_hash = password_hash_obj.hexdigest()

        login_success_bool = False
        try:
            # Checks all lines in username_info.txt
            file = open("volunteers.txt", "r")
            current_volunteer_list_2 = []
            for line in file:
                line_list = line.split("%")
                current_volunteer_list_2.append(line_list)

            logins_list = []
            for i in current_volunteer_list_2:
                string_user = i[3]
                string_password = i[4]
                string_login = str(string_user + string_password)
                logins_list.append(string_login)

            login_deets_string = str(username_hash + password_hash)
            print(logins_list)
            print(login_deets_string)

            if login_deets_string in logins_list:
                login_success_bool = True
                login_sucess()
                volunteer_home_page_gui.volunteer_home_page()
            if not login_success_bool:
                login_failure()
        except FileNotFoundError:
            login_failure()

    def check_user_active(username):
        for line in open("volunteers.txt", "r").readlines():
            lines = line.split('%')

            if lines[11] != "Active":
                continue

            return True

    # Designing window for registration
    def register():
        global register_screen
        register_screen = Toplevel(main_screen)
        register_screen.title("Register")
        register_screen.geometry("300x250")

        global username
        global password
        global username_entry
        global password_entry
        username = StringVar()
        password = StringVar()

        # Text Box - main
        Label(register_screen, text="Please enter details", bg="blue").pack()
        Label(register_screen, text="").pack()

        # Text Box - username
        username_label = Label(register_screen, text="Username * ")
        username_label.pack()

        # Username entry field
        username_entry = Entry(register_screen, textvariable=username)
        username_entry.pack()

        # Text Box - password
        password_label = Label(register_screen, text="Password * ")
        password_label.pack()

        # Password entry field
        password_entry = Entry(register_screen, textvariable=password, show='*')
        password_entry.pack()

        # Show/Hide Password Button
        global password_visability_btn
        password_visability_btn = Button(register_screen, text='Show', width=10, command=change_password_visability)
        password_visability_btn.pack(side=LEFT)

        # Register Button
        Label(register_screen, text="").pack()
        Button(register_screen, text="Register", width=10, height=1, bg="blue", command=register_user).pack()

    # Designing window for login
    def login():
        global login_screen
        login_screen = Toplevel(main_screen)
        login_screen.title("Login ")
        login_screen.geometry("300x250")

        # text box - main
        Label(login_screen, text="Please enter details").pack()
        Label(login_screen, text="").pack()

        global username_verify
        global password_verify

        username_verify = StringVar()
        password_verify = StringVar()

        global username_login_entry
        global password_entry

        # Username
        Label(login_screen, text="Username * ").pack()
        username_login_entry = Entry(login_screen, textvariable=username_verify)
        username_login_entry.pack()

        Label(login_screen, text="").pack()

        # Password
        Label(login_screen, text="Password * ").pack()
        password_entry = Entry(login_screen, textvariable=password_verify, show='*')
        password_entry.pack()

        # Password visability
        global password_visability_btn
        password_visability_btn = Button(login_screen, text='Show', width=10, command=change_password_visability)
        password_visability_btn.pack()

        # Button - login
        Label(login_screen, text="").pack()
        Button(login_screen, text="Login", width=10, height=1, command=login_verify).pack()

    # Show Password button functionailty
    def change_password_visability():
        # Check if password is hidden
        if password_entry.cget('show') == '*':
            # show password
            password_entry.config(show='')
            password_visability_btn.config(text='Hide')
        # Check if password is visable
        elif password_entry.cget('show') == '':
            # Hide password
            password_entry.config(show='*')
            password_visability_btn.config(text='Show')
        else:
            # Error catching
            messagebox.messagebox.showerror('Error:', 'Invalid visability state of password feild.')

    # Designing popup for login success
    def login_sucess():
        global login_success_screen
        login_success_screen = Toplevel(login_screen)
        login_success_screen.title("Success")
        login_success_screen.geometry("150x100")
        Label(login_success_screen, text="Login Success").pack()
        Button(login_success_screen, text="OK", command=main_screen.destroy).pack()

    # Designing popup for login failure
    def login_failure():
        global password_not_recog_screen
        password_not_recog_screen = Toplevel(login_screen)
        password_not_recog_screen.title("Failure")
        password_not_recog_screen.geometry("250x100")
        Label(password_not_recog_screen, wraplength=200,text="Invalid Login Information or User Not Activated: Please try again or contact system administrator.").pack()
        Button(password_not_recog_screen, text="OK", command=password_not_recog_screen.destroy).pack()


    # Designing Main(first) window
    def main_account_screen():
        global main_screen
        main_screen = Tk()
        main_screen.geometry("300x250")
        main_screen.title("Account Login")
        Label(text="Select Your Choice", bg="blue", width="300", height="2", font=("Calibri", 13)).pack()
        Label(text="").pack()
        Button(text="Login", height="2", width="30", command=login).pack()
        Label(text="").pack()
        Button(text="Register", height="2", width="30", command=register).pack()

        main_screen.mainloop()

    #Open the emergency database file and import camp names into a list
    def activationStatusFileChecker():
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
        select_camp_label = Label(camp_drop_down_screen, text="Please select a camp")
        select_camp_label.pack()
        select_camp_select = OptionMenu(camp_drop_down_screen, select_camp, *camp_name_list)
        select_camp_select.pack()


    #Camp Drop Down Screen Creation
    def campDropDownScreen():
        global camp_drop_down_screen
        camp_drop_down_screen = Tk()
        camp_drop_down_screen.geometry("500x650")
        camp_drop_down_screen.title("Mock Screen")
        activationStatusFileChecker()
        camp_drop_down_screen.mainloop()

    main_account_screen()

loginPage()