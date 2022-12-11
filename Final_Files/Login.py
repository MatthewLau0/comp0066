from tkinter import *
import hashlib
import Register_Info
import Volunteer_Home


def main_signin_screen():
    main_window = Toplevel()

    def register_volunteer():
        main_window.destroy()
        register_screen = Toplevel()
        register_screen.title("Register")
        register_screen.geometry("300x250")

        username = StringVar()
        password = StringVar()
        confirm_password = StringVar()

        register_label = Label(register_screen, text="Please enter a username and password below")
        register_label.pack()

        username_label = Label(register_screen, text="Username")
        username_label.pack()

        username_entry = Entry(register_screen, textvariable=username)
        username_entry.pack()

        password_label = Label(register_screen, text="Password")
        password_label.pack()

        password_entry = Entry(register_screen, textvariable=password, show="*")
        password_entry.pack()

        confirm_password_label = Label(register_screen, text="Confirm Password")
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

        password_visibility_btn = Button(register_screen, text='Show Passwords', command=change_password_visibility)
        password_visibility_btn.pack()

        requirements_label = Label(register_screen, text="Username and Password must not contain any spaces. \nUsername must not contain '%' \nPassword must be at least 8 characters long \nPassword must contain at least one number")
        requirements_label.pack()

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

            volunteers_file = open("volunteer_database.txt", "r")

            volunteer_list = []
            for line in volunteers_file:
                line_split = line.split("%")
                volunteer_list.append(line_split)

            username_list = []
            for i in volunteer_list:
                username_list.append(i[3])

            if username.get() in username_list:
                username_error3 = Label(register_errors, text="Username is taken. Please try again")
                username_error3.pack()
                error_count.append("u3")

            if password.get() == confirm_password.get():
                if len(password.get()) <= 7:
                    password_error1 = Label(register_errors, text="Password is too short. Minimum length is 8 characters")
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

            else:
                password_error4 = Label(register_errors, text="Passwords do not match. Please try again")
                password_error4.pack()
                error_count.append("p4")

            if len(error_count) > 0:
                register_errors.mainloop()
            else:
                register_errors.destroy()
                register_screen.destroy()
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

                if len(current_volunteer_list_1) == 0:
                    new_user[1] = "1"
                elif len(current_volunteer_list_1) >= 1:
                    new_user[1] = str((int((current_volunteer_list_1[-1])[1]) + 1))

                new_user[3] = verified_username
                new_user[4] = password_hash

                file.close()

                new_user_string = ("\n" + "%".join(new_user))

                volunteer_append = open("volunteer_database.txt", "a")

                volunteer_append.write(f"{new_user_string}")
                volunteer_append.close()

                Register_Info.volunteerList()

        register_button1 = Button(register_screen, text="Register", command=register_check)
        register_button1.pack()

        register_screen.mainloop()

    def volunteer_login():
        choose_role_window.destroy()
        volunteer_login_screen = Toplevel()
        volunteer_login_screen.title("Login")

        Label(volunteer_login_screen, text="Please enter details").pack()

        username_entry = StringVar()
        password_entry = StringVar()

        Label(volunteer_login_screen, text="Username * ").pack()
        username_login_entry = Entry(volunteer_login_screen, textvariable=username_entry)
        username_login_entry.pack()

        Label(volunteer_login_screen, text="Password * ").pack()
        password_entry = Entry(volunteer_login_screen, textvariable=password_entry, show='*')
        password_entry.pack()

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

            logins_list = []
            logins_status_list = []
            for i in current_volunteer_list_2:
                string_user = i[3]
                string_password = i[4]
                string_status = i[10]
                string_login = str(string_user + string_password)
                string_login_status = str(string_user + string_password + string_status)
                logins_list.append(string_login)
                logins_status_list.append(string_login_status)

            login_entry_string = str(username_entry.get() + password_hash)
            login_entry_status_string = str(username_entry.get() + password_hash + "Active")

            login_error_window = Toplevel()

            if (login_entry_string in logins_list) and (login_entry_status_string not in logins_status_list):
                deactivated_label = Label(login_error_window, text="Your Account has been Deactivated\nPlease contact the admin for support")
                deactivated_label.pack()
                close_button1 = Button(login_error_window, text="Close", command=login_error_window.destroy)
                close_button1.pack()
                login_error_window.mainloop()
            elif (login_entry_string not in logins_list) and (login_entry_status_string not in logins_status_list):
                wrong_detail_label = Label(login_error_window, text="Wrong details entered. Please try again")
                wrong_detail_label.pack()
                close_button2 = Button(login_error_window, text="Close", command=login_error_window.destroy)
                close_button2.pack()
                login_error_window.mainloop()
            elif (login_entry_string in logins_list) and (login_entry_status_string in logins_status_list):
                volunteer_login_screen.destroy()
                login_error_window.destroy()
                Volunteer_Home.function1()
            else:
                unknown_error_label = Label(login_error_window, text="An unknown error has occurred. Please try again")
                unknown_error_label.pack()
                close_button1 = Button(login_error_window, text="Close", command=login_error_window.destroy)
                close_button1.pack()
                login_error_window.mainloop()

        done_button = Button(volunteer_login_screen, text="Login", command=check_login_entry)
        done_button.pack()

        volunteer_login_screen.mainloop()

    def admin_login():
        global username_entry_admin
        global password_entry_admin
        global admin_login_screen
        choose_role_window.destroy()
        admin_login_screen = Toplevel()
        admin_login_screen.title("Login")

        Label(admin_login_screen, text="Please enter details").pack()

        username_entry_admin = StringVar()
        password_entry_admin = StringVar()

        Label(admin_login_screen, text="Username * ").pack()
        username_login_entry_admin = Entry(admin_login_screen, textvariable=username_entry_admin)
        username_login_entry_admin.pack()

        Label(admin_login_screen, text="Password * ").pack()
        password_entry_admin = Entry(admin_login_screen, textvariable=password_entry_admin, show='*')
        password_entry_admin.pack()

        def change_password_visibility_admin():
            if password_entry_admin.cget('show') == '*':
                password_entry_admin.config(show='')
                password_visibility_btn_admin.config(text='Hide Password')
            elif password_entry_admin.cget('show') == '':
                password_entry_admin.config(show='*')
                password_visibility_btn_admin.config(text='Show Password')

        password_visibility_btn_admin = Button(admin_login_screen, text='Show Password',
                                         command=change_password_visibility_admin)
        password_visibility_btn_admin.pack()

        done_button_admin = Button(admin_login_screen, text="Login", command=check_login_entry_admin)
        done_button_admin.pack()

        admin_login_screen.mainloop()

    def check_login_entry_admin():
        global username_entry_admin
        global password_entry_admin
        global admin_login_screen
        login_failure_window_admin = Toplevel()
        def adminfailwindowClose():
            login_failure_window_admin.destroy()

        if username_entry_admin.get() == "admin" and password_entry_admin.get() == "111":
            login_failure_window_admin.destroy()
            admin_login_screen.destroy()
            from Admin_Home import adminHome
            adminHome()
        else:
            login_failure_window_admin.title("Login unsuccessful")
            login_failure_window_admin_label = Label(login_failure_window_admin, text="Wrong details entered. Please try again")
            login_failure_window_admin_label.pack()
            login_failure_window_admin_button = Button(login_failure_window_admin_label, text="Close", command=adminfailwindowClose)
            login_failure_window_admin_button.pack()

    def choose_role():
        global choose_role_window
        main_window.destroy()
        choose_role_window = Toplevel()

        volunteer_button = Button(choose_role_window, text="Volunteer Login", command=volunteer_login)
        volunteer_button.pack()
        admin_button = Button(choose_role_window, text="Admin Login", command=admin_login)
        admin_button.pack()

        choose_role_window.mainloop()

    login_button = Button(main_window, text="Login", command=choose_role)
    login_button.pack()

    register_button = Button(main_window, text="Register", command=register_volunteer)
    register_button.pack()

    main_window.mainloop()
