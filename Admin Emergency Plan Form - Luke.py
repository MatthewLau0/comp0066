#Import Pandas to the dataset to store Emergency Data Information
import pandas as pd

#Open the Emergency Database File to edit
emergency_database_file = open("Emergency Database", "a+")

#Set up empty lists for the Emergency Database files - add area affected
sample_emergency = [1, "Camp 1", "Tsunami", "Sample Description", "01/01/1900", "02/01/1900", "Closed"]
emergency_database_list = [sample_emergency, ]
#emergency_database_dataframe = pd.DataFrame(emergency_database_list, index=1, columns =[camp_name, emergency_type, emergency_description, area_affected, start_date, close_date, status])
emergency_database_file.write(str(emergency_database_list))
#emergency_database_file.write(emergency_database_database)



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
print("You are going to make a new emergency plan. Please follow the below instructions.")

#Create new emergency
new_emergency = ["NA", "NA", "NA", "NA", "NA", "NA", "NA"]

#Generate the Camp Index Number


#Enter the Camp Name
new_emergency[1] = input("Please enter the name of the camp for this emergency:")

#Enter the Type of Emergency
print("[1] Flood\n[2]Tsunami\n[3]Earthquake\n[4]Drought\n[5]Other")
emergency_type_input = int(input("Please use the above index to enter the type of emergency:"))
while new_emergency[2] == "NA":
    try:
        if emergency_type_input == 1:
            new_emergency[2] = "Flood"
        elif emergency_type_input == 2:
            new_emergency[2] = "Tsunami"
        elif emergency_type_input == 3:
            new_emergency[2] = "Earthquake"
        elif emergency_type_input == 4:
            new_emergency[2] = "Drought"
        elif emergency_type_input == 5:
            new_emergency[2] = input("Please specify the specific type of emergency:")
    except Exception:
        print("You entered an invalid input")
        emergency_type_input = int(input("Please use the above index to enter the type of emergency:"))

#Descrpition of the Emergency
new_emergency[3] = input("Please briefly describe the emergency that you are registering")

#Area affected

#Start date - use a setting to enter today

#Close date

#Status
if new_emergency[6] == "NA":
    new_emergency[7] = "Active"
else:
    new_emergency[7] = "Closed"

#Set categories for the type of emergency


#Update Dataframe and reupload it into the Emergency Database File - change indexing variable


#Close the Emergency Database File
emergency_database = open("Emergency Database", "a+")

