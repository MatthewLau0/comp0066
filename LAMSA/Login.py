from tkinter import *
import hashlib
import Clean_Database


def main():
    Clean_Database.clean_volunteer_database()
    Clean_Database.clean_login_database()

    master_window = Tk()
    master_window.title("Home")

    screen_width = master_window.winfo_screenwidth()
    screen_height = master_window.winfo_screenheight()
    window_height = screen_height
    window_width = 900

    center_x = int(screen_width / 2 - window_width / 2)
    center_y = int(screen_height / 2 - window_height / 2)
    master_window.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

    Label(master_window, text="\nWelcome to", font=("TkDefaultFont", 22)).pack()
    Label(master_window, text="LAMSA", font=("TkDefaultFont", 80, "bold")).pack()
    Label(master_window, text="A State of the Art", font=("TkDefaultFont", 18)).pack()
    Label(master_window, text="Humanitarian Emergency Management System\n\n\n", font=("TkDefaultFont", 22, "bold")).pack()

    def main_signin_screen():
        master_window.destroy()
        main_window = Tk()
        main_window.title("Sign In")

        Label(main_window, text="\n\nLAMSA", font=("TkDefaultFont", 80, "bold")).pack()

        screen_width1 = main_window.winfo_screenwidth()
        screen_height1 = main_window.winfo_screenheight()
        window_height1 = screen_height1
        window_width1 = 900

        center_x1 = int(screen_width1 / 2 - window_width1 / 2)
        center_y1 = int(screen_height1 / 2 - window_height1 / 2)
        main_window.geometry(f'{window_width1}x{window_height1}+{center_x1}+{center_y1}')

        def register_volunteer():
            import Register_Info
            Clean_Database.clean_volunteer_database()
            Clean_Database.clean_login_database()
            main_window.destroy()
            register_screen = Tk()
            register_screen.title("Register")

            Label(register_screen, text="\nLAMSA", font=("TkDefaultFont", 80, "bold")).pack()

            screen_width2 = register_screen.winfo_screenwidth()
            screen_height2 = register_screen.winfo_screenheight()
            window_height2 = screen_height1
            window_width2 = 900

            center_x2 = int(screen_width2 / 2 - window_width2 / 2)
            center_y2 = int(screen_height2 / 2 - window_height2 / 2)
            register_screen.geometry(f'{window_width2}x{window_height2}+{center_x2}+{center_y2}')

            username = StringVar()
            password = StringVar()
            confirm_password = StringVar()

            register_label = Label(register_screen, text="Please enter a username and password below")
            register_label.pack()

            username_label = Label(register_screen, text="Username*")
            username_label.pack()

            username_entry = Entry(register_screen, textvariable=username)
            username_entry.pack()

            password_label = Label(register_screen, text="Password*")
            password_label.pack()

            password_entry = Entry(register_screen, textvariable=password, show="*")
            password_entry.pack()

            confirm_password_label = Label(register_screen, text="Confirm Password*")
            confirm_password_label.pack()

            confirm_password_entry = Entry(register_screen, textvariable=confirm_password, show="*")
            confirm_password_entry.pack()

            def change_password_visibility():
                if password_entry.cget('show') == '*':
                    password_entry.config(show='')
                    confirm_password_entry.config(show='')
                    password_visibility_btn.config(text='Hide Passwords')
                elif password_entry.cget('show') == '':
                    password_entry.config(show='*')
                    confirm_password_entry.config(show='*')
                    password_visibility_btn.config(text='Show Passwords')

            requirements_label = Label(register_screen, text="\nUsername and Password must not contain any spaces. \nUsername and Password must not contain the '%' sign \nUsername and Password must be at least 3 characters long \nPassword must contain at least one number\n")
            requirements_label.pack()

            password_visibility_btn = Button(register_screen, text='Show Passwords', command=change_password_visibility)
            password_visibility_btn.pack()

            error_count = []

            def register_check():

                error_count.clear()

                register_errors = Toplevel()
                register_errors.title("Register Errors")

                if " " in username.get():
                    username_error1 = Label(register_errors, text="Please enter a username without any spaces")
                    username_error1.pack()
                    error_count.append("u1")

                if "%" in username.get():
                    username_error2 = Label(register_errors, text="Please enter a username without the '%' sign")
                    username_error2.pack()
                    error_count.append("u2")

                if len(username.get()) <= 2:
                    username_error4 = Label(register_errors, text="Username is too short. Minimum length is 3 characters")
                    username_error4.pack()
                    error_count.append("u4")

                volunteers_file = open("volunteer_database.txt", "r")

                volunteer_list = []
                for line in volunteers_file:
                    line_split = line.split("%")
                    volunteer_list.append(line_split)

                volunteers_file.close()

                username_list = []
                for i in volunteer_list:
                    if i[10] == "Deleted":
                        pass
                    else:
                        username_list.append(i[3])

                if username.get() in username_list:
                    username_error3 = Label(register_errors, text="Username is taken. Please try again")
                    username_error3.pack()
                    error_count.append("u3")

                if password.get() == confirm_password.get():
                    if len(password.get()) <= 2:
                        password_error1 = Label(register_errors, text="Password is too short. Minimum length is 3 characters")
                        password_error1.pack()
                        error_count.append("p1")

                    def has_number(input_string):
                        return any(char.isdigit() for char in input_string)
                    if has_number(password.get()) is False:
                        password_error2 = Label(register_errors, text="Password must contain at least one number")
                        password_error2.pack()
                        error_count.append("p2")

                    if " " in password.get():
                        password_error3 = Label(register_errors, text="Please enter a password without any spaces")
                        password_error3.pack()
                        error_count.append("p3")

                    if "%" in password.get():
                        password_error5 = Label(register_errors, text="Please enter a password without the '%' sign")
                        password_error5.pack()
                        error_count.append("p5")

                else:
                    password_error4 = Label(register_errors, text="Passwords do not match. Please try again")
                    password_error4.pack()
                    error_count.append("p4")

                r_close_button1 = Button(register_errors, text="Close", command=register_errors.destroy)
                r_close_button1.pack()

                if len(error_count) > 0:
                    register_errors.mainloop()
                else:
                    register_errors.destroy()

                    global verified_username

                    verified_username = username.get()
                    verified_password = password.get()

                    def encrypt_password(p):
                        password_info_entry = p.encode()
                        secret_password_info = hashlib.sha3_256(password_info_entry)
                        return secret_password_info.hexdigest()

                    password_hash = encrypt_password(verified_password)

                    new_user = ["NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA"]

                    file = open("volunteer_database.txt", "r")
                    current_volunteer_list_1 = []
                    for line in file:
                        line_list = line.split("%")
                        current_volunteer_list_1.append(line_list)

                    file.close()

                    if len(current_volunteer_list_1) == 0:
                        new_user[1] = "1"
                    elif len(current_volunteer_list_1) >= 1:
                        new_user[1] = str((int((current_volunteer_list_1[-1])[1]) + 1))

                    new_user[3] = verified_username
                    new_user[4] = password_hash
                    new_user[10] = "Deactivated"
                    new_user[11] = "Standard"
                    new_user[12] = "0000-00-00#0000-00-00########"

                    new_user_string = "%".join(new_user)

                    volunteer_append = open("volunteer_database.txt", "a")

                    volunteer_append.write(f"\n{new_user_string}")
                    volunteer_append.close()

                    register_screen.destroy()
                    Register_Info.volunteerList()

            register_button1 = Button(register_screen, text="Register", command=register_check)
            register_button1.pack()
            back_button_1 = Button(register_screen, text="Home", command=lambda: [register_screen.destroy(), main()])
            back_button_1.pack()

            register_screen.mainloop()

        def volunteer_login():

            import Camp_Lead

            Clean_Database.clean_volunteer_database()
            Clean_Database.clean_login_database()

            choose_role_window.destroy()
            volunteer_login_screen = Tk()
            volunteer_login_screen.title("Login")

            Label(volunteer_login_screen, text="\nLAMSA", font=("TkDefaultFont", 80, "bold")).pack()

            screen_width2 = volunteer_login_screen.winfo_screenwidth()
            screen_height2 = volunteer_login_screen.winfo_screenheight()
            window_height2 = screen_height1
            window_width2 = 900

            center_x2 = int(screen_width2 / 2 - window_width2 / 2)
            center_y2 = int(screen_height2 / 2 - window_height2 / 2)
            volunteer_login_screen.geometry(f'{window_width2}x{window_height2}+{center_x2}+{center_y2}')

            Label(volunteer_login_screen, text="Volunteer & Camp Lead Login", font=("TkDefaultFont", 20)).pack()
            Label(volunteer_login_screen, text="Please enter your login details below\n").pack()

            username_entry = StringVar()
            password_entry = StringVar()

            Label(volunteer_login_screen, text="Username* ").pack()
            username_login_entry = Entry(volunteer_login_screen, textvariable=username_entry)
            username_login_entry.pack()

            Label(volunteer_login_screen, text="Password* ").pack()
            password_entry = Entry(volunteer_login_screen, textvariable=password_entry, show='*')
            password_entry.pack()

            Label(volunteer_login_screen, text="").pack()

            def change_password_visibility():
                if password_entry.cget('show') == '*':
                    password_entry.config(show='')
                    password_visibility_btn.config(text='Hide Password')
                elif password_entry.cget('show') == '':
                    password_entry.config(show='*')
                    password_visibility_btn.config(text='Show Password')

            password_visibility_btn = Button(volunteer_login_screen, text='Show Password', command=change_password_visibility)
            password_visibility_btn.pack()

            def check_login_entry():
                import Volunteer_Home

                def encrypt_password(p):
                    password_info_entry = p.encode()
                    secret_password_info = hashlib.sha3_256(password_info_entry)
                    return secret_password_info.hexdigest()

                password_hash = encrypt_password(password_entry.get())

                file = open("volunteer_database.txt", "r")
                current_volunteer_list_2 = []
                for line in file:
                    line_list = line.split("%")
                    current_volunteer_list_2.append(line_list)
                file.close()

                file1 = open("emergency_database.txt", "r")
                current_camp_list = []
                for line1 in file1:
                    line_list1 = line1.split("%")
                    current_camp_list.append(line_list1)
                file1.close()

                camp_status = []
                logins_list = []
                logins_status_list = []
                camp_lead_list = []
                usernames_list = []
                camp_lead_list.clear()
                camp_status.clear()
                for i in current_volunteer_list_2:
                    string_user = i[3]
                    string_password = i[4]
                    string_status = i[10]
                    string_camp = i[0]
                    string_camp_id = int(string_camp)-1
                    if current_camp_list[string_camp_id][7] == "Closed":
                        camp_status.append(string_user)
                    if i[10] == "Deleted":
                        pass
                    else:
                        usernames_list.append(string_user)
                    string_login = str(string_user + string_password)
                    string_login_status = str(string_user + string_password + string_status)
                    logins_list.append(string_login)
                    logins_status_list.append(string_login_status)
                    if i[11] == "Lead":
                        camp_lead_list.append(string_login)

                login_entry_string = str(username_entry.get() + password_hash)
                login_entry_status_string = str(username_entry.get() + password_hash + "Active")

                login_error_window = Toplevel()

                if (login_entry_string in logins_list) and (login_entry_status_string not in logins_status_list) and (username_entry.get() in usernames_list):
                    deactivated_label = Label(login_error_window, text="Your Account has been Deactivated\nPlease contact the admin for support")
                    deactivated_label.pack()
                    close_button1 = Button(login_error_window, text="Close", command=login_error_window.destroy)
                    close_button1.pack()
                    login_error_window.mainloop()
                elif username_entry.get() not in usernames_list:
                    wrong_detail_label = Label(login_error_window, text="Username does not exist, or Account has been deleted. Please Register")
                    wrong_detail_label.pack()
                    close_button2 = Button(login_error_window, text="Close", command=login_error_window.destroy)
                    close_button2.pack()
                    login_error_window.mainloop()
                elif (username_entry.get() in usernames_list) and (login_entry_string not in logins_list):
                    wrong_password_label = Label(login_error_window, text="Username exists. Wrong Password entered.")
                    wrong_password_label.pack()
                    close_button3 = Button(login_error_window, text="Close", command=login_error_window.destroy)
                    close_button3.pack()
                    login_error_window.mainloop()
                elif username_entry.get() in camp_status:
                    camp_closed_label = Label(login_error_window, text="This Camp has now been closed. Please conatct the admin for more details")
                    camp_closed_label.pack()
                    close_button4 = Button(login_error_window, text="Close", command=login_error_window.destroy)
                    close_button4.pack()
                    login_error_window.mainloop()
                elif (login_entry_string in logins_list) and (login_entry_status_string in logins_status_list):
                    for i in current_volunteer_list_2:
                        if i[3] == username_entry.get():
                            string = "%".join(i)
                            with open("successful_login.txt", "a") as login_s:
                                login_s.write(f"\n{string}")
                    login_s.close()
                    if login_entry_string not in camp_lead_list:
                        volunteer_login_screen.destroy()
                        Volunteer_Home.volunteer_home_page()
                    if login_entry_string in camp_lead_list:
                        volunteer_login_screen.destroy()
                        Camp_Lead.camp_id_generate()
                        Camp_Lead.run_camp_lead()
                else:
                    unknown_error_label_2 = Label(login_error_window, text="An unknown error has occurred. Please try again")
                    unknown_error_label_2.pack()
                    close_button4 = Button(login_error_window, text="Close", command=login_error_window.destroy)
                    close_button4.pack()
                    login_error_window.mainloop()

            done_button = Button(volunteer_login_screen, text="Login", command=check_login_entry)
            done_button.pack()
            back_button_2 = Button(volunteer_login_screen, text="Home", command=lambda: [volunteer_login_screen.destroy(), main()])
            back_button_2.pack()

            volunteer_login_screen.mainloop()

        def admin_login():
            import Admin_Home
            choose_role_window.destroy()
            admin_login_screen = Tk()
            admin_login_screen.title("Admin Login")

            Label(admin_login_screen, text="\nLAMSA", font=("TkDefaultFont", 80, "bold")).pack()

            screen_width2 = admin_login_screen.winfo_screenwidth()
            screen_height2 = admin_login_screen.winfo_screenheight()
            window_height2 = screen_height1
            window_width2 = 900

            center_x2 = int(screen_width2 / 2 - window_width2 / 2)
            center_y2 = int(screen_height2 / 2 - window_height2 / 2)
            admin_login_screen.geometry(f'{window_width2}x{window_height2}+{center_x2}+{center_y2}')

            Label(admin_login_screen, text="Admin Login", font=("TkDefaultFont", 20)).pack()
            Label(admin_login_screen, text="Please enter your login details below\n").pack()

            admin_username_entry = StringVar()
            admin_password_entry = StringVar()

            Label(admin_login_screen, text="Username* ").pack()
            username_login_entry = Entry(admin_login_screen, textvariable=admin_username_entry)
            username_login_entry.pack()

            Label(admin_login_screen, text="Password* ").pack()
            password_entry = Entry(admin_login_screen, textvariable=admin_password_entry, show='*')
            password_entry.pack()

            Label(admin_login_screen, text="").pack()

            def change_password_visibility():
                if password_entry.cget('show') == '*':
                    password_entry.config(show='')
                    password_visibility_btn.config(text='Hide Password')
                elif password_entry.cget('show') == '':
                    password_entry.config(show='*')
                    password_visibility_btn.config(text='Show Password')

            password_visibility_btn = Button(admin_login_screen, text='Show Password',
                                             command=change_password_visibility)
            password_visibility_btn.pack()

            def check_login_entry():

                file = open("admin_login.txt", "r")
                admin_login_list = []
                for line in file:
                    line_list = line.split("%")
                    admin_login_list.append(line_list)

                file.close()

                logins_list = []
                for i in admin_login_list:
                    string_user = i[0]
                    string_password = i[1]
                    string_login = str(string_user + string_password)
                    logins_list.append(string_login)

                login_entry_string = str(admin_username_entry.get() + admin_password_entry.get())

                admin_login_error_window = Toplevel()

                if login_entry_string not in logins_list:
                    wrong_detail_label = Label(admin_login_error_window, text="Wrong details entered. Please try again")
                    wrong_detail_label.pack()
                    close_button2 = Button(admin_login_error_window, text="Close", command=admin_login_error_window.destroy)
                    close_button2.pack()
                    admin_login_error_window.mainloop()
                elif login_entry_string in logins_list:
                    admin_login_screen.destroy()
                    Admin_Home.adminHome()
                else:
                    unknown_error_label = Label(admin_login_error_window, text="An unknown error has occurred. Please try again")
                    unknown_error_label.pack()
                    close_button3 = Button(admin_login_error_window, text="Close", command=admin_login_error_window.destroy)
                    close_button3.pack()
                    admin_login_error_window.mainloop()

            done_button = Button(admin_login_screen, text="Login", command=check_login_entry)
            done_button.pack()
            back_button_4 = Button(admin_login_screen, text="Home", command=lambda: [admin_login_screen.destroy(), main()])
            back_button_4.pack()

            admin_login_screen.mainloop()

        def choose_role():
            Clean_Database.clean_volunteer_database()
            Clean_Database.clean_login_database()
            global choose_role_window
            main_window.destroy()
            choose_role_window = Tk()
            choose_role_window.title("Login")

            Label(choose_role_window, text="\n\nLAMSA", font=("TkDefaultFont", 80, "bold")).pack()

            screen_width2 = choose_role_window.winfo_screenwidth()
            screen_height2 = choose_role_window.winfo_screenheight()
            window_height2 = screen_height2
            window_width2 = 900

            center_x2 = int(screen_width2 / 2 - window_width2 / 2)
            center_y2 = int(screen_height2 / 2 - window_height2 / 2)
            choose_role_window.geometry(f'{window_width2}x{window_height2}+{center_x2}+{center_y2}')

            volunteer_button = Button(choose_role_window, text="Volunteer & Camp Lead Login", command=volunteer_login)
            volunteer_button.pack()
            admin_button = Button(choose_role_window, text="Admin Login", command=admin_login)
            admin_button.pack()
            back_button_5 = Button(choose_role_window, text="Home", command=lambda: [choose_role_window.destroy(), main()])
            back_button_5.pack()

            choose_role_window.mainloop()

        login_button = Button(main_window, text="Login", command=choose_role)
        login_button.pack()

        register_button = Button(main_window, text="Register", command=register_volunteer)
        register_button.pack()

        back_button = Button(main_window, text="Back", command=lambda: [main_window.destroy(), main()])
        back_button.pack()

        main_window.mainloop()

    def app_info():
        app_info_screen = Toplevel(master_window)
        app_info_screen.title("How to Use")

        screen_width3 = app_info_screen.winfo_screenwidth()
        screen_height3 = app_info_screen.winfo_screenheight()
        window_height3 = screen_height3
        window_width3 = 800

        center_x3 = int(screen_width3 / 2 - window_width3 / 2)
        center_y3 = int(screen_height3 / 2 - window_height3 / 2)
        app_info_screen.geometry(f'{window_width3}x{window_height3}+{center_x3}+{center_y3}')

        Label(app_info_screen, text="\nHow to Use LAMSA", font=("TkDefaultFont", 44)).pack()

        Label(app_info_screen, text="LAMSA is a state of the art humanitarian system, to facilitate a global "
                                    "co-ordinated response to emergencies and disasters.\n\n\n").pack()

        Label(app_info_screen, text="\nAdmin", font=("TkDefaultFont", 24, "bold")).pack()

        Label(app_info_screen, text="The admin is able to manage the entire database globally.\n They can view "
                                    "register a new emergency that has occurred, update this emergency, "
                                    "view and manage \nthe volunteers around the world, and view a summary of "
                                    "all camps and refugees.\n\n\n").pack()

        Label(app_info_screen, text="\nCamp Lead", font=("TkDefaultFont", 24, "bold")).pack()

        Label(app_info_screen, text="A camp lead will run the administrative side of the camp to which they are "
                                    "assigned.\n In addition to managing the volunteers within their camp, "
                                    "they are able to register any additional amenities \nthat their camp receives ("
                                    "e.g., accommodation, rations, medical supplies) as well as their capacity \n and "
                                    "current occupancy.\n\n\n").pack()

        Label(app_info_screen, text="\nVolunteer", font=("TkDefaultFont", 24, "bold")).pack()

        Label(app_info_screen, text="A standard volunteer's primary role is the management of refugees within their "
                                    "camp.\n They are able to add refugees, assign them to amenities made available "
                                    "by a camp lead, and \n to view a list of refugees currently in their camp.\n In "
                                    "addition to this, volunteers are able to use our system to manage their own "
                                    "availability and details.\n\n\n").pack()

        back_button = Button(app_info_screen, text="Close", command=app_info_screen.destroy)
        back_button.pack()

        app_info_screen.mainloop()

    signin = Button(master_window, text="Sign In", command=main_signin_screen)
    signin.pack()
    info = Button(master_window, text="How to use this Application", command=app_info)
    info.pack()
    exit_app = Button(master_window, text="Exit Application", command=exit)
    exit_app.pack()

    master_window.mainloop()


if __name__ == '__main__':
    main()
