#Import Pretty Table
from prettytable import PrettyTable

#Open files Emergency Plan Files
emergency_database_file = open("Emergency_Database", "r")

#Clarify the path selected
print("You are going to update an existing emergency plan. Please follow the below instructions.")

#Extract from Emergency_Database into a list
emergency_database_list = []
for line in emergency_database_file:
    line_list = line.split(",")
    emergency_database_list.append(line_list)


#Print the table, if requested
map_view = int(input("Would you like to view a summary of the camps currently stored in the database? (1 = Yes, 2 = No)"))
if map_view == 1:
    t = PrettyTable(["Index Number", "Camp Name", "Type of Emergency", "Description of Emergency", "Area Affected", "Start date", "Close date", "Emergency status"])
    for i in range(0, len(emergency_database_list)):
        t.add_row(emergency_database_list[i])
    print(t)

#Define function for updating an emergency
def emergency_update(update_selection):
    if update_selection == 1:
        new_camp_name = input("Please enter the new camp name:")
        # Check if the name is already in the directory
        camp_name_list = []
        for i in range(0, len(emergency_database_list)):
            camp_name_list.append((emergency_database_list[i])[1])
        while new_camp_name in camp_name_list:
            new_camp_name = input("This name is already in use. Please enter a new name of the camp for this emergency:")
        update_camp_list[1] = new_camp_name
    elif update_selection == 2:
        print("[1] Flood\n[2]Tsunami\n[3]Earthquake\n[4]Drought\n[5]Other")
        new_emergency_type = int(input("Please use the above index to enter the type of emergency:"))
        if new_emergency_type == 1:
            update_camp_list[2] = "Flood"
        elif new_emergency_type == 2:
            update_camp_list[2] = "Tsunami"
        elif new_emergency_type == 3:
            update_camp_list[2] = "Earthquake"
        elif new_emergency_type == 4:
            update_camp_list[2] = "Drought"
        elif new_emergency_type == 5:
            update_camp_list[2] = input("Please specify the specific type of emergency:")
    elif update_selection == 3:
         update_camp_list[3] = input("Please briefly describe the emergency that you are registering")
    elif update_selection == 4:
        pass
    elif update_selection == 5:
        from datetime import date
        start_date_binary_update = int(input("Did this event begin today (1 = Yes, 2 = No)?"))
        if start_date_binary_update == 1:
            update_camp_list[5] = str(date.today())
        if start_date_binary_update == 2:
            year_input_update = int(input("Please enter the start year of the emergency:"))
            month_input_update = int(input("Please enter the start month of the emergency:"))
            day_input_update = int(input("Please enter the start day of the emergency:"))
            while update_camp_list[5] == "NA":
                try:
                    update_camp_list[5] = str(date(year_input_update, month_input_update, day_input_update))
                except Exception:
                    print("Invalid date entered. Please re-enter the start date of the emergency.")
                    year_input_update = int(input("Please enter the start year of the emergency:"))
                    month_input_update = int(input("Please enter the start month of the emergency:"))
                    day_input_update = int(input("Please enter the start day of the emergency:"))
    elif update_selection == 6:
        from datetime import date
        status_update = int(input("Has the event finished yet? (1 = Yes, 2 = No):"))
        if status_update == 1:
            update_camp_list[7] = "Closed"
            year_close_input_update = int(input("Please enter the close year of the emergency:"))
            month_close_input_update = int(input("Please enter the close month of the emergency:"))
            day_close_input_update = int(input("Please enter the close day of the emergency:"))
            while update_camp_list[6] == "NA":
                try:
                    update_camp_list[6] = str(date(year_close_input_update, month_close_input_update, day_close_input_update))
                except Exception:
                    print("Invalid date entered. Please re-enter the start date of the emergency.")
                    year_close_input_update = int(input("Please enter the close year of the emergency:"))
                    month_close_input_update = int(input("Please enter the close month of the emergency:"))
                    day_close_input_update = int(input("Please enter the close day of the emergency:"))
        if status_update == 2:
            update_camp_list[6] = "NA"
            update_camp_list[7] = "Active"
    print("See below the updated emergency")
    t_updatedemergency = PrettyTable(["Index Number", "Camp Name", "Type of Emergency", "Description of Emergency", "Area Affected", "Start date", "Close date", "Emergency status"])
    t_updatedemergency.add_row(update_camp_list)
    print(t_updatedemergency)


#Select the index number for the chosen camp
index_number_known = int(input("Do you know the index number of the camp that you would like to update? (1 = Yes, 2 = No)"))
while index_number_known != 1:
    print("Please see the below table to determine the index number of the camp that you would like to update.")
    t = PrettyTable(["Index Number", "Camp Name", "Type of Emergency", "Description of Emergency", "Area Affected", "Start date", "Close date", "Emergency status"])
    for i in range(0, len(emergency_database_list)):
        t.add_row(emergency_database_list[i])
    print(t)
    index_number_known = int(input("Do you know the index number of the camp that you would like to update? (1 = Yes, 2 = No)"))
index_number = int(input("Please enter the index number for the camp that you would like to update:"))
update_camp_list = emergency_database_list[(index_number - 1)]

#Select what aspect of the emergency you would like to update
t_selected_update = PrettyTable(["Index Number", "Camp Name", "Type of Emergency", "Description of Emergency", "Area Affected", "Start date", "Close date", "Emergency status"])
t_selected_update.add_row(update_camp_list)
print(t_selected_update)
update_selection = int(input("Please enter the component of the emergency that you would like to update (1=Camp Name, 2=Type of Emergency, 3=Description of Emergency, 4=Area affected, 5=Start date, 6=Close date, 7=Emergency status)"))

#Run the first update
emergency_update(update_selection)

#Check if you would like to update another portion of the same camp index
further_update_question = int(input("Would you like to update another aspect of this emergency? (1 = Yes, 2 = No)"))
while further_update_question == 1:
    further_update_selection = int(input("Please enter the component of the emergency that you would like to update (1=Camp Name, 2=Type of Emergency, 3=Description of Emergency, 4=Area affected, 5=Start date, 6=Close date, 7=Emergency status)"))
    emergency_update(further_update_selection)
    further_update_question = int(input("Would you like to update another aspect of this emergency? (1 = Yes, 2 = No)"))

#Append to the new database
emergency_database_list[(index_number - 1)] = update_camp_list
emergency_database_file.close()
emergency_database_file_write = open("Emergency_Database", "r+")
emergency_database_one_string = ','.join(emergency_database_list[0])
emergency_database_file_write.write(emergency_database_one_string)
for i in range(1, len(emergency_database_list)):
    emergency_database_string = ','.join(emergency_database_list[i])
    emergency_database_file_write.write(emergency_database_string)
    i += 1
emergency_database_file_write.close()
