import os

# Opening current database and reading it into a list
volunteer_list_file = open("username_info.txt", "r")
volunteer_database_list = []
for line in volunteer_list_file:
    x = line.split(",")
    volunteer_database_list.append(x)






#Choose the pathway
i = 0
while i == 0:
    try:
        print("[1] Create a New Refugee \n[2] Update an Existing Refugee \n[3] Return to Main Menu")
        pathway_question = int(input("Please enter your preferred option: "))
        if pathway_question == 1:
            i = 1
            import volunteer_create_family_gui
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
