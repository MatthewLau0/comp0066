import tkinter
from tkinter import *
import os
import datetime
import subprocess
import sys
from tkinter import messagebox
def delete1():
    screen1.destroy()


def name_validate():
    name = refugee_name_entry.get()

    if len(name) == 0:
        namestatus.config(text = "Name cannot be 0")

    else:
        try:
            if len(name) <= 2:
                namestatus.config(text = "Name too short!")

            elif any(i.isdigit() for i in name):
                namestatus.config(text = "Name can't be numeric!")

            elif name.count(" ") > 3:
                namestatus.config(text = "Please enter less than 4 separate names")

            else:
                namestatus.config(text = "Valid :)")
        except:
            pass
    return True
def noinput_error():
    global screen1
    screen1 = Toplevel(screen)
    screen1.geometry("300x120")
    screen1.title("Warning!")
    noinput_error_text = Label(screen1, text = "All fields required are marked with an *", fg = 'red')
    noinput_error_text.place(x = 40, y = 40)
    close_button = Button(screen1, text = "I understand", command = delete1)
    close_button.place(x = 95, y = 80)


#defining some functions
def save_to_file():

    #Opening current database and reading it into a list
    volunteer_list_file = open("Volunteer_Database", "r")
    volunteer_database_list = []
    for line in volunteer_database_list:
        x = line.split(",")
        volunteer_list_file.append(x)

    #Creating new refugee
    new_refugee = [""]*14

    #Finding index for new refugee
    if len(volunteer_database_list) == 0:
        new_refugee[0] = "1"
    elif len() >= 1:
        new_refugee[0] = str((int((volunteer_database_list[-1])[0]) + 1))
    print("The index number for this emergency is ", new_refugee[0])

    name = refugee_name.get()
    number = refugee_number.get()
    dob = refugee_dob.get()
    age = refugee_age.get()
    sex = refugee_sex.get()
    address = refugee_address.get()
    weight = refugee_weight.get()
    height = refugee_height.get()

    #Check if there is no input in the required fields
    if name == "" or number == "" or sex == "":
        noinput_error()
        messagebox.showerror("Missing input for n ame, number, or sex")
        return

    #Check if name has errors
    for i in name:
        if i.isalpha() != True and i != " ":
            return




    new_refugee[1] = name

    try:
        int(number)
    except ValueError:
        print("Not a number!")
    new_refugee[2] = number
    new_refugee[3] = dob
    new_refugee[4] = age
    new_refugee[5] = sex
    new_refugee[6] = address
    new_refugee[7] = weight
    new_refugee[8] = height
    new_refugee_string = ",".join(new_refugee)
    volunteer_list_file.close()
    volunteer_list_file_append = open("Volunteer_Database", "a")
    volunteer_list_file_append.write("\n%s" % (new_refugee_string))
    volunteer_list_file_append.close()







#define text file


#Setting up the screen
screen = Tk()
screen.geometry("500x1000")
screen.title("Create Refugee Form")

#Title text
intro_text = Label(text = "Use this section to create a refugee within this Database.", fg = 'Green', bg="Light Grey", width= 500)
intro_text.pack()

#Input from user



refugee_name_text = Label(text = "Refugee name* ")
refugee_name_text.place(x = 20, y = 50)
refugee_name = StringVar()
refugee_name_entry = Entry(screen, validate = 'all', validatecommand = name_validate, textvariable=refugee_name)
refugee_name_entry.place(x = 175, y = 50, width=300)

namestatus = Label(screen, text = "waiting for input")
namestatus.place(x = 20, y = 70)



refugee_number_text = Label(text = "Refugee Number* ")
refugee_number_text.place(x = 20, y = 100)
refugee_number = StringVar()
refugee_number_entry = Entry(textvariable=refugee_number, show="*")
refugee_number_entry.place(x = 175, y = 100, width=300)

refugee_sex_text = Label(text = "Sex*")
refugee_sex_text.place(x = 20, y = 150)
refugee_sex = StringVar()
#refugee_sex_entry = Entry(textvariable=refugee_sex)
#refugee_sex_entry.place(x = 175, y = 150, width=300)
drop = OptionMenu(screen, refugee_sex, "Male", "Female", "Prefer not to say")
drop.place(x = 175, y = 150, width = 300)

refugee_dob_text = Label(text = "Date of Birth")
refugee_dob_text.place(x = 20, y = 200)
refugee_dob = StringVar()
refugee_dob_entry = Entry(textvariable=refugee_dob)
refugee_dob_entry.place(x = 175, y = 200, width=300)

refugee_age_text = Label(text = "Age")
refugee_age_text.place(x = 20, y = 250)
refugee_age = StringVar()
refugee_age_entry = Entry(textvariable=refugee_age)
refugee_age_entry.place(x = 175, y = 250, width=300)

refugee_address_text = Label(text = "Address")
refugee_address_text.place(x = 20, y = 300)
refugee_address = StringVar()
refugee_address_entry = Entry(textvariable=refugee_address)
refugee_address_entry.place(x = 175, y = 300, width=300)

refugee_weight_text = Label(text = "Weight")
refugee_weight_text.place(x = 20, y = 350)
refugee_weight = StringVar()
refugee_weight_entry = Entry(textvariable=refugee_weight)
refugee_weight_entry.place(x = 175, y = 350, width=300)

refugee_height_text = Label(text = "Height")
refugee_height_text.place(x = 20, y = 400)
refugee_height = StringVar()
refugee_height_entry = Entry(textvariable=refugee_height)
refugee_height_entry.place(x = 175, y = 400, width=300)

submit = Button(text = "Submit the form", width=30, command=save_to_file)
submit.place(x = 100, y= 450)


#click_me = Button(text = "Click me", fg = "red", height = 20, width = 20)
#click_me.place(x = 10, y = 20)

#name_storage = StringVar()
#name = Entry(textvariable=name_storage)
#name.pack()

#tkinter.mainloop()
screen.mainloop()