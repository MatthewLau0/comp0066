#Import Pandas to the dataset to store Emergency Data Information
import pandas as pd

#Open the Emergency Database File to edit
emergency_database = open("Emergency Database", "a+")

#Introduce the portion of the programme
print("Use this section to Create or Update an Emergency within this Database.")

#Choose the pathway
print("[1] Create a New Emergency Plan \n [2] Update an Existing Emergency Plan \n [3] Return to Main Menu")
pathway_question = int(input("Would you like to Create a New Emergency Plan, or Update and Existing Emergency PLan?"))
try:
    if pathway_question == 2:
        pass
        #Load new module on Creating a new emergency plan?
    elif pathway_question == 1:
        pass
    elif pathway_question == 3:
        pass
except Exception:
    print("Invalid Entry. Please select 1 or 2 to continue in this section, or 3 to return to the homepage.")

#Clarify that you are going to create a new emergency plan
print("You are going to make a new emergency plan. Please follow the below instructions")

#Enter the Camp Name

#Enter the Type of Emergency

#Descrpition of the Emergency

#Area affected

#Start date - use a setting to enter today

#Close date

#Status

#Close the Emergency Database File
emergency_database = open("Emergency Database", "a+")

