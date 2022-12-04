from prettytable import PrettyTable


def volunteers_portal():
    pass


def accommodation_portal():
    accommodations = open("accommodations.txt", "r+")

    blocks_list = []
    for line in accommodations:
        line_list = line.split(",")
        blocks_list.append(line_list)

    def add_new_block():
        new_accommodation = ["NA", "NA", "NA", "NA", "NA", "NA", "NA"]

        def new_block_id():
            if len(blocks_list) == 0:
                new_accommodation[0] = "1"
            elif len(blocks_list) >= 1:
                new_accommodation[0] = str((int((blocks_list[-1])[0]) + 1))
            print("The index number for this emergency is ", new_accommodation[0])

        new_block_id()

        def new_block_name():
            new_accommodation[1] = input("Accommodation Block Name: ")

            accommodation_name_list = []
            for n in range(0, len(blocks_list)):
                accommodation_name_list.append((blocks_list[n])[1])
            while new_accommodation[1] in accommodation_name_list:
                new_accommodation[1] = input(
                    "This name is already in use. Please enter a new name for this accommodation: ")

        new_block_name()

        def capacity_input():
            new_accommodation[2] = input("Block Capacity: ")
            try:
                new_accommodation[2] = str(int(new_accommodation[2]))
            except TypeError:
                print("Please enter a integer")
                capacity_input()

        capacity_input()

        def occupancy_input():
            new_accommodation[3] = input("Block Occupancy: ")
            try:
                new_accommodation[3] = str(int(new_accommodation[3]))
            except TypeError:
                print("Please enter a integer")
                occupancy_input()
            if int(new_accommodation[3]) <= int(new_accommodation[2]):
                new_accommodation[3] = new_accommodation[3]
            else:
                print("Please enter a occupancy under than the capacity")
                occupancy_input()

        occupancy_input()

        def new_block_status_spaces():
            new_accommodation[5] = str(int(new_accommodation[2]) - int(new_accommodation[3]))
            if int(new_accommodation[5]) > 0:
                new_accommodation[4] = "VACANT SPACES"
            else:
                new_accommodation[4] = "FULL"

        new_block_status_spaces()

        def new_block_location():

            new_accommodation[6] = input("Location: ")

        new_block_location()

        new_accommodation_string = ','.join(new_accommodation)

        accommodations.close()

        accommodations_append = open("accommodations.txt", "a")
        accommodations_append.write(new_accommodation_string + ",\n")
        accommodations_append.close()

    def update_choice():
        update = input("Would you like to edit any of the accommodation blocks? [Y/N]: ").strip().upper()
        if update == "Y":
            row_choose()
        elif update == "N":
            home()
        else:
            print("Please enter a valid option ")
            update_choice()

    def row_choose():
        row_choice = input("Which accommodation would you like to update? Enter Block ID: ")
        try:
            row_choice = str(int(row_choice))
        except TypeError:
            print("Please enter a integer")
            row_choose()
        block_id_list = []
        for x in blocks_list:
            block_id_list.append(x[0])
        while row_choice not in block_id_list:
            print("Please choose from one of the IDs in the table")
            row_choose()
        row_choice_index = int(row_choice) - 1

        def update_block_name():
            blocks_list[row_choice_index][1] = input("Accommodation Block Name: ")

            accommodation_name_list = []
            for y in range(0, len(blocks_list)):
                accommodation_name_list.append((blocks_list[y])[1])
            while blocks_list[row_choice_index][1] in accommodation_name_list:
                blocks_list[row_choice_index][1] = input(
                    "This name is already in use. Please enter a new name for this accommodation: ")

        def update_capacity_input():
            blocks_list[row_choice_index][2] = input("Block Capacity: ")
            try:
                blocks_list[row_choice_index][2] = str(int(blocks_list[row_choice_index][2]))
            except TypeError:
                print("Please enter a integer")
                update_capacity_input()

        def update_occupancy_input():
            blocks_list[row_choice_index][3] = input("Block Occupancy: ")
            try:
                blocks_list[row_choice_index][3] = str(int(blocks_list[row_choice_index][3]))
            except TypeError:
                print("Please enter a integer")
                update_occupancy_input()
            if int(blocks_list[row_choice_index][3]) <= int(blocks_list[row_choice_index][2]):
                blocks_list[row_choice_index][3] = blocks_list[row_choice_index][3]
            else:
                print("Please enter a occupancy under than the capacity")
                update_occupancy_input()

        def update_block_status_spaces():
            blocks_list[row_choice_index][5] = \
                str(int(blocks_list[row_choice_index][2]) - int(blocks_list[row_choice_index][3]))
            if int(blocks_list[row_choice_index][5]) > 0:
                blocks_list[row_choice_index][4] = "VACANT SPACES"
            else:
                blocks_list[row_choice_index][4] = "FULL"

        def update_block_location():
            blocks_list[row_choice_index][6] = input("Location: ")

        def column_choose():
            column_choice = input("""Which field would you like to update? 
            [1] Name
            [2] Capacity
            [3] Occupancy
            [4] Location
            Enter column number [1-4]: """)
            try:
                column_choice = str(int(column_choice))
            except TypeError:
                print("Please enter a integer")
                column_choose()
            try:
                1 <= int(column_choice) <= 4
            except ArithmeticError:
                print("Please enter a number between 1 and 4")
                column_choose()

            if column_choice == "1":
                update_block_name()
            elif column_choice == "2":
                update_capacity_input()
                update_block_status_spaces()
            elif column_choice == "3":
                update_occupancy_input()
                update_block_status_spaces()
            elif column_choice == "4":
                update_block_location()

        column_choose()

        new_string = ','.join(blocks_list[row_choice_index])

        accommodations.close()

        accommodations_read = open("accommodations.txt", "r")

        lines = accommodations_read.readlines()

        lines[int(row_choice_index)] = new_string

        with open('accommodations.txt', 'w') as file:
            file.writelines(lines)

        print("File Updated!")

    def add_or_view_func():
        add_or_view = int(input("""
    Would you like to: 
        [1] View 
        [2] Add
    Your Choice: """))

        if add_or_view == 1:
            t_accommodation = PrettyTable([
                "Block ID",
                "Block Name",
                "Block Capacity",
                "Block Occupancy",
                "Block Status",
                "Block Space",
                "Block Location"
            ])
            for z in blocks_list:
                t_accommodation.add_row(z[0:7])
            print(t_accommodation)
            update_choice()

            home()
        elif add_or_view == 2:
            add_new_block()
            home()

    add_or_view_func()


