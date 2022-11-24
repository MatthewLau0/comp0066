import tkinter
from tkinter import *
import os
import datetime
import subprocess
import sys

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
    new_refugee[1] = name
    new_refugee[2] = number

    new_refugee_string = ",".join(new_refugee)
    volunteer_list_file.close()
    volunteer_list_file_append = open("Volunteer_Database", "a")
    volunteer_list_file_append.write("\n%s" % (new_refugee_string))
    volunteer_list_file_append.close()







#define text file


#Setting up the screen
screen = Tk()
screen.geometry("500x500")
screen.title("Create Refugee Form")

#Title text
intro_text = Label(text = "Use this section to create a refugee within this Database.", fg = 'Green', bg="Light Grey", width= 500)
intro_text.pack()

#Input from user
refugee_name_text = Label(text = "Refugee name")
refugee_name_text.place(x = 20, y = 50)
refugee_name = StringVar()
refugee_name_entry = Entry(textvariable=refugee_name)
refugee_name_entry.place(x = 175, y = 50, width=300)

refugee_number_text = Label(text = "Refugee Number")
refugee_number_text.place(x = 20, y = 100)
refugee_number = StringVar()
refugee_number_entry = Entry(textvariable=refugee_number)
refugee_number_entry.place(x = 175, y = 100, width=300)


submit = Button(text = "Submit the form", width=30, command=save_to_file)
submit.place(x = 100, y= 400)


#click_me = Button(text = "Click me", fg = "red", height = 20, width = 20)
#click_me.place(x = 10, y = 20)

#name_storage = StringVar()
#name = Entry(textvariable=name_storage)
#name.pack()

tkinter.mainloop()
#or screen.mainloop()