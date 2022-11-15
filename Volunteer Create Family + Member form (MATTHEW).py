#Importing pandas
import pandas as pd
import os

#Opening the volunteer database
volunteer_database = open("Volunteer Database", "a+")

sample_refugee = ["Matthew", "001", "09/07/2002", "20",  "Male", "Home"]
refugee_database_list = [sample_refugee]
#refugee_database_dataframe = pd.DataFrame(refugee_database_list, index=[1, ], columns =['Name', 'Number', 'DoB', 'Age', 'Gender', 'Address'])
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



def create_refugee():
    #Explain the function
    print("You have selected to create a new refugee.")
    print("Personal detail section: ")