def ration_portal():
    ration_stalls = open("ration_stall.txt", "r+")

    ration_list = []
    for line in ration_stalls:
        line_list = line.split(",")
        ration_list.append(line_list)

    def add_new_stall():
        new_stall = ["NA", "NA", "NA", "NA", "NA", "NA", "NA"]

        def new_stall_id():
            if len(ration_list) == 0:
                new_stall[0] = "1"
            elif len(ration_list) >= 1:
                new_stall[0] = str((int((ration_list[-1])[0]) + 1))
            print("The index number for this Ration Stall is ", new_stall[0])

        new_stall_id()

        def new_stall_name():
            new_stall[1] = input("Ration Stall Name: ")

            stall_name_list = []
            for n in range(0, len(ration_list)):
                stall_name_list.append((ration_list[n])[1])
            while new_stall[1] in stall_name_list:
                new_stall[1] = input(
                    "This name is already in use. Please enter a new name for this stall: ")

        new_stall_name()

        def packs_supplied():
            new_stall[2] = input("No. Ration Packages Supplied to this Ration Stall: ")
            try:
                new_stall[2] = str(int(new_stall[2]))
            except TypeError:
                print("Please enter a integer")
                packs_supplied()

        packs_supplied()

        def packs_used():
            new_stall[3] = input("No. Ration Packages Distributed from this Ration Stall: ")
            try:
                new_stall[3] = str(int(new_stall[3]))
            except TypeError:
                print("Please enter a integer")
                packs_used()
            if int(new_stall[3]) <= int(new_stall[2]):
                new_stall[3] = new_stall[3]
            else:
                print("Please enter a No. Used under than the No. Supplied")
                packs_used()

        packs_used()

        def new_stall_status_remaining():
            new_stall[5] = str(int(new_stall[2]) - int(new_stall[3]))
            if int(new_stall[5]) > 0:
                new_stall[4] = "PACKS REMAINING"
            else:
                new_stall[4] = "ALL DEPLETED"

        new_stall_status_remaining()

        def new_stall_location():

            new_stall[6] = input("Ration Stall Location: ")

        new_stall_location()

        new_stall_string = ','.join(new_stall)

        ration_stalls.close()

        ration_stalls_append = open("ration_stall.txt", "a")
        ration_stalls_append.write(new_stall_string + ",\n")
        ration_stalls_append.close()

    def update_choice():
        update = input("Would you like to edit any of the ration stalls? [Y/N]: ").strip().upper()
        if update == "Y":
            row_choose()
        elif update == "N":
            home()
        else:
            print("Please enter a valid option ")
            update_choice()

    def row_choose():
        row_choice = input("Which ration stall would you like to update? Enter Stall ID: ")
        try:
            row_choice = str(int(row_choice))
        except TypeError:
            print("Please enter a integer")
            row_choose()
        ration_id_list = []
        for x in ration_list:
            ration_id_list.append(x[0])
        while row_choice not in ration_id_list:
            print("Please choose from one of the IDs in the table")
            row_choose()
        row_choice_index = int(row_choice) - 1

        def update_stall_name():
            ration_list[row_choice_index][1] = input("Ration Stall Name: ")

            ration_name_list = []
            for y in range(0, len(ration_list)):
                ration_name_list.append((ration_list[y])[1])
            while ration_list[row_choice_index][1] in ration_name_list:
                ration_list[row_choice_index][1] = input(
                    "This name is already in use. Please enter a new name for this ration stall: ")

        def update_packs_supplied():
            ration_list[row_choice_index][2] = input("No. Ration Packages Supplied to this Ration Stall: ")
            try:
                ration_list[row_choice_index][2] = str(int(ration_list[row_choice_index][2]))
            except TypeError:
                print("Please enter a integer")
                update_packs_supplied()

        def update_packs_used():
            ration_list[row_choice_index][3] = input("No. Ration Packages Distributed from this Ration Stall: ")
            try:
                ration_list[row_choice_index][3] = str(int(ration_list[row_choice_index][3]))
            except TypeError:
                print("Please enter a integer")
                update_packs_used()
            if int(ration_list[row_choice_index][3]) <= int(ration_list[row_choice_index][2]):
                ration_list[row_choice_index][3] = ration_list[row_choice_index][3]
            else:
                print("Please enter a occupancy under than the capacity")
                update_packs_used()

        def update_stall_status_remaining():
            ration_list[row_choice_index][5] = \
                str(int(ration_list[row_choice_index][2]) - int(ration_list[row_choice_index][3]))
            if int(ration_list[row_choice_index][5]) > 0:
                ration_list[row_choice_index][4] = "PACKS REMAINING"
            else:
                ration_list[row_choice_index][4] = "ALL DEPLETED"

        def update_stall_location():
            ration_list[row_choice_index][6] = input("Ration Stall Location: ")

        def column_choose():
            column_choice = input("""Which field would you like to update? 
                [1] Name
                [2] Packs Supplied
                [3] Packs Used
                [4] Location
                Enter column number [1-4]: """)
            try:
                column_choice = str(int(column_choice))
            except TypeError:
                print("Please enter a integer")
                column_choose()
            try:
                1 <= int(column_choice) <= 4
            except ArithmeticError:
                print("Please enter a number between 1 and 4")
                column_choose()

            if column_choice == "1":
                update_stall_name()
            elif column_choice == "2":
                update_packs_supplied()
                update_stall_status_remaining()
            elif column_choice == "3":
                update_packs_used()
                update_stall_status_remaining()
            elif column_choice == "4":
                update_stall_location()

        column_choose()

        new_string = ','.join(ration_list[row_choice_index])

        ration_stalls.close()

        stalls_read = open("ration_stall.txt", "r")

        lines = stalls_read.readlines()

        lines[int(row_choice_index)] = new_string

        with open('ration_stall.txt', 'w') as file1:
            file1.writelines(lines)

        print("File Updated!")

    def add_or_view_func():
        add_or_view = int(input("""
        Would you like to: 
            [1] View 
            [2] Add
        Your Choice: """))

        if add_or_view == 1:
            t_ration = PrettyTable([
                "Stall ID",
                "Ration Stall Name",
                "Packs Supplied",
                "Packs Distributed",
                "Stall Status",
                "Remaining Stock",
                "Stall Location"
            ])
            for z in ration_list:
                t_ration.add_row(z[0:7])
            print(t_ration)
            update_choice()

            home()
        elif add_or_view == 2:
            add_new_stall()
            home()

    add_or_view_func()


