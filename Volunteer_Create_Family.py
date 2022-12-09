#Importing modules
import os
import datetime
import subprocess
import sys
subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'prettytable'])
from prettytable import PrettyTable


#Function to calculate age of refugee from date
def calculate_age(lol):
    today = datetime.date.today()
    x = lol.split("/")
    birthyear = int(x[0])
    birthmonth = int(x[1])
    birthday = int(x[2])

    birthdate = datetime.date(birthyear, birthmonth, birthday)
    age = 0

    if birthdate.month < today.month and today.year > birthdate.year:
        age = today.year - birthdate.year

    elif birthdate.month > today.month and today.year > birthdate.year:
        age = today.year - birthdate.year - 1

    elif birthdate.month == today.month and today.year > birthdate.year and today.day < birthdate.day:
        age = today.year - birthdate.year - 1

    elif birthdate.month == today.month and today.year > birthdate.year and today.day > birthdate.day:
        age = today.year - birthdate.year

    return age

#New list with volunteer
new_refugee = [""]*14



#Opening the volunteer database and adding current volunteers into a list
volunteer_list_file = open("Refugee_Database", "r")
volunteer_database_list = []
for line in volunteer_database_list:
    x = line.split(",")
    volunteer_list_file.append(x)


#Create index number for new emergency
if len(volunteer_database_list) == 0:
    new_refugee[0] = "1"
elif len() >= 1:
    new_refugee[0] = str((int((volunteer_database_list[-1])[0]) + 1))
print("The index number for this emergency is ", new_refugee[0])


#Intro to coding portion
print("Use this section to create a refugee within this Database.")


#Filling in details
print("Personal detail section: ")

#Name
refugee_name = str(input("Please enter the refugee name: "))
new_refugee[1] = str(refugee_name)

#Number
i = 0
while i == 0:
    refugee_number = input("Please enter the refugee number: ")
    counter = 0
    for j in range(0, len(volunteer_database_list)):
        if refugee_number == volunteer_database_list[j][2]:
            counter = counter + 1

    if counter == 0:
        i = i + 1

    if counter != 0:
        print("Refugee number already exists! Please try again")

new_refugee[2] = str(refugee_number)


refugee_dob = input("Please enter the refugee date of birth (yyyy/mm/dd format): ")
new_refugee[3] = str(refugee_dob)

refugee_age =calculate_age(refugee_dob)
new_refugee[4] = str(refugee_age)

refugee_gender = input("Please enter the refugee gender: ")
new_refugee[5] = str(refugee_gender)

refugee_address = input("Please enter the refugee address: ")
new_refugee[6] = str(refugee_address)

refugee_weight = input("Please enter the refugee weight: ")
new_refugee[7] = str(refugee_weight)

refugee_disabilities = input("Please enter any refugee disabilities: ")
new_refugee[8] = str(refugee_disabilities)

refugee_height = input("Please enter the refugee height: ")
new_refugee[9] = str(refugee_height)

refugee_healthconditions = input("Please enter any refugee health conditions: ")
new_refugee[10] = str(refugee_healthconditions)

refugee_vaccines = input("Please enter the refugee vaccination status: ")
new_refugee[11] = str(refugee_vaccines)

refugee_bloodgroup = input("Please enter the refugee blood group: ")
new_refugee[12] = str(refugee_bloodgroup)

refugee_alive = input("Please enter whether the refugee is alive or not: ")
new_refugee[13] = str(refugee_alive)

#View the new refugee
view_emergency = int(input("Would you like to review the emergency that you are adding to the database? (1 = Yes, 2 = No)"))
if view_emergency == 1:
    t_newrefugee = PrettyTable(["Index Number", "Name", "Number", "Date of Birth", "Age", "Gender", "Address", "Weight", "Disabilities", "Height", "Health Conditions", "Vaccines", "Bloodgroup", "Alive"])
    t_newrefugee.add_row(new_refugee)
    print(t_newrefugee)

new_volunteer_string = ','.join(new_refugee)


volunteer_list_file.close()

volunteer_list_file_append = open("Refugee_Database", "a")
volunteer_list_file_append.write("\n%s" %(new_volunteer_string))
volunteer_list_file_append.close()


print("Process complete! New refugee created.")
