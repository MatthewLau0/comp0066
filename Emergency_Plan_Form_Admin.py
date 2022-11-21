#Recreation of Emergency Plan Form with lists instead of Pandas - do the same with pip

import datetime
import sys
import subprocess
subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'prettytable'])
from prettytable import PrettyTable

#Introduce the portion of the programme
print("Use this section to Create or Update an Emergency within this Database.")

#Choose the pathway
print(" [1] Create a New Emergency Plan \n [2] Update an Existing Emergency Plan \n [3] Return to Main Menu")
pathway_question = int(input("Would you like to Create a New Emergency Plan, or Update and Existing Emergency Plan?"))
if pathway_question == 2:
    import Update_Existing_Form_Admin
elif pathway_question == 1:
    import Create_New_Emergency_Plan
elif pathway_question == 3:
    pass

#Clarify if anything else needs to be done
further_action = int(input("Would you like to update/create another emergency file? (1 = Yes, 2 = No)"))
while further_action == 1:
    pathway_question = int(input("Would you like to Create a New Emergency Plan, or Update and Existing Emergency Plan?"))
    if pathway_question == 2:
        import Update_Existing_Form_Admin
        further_action = int(input("Would you like to update/create another emergency file? (1 = Yes, 2 = No)"))
    elif pathway_question == 1:
        import Create_New_Emergency_Plan
        further_action = int(input("Would you like to update/create another emergency file? (1 = Yes, 2 = No)"))


#Return to homescreen