def toilets_portal():
    toilets = open("toilets.txt", "r+")

    toilets_list = []
    for line in toilets:
        line_list = line.split(",")
        toilets_list.append(line_list)

    def add_new_toilet():
        new_toilet = ["NA", "NA", "NA", "NA", "NA", "NA", "NA"]

        def new_toilet_id():
            if len(toilets_list) == 0:
                new_toilet[0] = "1"
            elif len(toilets_list) >= 1:
                new_toilet[0] = str((int((toilets_list[-1])[0]) + 1))
            print("The index number for this emergency is ", new_toilet[0])

        new_toilet_id()

        def new_toilet_name():
            new_toilet[1] = input("Toilet Block Name: ")

            toilets_name_list = []
            for n in range(0, len(toilets_list)):
                toilets_name_list.append((toilets_list[n])[1])
            while new_toilet[1] in toilets_name_list:
                new_toilet[1] = input(
                    "This name is already in use. Please enter a new name for this toilet block: ")

        new_toilet_name()

        def new_toilet_location():

            new_toilet[2] = input("Location: ")

        new_toilet_location()

        def new_toilet_proximity():
            accommodations_1 = open("accommodations.txt", "r+")

            blocks_list_1 = []
            for line_1 in accommodations_1:
                line_list_1 = line_1.split(",")
                blocks_list_1.append(line_list_1)

            new_toilet[3] = ""
            for x in blocks_list_1:
                if x[6] == new_toilet[2]:
                    new_toilet[3] += (x[0] + '/')

            new_toilet[3]=new_toilet[3][:-1]

            print("Accommodation Blocks in proximity are ", new_toilet[3])

        new_toilet_proximity()

        new_toilet_string = ','.join(new_toilet)

        toilets.close()

        toilet_append = open("toilets.txt", "a")
        toilet_append.write(new_toilet_string + ",\n")
        toilet_append.close()


    def add_or_view_func():
        add_or_view = int(input("""
        Would you like to: 
            [1] View 
            [2] Add
        Your Choice: """))

        if add_or_view == 1:
            t_toilets = PrettyTable([
                "Toilet ID",
                "Toilet Name",
                "Toilet Location",
                "Toilet Proximity",
                "Block Status",
                "Block Space",
                "Block Location"
            ])
            for z in toilets_list:
                t_toilets.add_row(z[0:7])
            print(t_toilets)

            home()
        elif add_or_view == 2:
            add_new_toilet()
            home()

    add_or_view_func()


def medical_portal():
    pass


def home():
    home_choice = input("""
What would you like to do now?
    [1] Home
    [2] Exit Application
Your Choice: """)

    if home_choice == "1":
        main()
    elif home_choice == "2":
        exit()
    else:
        print("Please enter valid option")
        home()


def main():

    choice = input("""
Select an option: 
    [1] Volunteers
    [2] Accommodation Blocks
    [3] Ration Stalls
    [4] Toilet Blocks
    [5] Medical Dispensaries 
    [6] Exit Application 
Your Choice: """)

    if choice == "1":
        volunteers_portal()
    elif choice == "2":
        accommodation_portal()
    elif choice == "3":
        ration_portal()
    elif choice == "4":
        toilets_portal()
    elif choice == "5":
        medical_portal()
    elif choice == "6":
        exit()
    else:
        print("Please enter valid option")
        main()


if __name__ == '__main__':
    main()
