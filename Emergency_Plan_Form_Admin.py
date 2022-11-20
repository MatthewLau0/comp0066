#Recreation of Emergency Plan Form with lists instead of Pandas

import datetime

#Open the Emergency_Database File to edit - write or append"
emergency_database_file = open("Emergency_Database", "r")

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

#Clarify the path selected
print("You are going to make a new emergency plan. Please follow the below instructions.")

#Create a new emergency (index, camp name, type of emergency, description of emergency, area affected, start date, close date, emergency status)
new_emergency = ["NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA"]

#Convert extracted emergencies into a list
emergency_database_list = []
for line in emergency_database_file:
    line_list = line.split(",")
    emergency_database_list.append(line_list)



#Create the index number for the new emergency
if len(emergency_database_list) == 0:
    new_emergency[0] = "1"
elif len(emergency_database_list) >= 1:
    new_emergency[0] = str((int((emergency_database_list[-1])[0]) + 1))
print("The index number for this emergency is ", new_emergency[0])


#Enter the Camp Name - MAKE SURE THIS IS NOT A DUPLICATE
new_emergency[1] = input("Please enter the name of the camp for this emergency:")

#Check if the name is already in the directory
camp_name_list = []
for i in range(0, len(emergency_database_list)):
    camp_name_list.append((emergency_database_list[i])[1])
while new_emergency[1] in camp_name_list:
    new_emergency[1] = input("This name is already in use. Please enter a new name of the camp for this emergency:")


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
pass

#Start date - use a setting to enter today - fix this
start_date_binary = int(input("Did this event begin today (1 = Yes, 2 = No)?"))
if start_date_binary == 1:
    new_emergency[5] = str(datetime.datetime.today())
if start_date_binary == 2:
    year_input = int(input("Please enter the start year of the emergency:"))
    month_input = int(input("Please enter the start month of the emergency:"))
    day_input = int(input("Please enter the start day of the emergency:"))
    while new_emergency[5] == "NA":
        try:
            new_emergency[5] = str(datetime.datetime(year_input, month_input, day_input))
        except Exception:
            print("Invalid date entered. Please re-enter the start date of the emergency.")
            year_input = int(input("Please enter the start year of the emergency:"))
            month_input = int(input("Please enter the start month of the emergency:"))
            day_input = int(input("Please enter the start day of the emergency:"))

#Close date/status - add error if close date is before start date
status = int(input("Has the event finished yet? (1 = Yes, 2 = No):"))
if status == 1:
    new_emergency[6] = "Closed"
    year_close_input = int(input("Please enter the close year of the emergency:"))
    month_close_input = int(input("Please enter the close month of the emergency:"))
    day_close_input = int(input("Please enter the close day of the emergency:"))
    while new_emergency[7] == "NA":
        try:
            new_emergency[6] = str(datetime.datetime(year_close_input, month_close_input, day_close_input))
        except Exception:
            print("Invalid date entered. Please re-enter the start date of the emergency.")
            year_close_input = int(input("Please enter the close year of the emergency:"))
            month_close_input = int(input("Please enter the close month of the emergency:"))
            day_close_input = int(input("Please enter the close day of the emergency:"))
if status == 2:
    new_emergency[6] = "NA"
    new_emergency[7] = "Active"

#View the new emergency - add exception
view_emergency = int(input("Would you like to review the emergency that you are adding to the database? (1 = Yes, 2 = No)"))
if view_emergency == 1:
    print(new_emergency)
new_emergency_string = ','.join(new_emergency)

#Close file for reading
emergency_database_file.close()

#Open File for appending and add new emergency
emergency_database_file_append = open("Emergency_Database", "a")
emergency_database_file_append.write("\n%s" %(new_emergency_string))

#Close file for appending
emergency_database_file_append.close()

#Return to homescreen



