#Importing pandas
import pandas as pd
import os
import datetime

#Opening the volunteer database
volunteer_database = open("Volunteer Database", "a+")

sample_refugee = ["Matthew", "001", "09/07/2002", "20",  "Male", "Home"]
refugee_database_list = [sample_refugee]
refugee_database_dataframe = pd.DataFrame(refugee_database_list, index=[1, ], columns =['Name', 'Number', 'DoB', 'Age', 'Gender', 'Address'])
volunteer_database.write(str(refugee_database_dataframe))



#Intro to coding portion
print("Use this section to create a refugee within this Database.")


#Loop to choose the pathway
i = 0
while i == 0:
    try:
        print("[1] Create a New Refugee \n[2] Update an Existing Refugee \n[3] Return to Main Menu")
        pathway_question = int(input("Please enter your preferred option: "))
        if pathway_question == 2:
            i = 1
            break
            #Load new module on Creating a new emergency plan?
        elif pathway_question == 1:
            i = 1
            break
        elif pathway_question == 3:
            i = 1
            break
    except ValueError:
        print("You may have entered a non-numerical answer!")

    except OverflowError:
        print("Your number is too large!")

    else:
        os.system('clear')
        print("Invalid Entry. Please select 1 or 2 to continue in this section, or 3 to return to the homepage.")

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

def create_refugee():
    #Explain the function
    print("You have selected to create a new refugee.")
    print("Personal detail section: ")
    refugee_name = input("Please enter the refugee name: ")
    refugee_number = input("Please enter the refugee number: ")
    refugee_dob = input("Please enter the refugee date of birth (yyyy/mm/dd format): ")
    refugee_age =calculate_age(refugee_dob)
    refugee_gender = input("Please enter the refugee gender: ")
    refugee_address = input("Please enter the refugee address: ")
    refugee_weight = input("Please enter the refugee weight")
    refugee_disabilities = input("Please enter any refugee disabilities")
    refugee_height = input("Please enter the refugee height")
    refugee_healthconditions = input("Please enter any refugee health conditions")
    refugee_vaccines = input("Please enter the refugee vaccination status")
    refugee_bloodgroup = input("Please enter the refugee blood group")
    refugee_alive = input("Please enter whether the refugee is alive or not")




