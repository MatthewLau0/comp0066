#Import Pandas and datetime to the dataset to store Emergency Data Information
import pandas as pd
import datetime

#Open files Emergency Plan Files
emergency_database_file = open("Emergency_Database", "a+")

#Clarify the path selected
print("You are going to update an existing emergency plan. Please follow the below instructions.")

#Select the Camp Name that you would like to extract - include for not relevant variables
emergency_plans_view = int(input("Do you know the camp name of the camp you would like to update? (1 = Yes, 2 = No)"))
if emergency_plans_view == 1:
    emergency_plan_update = input("Please enter the camp name that you would like to edit information for:")
elif emergency_plans_view == 2:
    num_emergency_plans_database = list(emergency_database_file)
    print(num_emergency_plans_database)
    emergency_plan_update = input("Please enter the camp ID that you would like to edit information for:")

#Select the relavent row of data
emergency_database_file.loc[emergency_database_file['Camp Name'] = emergency_plan_update]
emergency_plan_edit_list = list()

