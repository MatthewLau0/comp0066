#Import modules

import datetime
import sys
import subprocess
import os
subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'prettytable'])
from prettytable import PrettyTable


#Choose the pathway
i = 0
while i == 0:
    try:
        print("[1] Create a New Refugee \n[2] Update an Existing Refugee \n[3] Return to Main Menu")
        pathway_question = int(input("Please enter your preferred option: "))
        if pathway_question == 1:
            i = 1
            import Volunteer_Create_Family
            break

        elif pathway_question == 2:
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
