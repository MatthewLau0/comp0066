#Import Pandas and datetime to the dataset to store Emergency Data Information
import datetime

#Open the Emergency Database File to edit - write or append"
emergency_database_file = open("Emergency Database", "r+")

#Set up empty lists for the Emergency Database files - add area affected - how to make sure does not generate new area every time
#sample_emergency = ["Sample Camp", "Tsunami", "Sample Description", "NA",  "01/01/1900", "02/01/1900", "Closed"]
#emergency_database_list = [sample_emergency, ]
emergency_database_dataframe = pd.DataFrame(emergency_database_file, index=[1, ], columns=['Camp Name', 'Type of Emergency', 'Description of Emergency', 'Area Affected', 'Start Date', 'Close Date', 'Emergency Status'])
#emergency_database_dataframe = pd.DataFrame(emergency_database_list, index=[1, ], columns=['Camp Name', 'Type of Emergency', 'Description of Emergency', 'Area Affected', 'Start Date', 'Close Date', 'Emergency Status'])




#Introduce the portion of the programme
print("Use this section to Create or Update an Emergency within this Database.")

#Choose the pathway
print("[1] Create a New Emergency Plan \n [2] Update an Existing Emergency Plan \n [3] Return to Main Menu")
pathway_question = int(input("Would you like to Create a New Emergency Plan, or Update and Existing Emergency PLan?"))
try:
    if pathway_question == 2:
        import Update_Existing_Form_Admin
        exit()
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


#Enter the Camp Name - NEED TO MAKE SURE IT IS NOT A DUPLICATE
new_emergency[0] = input("Please enter the name of the camp for this emergency:")

#Enter the Type of Emergency
print("[1] Flood\n[2]Tsunami\n[3]Earthquake\n[4]Drought\n[5]Other")
emergency_type_input = int(input("Please use the above index to enter the type of emergency:"))
while new_emergency[1] == "NA":
    try:
        if emergency_type_input == 1:
            new_emergency[1] = "Flood"
        elif emergency_type_input == 2:
            new_emergency[1] = "Tsunami"
        elif emergency_type_input == 3:
            new_emergency[1] = "Earthquake"
        elif emergency_type_input == 4:
            new_emergency[1] = "Drought"
        elif emergency_type_input == 5:
            new_emergency[1] = input("Please specify the specific type of emergency:")
    except Exception:
        print("You entered an invalid input")
        emergency_type_input = int(input("Please use the above index to enter the type of emergency:"))

#Descrpition of the Emergency
new_emergency[2] = input("Please briefly describe the emergency that you are registering")

#Area affected
pass

#Start date - use a setting to enter today - fix this
start_date_binary = int(input("Did this event begin today (1 = Yes, 2 = No)?"))
if start_date_binary == 1:
    new_emergency[4] = datetime.datetime.today()
if start_date_binary == 2:
    year_input = int(input("Please enter the start year of the emergency:"))
    month_input = int(input("Please enter the start month of the emergency:"))
    day_input = int(input("Please enter the start day of the emergency:"))
    while new_emergency[4] == "NA":
        try:
            new_emergency[4] = datetime.datetime(year_input, month_input, day_input)
        except Exception:
            print("Invalid date entered. Please re-enter the start date of the emergency.")
            year_input = int(input("Please enter the start year of the emergency:"))
            month_input = int(input("Please enter the start month of the emergency:"))
            day_input = int(input("Please enter the start day of the emergency:"))


#Close date/status - add error if close date is before start date
status = int(input("Has the event finished yet? (1 = Yes, 2 = No):"))
if status == 1:
    new_emergency[5] = "Closed"
    year_close_input = int(input("Please enter the close year of the emergency:"))
    month_close_input = int(input("Please enter the close month of the emergency:"))
    day_close_input = int(input("Please enter the close day of the emergency:"))
    while new_emergency[6] == "NA":
        try:
            new_emergency[6] = datetime.datetime(year_close_input, month_close_input, day_close_input)
        except Exception:
            print("Invalid date entered. Please re-enter the start date of the emergency.")
            year_close_input = int(input("Please enter the close year of the emergency:"))
            month_close_input = int(input("Please enter the close month of the emergency:"))
            day_close_input = int(input("Please enter the close day of the emergency:"))
if status == 2:
    new_emergency[5] = "NA"
    new_emergency[6] = "Active"

#Update Dataframe and reupload it into the Emergency Database File - change indexing variable
emergency_database_dataframe.loc[len(emergency_database_dataframe)] = new_emergency
emergency_database_file.write(str(emergency_database_dataframe))


#Close the Emergency Database File
emergency_database_file.close()

