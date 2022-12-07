# import modules

from distutils.command.config import config
from tkinter import *
from tkinter import messagebox
import hashlib

from distutils.command.config import config
from tkinter import *
from tkinter import messagebox
import hashlib


# Functionality of user registration
def register_user():
    # Gets user info from UI
    username_info_entry = username.get().encode()
    password_info_entry = password.get().encode()

    # Creating hashing object
    secret_username_info = hashlib.sha3_256(username_info_entry)
    secret_password_info = hashlib.sha3_256(password_info_entry)

    # getting binary hash from object
    username_hash = secret_username_info.hexdigest()
    password_hash = secret_password_info.hexdigest()

    # Writes binary hash's to file
    new_user = [username_hash, password_hash]
    new_user_string = ' '.join(new_user)
    file = open("username_info.txt", "a")
    file.write(f"{new_user_string} \n")
    file.close()

    # Cleaning
    username_entry.delete(0, END)
    password_entry.delete(0, END)

    # Success message
    Label(register_screen, text="Registration Successful", fg="green", font=("calibri", 12)).pack()


# Functionality of user login
def login_verify():
    # Gets username and password from UI
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
        for line in open("username_info.txt", "r").readlines():
            # Checks if hashes equal
            login_info = line.split("%")
            if username_hash == login_info[0] and password_hash == login_info[1]:
                login_success_bool = True
                login_sucess()
                break
            else:
                continue
        if not login_success_bool:
            password_not_recognised()
    except FileNotFoundError:
        user_not_found()


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


# Find a way to add "activation status" next to login of volunteer

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
    Button(login_success_screen, text="OK", command=login_success_screen.destroy).pack()


# Designing popup for login invalid password
def password_not_recognised():
    global password_not_recog_screen
    password_not_recog_screen = Toplevel(login_screen)
    password_not_recog_screen.title("Success")
    password_not_recog_screen.geometry("150x100")
    Label(password_not_recog_screen, text="Invalid Password ").pack()
    Button(password_not_recog_screen, text="OK", command=password_not_recog_screen.destroy).pack()


# Designing popup for user not found
def user_not_found():
    global user_not_found_screen
    user_not_found_screen = Toplevel(login_screen)
    user_not_found_screen.title("Success")
    user_not_found_screen.geometry("150x100")
    Label(user_not_found_screen, text="User Not Found").pack()
    Button(user_not_found_screen, text="OK", command=user_not_found_screen.destroy).pack()


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


main_account_screen()