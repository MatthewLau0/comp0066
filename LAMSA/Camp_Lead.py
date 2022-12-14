from tkinter import *
from tkinter import ttk
import datetime
import Login

camp_id = ""
user_id = ""
user_name = ""
user_username = ""
user_password = ""
user_email = ""
user_number_area = ""
user_number = ""
user_gender = ""
user_dob = ""
user_age = ""
user_status = ""
user_role = ""
user_availability = ""


def camp_id_generate():
    global camp_id
    global user_id
    global user_name
    global user_username
    global user_password
    global user_email
    global user_number_area
    global user_number
    global user_gender
    global user_dob
    global user_age
    global user_status
    global user_role
    global user_availability
    logins_file = open("successful_login.txt", "r")

    logins_list = []
    for line in logins_file:
        line_string = line.split("%")
        logins_list.append(line_string)
    logins_file.close()
    if len(logins_list) > 0:
        camp_id = logins_list[-1][0]
        user_id = logins_list[-1][1]
        user_name = logins_list[-1][2]
        user_username = logins_list[-1][3]
        user_password = logins_list[-1][4]
        user_email = logins_list[-1][5]
        if "#" in logins_list[-1][6]:
            number = []
            number_string = logins_list[-1][6].split("#")
            for i in number_string:
                number.append(i)
            user_number_area = number[0]
            user_number = number[1]
        else:
            user_number = logins_list[-1][6]
        user_gender = logins_list[-1][7]
        user_dob = logins_list[-1][8]
        user_age = logins_list[-1][9]
        user_status = logins_list[-1][10]
        user_role = logins_list[-1][11]
        user_availability = logins_list[-1][12]


def volunteers_portal():
    volunteers_file = open("volunteer_database.txt", "r")

    volunteer_file_extract = []
    for line in volunteers_file:
        line_string = line.split("%")
        if line_string[0] == str(camp_id):
            volunteer_file_extract.append(line_string)

    volunteers_file.close()

    volunteers_list_print = []

    for i in volunteer_file_extract:
        if i[-3] == "Deleted":
            pass
        else:
            volunteers_list_print.append(i)

    volunteers_list = []
    for i in range(0, len(volunteer_file_extract)):
        volunteers_list.append(volunteer_file_extract[i])

    def view_volunteers_list():

        view_volunteers_screen = Toplevel()

        view_volunteers_screen.title("View Volunteers List")

        screen_width = view_volunteers_screen.winfo_screenwidth()
        screen_height = view_volunteers_screen.winfo_screenheight()
        window_height = screen_height
        window_width = 900

        center_x = int(screen_width / 2 - window_width / 2)
        center_y = int(screen_height / 2 - window_height / 2)
        view_volunteers_screen.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

        Label(view_volunteers_screen, text=f"\nPlease see below a lost of all the volunteers at Camp {camp_id}\n").pack()

        game_frame = Frame(view_volunteers_screen)
        game_frame.pack()

        my_game = ttk.Treeview(game_frame)

        my_game['columns'] = (
            "Camp ID",
            "Volunteer ID",
            "Volunteer Name",
            "Volunteer Username",
            "Volunteer Email",
            "Volunteer Number",
            "Volunteer Gender",
            "Volunteer DoB",
            "Volunteer Age",
            "Volunteer Account Status"
        )

        my_game.column("#0", width=0, stretch=NO)
        my_game.column("Camp ID", anchor=CENTER, width=70)
        my_game.column("Volunteer ID", anchor=CENTER, width=75)
        my_game.column("Volunteer Name", anchor=CENTER, width=140)
        my_game.column("Volunteer Username", anchor=CENTER, width=140)
        my_game.column("Volunteer Email", anchor=CENTER, width=160)
        my_game.column("Volunteer Number", anchor=CENTER, width=100)
        my_game.column("Volunteer Gender", anchor=CENTER, width=100)
        my_game.column("Volunteer DoB", anchor=CENTER, width=85)
        my_game.column("Volunteer Age", anchor=CENTER, width=50)
        my_game.column("Volunteer Account Status", anchor=CENTER, width=80)

        my_game.heading("#0", text="", anchor=CENTER)
        my_game.heading("Camp ID", text="Camp ID", anchor=CENTER)
        my_game.heading("Volunteer ID", text="Volunteer ID", anchor=CENTER)
        my_game.heading("Volunteer Name", text="Name", anchor=CENTER)
        my_game.heading("Volunteer Username", text="Username", anchor=CENTER)
        my_game.heading("Volunteer Email", text="Email", anchor=CENTER)
        my_game.heading("Volunteer Number", text="Number", anchor=CENTER)
        my_game.heading("Volunteer Gender", text="Gender", anchor=CENTER)
        my_game.heading("Volunteer DoB", text="DoB", anchor=CENTER)
        my_game.heading("Volunteer Age", text="Age", anchor=CENTER)
        my_game.heading("Volunteer Account Status", text="Account Status", anchor=CENTER)

        for l in range(0, len(volunteers_list_print)):
            current_number = volunteers_list_print[l][6].split('#')
            my_game.insert(parent='', index=l, iid=l, values=(
                volunteers_list_print[l][0],
                volunteers_list_print[l][1],
                volunteers_list_print[l][2],
                volunteers_list_print[l][3],
                volunteers_list_print[l][5],
                f"+{current_number[0]} {current_number[1]}",
                volunteers_list_print[l][7],
                volunteers_list_print[l][8],
                volunteers_list_print[l][9],
                volunteers_list_print[l][10],
            ))

        my_game.pack()

        Label(view_volunteers_screen, text="Please note, you can scroll through the table horizontally and vertically\n").pack()
        Button(view_volunteers_screen, text="Close", command=view_volunteers_screen.destroy).pack()

        view_volunteers_screen.mainloop()

    view_volunteers_list()

def accommodation_portal():

    accommodations = open("accommodation_database.txt", "r+")

    blocks_list = []
    for line in accommodations:
        line_string = line.split(",")
        if line_string[0] == str(camp_id):
            blocks_list.append(line_string)

    accommodations.close()

    def add_new_block():

        new_accommodation = ["NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA"]

        new_accommodation_screen = Toplevel()
        new_accommodation_screen.title("Add New Block")


        new_accommodation[0] = str(camp_id)

        def new_block_id():
            if len(blocks_list) == 0:
                new_accommodation[1] = "1"
            elif len(blocks_list) >= 1:
                new_accommodation[1] = str((int((blocks_list[-1])[1]) + 1))

        new_block_id()

        block_name = StringVar()
        block_cap = StringVar()
        block_location = StringVar()

        new_block_intro_label = Label(new_accommodation_screen, text="To create a new Accommodation Block, please fill in the form below.")
        new_block_intro_label.pack()

        new_block_id_label = Label(new_accommodation_screen, text=f"The ID Number of this Accommodation Block is {new_accommodation[1]}")
        new_block_id_label.pack()

        new_block_name_label = Label(new_accommodation_screen, text="Block Name: ")
        new_block_name_label.pack()
        new_block_name_entry = Entry(new_accommodation_screen, textvariable=block_name)
        new_block_name_entry.pack()

        new_block_capacity_label = Label(new_accommodation_screen, text="Block Capacity: ")
        new_block_capacity_label.pack()
        new_block_capacity_entry = Entry(new_accommodation_screen, textvariable=block_cap)
        new_block_capacity_entry.pack()

        block_location.set("Select Camp Area")
        new_block_location_label = Label(new_accommodation_screen, text="Block Location: ")
        new_block_location_label.pack()
        new_block_location_entry = ttk.Combobox(new_accommodation_screen, textvariable=block_location, values=["North Wing", "East Wing", "South Wing", "West Wing"])
        new_block_location_entry.pack()

        def summary():
            accommodation_summary = Toplevel()

            accommodation_summary.title("Accommodation Block Summary")

            label_1 = Label(accommodation_summary, text="Please check that you are happy with the entry below:")
            label_1.pack()

            summary_label = Label(accommodation_summary, text=f"""
            Block Name: {block_name.get()} \n 
            Block Capacity: {block_cap.get()} \n 
            Block Location: {block_location.get()}""")
            summary_label.pack()

            def edit_command():
                accommodation_summary.destroy()

            def submit_command():
                new_accommodation[2] = block_name.get()
                new_accommodation[3] = str(block_cap.get())
                new_accommodation[4] = str(0)
                new_accommodation[6] = str(int(new_accommodation[3]) - int(new_accommodation[4]))
                if int(new_accommodation[6]) > 0:
                    new_accommodation[5] = "VACANCIES"
                else:
                    new_accommodation[5] = "FULL"
                new_accommodation[7] = block_location.get()

                new_accommodation_string = ','.join(new_accommodation)

                accommodations_append = open("accommodation_database.txt", "a")
                accommodations_append.write(new_accommodation_string + ",\n")
                accommodations_append.close()

                accommodation_summary.destroy()
                new_accommodation_screen.destroy()
                accommodation_window.destroy()
                main_window.destroy()
                run_camp_lead()

            edit_button = Button(accommodation_summary, text="Edit", command=edit_command)
            edit_button.pack()
            submit_button = Button(accommodation_summary, text="Submit", command=submit_command)
            submit_button.pack()

            accommodation_summary.mainloop()

        error_frame = Frame(new_accommodation_screen)

        def check_block():

            for widget in error_frame.winfo_children():
                widget.destroy()

            check_status = ["0", "0", "0", "0", "0", "0"]

            def name_check():
                if block_name.get().strip() == "":
                    new_block_name_reentry_1 = Label(error_frame, text="Please enter a Block Name")
                    new_block_name_reentry_1.pack()
                else:
                    check_status[0] = "1"

                accommodation_name_list = []
                for n in range(0, len(blocks_list)):
                    accommodation_name_list.append(blocks_list[n][2])
                if block_name.get() in accommodation_name_list:
                    new_block_name_reentry_2 = Label(error_frame, text="Name is taken. Please try again")
                    new_block_name_reentry_2.pack()
                else:
                    check_status[1] = "1"

            name_check()

            def cap_check():
                try:
                    int(block_cap.get())
                    check_status[2] = "1"
                except ValueError:
                    new_block_capacity_reentry = Label(error_frame, text="Please enter an integer for capacity")
                    new_block_capacity_reentry.pack()

            cap_check()

            def occ_check():
                try:
                    check_status[3] = "1"
                except ValueError:
                    new_block_occupancy_reentry_1 = Label(error_frame, text="Please enter an integer for occupancy")
                    new_block_occupancy_reentry_1.pack()
                if check_status[3] == "1" and check_status[1] == "1":
                    try:
                        check_status[4] = "1"
                    except ValueError:
                        pass

            occ_check()

            def location_check():
                if block_location.get() == "Select Camp Area":
                    new_block_location_reentry = Label(error_frame, text="Please choose a location")
                    new_block_location_reentry.pack()
                else:
                    check_status[5] = "1"

            location_check()


            if "0" in check_status:
                error_frame.pack()
            else:
                summary()

        new_block_done = Button(new_accommodation_screen, text="Done", command=check_block)
        new_block_done.pack()

        new_accommodation_screen.mainloop()

    def view_existing_blocks():

        view_existing_blocks_screen = Toplevel()

        view_existing_blocks_screen.title("View/Update Accommodation Blocks")

        game_frame = Frame(view_existing_blocks_screen)
        game_frame.pack()

        my_game = ttk.Treeview(game_frame)

        my_game['columns'] = (
            "Camp ID",
            "Block ID",
            "Block Name",
            "Block Capacity",
            "Block Occupancy",
            "Block Status",
            "Block Space",
            "Block Location"
        )

        my_game.column("#0", width=0, stretch=NO)
        my_game.column("Camp ID", anchor=CENTER, width=100)
        my_game.column("Block ID", anchor=CENTER, width=100)
        my_game.column("Block Name", anchor=CENTER, width=150)
        my_game.column("Block Capacity", anchor=CENTER, width=150)
        my_game.column("Block Occupancy", anchor=CENTER, width=150)
        my_game.column("Block Status", anchor=CENTER, width=150)
        my_game.column("Block Space", anchor=CENTER, width=150)
        my_game.column("Block Location", anchor=CENTER, width=150)

        my_game.heading("#0", text="", anchor=CENTER)
        my_game.heading("Camp ID", text="Camp ID", anchor=CENTER)
        my_game.heading("Block ID", text="Block ID", anchor=CENTER)
        my_game.heading("Block Name", text="Name", anchor=CENTER)
        my_game.heading("Block Capacity", text="Capacity", anchor=CENTER)
        my_game.heading("Block Occupancy", text="Occupancy", anchor=CENTER)
        my_game.heading("Block Status", text="Status", anchor=CENTER)
        my_game.heading("Block Space", text="Spaces", anchor=CENTER)
        my_game.heading("Block Location", text="Location", anchor=CENTER)

        for i in range(0, len(blocks_list)):
            my_game.insert(parent='', index=i, iid=i, values=(
                blocks_list[i][0],
                blocks_list[i][1],
                blocks_list[i][2],
                blocks_list[i][3],
                blocks_list[i][4],
                blocks_list[i][5],
                blocks_list[i][6],
                blocks_list[i][7]
            ))

        my_game.pack()

        update_button = Button(view_existing_blocks_screen, text="Update a Block", command=update_block)
        Button(view_existing_blocks_screen, text="Close", command=view_existing_blocks_screen.destroy).pack()

        if len(blocks_list) > 0:
            update_button.pack()

        view_existing_blocks_screen.mainloop()

    def update_block():
        update_block_screen_id = Toplevel()
        update_block_screen_id.title("Update ID Select")

        id_list = []

        for i in blocks_list:
            id_list.append(i[1])

        block_id = StringVar()
        block_name = StringVar()
        block_cap = StringVar()
        block_location = StringVar()

        id_select_label = Label(update_block_screen_id, text="Please choose a block ID to update")
        id_select_label.pack()
        block_id.set("Select ID")
        id_select_option = ttk.Combobox(update_block_screen_id, textvariable=block_id, values=id_list)
        id_select_option.pack()

        def update_run():

            update_block_screen = Toplevel()
            update_block_screen.title("Update Block")

            id1 = int(block_id.get())
            x = id1 - 1

            update_accommodation = [blocks_list[x][0], id1, blocks_list[x][2], blocks_list[x][3], blocks_list[x][4], blocks_list[x][5], blocks_list[x][6], blocks_list[x][7]]

            new_block_intro_label = Label(update_block_screen, text="To update this Accommodation Block, please fill in the form below.")
            new_block_intro_label.pack()

            new_block_id_label = Label(update_block_screen, text=f"The ID Number of this Accommodation Block is {id1}")
            new_block_id_label.pack()

            new_block_name_label = Label(update_block_screen, text="Block Name: ")
            new_block_name_label.pack()
            new_block_name_entry = Entry(update_block_screen, textvariable=block_name)
            new_block_name_entry.insert(END, f"{blocks_list[x][2]}")
            new_block_name_entry.pack()

            new_block_capacity_label = Label(update_block_screen, text="Block Capacity: ")
            new_block_capacity_label.pack()
            new_block_capacity_entry = Entry(update_block_screen, textvariable=block_cap)
            new_block_capacity_entry.insert(END, f"{blocks_list[x][3]}")
            new_block_capacity_entry.pack()

            new_block_occupancy_label = Label(update_block_screen, text=f"Block Occupancy: \n{blocks_list[x][4]}")
            new_block_occupancy_label.pack()

            block_location.set(f"{blocks_list[x][7]}")
            new_block_location_label = Label(update_block_screen, text="Block Location: ")
            new_block_location_label.pack()
            new_block_location_entry = ttk.Combobox(update_block_screen, textvariable=block_location, values=["North Wing", "East Wing", "South Wing", "West Wing"])
            new_block_location_entry.pack()

            def summary():
                accommodation_summary = Toplevel()

                accommodation_summary.title("Accommodation Block Summary")

                label_1 = Label(accommodation_summary, text="Please check that you are happy with the entry below:")
                label_1.pack()

                summary_label = Label(accommodation_summary, text=f"""
                        Block Name: {block_name.get()} \n 
                        Block Capacity: {block_cap.get()} \n 
                        Block Occupancy: {blocks_list[x][4]} \n 
                        Block Location: {block_location.get()}""")
                summary_label.pack()

                def edit_command():
                    accommodation_summary.destroy()

                def submit_command():
                    update_accommodation[1] = str(block_id.get())
                    update_accommodation[2] = block_name.get()
                    update_accommodation[3] = str(block_cap.get())
                    update_accommodation[4] = str(blocks_list[x][4])
                    update_accommodation[6] = str(int(update_accommodation[3]) - int(update_accommodation[4]))
                    if int(update_accommodation[6]) > 0:
                        update_accommodation[5] = "VACANCIES"
                    else:
                        update_accommodation[5] = "FULL"
                    update_accommodation[7] = block_location.get()

                    new_accommodation_string = ','.join(update_accommodation) + ","

                    accommodations.close()

                    accommodations_read = open("accommodation_database.txt", "r")

                    lines = accommodations_read.readlines()

                    list_relevant_lines = []
                    for l in lines:
                        if l[0] == str(camp_id):
                            list_relevant_lines.append(l)

                    for n in list_relevant_lines:
                        lines.remove(n)

                    list_relevant_lines[int(x)] = new_accommodation_string + "\n"

                    for e in list_relevant_lines:
                        lines.append(e)

                    with open('accommodation_database.txt', 'w') as file1:
                        file1.writelines(lines)

                    accommodations_read.close()
                    file1.close()

                    accommodation_summary.destroy()
                    update_block_screen.destroy()
                    accommodation_window.destroy()
                    main_window.destroy()
                    run_camp_lead()

                edit_button = Button(accommodation_summary, text="Edit", command=edit_command)
                edit_button.pack()
                submit_button = Button(accommodation_summary, text="Submit", command=submit_command)
                submit_button.pack()

                accommodation_summary.mainloop()

            error_frame = Frame(update_block_screen)

            def check_block():

                for widget in error_frame.winfo_children():
                    widget.destroy()

                check_status = ["0", "0", "0", "0", "0"]

                def name_check():
                    if block_name.get().strip() == "":
                        new_block_name_reentry_1 = Label(error_frame, text="Please enter a Block Name")
                        new_block_name_reentry_1.pack()
                    else:
                        check_status[0] = "1"
                    accommodation_name_list = []
                    for n in range(0, len(blocks_list)):
                        accommodation_name_list.append(blocks_list[n][2])
                    accommodation_name_list.remove(blocks_list[x][2])
                    if block_name.get() in accommodation_name_list:
                        new_block_name_reentry_2 = Label(error_frame, text="Name is taken. Please try again")
                        new_block_name_reentry_2.pack()
                    else:
                        check_status[0] = "1"

                name_check()

                def cap_check():
                    try:
                        int(block_cap.get())
                        check_status[1] = "1"
                    except ValueError:
                        new_block_capacity_reentry = Label(error_frame, text="Please enter an integer for capacity")
                        new_block_capacity_reentry.pack()

                cap_check()

                def occ_check():
                    try:
                        check_status[2] = "1"
                    except ValueError:
                        new_block_occupancy_reentry_1 = Label(error_frame, text="Please enter an integer for occupancy")
                        new_block_occupancy_reentry_1.pack()
                    if check_status[2] == "1" and check_status[1] == "1":
                        try:
                            if int(blocks_list[x][4]) <= int(block_cap.get()):
                                check_status[4] = "1"
                            else:
                                new_block_occupancy_reentry_2 = Label(error_frame,
                                                                      text="Please enter a capacity higher than the occupancy")
                                new_block_occupancy_reentry_2.pack()
                        except ValueError:
                            pass

                occ_check()

                def location_check():
                    if block_location.get() == "Select Camp Area":
                        new_block_location_reentry = Label(error_frame, text="Please choose a location")
                        new_block_location_reentry.pack()
                    else:
                        check_status[4] = "1"

                location_check()

                if "0" in check_status:
                    error_frame.pack()
                else:
                    summary()

            new_block_done = Button(update_block_screen, text="Done", command=check_block)
            new_block_done.pack()

            update_block_screen.mainloop()

        def run_the_update():
            if block_id.get() == "Select ID":
                id_select_label.config(fg="#f00")
            else:
                update_block_screen_id.destroy()
                update_run()

        id_done = Button(update_block_screen_id, text="Done", command=run_the_update)
        id_done.pack()

        update_block_screen_id.mainloop()

    def generate_accommodation_window():
        global accommodation_window
        accommodation_window = Toplevel()

        accommodation_window.title("Accommodation Portal")

        screen_width = accommodation_window.winfo_screenwidth()
        screen_height = accommodation_window.winfo_screenheight()
        window_height = 500
        window_width = 900

        center_x = int(screen_width / 2 - window_width / 2)
        center_y = int(screen_height / 2 - window_height / 2)
        accommodation_window.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

        accommodation_label = Label(accommodation_window, text="\nAccommodation Portal\n", font=("TkDefaultFont", 22))
        accommodation_label.pack()

        view_block_button = Button(accommodation_window, text="View/Update Accommodation Blocks", command=view_existing_blocks)
        view_block_button.pack()

        add_block_button = Button(accommodation_window, text="Add New Block", command=add_new_block)
        add_block_button.pack()

        camp_layout_button = Button(accommodation_window, text="View Camp Layout", command=camp_layout)
        camp_layout_button.pack()

        Button(accommodation_window, text="Close", command=accommodation_window.destroy).pack()

        accommodation_window.mainloop()

    generate_accommodation_window()


def ration_portal():
    ration = open("ration_database.txt", "r+")

    ration_list = []
    for line in ration:
        line_list = line.split(",")
        if line_list[0] == str(camp_id):
            ration_list.append(line_list)

    def add_new_ration():

        new_ration = ["NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA"]

        new_ration_screen = Toplevel()
        new_ration_screen.title("Add New Ration Stall")

        new_ration[0] = str(camp_id)

        def new_ration_id():
            if len(ration_list) == 0:
                new_ration[1] = "1"
            elif len(ration_list) >= 1:
                new_ration[1] = str((int((ration_list[-1])[1]) + 1))

        new_ration_id()

        ration_name = StringVar()
        ration_supply = StringVar()
        ration_location = StringVar()

        new_block_intro_label = Label(new_ration_screen,
                                      text="To create a new Ration Stall, please fill in the form below.")
        new_block_intro_label.pack()

        new_block_id_label = Label(new_ration_screen,
                                   text=f"The ID Number of this Ration Stall is {new_ration[1]}")
        new_block_id_label.pack()

        new_block_name_label = Label(new_ration_screen, text="Ration Stall Name: ")
        new_block_name_label.pack()
        new_block_name_entry = Entry(new_ration_screen, textvariable=ration_name)
        new_block_name_entry.pack()

        new_block_capacity_label = Label(new_ration_screen, text="Ration Packs Supplied: ")
        new_block_capacity_label.pack()
        new_block_capacity_entry = Entry(new_ration_screen, textvariable=ration_supply)
        new_block_capacity_entry.pack()

        ration_location.set("Select Camp Area")
        new_block_location_label = Label(new_ration_screen, text="Stall Location: ")
        new_block_location_label.pack()
        new_block_location_entry = ttk.Combobox(new_ration_screen, textvariable=ration_location, values=["North Wing", "East Wing", "South Wing", "West Wing"])
        new_block_location_entry.pack()

        def summary():
            ration_summary = Toplevel()

            ration_summary.title("Ration Stall Summary")

            label_1 = Label(ration_summary, text="Please check that you are happy with the entry below:")
            label_1.pack()

            summary_label = Label(ration_summary, text=f"""
                Stall Name: {ration_name.get()} \n 
                Packs Supplied: {ration_supply.get()} \n 
                Stall Location: {ration_location.get()}""")
            summary_label.pack()

            def edit_command():
                ration_summary.destroy()

            def submit_command():
                new_ration[2] = ration_name.get()
                new_ration[3] = str(ration_supply.get())
                new_ration[4] = str(0)
                new_ration[6] = str(int(new_ration[3]) - int(new_ration[4]))
                if int(new_ration[6]) > 0:
                    new_ration[5] = "PACKS REMAINING"
                else:
                    new_ration[5] = "PACKS DEPLETED"
                new_ration[7] = ration_location.get()

                new_ration_string = ','.join(new_ration)

                ration.close()

                ration_append = open("ration_database.txt", "a")
                ration_append.write(new_ration_string + ",\n")
                ration_append.close()

                ration_summary.destroy()
                new_ration_screen.destroy()
                ration_window.destroy()
                main_window.destroy()
                run_camp_lead()

            edit_button = Button(ration_summary, text="Edit", command=edit_command)
            edit_button.pack()
            submit_button = Button(ration_summary, text="Submit", command=submit_command)
            submit_button.pack()

            ration_summary.mainloop()

        error_frame = Frame(new_ration_screen)

        def check_block():

            for widget in error_frame.winfo_children():
                widget.destroy()

            check_status = ["0", "0", "0", "0", "0", "0"]

            def name_check():
                if ration_name.get().strip() == "":
                    new_block_name_reentry_1 = Label(error_frame, text="Please enter a Stall Name")
                    new_block_name_reentry_1.pack()
                else:
                    check_status[0] = "1"

                ration_name_list = []
                for n in range(0, len(ration_list)):
                    ration_name_list.append(ration_list[n][2])
                if ration_name.get() in ration_name_list:
                    new_block_name_reentry_2 = Label(error_frame, text="Name is taken. Please try again")
                    new_block_name_reentry_2.pack()
                else:
                    check_status[1] = "1"

            name_check()

            def supply_check():
                try:
                    int(ration_supply.get())
                    check_status[2] = "1"
                except ValueError:
                    new_block_capacity_reentry = Label(error_frame, text="Please enter an integer for packs supplied")
                    new_block_capacity_reentry.pack()

            supply_check()

            def use_check():
                try:
                    check_status[3] = "1"
                except ValueError:
                    new_block_occupancy_reentry_1 = Label(error_frame, text="Please enter an integer for packs distributed")
                    new_block_occupancy_reentry_1.pack()
                if check_status[3] == "1" and check_status[1] == "1":
                    try:
                        check_status[4] = "1"
                    except ValueError:
                        pass

            use_check()

            def location_check():
                if ration_location.get() == "Select Camp Area":
                    new_block_location_reentry = Label(error_frame, text="Please choose a location")
                    new_block_location_reentry.pack()
                else:
                    check_status[5] = "1"

            location_check()

            if "0" in check_status:
                error_frame.pack()
            else:
                summary()

        new_block_done = Button(new_ration_screen, text="Done", command=check_block)
        new_block_done.pack()

        new_ration_screen.mainloop()

    def view_existing_stalls():

        view_existing_stalls_screen = Toplevel()

        view_existing_stalls_screen.title("View/Update Ration Stalls")

        game_frame = Frame(view_existing_stalls_screen)
        game_frame.pack()

        my_game = ttk.Treeview(game_frame)

        my_game['columns'] = (
            "Camp ID",
            "Stall ID",
            "Ration Stall Name",
            "Ration Packs Supplied",
            "Ration Packs Depleted",
            "Stock Status",
            "Packs Remaining",
            "Stall Location"
        )

        my_game.column("#0", width=0, stretch=NO)
        my_game.column("Camp ID", anchor=CENTER, width=100)
        my_game.column("Stall ID", anchor=CENTER, width=100)
        my_game.column("Ration Stall Name", anchor=CENTER, width=150)
        my_game.column("Ration Packs Supplied", anchor=CENTER, width=150)
        my_game.column("Ration Packs Depleted", anchor=CENTER, width=150)
        my_game.column("Stock Status", anchor=CENTER, width=150)
        my_game.column("Packs Remaining", anchor=CENTER, width=150)
        my_game.column("Stall Location", anchor=CENTER, width=150)

        my_game.heading("#0", text="", anchor=CENTER)
        my_game.heading("Camp ID", text="Camp ID", anchor=CENTER)
        my_game.heading("Stall ID", text="Stall ID", anchor=CENTER)
        my_game.heading("Ration Stall Name", text="Name", anchor=CENTER)
        my_game.heading("Ration Packs Supplied", text="Packs Supplied", anchor=CENTER)
        my_game.heading("Ration Packs Depleted", text="Packs Distributed", anchor=CENTER)
        my_game.heading("Stock Status", text="Stock Status", anchor=CENTER)
        my_game.heading("Packs Remaining", text="Packs Remaining", anchor=CENTER)
        my_game.heading("Stall Location", text="Location", anchor=CENTER)

        for i in range(0, len(ration_list)):
            my_game.insert(parent='', index=i, iid=i, values=(
                ration_list[i][0],
                ration_list[i][1],
                ration_list[i][2],
                ration_list[i][3],
                ration_list[i][4],
                ration_list[i][5],
                ration_list[i][6],
                ration_list[i][7]
            ))

        my_game.pack()

        update_button = Button(view_existing_stalls_screen, text="Update a Stall", command=update_stall)
        Button(view_existing_stalls_screen, text="Close", command=view_existing_stalls_screen.destroy).pack()

        if len(ration_list) > 0:
            update_button.pack()

        view_existing_stalls_screen.mainloop()

    def update_stall():
        update_block_screen_id = Toplevel()
        update_block_screen_id.title("Update ID Select")

        id_list = []

        for i in ration_list:
            id_list.append(i[1])

        ration_id = StringVar()
        ration_name = StringVar()
        ration_supply = StringVar()
        ration_location = StringVar()

        id_select_label = Label(update_block_screen_id, text="Please choose a Stall ID to update")
        id_select_label.pack()
        ration_id.set("Select ID")
        id_select_option = ttk.Combobox(update_block_screen_id, textvariable=ration_id, values=id_list)
        id_select_option.pack()

        def update_run():

            update_block_screen = Toplevel()
            update_block_screen.title("Update Stall")

            idd = int(ration_id.get())
            x = idd - 1

            updated_stall = [ration_list[x][0], idd, ration_list[x][2], ration_list[x][3], ration_list[x][4],
                                    ration_list[x][5], ration_list[x][6], ration_list[x][7]]

            new_block_intro_label = Label(update_block_screen,
                                          text="To update this Ration Stall, please fill in the form below.")
            new_block_intro_label.pack()

            new_block_id_label = Label(update_block_screen, text=f"The ID Number of this Ration Stall is {idd}")
            new_block_id_label.pack()

            new_block_name_label = Label(update_block_screen, text="Stall Name: ")
            new_block_name_label.pack()
            new_block_name_entry = Entry(update_block_screen, textvariable=ration_name)
            new_block_name_entry.insert(END, f"{ration_list[x][2]}")
            new_block_name_entry.pack()

            new_block_capacity_label = Label(update_block_screen, text="Packs Supplied: ")
            new_block_capacity_label.pack()
            new_block_capacity_entry = Entry(update_block_screen, textvariable=ration_supply)
            new_block_capacity_entry.insert(END, f"{ration_list[x][3]}")
            new_block_capacity_entry.pack()

            new_block_occupancy_label = Label(update_block_screen, text=f"Packs Distributed: \n{ration_list[x][4]}")
            new_block_occupancy_label.pack()

            ration_location.set(f"{ration_list[x][7]}")
            new_block_location_label = Label(update_block_screen, text="Stall Location: ")
            new_block_location_label.pack()
            new_block_location_entry = ttk.Combobox(update_block_screen, textvariable=ration_location, values=["North Wing", "East Wing", "South Wing", "West Wing"])
            new_block_location_entry.pack()

            def summary():
                ration_summary = Toplevel()

                ration_summary.title("Ration Stall Summary")

                label_1 = Label(ration_summary, text="Please check that you are happy with the entry below:")
                label_1.pack()

                summary_label = Label(ration_summary, text=f"""
                            Stall Name: {ration_name.get()} \n 
                            Packs Supplied: {ration_supply.get()} \n 
                            Packs Distributed: {ration_list[x][4]} \n 
                            Stall Location: {ration_location.get()}""")
                summary_label.pack()

                def edit_command():
                    ration_summary.destroy()

                def submit_command():
                    updated_stall[1] = str(ration_id.get())
                    updated_stall[2] = ration_name.get()
                    updated_stall[3] = str(ration_supply.get())
                    updated_stall[4] = str(ration_list[x][4])
                    updated_stall[6] = str(int(updated_stall[3]) - int(updated_stall[4]))
                    if int(updated_stall[6]) > 0:
                        updated_stall[5] = "PACKS AVAILABLE"
                    else:
                        updated_stall[5] = "PACKS DEPLETED"
                    updated_stall[7] = ration_location.get()

                    new_ration_string = ','.join(updated_stall) + ","

                    ration.close()

                    ration_read = open("ration_database.txt", "r")

                    lines = ration_read.readlines()

                    list_relevant_lines = []
                    for h in lines:
                        if h[0] == str(camp_id):
                            list_relevant_lines.append(h)

                    for j in list_relevant_lines:
                        lines.remove(j)

                    list_relevant_lines[int(x)] = new_ration_string + "\n"

                    for k in list_relevant_lines:
                        lines.append(k)

                    with open('ration_database.txt', 'w') as file2:
                        file2.writelines(lines)

                    ration_read.close()
                    file2.close()

                    ration_summary.destroy()
                    update_block_screen.destroy()
                    ration_window.destroy()
                    main_window.destroy()
                    run_camp_lead()

                edit_button = Button(ration_summary, text="Edit", command=edit_command)
                edit_button.pack()
                submit_button = Button(ration_summary, text="Submit", command=submit_command)
                submit_button.pack()

                ration_summary.mainloop()

            error_frame = Frame(update_block_screen)

            def check_block():

                for widget in error_frame.winfo_children():
                    widget.destroy()

                check_status = ["0", "0", "0", "0", "0", "0"]

                def name_check():
                    if ration_name.get().strip() == "":
                        new_block_name_reentry_1 = Label(error_frame, text="Please enter a Stall Name")
                        new_block_name_reentry_1.pack()
                    else:
                        check_status[0] = "1"

                    ration_name_list = []
                    for n in range(0, len(ration_list)):
                        ration_name_list.append(ration_list[n][2])
                    ration_name_list.remove(ration_list[x][2])
                    if ration_name.get() in ration_name_list:
                        new_block_name_reentry_2 = Label(error_frame, text="Name is taken. Please try again")
                        new_block_name_reentry_2.pack()
                    else:
                        check_status[1] = "1"

                name_check()

                def supply_check():
                    try:
                        int(ration_supply.get())
                        check_status[2] = "1"
                    except ValueError:
                        new_block_capacity_reentry = Label(error_frame,
                                                           text="Please enter an integer for packs supplied")
                        new_block_capacity_reentry.pack()

                supply_check()

                def use_check():
                    try:
                        check_status[3] = "1"
                    except ValueError:
                        new_block_occupancy_reentry_1 = Label(error_frame,
                                                              text="Please enter an integer for packs distributed")
                        new_block_occupancy_reentry_1.pack()
                    if check_status[3] == "1" and check_status[1] == "1":
                        try:
                            if int(ration_list[x][4]) <= int(ration_supply.get()):
                                check_status[4] = "1"
                            else:
                                new_block_occupancy_reentry_2 = Label(error_frame,
                                                                      text="Please enter a supply higher than the used")
                                new_block_occupancy_reentry_2.pack()
                        except ValueError:
                            pass

                use_check()

                def location_check():
                    if ration_location.get() == "Select Camp Area":
                        new_block_location_reentry = Label(error_frame, text="Please choose a location")
                        new_block_location_reentry.pack()
                    else:
                        check_status[5] = "1"

                location_check()

                if "0" in check_status:
                    error_frame.pack()
                else:
                    summary()

            new_block_done = Button(update_block_screen, text="Done", command=check_block)
            new_block_done.pack()

            update_block_screen.mainloop()

        def run_the_update():
            if ration_id.get() == "Select ID":
                id_select_label.config(fg="#f00")
            else:
                update_block_screen_id.destroy()
                update_run()

        id_done = Button(update_block_screen_id, text="Done", command=run_the_update)
        id_done.pack()

        update_block_screen_id.mainloop()

    def generate_ration_window():
        global ration_window
        ration_window = Toplevel()

        ration_window.title("Ration Portal")

        screen_width = ration_window.winfo_screenwidth()
        screen_height = ration_window.winfo_screenheight()
        window_height = 500
        window_width = 900

        center_x = int(screen_width / 2 - window_width / 2)
        center_y = int(screen_height / 2 - window_height / 2)
        ration_window.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

        ration_label = Label(ration_window, text="Ration Portal", font=("TkDefaultFont", 22))
        ration_label.pack()

        view_block_button = Button(ration_window, text="View/Update Ration Stalls", command=view_existing_stalls)
        view_block_button.pack()

        add_block_button = Button(ration_window, text="Add New Stall", command=add_new_ration)
        add_block_button.pack()

        camp_layout_button = Button(ration_window, text="View Camp Layout", command=camp_layout)
        camp_layout_button.pack()

        Button(ration_window, text="Close", command=ration_window.destroy).pack()

        ration_window.mainloop()

    generate_ration_window()


def toilets_portal():
    toilets = open("toilet_database.txt", "r+")

    toilet_list = []
    for line in toilets:
        line_list = line.split(",")
        if line_list[0] == str(camp_id):
            toilet_list.append(line_list)

    def add_new_toilet():

        new_toilet = ["NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA"]

        new_toilet_screen = Toplevel()
        new_toilet_screen.title("Add New Toilet Block")

        new_toilet[0] = str(camp_id)

        def new_toilet_id():
            if len(toilet_list) == 0:
                new_toilet[1] = "1"
            elif len(toilet_list) >= 1:
                new_toilet[1] = str((int((toilet_list[-1])[1]) + 1))

        new_toilet_id()

        toilet_name = StringVar()
        toilet_cap = StringVar()
        toilet_location = StringVar()

        new_block_intro_label = Label(new_toilet_screen,
                                      text="To create a new Toilet Block, please fill in the form below.")
        new_block_intro_label.pack()

        new_block_id_label = Label(new_toilet_screen,
                                   text=f"The ID Number of this Toilet Block is {new_toilet[1]}")
        new_block_id_label.pack()

        new_block_name_label = Label(new_toilet_screen, text="Toilet Block Name: ")
        new_block_name_label.pack()
        new_block_name_entry = Entry(new_toilet_screen, textvariable=toilet_name)
        new_block_name_entry.pack()

        new_block_capacity_label = Label(new_toilet_screen, text="Toilet Block Capacity: ")
        new_block_capacity_label.pack()
        new_block_capacity_entry = Entry(new_toilet_screen, textvariable=toilet_cap)
        new_block_capacity_entry.pack()

        toilet_location.set("Select Camp Area")
        new_block_location_label = Label(new_toilet_screen, text="Toilet Block Location: ")
        new_block_location_label.pack()
        new_block_location_entry = ttk.Combobox(new_toilet_screen, textvariable=toilet_location, values=["North Wing", "East Wing", "South Wing", "West Wing"])
        new_block_location_entry.pack()

        def summary():
            toilet_summary = Toplevel()

            toilet_summary.title("Toilet Block Summary")

            label_1 = Label(toilet_summary, text="Please check that you are happy with the entry below:")
            label_1.pack()

            summary_label = Label(toilet_summary, text=f"""
                    Toilet Block Name: {toilet_name.get()} \n 
                    Toilet Block Capacity: {toilet_cap.get()} \n 
                    Toilet Block Location: {toilet_location.get()}""")
            summary_label.pack()

            def edit_command():
                toilet_summary.destroy()

            def submit_command():
                new_toilet[2] = toilet_name.get()
                new_toilet[3] = str(toilet_cap.get())
                new_toilet[4] = str(0)
                new_toilet[6] = str(int(new_toilet[3]) - int(new_toilet[4]))
                if int(new_toilet[6]) > 0:
                    new_toilet[5] = "VACANCIES"
                else:
                    new_toilet[5] = "FULL"
                new_toilet[7] = toilet_location.get()

                new_toilet_string = ','.join(new_toilet)

                toilets.close()

                toilet_append = open("toilet_database.txt", "a")
                toilet_append.write(new_toilet_string + ",\n")
                toilet_append.close()

                toilet_summary.destroy()
                new_toilet_screen.destroy()
                toilet_window.destroy()
                main_window.destroy()
                run_camp_lead()

            edit_button = Button(toilet_summary, text="Edit", command=edit_command)
            edit_button.pack()
            submit_button = Button(toilet_summary, text="Submit", command=submit_command)
            submit_button.pack()

            toilet_summary.mainloop()

        error_frame = Frame(new_toilet_screen)

        def check_block():

            for widget in error_frame.winfo_children():
                widget.destroy()

            check_status = ["0", "0", "0", "0", "0", "0"]

            def name_check():
                if toilet_name.get().strip() == "":
                    new_block_name_reentry_1 = Label(error_frame, text="Please enter a Block Name")
                    new_block_name_reentry_1.pack()
                else:
                    check_status[0] = "1"

                ration_name_list = []
                for n in range(0, len(toilet_list)):
                    ration_name_list.append(toilet_list[n][2])
                if toilet_name.get() in ration_name_list:
                    new_block_name_reentry_2 = Label(error_frame, text="Name is taken. Please try again")
                    new_block_name_reentry_2.pack()
                else:
                    check_status[1] = "1"

            name_check()

            def supply_check():
                try:
                    int(toilet_cap.get())
                    check_status[2] = "1"
                except ValueError:
                    new_block_capacity_reentry = Label(error_frame, text="Please enter an integer for toilet capacity")
                    new_block_capacity_reentry.pack()

            supply_check()

            def use_check():
                try:
                    check_status[3] = "1"
                except ValueError:
                    new_block_occupancy_reentry_1 = Label(error_frame,
                                                          text="Please enter an integer for toilet occupancy")
                    new_block_occupancy_reentry_1.pack()
                if check_status[3] == "1" and check_status[1] == "1":
                    try:
                        check_status[4] = "1"
                    except ValueError:
                        pass

            use_check()

            def location_check():
                if toilet_location.get() == "Select Camp Area":
                    new_block_location_reentry = Label(error_frame, text="Please choose a location")
                    new_block_location_reentry.pack()
                else:
                    check_status[5] = "1"

            location_check()

            if "0" in check_status:
                error_frame.pack()
            else:
                summary()

        new_block_done = Button(new_toilet_screen, text="Done", command=check_block)
        new_block_done.pack()

        new_toilet_screen.mainloop()

    def view_existing_toilets():

        view_existing_toilets_screen = Toplevel()

        view_existing_toilets_screen.title("View/Update Toilet Blocks")

        game_frame = Frame(view_existing_toilets_screen)
        game_frame.pack()

        my_game = ttk.Treeview(game_frame)

        my_game['columns'] = (
            "Camp ID",
            "Toilet Block ID",
            "Toilet Block Name",
            "Toilet Block Capacity",
            "Toilet Block Occupancy",
            "Toilet Block Status",
            "Toilet Block Spaces",
            "Toilet Block Location"
        )

        my_game.column("#0", width=0, stretch=NO)
        my_game.column("Camp ID", anchor=CENTER, width=100)
        my_game.column("Toilet Block ID", anchor=CENTER, width=100)
        my_game.column("Toilet Block Name", anchor=CENTER, width=150)
        my_game.column("Toilet Block Capacity", anchor=CENTER, width=150)
        my_game.column("Toilet Block Occupancy", anchor=CENTER, width=150)
        my_game.column("Toilet Block Status", anchor=CENTER, width=150)
        my_game.column("Toilet Block Spaces", anchor=CENTER, width=150)
        my_game.column("Toilet Block Location", anchor=CENTER, width=150)

        my_game.heading("#0", text="", anchor=CENTER)
        my_game.heading("Camp ID", text="Camp ID", anchor=CENTER)
        my_game.heading("Toilet Block ID", text="Block ID", anchor=CENTER)
        my_game.heading("Toilet Block Name", text="Name", anchor=CENTER)
        my_game.heading("Toilet Block Capacity", text="Capacity", anchor=CENTER)
        my_game.heading("Toilet Block Occupancy", text="Occupancy", anchor=CENTER)
        my_game.heading("Toilet Block Status", text="Status", anchor=CENTER)
        my_game.heading("Toilet Block Spaces", text="Spaces", anchor=CENTER)
        my_game.heading("Toilet Block Location", text="Location", anchor=CENTER)

        for i in range(0, len(toilet_list)):
            my_game.insert(parent='', index=i, iid=i, values=(
                toilet_list[i][0],
                toilet_list[i][1],
                toilet_list[i][2],
                toilet_list[i][3],
                toilet_list[i][4],
                toilet_list[i][5],
                toilet_list[i][6],
                toilet_list[i][7]
            ))

        my_game.pack()

        update_button = Button(view_existing_toilets_screen, text="Update a Toilet Block", command=update_toilet)
        Button(view_existing_toilets_screen, text="Close", command=view_existing_toilets_screen.destroy).pack()


        if len(toilet_list) > 0:
            update_button.pack()

        view_existing_toilets_screen.mainloop()

    def update_toilet():
        update_block_screen_id = Toplevel()
        update_block_screen_id.title("Update ID Select")

        id_list = []

        for i in toilet_list:
            id_list.append(i[1])

        toilet_id = StringVar()
        toilet_name = StringVar()
        toilet_cap = StringVar()
        toilet_location = StringVar()

        id_select_label = Label(update_block_screen_id, text="Please choose a Block ID to update")
        id_select_label.pack()
        toilet_id.set("Select ID")
        id_select_option = ttk.Combobox(update_block_screen_id, textvariable=toilet_id, values=id_list)
        id_select_option.pack()

        def update_run():

            update_block_screen = Toplevel()
            update_block_screen.title("Update Block")

            idd = int(toilet_id.get())
            x = idd - 1

            updated_toilet = [toilet_list[x][0], idd, toilet_list[x][2], toilet_list[x][3], toilet_list[x][4],
                            toilet_list[x][5], toilet_list[x][6], toilet_list[x][7]]

            new_block_intro_label = Label(update_block_screen,
                                          text="To update this Toilet Block, please fill in the form below.")
            new_block_intro_label.pack()

            new_block_id_label = Label(update_block_screen, text=f"The ID Number of this Toilet Block is {idd}")
            new_block_id_label.pack()

            new_block_name_label = Label(update_block_screen, text="Toilet Block Name: ")
            new_block_name_label.pack()
            new_block_name_entry = Entry(update_block_screen, textvariable=toilet_name)
            new_block_name_entry.insert(END, f"{toilet_list[x][2]}")
            new_block_name_entry.pack()

            new_block_capacity_label = Label(update_block_screen, text="Toilet Block Capacity: ")
            new_block_capacity_label.pack()
            new_block_capacity_entry = Entry(update_block_screen, textvariable=toilet_cap)
            new_block_capacity_entry.insert(END, f"{toilet_list[x][3]}")
            new_block_capacity_entry.pack()

            new_block_occupancy_label = Label(update_block_screen, text=f"Toilet Block Occupancy: \n{toilet_list[x][4]}")
            new_block_occupancy_label.pack()

            toilet_location.set(f"{toilet_list[x][7]}")
            new_block_location_label = Label(update_block_screen, text="Toilet Block Location: ")
            new_block_location_label.pack()
            new_block_location_entry = ttk.Combobox(update_block_screen, textvariable=toilet_location, values=["North Wing", "East Wing", "South Wing", "West Wing"])
            new_block_location_entry.pack()

            def summary():
                toilet_summary = Toplevel()

                toilet_summary.title("Toilet Block Summary")

                label_1 = Label(toilet_summary, text="Please check that you are happy with the entry below:")
                label_1.pack()

                summary_label = Label(toilet_summary, text=f"""
                                Toilet Block Name: {toilet_name.get()} \n 
                                Toilet Block Capacity: {toilet_cap.get()} \n 
                                Toilet Block Occupancy: {toilet_list[x][4]} \n 
                                Toilet Block Location: {toilet_location.get()}""")
                summary_label.pack()

                def edit_command():
                    toilet_summary.destroy()

                def submit_command():
                    updated_toilet[1] = str(toilet_id.get())
                    updated_toilet[2] = toilet_name.get()
                    updated_toilet[3] = str(toilet_cap.get())
                    updated_toilet[4] = str(toilet_list[x][4])
                    updated_toilet[6] = str(int(updated_toilet[3]) - int(updated_toilet[4]))
                    if int(updated_toilet[6]) > 0:
                        updated_toilet[5] = "VACANCIES"
                    else:
                        updated_toilet[5] = "FULL"
                    updated_toilet[7] = toilet_location.get()

                    new_toilet_string = ','.join(updated_toilet) + ","

                    toilets.close()

                    toilets_read = open("toilet_database.txt", "r")

                    lines = toilets_read.readlines()

                    list_relevant_lines = []
                    for s in lines:
                        if s[0] == str(camp_id):
                            list_relevant_lines.append(s)

                    for t in list_relevant_lines:
                        lines.remove(t)

                    list_relevant_lines[int(x)] = new_toilet_string + "\n"

                    for u in list_relevant_lines:
                        lines.append(u)

                    with open('toilet_database.txt', 'w') as file3:
                        file3.writelines(lines)

                    toilets_read.close()
                    file3.close()

                    toilet_summary.destroy()
                    update_block_screen.destroy()
                    toilet_window.destroy()
                    main_window.destroy()
                    run_camp_lead()

                edit_button = Button(toilet_summary, text="Edit", command=edit_command)
                edit_button.pack()
                submit_button = Button(toilet_summary, text="Submit", command=submit_command)
                submit_button.pack()

                toilet_summary.mainloop()

            error_frame = Frame(update_block_screen)

            def check_block():

                for widget in error_frame.winfo_children():
                    widget.destroy()

                check_status = ["0", "0", "0", "0", "0", "0"]

                def name_check():
                    if toilet_name.get().strip() == "":
                        new_block_name_reentry_1 = Label(error_frame, text="Please enter a Block Name")
                        new_block_name_reentry_1.pack()
                    else:
                        check_status[0] = "1"

                    ration_name_list = []
                    for n in range(0, len(toilet_list)):
                        ration_name_list.append(toilet_list[n][2])
                    ration_name_list.remove(toilet_list[x][2])
                    if toilet_name.get() in ration_name_list:
                        new_block_name_reentry_2 = Label(error_frame, text="Name is taken. Please try again")
                        new_block_name_reentry_2.pack()
                    else:
                        check_status[1] = "1"

                name_check()

                def supply_check():
                    try:
                        int(toilet_cap.get())
                        check_status[2] = "1"
                    except ValueError:
                        new_block_capacity_reentry = Label(error_frame,
                                                           text="Please enter an integer for toilet capacity")
                        new_block_capacity_reentry.pack()

                supply_check()

                def use_check():
                    try:
                        check_status[3] = "1"
                    except ValueError:
                        new_block_occupancy_reentry_1 = Label(error_frame,
                                                              text="Please enter an integer for toilet occupancy")
                        new_block_occupancy_reentry_1.pack()
                    if check_status[3] == "1" and check_status[1] == "1":
                        try:
                            if int(toilet_list[x][4]) <= int(toilet_cap.get()):
                                check_status[4] = "1"
                            else:
                                new_block_occupancy_reentry_2 = Label(error_frame,
                                                                      text="Please enter a capacity higher than the occupancy")
                                new_block_occupancy_reentry_2.pack()
                        except ValueError:
                            pass

                use_check()

                def location_check():
                    if toilet_location.get() == "Select Camp Area":
                        new_block_location_reentry = Label(error_frame, text="Please choose a location")
                        new_block_location_reentry.pack()
                    else:
                        check_status[5] = "1"

                location_check()

                if "0" in check_status:
                    error_frame.pack()
                else:
                    summary()

            new_block_done = Button(update_block_screen, text="Done", command=check_block)
            new_block_done.pack()

            update_block_screen.mainloop()

        def run_the_update():
            if toilet_id.get() == "Select ID":
                id_select_label.config(fg="#f00")
            else:
                update_block_screen_id.destroy()
                update_run()

        id_done = Button(update_block_screen_id, text="Done", command=run_the_update)
        id_done.pack()

        update_block_screen_id.mainloop()

    def generate_toilet_window():
        global toilet_window
        toilet_window = Toplevel()

        toilet_window.title("Toilets Portal")

        screen_width = toilet_window.winfo_screenwidth()
        screen_height = toilet_window.winfo_screenheight()
        window_height = 500
        window_width = 900

        center_x = int(screen_width / 2 - window_width / 2)
        center_y = int(screen_height / 2 - window_height / 2)
        toilet_window.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

        toilet_label = Label(toilet_window, text="Toilets Portal", font=("TkDefaultFont", 22))
        toilet_label.pack()

        view_block_button = Button(toilet_window, text="View/Update Toilet Blocks", command=view_existing_toilets,
                            )
        view_block_button.pack()

        add_block_button = Button(toilet_window, text="Add New Toilet", command=add_new_toilet)
        add_block_button.pack()

        camp_layout_button = Button(toilet_window, text="View Camp Layout", command=camp_layout)
        camp_layout_button.pack()

        Button(toilet_window, text="Close", command=toilet_window.destroy).pack()

        toilet_window.mainloop()

    generate_toilet_window()


def medical_portal():
    medical = open("medical_database.txt", "r+")

    medical_list = []
    for line in medical:
        line_list = line.split(",")
        if line_list[0] == str(camp_id):
            medical_list.append(line_list)

    def add_new_medical():

        new_medical = ["NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA"]

        new_medical_screen = Toplevel()
        new_medical_screen.title("Add New Medical Dispensary")

        new_medical[0] = str(camp_id)

        def new_medical_id():
            if len(medical_list) == 0:
                new_medical[1] = "1"
            elif len(medical_list) >= 1:
                new_medical[1] = str((int((medical_list[-1])[1]) + 1))

        new_medical_id()

        medical_name = StringVar()
        medical_cap = StringVar()
        medical_location = StringVar()

        new_block_intro_label = Label(new_medical_screen,
                                      text="To create a new Medical Dispensary, please fill in the form below.")
        new_block_intro_label.pack()

        new_block_id_label = Label(new_medical_screen,
                                   text=f"The ID Number of this Medical Dispensary is {new_medical[1]}")
        new_block_id_label.pack()

        new_block_name_label = Label(new_medical_screen, text="Medical Dispensary Name: ")
        new_block_name_label.pack()
        new_block_name_entry = Entry(new_medical_screen, textvariable=medical_name)
        new_block_name_entry.pack()

        new_block_capacity_label = Label(new_medical_screen, text="Medical Dispensary Capacity: ")
        new_block_capacity_label.pack()
        new_block_capacity_entry = Entry(new_medical_screen, textvariable=medical_cap)
        new_block_capacity_entry.pack()

        medical_location.set("Select Camp Area")
        new_block_location_label = Label(new_medical_screen, text="Medical Dispensary Location: ")
        new_block_location_label.pack()
        new_block_location_entry = ttk.Combobox(new_medical_screen, textvariable=medical_location, values=["North Wing", "East Wing", "South Wing", "West Wing"])
        new_block_location_entry.pack()

        def summary():
            medical_summary = Toplevel()

            medical_summary.title("Medical Dispensary Summary")

            label_1 = Label(medical_summary, text="Please check that you are happy with the entry below:")
            label_1.pack()

            summary_label = Label(medical_summary, text=f"""
                    Medical Dispensary Name: {medical_name.get()} \n 
                    Medical Dispensary Capacity: {medical_cap.get()} \n 
                    Medical Dispensary Location: {medical_location.get()}""")
            summary_label.pack()

            def edit_command():
                medical_summary.destroy()

            def submit_command():
                new_medical[2] = medical_name.get()
                new_medical[3] = str(medical_cap.get())
                new_medical[4] = str(0)
                new_medical[6] = str(int(new_medical[3]) - int(new_medical[4]))
                if int(new_medical[6]) > 0:
                    new_medical[5] = "VACANCIES"
                else:
                    new_medical[5] = "FULL"
                new_medical[7] = medical_location.get()

                new_medical_string = ','.join(new_medical)

                medical.close()

                medical_append = open("medical_database.txt", "a")
                medical_append.write(new_medical_string + ",\n")
                medical_append.close()

                medical_summary.destroy()
                new_medical_screen.destroy()
                medical_window.destroy()
                main_window.destroy()
                run_camp_lead()

            edit_button = Button(medical_summary, text="Edit", command=edit_command)
            edit_button.pack()
            submit_button = Button(medical_summary, text="Submit", command=submit_command)
            submit_button.pack()

            medical_summary.mainloop()

        error_frame = Frame(new_medical_screen)

        def check_block():

            for widget in error_frame.winfo_children():
                widget.destroy()

            check_status = ["0", "0", "0", "0", "0", "0"]

            def name_check():
                if medical_name.get().strip() == "":
                    new_block_name_reentry_1 = Label(error_frame, text="Please enter a Dispensary Name")
                    new_block_name_reentry_1.pack()
                else:
                    check_status[0] = "1"

                medical_name_list = []
                for n in range(0, len(medical_list)):
                    medical_name_list.append(medical_list[n][2])
                if medical_name.get() in medical_name_list:
                    new_block_name_reentry_2 = Label(error_frame, text="Name is taken. Please try again")
                    new_block_name_reentry_2.pack()
                else:
                    check_status[1] = "1"

            name_check()

            def supply_check():
                try:
                    int(medical_cap.get())
                    check_status[2] = "1"
                except ValueError:
                    new_block_capacity_reentry = Label(error_frame, text="Please enter an integer for dispensary capacity")
                    new_block_capacity_reentry.pack()

            supply_check()

            def use_check():
                try:
                    check_status[3] = "1"
                except ValueError:
                    new_block_occupancy_reentry_1 = Label(error_frame,
                                                          text="Please enter an integer for dispensary occupancy")
                    new_block_occupancy_reentry_1.pack()
                if check_status[3] == "1" and check_status[1] == "1":
                    try:
                        check_status[4] = "1"
                    except ValueError:
                        pass

            use_check()

            def location_check():
                if medical_location.get() == "Select Camp Area":
                    new_block_location_reentry = Label(error_frame, text="Please choose a location")
                    new_block_location_reentry.pack()
                else:
                    check_status[5] = "1"

            location_check()

            if "0" in check_status:
                error_frame.pack()
            else:
                summary()

        new_block_done = Button(new_medical_screen, text="Done", command=check_block)
        new_block_done.pack()

        new_medical_screen.mainloop()

    def view_existing_medical():

        view_existing_medical_screen = Toplevel()

        view_existing_medical_screen.title("View/Update Medical Dispensaries")

        game_frame = Frame(view_existing_medical_screen)
        game_frame.pack()

        my_game = ttk.Treeview(game_frame)

        my_game['columns'] = (
            "Camp ID",
            "Medical Dispensary ID",
            "Medical Dispensary Name",
            "Medical Dispensary Capacity",
            "Medical Dispensary Occupancy",
            "Medical Dispensary Status",
            "Medical Dispensary Spaces",
            "Medical Dispensary Location"
        )

        my_game.column("#0", width=0, stretch=NO)
        my_game.column("Camp ID", anchor=CENTER, width=100)
        my_game.column("Medical Dispensary ID", anchor=CENTER, width=100)
        my_game.column("Medical Dispensary Name", anchor=CENTER, width=150)
        my_game.column("Medical Dispensary Capacity", anchor=CENTER, width=150)
        my_game.column("Medical Dispensary Occupancy", anchor=CENTER, width=150)
        my_game.column("Medical Dispensary Status", anchor=CENTER, width=150)
        my_game.column("Medical Dispensary Spaces", anchor=CENTER, width=150)
        my_game.column("Medical Dispensary Location", anchor=CENTER, width=150)

        my_game.heading("#0", text="", anchor=CENTER)
        my_game.heading("Camp ID", text="Camp ID", anchor=CENTER)
        my_game.heading("Medical Dispensary ID", text="Medical Dispensary ID", anchor=CENTER)
        my_game.heading("Medical Dispensary Name", text="Name", anchor=CENTER)
        my_game.heading("Medical Dispensary Capacity", text="Capacity", anchor=CENTER)
        my_game.heading("Medical Dispensary Occupancy", text="Occupancy", anchor=CENTER)
        my_game.heading("Medical Dispensary Status", text="Status", anchor=CENTER)
        my_game.heading("Medical Dispensary Spaces", text="Spaces", anchor=CENTER)
        my_game.heading("Medical Dispensary Location", text="Location", anchor=CENTER)

        for i in range(0, len(medical_list)):
            my_game.insert(parent='', index=i, iid=i, values=(
                medical_list[i][0],
                medical_list[i][1],
                medical_list[i][2],
                medical_list[i][3],
                medical_list[i][4],
                medical_list[i][5],
                medical_list[i][6],
                medical_list[i][7]
            ))

        my_game.pack()

        update_button = Button(view_existing_medical_screen, text="Update a Medical Dispensary", command=update_stall)
        Button(view_existing_medical_screen, text="Close", command=view_existing_medical_screen.destroy).pack()

        if len(medical_list) > 0:
            update_button.pack()

        view_existing_medical_screen.mainloop()

    def update_stall():
        update_block_screen_id = Toplevel()
        update_block_screen_id.title("Update ID Select")

        id_list = []

        for i in medical_list:
            id_list.append(i[1])

        medical_id = StringVar()
        medical_name = StringVar()
        medical_cap = StringVar()
        medical_location = StringVar()

        id_select_label = Label(update_block_screen_id, text="Please choose a Medical Dispensary ID to update")
        id_select_label.pack()
        medical_id.set("Select ID")
        id_select_option = ttk.Combobox(update_block_screen_id, textvariable=medical_id, values=id_list)
        id_select_option.pack()

        def update_run():

            update_block_screen = Toplevel()
            update_block_screen.title("Update Medical Dispensary")

            idd = int(medical_id.get())
            x = idd - 1

            update_medical = [medical_list[x][0], idd, medical_list[x][2], medical_list[x][3], medical_list[x][4],
                            medical_list[x][5], medical_list[x][6], medical_list[x][7]]

            new_block_intro_label = Label(update_block_screen,
                                          text="To update this Medical Dispensary, please fill in the form below.")
            new_block_intro_label.pack()

            new_block_id_label = Label(update_block_screen, text=f"The ID Number of this Medical Dispensary is {idd}")
            new_block_id_label.pack()

            new_block_name_label = Label(update_block_screen, text="Medical Dispensary Name: ")
            new_block_name_label.pack()
            new_block_name_entry = Entry(update_block_screen, textvariable=medical_name)
            new_block_name_entry.insert(END, f"{medical_list[x][2]}")
            new_block_name_entry.pack()

            new_block_capacity_label = Label(update_block_screen, text="Medical Dispensary Capacity: ")
            new_block_capacity_label.pack()
            new_block_capacity_entry = Entry(update_block_screen, textvariable=medical_cap)
            new_block_capacity_entry.insert(END, f"{medical_list[x][3]}")
            new_block_capacity_entry.pack()

            new_block_occupancy_label = Label(update_block_screen, text=f"Medical Dispensary Occupancy: \n{medical_list[x][4]}")
            new_block_occupancy_label.pack()

            medical_location.set(f"{medical_list[x][7]}")
            new_block_location_label = Label(update_block_screen, text="Medical Dispensary Location: ")
            new_block_location_label.pack()
            new_block_location_entry = ttk.Combobox(update_block_screen, textvariable=medical_location, values=["North Wing", "East Wing", "South Wing", "West Wing"])
            new_block_location_entry.pack()

            def summary():
                medical_summary = Toplevel()

                medical_summary.title("Medical Dispensary Summary")

                label_1 = Label(medical_summary, text="Please check that you are happy with the entry below:")
                label_1.pack()

                summary_label = Label(medical_summary, text=f"""
                                Medical Dispensary Name: {medical_name.get()} \n 
                                Medical Dispensary Capacity: {medical_cap.get()} \n 
                                Medical Dispensary Occupancy: {medical_list[x][4]} \n 
                                Medical Dispensary Location: {medical_location.get()}""")
                summary_label.pack()

                def edit_command():
                    medical_summary.destroy()

                def submit_command():
                    update_medical[1] = str(medical_id.get())
                    update_medical[2] = medical_name.get()
                    update_medical[3] = str(medical_cap.get())
                    update_medical[4] = str(medical_list[x][4])
                    update_medical[6] = str(int(update_medical[3]) - int(update_medical[4]))
                    if int(update_medical[6]) > 0:
                        update_medical[5] = "VACANCIES"
                    else:
                        update_medical[5] = "FULL"
                    update_medical[7] = medical_location.get()

                    new_medical_string = ','.join(update_medical) + ","

                    medical.close()

                    medical_read = open("medical_database.txt", "r")

                    lines = medical_read.readlines()

                    list_relevant_lines = []
                    for w in lines:
                        if w[0] == str(camp_id):
                            list_relevant_lines.append(w)

                    for y in list_relevant_lines:
                        lines.remove(y)

                    list_relevant_lines[int(x)] = new_medical_string + "\n"

                    for z in list_relevant_lines:
                        lines.append(z)

                    with open('medical_database.txt', 'w') as file4:
                        file4.writelines(lines)

                    medical_read.close()
                    file4.close()

                    medical_summary.destroy()
                    update_block_screen.destroy()
                    medical_window.destroy()
                    main_window.destroy()
                    run_camp_lead()

                edit_button = Button(medical_summary, text="Edit", command=edit_command)
                edit_button.pack()
                submit_button = Button(medical_summary, text="Submit", command=submit_command)
                submit_button.pack()

                medical_summary.mainloop()

            error_frame = Frame(update_block_screen)

            def check_block():

                for widget in error_frame.winfo_children():
                    widget.destroy()

                check_status = ["0", "0", "0", "0", "0", "0"]

                def name_check():
                    if medical_name.get().strip() == "":
                        new_block_name_reentry_1 = Label(error_frame, text="Please enter a Medical Dispensary")
                        new_block_name_reentry_1.pack()
                    else:
                        check_status[0] = "1"

                    medical_name_list = []
                    for n in range(0, len(medical_list)):
                        medical_name_list.append(medical_list[n][2])
                    medical_name_list.remove(medical_list[x][2])
                    if medical_name.get() in medical_name_list:
                        new_block_name_reentry_2 = Label(error_frame, text="Name is taken. Please try again")
                        new_block_name_reentry_2.pack()
                    else:
                        check_status[1] = "1"

                name_check()

                def supply_check():
                    try:
                        int(medical_cap.get())
                        check_status[2] = "1"
                    except ValueError:
                        new_block_capacity_reentry = Label(error_frame,
                                                           text="Please enter an integer for dispensary capacity")
                        new_block_capacity_reentry.pack()

                supply_check()

                def use_check():
                    try:
                        check_status[3] = "1"
                    except ValueError:
                        new_block_occupancy_reentry_1 = Label(error_frame, text="Please enter an integer for dispensary occupancy")
                        new_block_occupancy_reentry_1.pack()
                    if check_status[3] == "1" and check_status[1] == "1":
                        try:
                            if int(medical_list[x][4]) <= int(medical_cap.get()):
                                check_status[4] = "1"
                            else:
                                new_block_occupancy_reentry_2 = Label(error_frame,
                                                                      text="Please enter a capacity higher than the occupancy")
                                new_block_occupancy_reentry_2.pack()
                        except ValueError:
                            pass

                use_check()

                def location_check():
                    if medical_location.get() == "Select Camp Area":
                        new_block_location_reentry = Label(error_frame, text="Please choose a location")
                        new_block_location_reentry.pack()
                    else:
                        check_status[5] = "1"

                location_check()

                if "0" in check_status:
                    error_frame.pack()
                else:
                    summary()

            new_block_done = Button(update_block_screen, text="Done", command=check_block)
            new_block_done.pack()

            update_block_screen.mainloop()

        def run_the_update():
            if medical_id.get() == "Select ID":
                id_select_label.config(fg="#f00")
            else:
                update_block_screen_id.destroy()
                update_run()

        id_done = Button(update_block_screen_id, text="Done", command=run_the_update)
        id_done.pack()

        update_block_screen_id.mainloop()

    def generate_medical_window():
        global medical_window
        medical_window = Toplevel()

        medical_window.title("Medical Portal")

        screen_width = medical_window.winfo_screenwidth()
        screen_height = medical_window.winfo_screenheight()
        window_height = 500
        window_width = 900

        center_x = int(screen_width / 2 - window_width / 2)
        center_y = int(screen_height / 2 - window_height / 2)
        medical_window.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

        medical_label = Label(medical_window, text="Medical Portal", font=("TkDefaultFont", 22))
        medical_label.pack()

        view_block_button = Button(medical_window, text="View/Update Medical Dispensaries", command=view_existing_medical)
        view_block_button.pack()

        add_block_button = Button(medical_window, text="Add New Medical Dispensary", command=add_new_medical)
        add_block_button.pack()

        camp_layout_button = Button(medical_window, text="View Camp Layout", command=camp_layout)
        camp_layout_button.pack()

        Button(medical_window, text="Close", command=medical_window.destroy).pack()


        medical_window.mainloop()

    generate_medical_window()


def camp_layout():

    accommodation_file = open("accommodation_database.txt", "r")
    ration_file = open("ration_database.txt", "r")
    toilet_file = open("toilet_database.txt", "r")
    medical_file = open("medical_database.txt", "r")
    volunteer_file = open("volunteer_database.txt", "r")
    refugee_file = open("refugee_database.txt", "r")

    accom_list = []
    for line1 in accommodation_file:
        list1 = line1.split(",")
        if list1[0] == str(camp_id):
            accom_list.append(list1)

    ration_list = []
    for line2 in ration_file:
        list2 = line2.split(",")
        if list2[0] == str(camp_id):
            ration_list.append(list2)

    toilet_list = []
    for line3 in toilet_file:
        list3 = line3.split(",")
        if list3[0] == str(camp_id):
            toilet_list.append(list3)

    medical_list = []
    for line4 in medical_file:
        list4 = line4.split(",")
        if list4[0] == str(camp_id):
            medical_list.append(list4)

    volunteer_list = []
    for line5 in volunteer_file:
        list5 = line5.split("%")
        if list5[0] == str(camp_id):
            volunteer_list.append(list5)

    refugee_list = []
    for line6 in refugee_file:
        list6 = line6.split("%")
        if list6[0] == str(camp_id):
            refugee_list.append(list6)

    accommodation_file.close()
    ration_file.close()
    toilet_file.close()
    medical_file.close()
    volunteer_file.close()
    refugee_file.close()

    accom_north = []
    ration_north = []
    toilet_north = []
    medical_north = []

    accom_east = []
    ration_east = []
    toilet_east = []
    medical_east = []

    accom_south = []
    ration_south = []
    toilet_south = []
    medical_south = []

    accom_west = []
    ration_west = []
    toilet_west = []
    medical_west = []

    for i in accom_list:
        if i[7] == "North Wing":
            accom_north.append(i)
        elif i[7] == "East Wing":
            accom_east.append(i)
        elif i[7] == "South Wing":
            accom_south.append(i)
        elif i[7] == "West Wing":
            accom_west.append(i)

    for i in ration_list:
        if i[7] == "North Wing":
            ration_north.append(i)
        elif i[7] == "East Wing":
            ration_east.append(i)
        elif i[7] == "South Wing":
            ration_south.append(i)
        elif i[7] == "West Wing":
            ration_west.append(i)

    for i in toilet_list:
        if i[7] == "North Wing":
            toilet_north.append(i)
        elif i[7] == "East Wing":
            toilet_east.append(i)
        elif i[7] == "South Wing":
            toilet_south.append(i)
        elif i[7] == "West Wing":
            toilet_west.append(i)

    for i in medical_list:
        if i[7] == "North Wing":
            medical_north.append(i)
        elif i[7] == "East Wing":
            medical_east.append(i)
        elif i[7] == "South Wing":
            medical_south.append(i)
        elif i[7] == "West Wing":
            medical_west.append(i)

    list_occ_north = []
    for i in accom_north:
        x = int(i[4])
        list_occ_north.append(x)
    refugee_north = sum(list_occ_north)

    list_occ_east = []
    for i in accom_east:
        x = int(i[4])
        list_occ_east.append(x)
    refugee_east = sum(list_occ_east)

    list_occ_south = []
    for i in accom_south:
        x = int(i[4])
        list_occ_south.append(x)
    refugee_south = sum(list_occ_south)

    list_occ_west = []
    for i in accom_west:
        x = int(i[4])
        list_occ_west.append(x)
    refugee_west = sum(list_occ_west)

    camp_summary_window = Toplevel()
    camp_summary_window.title("Camp Layout")

    screen_width = camp_summary_window.winfo_screenwidth()
    screen_height = camp_summary_window.winfo_screenheight()
    window_height = screen_height
    window_width = screen_width

    center_x = int(screen_width / 2 - window_width / 2)
    center_y = int(screen_height / 2 - window_height / 2)
    camp_summary_window.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

    summary_frame = Frame(camp_summary_window, highlightbackground="purple", highlightthickness=3)
    summary_frame.pack()
    summary_frame.place(relx=0.88, rely=0.02, anchor=N)

    summary_label = Label(summary_frame, text="Camp Summary", font=("TkDefaultFont", 22, "bold", "underline"))
    summary_label.pack()

    volunteer_label = Label(summary_frame, text=f"No. of Volunteers at this camp: \n{len(volunteer_list)}")
    volunteer_label.pack()

    refugee_total = 0
    for i in refugee_list:
        refugee_total += int(i[3])

    refugee_label = Label(summary_frame, text=f"No. of Refugees at this camp: \n{refugee_total}")
    refugee_label.pack()

    north_frame = Frame(camp_summary_window, highlightbackground="orange", highlightthickness=3)
    north_frame.pack()
    north_frame.place(relx=0.12, rely=0.02, anchor=N)

    north_label = Label(north_frame, text="North Wing", font=("TkDefaultFont", 22, "bold", "underline"))
    north_label.pack()

    north_accom_label = Label(north_frame, text="Accommodation Blocks", font=("TkDefaultFont", 16, "bold", "underline"))
    north_accom_label.pack()

    for i in accom_north:
        accom_north_label = Label(north_frame, text=f"Block {i[1]} ({i[4]} occupants)")
        accom_north_label.pack()

    north_ration_label = Label(north_frame, text="Ration Stalls", font=("TkDefaultFont", 16, "bold", "underline"))
    north_ration_label.pack()

    for i in ration_north:
        ration_north_label = Label(north_frame, text=f"Ration {i[1]}")
        ration_north_label.pack()

    north_toilet_label = Label(north_frame, text="Toilet Blocks", font=("TkDefaultFont", 16, "bold", "underline"))
    north_toilet_label.pack()

    for i in toilet_north:
        toilet_north_label = Label(north_frame, text=f"Toilet {i[1]}")
        toilet_north_label.pack()

    north_medical_label = Label(north_frame, text="Medical Dispensaries", font=("TkDefaultFont", 16, "bold", "underline"))
    north_medical_label.pack()

    for i in medical_north:
        medical_north_label = Label(north_frame, text=f"Medical {i[1]}")
        medical_north_label.pack()

    north_summary_heading = Label(north_frame, text="\nNorth Wing Summary", font=("TkDefaultFont", 16, "bold", "underline"))
    north_summary_heading.pack()

    north_summary_label = Label(north_frame, text=
f"""Accommodation Blocks: 
{len(accom_north)}
Ration Stalls: 
{len(ration_north)}
Toilet Blocks: 
{len(toilet_north)}
Medical Dispensaries: 
{len(medical_north)}
Refugees: 
{str(refugee_north)}
""")

    north_summary_label.pack()

    east_frame = Frame(camp_summary_window, highlightbackground="orange", highlightthickness=3)
    east_frame.pack()
    east_frame.place(relx=0.31, rely=0.02, anchor=N)

    east_label = Label(east_frame, text="East Wing", font=("TkDefaultFont", 22, "bold", "underline"))
    east_label.pack()

    east_accom_label = Label(east_frame, text="Accommodation Blocks", font=("TkDefaultFont", 16, "bold", "underline"))
    east_accom_label.pack()

    for x in accom_east:
        accom_east_label = Label(east_frame, text=f"Block {x[1]} ({x[4]} occupants)")
        accom_east_label.pack()

    east_ration_label = Label(east_frame, text="Ration Stalls", font=("TkDefaultFont", 16, "bold", "underline"))
    east_ration_label.pack()

    for x in ration_east:
        ration_east_label = Label(east_frame, text=f"Ration {x[1]}")
        ration_east_label.pack()

    east_toilet_label = Label(east_frame, text="Toilet Blocks", font=("TkDefaultFont", 16, "bold", "underline"))
    east_toilet_label.pack()

    for x in toilet_east:
        toilet_east_label = Label(east_frame, text=f"Toilet {x[1]}")
        toilet_east_label.pack()

    east_medical_label = Label(east_frame, text="Medical Dispensaries", font=("TkDefaultFont", 16, "bold", "underline"))
    east_medical_label.pack()

    for x in medical_east:
        medical_east_label = Label(east_frame, text=f"Medical {x[1]}")
        medical_east_label.pack()

    east_summary_heading = Label(east_frame, text="\nEast Wing Summary", font=("TkDefaultFont", 16, "bold", "underline"))
    east_summary_heading.pack()

    east_summary_label = Label(east_frame, text=
f"""Accommodation Blocks: 
{len(accom_east)}
Ration Stalls: 
{len(ration_east)}
Toilet Blocks: 
{len(toilet_east)}
Medical Dispensaries: 
{len(medical_east)}
Refugees: 
{str(refugee_east)}
""")

    east_summary_label.pack()

    south_frame = Frame(camp_summary_window, highlightbackground="orange", highlightthickness=3)
    south_frame.pack()
    south_frame.place(relx=0.50, rely=0.02, anchor=N)

    south_label = Label(south_frame, text="South Wing", font=("TkDefaultFont", 22, "bold", "underline"))
    south_label.pack()

    south_accom_label = Label(south_frame, text="Accommodation Blocks", font=("TkDefaultFont", 16, "bold", "underline"))
    south_accom_label.pack()

    for y in accom_south:
        accom_south_label = Label(south_frame, text=f"Block {y[1]} ({y[4]} occupants)")
        accom_south_label.pack()

    south_ration_label = Label(south_frame, text="Ration Stalls", font=("TkDefaultFont", 16, "bold", "underline"))
    south_ration_label.pack()

    for y in ration_south:
        ration_south_label = Label(south_frame, text=f"Ration {y[1]}")
        ration_south_label.pack()

    south_toilet_label = Label(south_frame, text="Toilet Blocks", font=("TkDefaultFont", 16, "bold", "underline"))
    south_toilet_label.pack()

    for y in toilet_south:
        toilet_south_label = Label(south_frame, text=f"Toilet {y[1]}")
        toilet_south_label.pack()

    south_medical_label = Label(south_frame, text="Medical Dispensaries", font=("TkDefaultFont", 16, "bold", "underline"))
    south_medical_label.pack()

    for y in medical_south:
        medical_south_label = Label(south_frame, text=f"Medical {y[1]}")
        medical_south_label.pack()

    south_summary_heading = Label(south_frame, text="\nSouth Wing Summary", font=("TkDefaultFont", 16, "bold", "underline"))
    south_summary_heading.pack()

    south_summary_label = Label(south_frame, text=
f"""Accommodation Blocks: 
{len(accom_south)}
Ration Stalls: 
{len(ration_south)}
Toilet Blocks: 
{len(toilet_south)}
Medical Dispensaries: 
{len(medical_south)}
Refugees: 
{str(refugee_south)}
""")

    south_summary_label.pack()

    west_frame = Frame(camp_summary_window, highlightbackground="orange", highlightthickness=3)
    west_frame.pack()
    west_frame.place(relx=0.69, rely=0.02, anchor=N)

    west_label = Label(west_frame, text="West Wing", font=("TkDefaultFont", 22, "bold", "underline"))
    west_label.pack()

    west_accom_label = Label(west_frame, text="Accommodation Blocks", font=("TkDefaultFont", 16, "bold", "underline"))
    west_accom_label.pack()

    for z in accom_west:
        accom_west_label = Label(west_frame, text=f"Block {z[1]} ({z[4]} occupants)")
        accom_west_label.pack()

    west_ration_label = Label(west_frame, text="Ration Stalls", font=("TkDefaultFont", 16, "bold", "underline"))
    west_ration_label.pack()

    for z in ration_west:
        ration_west_label = Label(west_frame, text=f"Ration {z[1]}")
        ration_west_label.pack()

    west_toilet_label = Label(west_frame, text="Toilet Blocks", font=("TkDefaultFont", 16, "bold", "underline"))
    west_toilet_label.pack()

    for z in toilet_west:
        toilet_west_label = Label(west_frame, text=f"Toilet {z[1]}")
        toilet_west_label.pack()

    west_medical_label = Label(west_frame, text="Medical Dispensaries", font=("TkDefaultFont", 16, "bold", "underline"))
    west_medical_label.pack()

    for z in medical_west:
        medical_west_label = Label(west_frame, text=f"Medical {z[1]}")
        medical_west_label.pack()

    west_summary_heading = Label(west_frame, text="\nWest Wing Summary", font=("TkDefaultFont", 16, "bold", "underline"))
    west_summary_heading.pack()

    west_summary_label = Label(west_frame, text=
f"""Accommodation Blocks: 
{len(accom_west)}
Ration Stalls: 
{len(ration_west)}
Toilet Blocks: 
{len(toilet_west)}
Medical Dispensaries: 
{len(medical_west)}
Refugees: 
{str(refugee_west)}
""")

    west_summary_label.pack()
    Button(camp_summary_window, text="Close", command=camp_summary_window.destroy).pack(side=BOTTOM, pady=20)
    camp_summary_window.mainloop()

def Settings():
    camp_id_generate()
    volunteer_entry_screen = Toplevel()
    volunteer_entry_screen.title("Volunteer Entry Screen")

    screen_width3 = volunteer_entry_screen.winfo_screenwidth()
    screen_height3 = volunteer_entry_screen.winfo_screenheight()
    window_height3 = screen_height3
    window_width3 = 900

    center_x3 = int(screen_width3 / 2 - window_width3 / 2)
    center_y3 = int(screen_height3 / 2 - window_height3 / 2)
    volunteer_entry_screen.geometry(f'{window_width3}x{window_height3}+{center_x3}+{center_y3}')

    emergency_database_file = open("emergency_database.txt", "r")
    emergency_database_list = []
    for line1 in emergency_database_file:
        line_list1 = line1.split("%")
        emergency_database_list.append(line_list1)
    emergency_database_file.close()

    camp_ID_list = []
    for i in range(0, len(emergency_database_list)):
        camp_ID_list.append(emergency_database_list[i][0])

    def campTable():

        headings_frame = Frame(volunteer_entry_screen)

        Label(headings_frame, text="Camp ID:").pack()
        Label(headings_frame, text=f"{camp_id}").pack()
        Label(headings_frame, text="Volunteer ID:").pack()
        Label(headings_frame, text=f"{user_id}").pack()
        Label(headings_frame, text="Full Name:").pack()
        Label(headings_frame, text=f"{user_name}").pack()
        Label(headings_frame, text="Username:").pack()
        Label(headings_frame, text=f"{user_username}").pack()
        Label(headings_frame, text="Email:").pack()
        Label(headings_frame, text=f"{user_email}").pack()
        Label(headings_frame, text="Phone Number:").pack()
        Label(headings_frame, text=f"+{user_number_area} {user_number}").pack()
        Label(headings_frame, text="Gender:").pack()
        Label(headings_frame, text=f"{user_gender}").pack()
        Label(headings_frame, text="Date of Birth:").pack()
        Label(headings_frame, text=f"{user_dob} (Age: {user_age})").pack()
        Label(headings_frame, text="Account Status:").pack()
        Label(headings_frame, text=f"{user_status}").pack()
        Label(headings_frame, text="Account Role:").pack()
        Label(headings_frame, text=f"{user_role}").pack()
        Label(headings_frame, text="Your Availability:").pack()
        Label(headings_frame, text=f"{user_availability}").pack()
        Label(headings_frame,
              text="To edit your availability, please go back to the home page and use Edit Availability Section").pack()

        headings_frame.pack()

        form_frame = Frame(volunteer_entry_screen)
        form_frame.pack()

        def volunteerEntry():
            headings_frame.destroy()

            select_camp_table_button.destroy()

            select_camp_table_label = Label(form_frame,
                                            text="See below the respective locations of the available camps that you could volunteer at. \n Make note of the camp that is closest to your current location.")
            select_camp_table_label.pack()

            select_camp_table_frame = Frame(form_frame)
            select_camp_table_frame.pack()

            select_camp_table = ttk.Treeview(form_frame)
            select_camp_table['columns'] = ("Camp ID", "Camp Name", "Location")

            select_camp_table.column("#0", width=0, stretch=NO)
            select_camp_table.column('Camp ID', anchor=CENTER, width=100)
            select_camp_table.column("Camp Name", anchor=CENTER, width=100)
            select_camp_table.column("Location", anchor=CENTER, width=100)

            select_camp_table.heading('Camp ID', text="Camp ID", anchor=CENTER)
            select_camp_table.heading("Camp Name", text="Camp Name", anchor=CENTER)
            select_camp_table.heading("Location", text="Location", anchor=CENTER)

            for n in range(0, len(emergency_database_list)):
                select_camp_table.insert(parent='', index=n, iid=n, values=(
                    emergency_database_list[n][0], emergency_database_list[n][1],
                    emergency_database_list[n][4]))

            select_camp_table.pack()

            select_camp = StringVar()
            full_name = StringVar()
            email = StringVar()
            phone_area_code = StringVar()
            phone_number = StringVar()
            gender = StringVar()
            volunteer_date = StringVar()
            volunteer_month = StringVar()
            volunteer_year = StringVar()

            select_camp_label = Label(form_frame, text="Please enter the Camp ID")
            select_camp_label.pack()
            select_camp_select = Entry(form_frame, textvariable=select_camp)
            select_camp_select.insert(END, f"{camp_id}")
            select_camp_select.pack()

            full_name_label = Label(form_frame, text="Please enter your full name")
            full_name_label.pack()
            full_name_entry = Entry(form_frame, textvariable=full_name)
            full_name_entry.insert(END, f"{user_name}")
            full_name_entry.pack()

            email_label = Label(form_frame, text="Please enter an email address")
            email_label.pack()
            email_entry = Entry(form_frame, textvariable=email)
            email_entry.insert(END, f"{user_email}")
            email_entry.pack()

            phone_frame = Frame(form_frame)
            phone_frame.pack()

            phone_number_label = Label(phone_frame, text="Please enter a phone number")
            phone_number_label.pack()
            area_code_sign = Label(phone_frame, text="+")
            area_code_sign.pack(side=LEFT)
            phone_number_area_code_entry = Entry(phone_frame, textvariable=phone_area_code)
            phone_number_area_code_entry.insert(END, f"{user_number_area}")
            phone_number_area_code_entry.pack(side=LEFT)
            phone_number_entry = Entry(phone_frame, textvariable=phone_number)
            phone_number_entry.insert(END, f"{user_number}")
            phone_number_entry.pack(side=LEFT)

            gender_list = ["Male", "Female", "Other", "Prefer not to say"]

            gender_label = Label(form_frame, text="Gender:")
            gender_label.pack()
            gender_entry = ttk.Combobox(form_frame, textvariable=gender, values=gender_list)
            gender_entry.insert(END, user_gender)
            gender_entry.pack()

            today = datetime.datetime.today()

            day_list = [str(f) for f in range(1, 32)]
            month_list = [str(f) for f in range(1, 13)]
            year_list = [str(f) for f in range(2023, 1899, -1)]

            dob_label = Label(form_frame, text="Enter your date of birth")
            dob_label.pack()
            dob_frame = Frame(form_frame)
            dob_frame.pack()
            date_day_combobox = ttk.Combobox(dob_frame, textvariable=volunteer_date, values=day_list)
            date_day_combobox.insert(END, user_dob[8:10])
            date_day_combobox.pack(side=LEFT)
            date_month_combobox = ttk.Combobox(dob_frame, textvariable=volunteer_month, values=month_list)
            date_month_combobox.insert(END, user_dob[5:7])
            date_month_combobox.pack(side=LEFT)
            date_year_combobox = ttk.Combobox(dob_frame, textvariable=volunteer_year, values=year_list)
            date_year_combobox.insert(END, user_dob[0:4])
            date_year_combobox.pack(side=LEFT)

            def generate_dob():
                if len(volunteer_date.get()) == 0 or len(volunteer_month.get()) == 0 or len(
                        volunteer_year.get()) == 0:
                    return "empty"
                else:
                    try:
                        startdateComplete = ("%s-%s-%s" % (
                            volunteer_year.get(), volunteer_month.get(), volunteer_date.get()))
                        startDateTime = datetime.datetime.strptime(startdateComplete, "%Y-%m-%d")
                        startDate = datetime.datetime.date(startDateTime)
                        return startDate
                    except ValueError:
                        return "empty"

            def generate_age():
                x = generate_dob()
                if x == "empty":
                    pass
                else:
                    DOB = datetime.datetime.strptime(str(x), "%Y-%m-%d").date()
                    volunteer_age = 0

                    if DOB.month < today.month and today.year > DOB.year:
                        volunteer_age = today.year - DOB.year

                    elif DOB.month > DOB.month and today.year > DOB.year:
                        volunteer_age = today.year - DOB.year - 1

                    elif DOB.month == today.month and today.year > DOB.year and today.day < DOB.day:
                        volunteer_age = today.year - DOB.year - 1

                    elif DOB.month == today.month and today.year > DOB.year and today.day > DOB.day:
                        volunteer_age = today.year - DOB.year
                    return volunteer_age

            new_volunteer_error_list = []

            def newvolunteerVerify():
                dob_label.config(text="DoB is Valid!", fg="green")
                select_camp_label.config(text="Camp ID is Valid!", fg="green")
                full_name_label.config(text="Name is Valid!", fg="green")
                email_label.config(text="Email is Valid!", fg="green")
                phone_number_label.config(text="Phone Number is Valid!", fg="green")
                gender_label.config(text="Gender is Valid!", fg="green")
                new_volunteer_error_list.clear()
                if generate_age() == 0:
                    dob_label.config(
                        text="Please enter your DOB",
                        fg="#f00")
                    new_volunteer_error_list.append("d1")
                if select_camp.get() not in camp_ID_list:
                    select_camp_label.config(
                        text="\nPlease enter a valid Camp ID",
                        fg="#f00")
                    new_volunteer_error_list.append("e1")
                if len(full_name.get()) == 0 or full_name.get() == ' ':
                    full_name_label.config(
                        text="Please enter your full name.",
                        fg='#f00')
                    new_volunteer_error_list.append("e2")
                if all(char.isalpha() for char in full_name.get().replace(" ", "")) is False:
                    full_name_label.config(text="Name can only contain alphabetical characters", fg='#f00')
                    new_volunteer_error_list.append(1.1)
                if '@' not in email.get() or '.' not in email.get():
                    email_label.config(
                        text="Please enter a valid email address",
                        fg='#f00')
                    new_volunteer_error_list.append("e3")
                if len(phone_area_code.get()) > 4 or len(phone_area_code.get()) == 0 or all(char.isdigit() for char in phone_area_code.get()) is False:
                    phone_number_label.config(
                        text="Please enter a valid phone area code and a valid phone number",
                        fg='#f00')
                    new_volunteer_error_list.append("e4")
                if len(phone_number.get()) > 15 or len(phone_number.get()) < 7 or all(char.isdigit() for char in phone_number.get()) is False:
                    phone_number_label.config(
                        text="Please enter a valid phone area code and a valid phone number",
                        fg='#f00')
                    new_volunteer_error_list.append("e5")
                if gender.get() not in gender_list:
                    gender_label.config(text="Please enter a gender from the provided list", fg='#f00')
                    new_volunteer_error_list.append("gender")
                if generate_dob() == "empty":
                    dob_label.config(text="Please enter DoB", fg='#f00')
                    new_volunteer_error_list.append(5)
                if generate_dob() != "empty":
                    test_start_date = datetime.datetime.strptime(str(generate_dob()), "%Y-%m-%d")
                    if test_start_date > today:
                        dob_label.config(text="Please enter a valid DoB", fg='#f00')

                if len(new_volunteer_error_list) > 0:
                    pass
                else:
                    def createvolunteerSubmit():

                        phone_number_complete = ("%s#%s" % (phone_area_code.get(), phone_number.get()))

                        updated_user = ["NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA"]

                        updated_user[0] = select_camp.get()
                        updated_user[1] = user_id
                        updated_user[2] = full_name.get()
                        updated_user[3] = user_username
                        updated_user[4] = user_password
                        updated_user[5] = email.get()
                        updated_user[6] = phone_number_complete
                        updated_user[7] = gender.get()
                        updated_user[8] = str(generate_dob())
                        updated_user[9] = str(generate_age())
                        if select_camp.get() == camp_id:
                            updated_user[10] = user_status
                            updated_user[11] = user_role
                        else:
                            updated_user[10] = "Deactivated"
                            updated_user[11] = "Standard"
                        updated_user[12] = user_availability

                        update_details_toplevel = Toplevel()

                        Label(update_details_toplevel,
                              text="You will now be logged out. Please log back in to see your updated details").pack()
                        if select_camp.get() == camp_id:
                            pass
                        else:
                            Label(update_details_toplevel,
                                  text=f"As you have changed the Camp you wish to volunteer at,\nyour account will be temporarily deactivated and moved to standard volunteer.\nPlease contact the admin to get your account reactivated at made Camp Lead at Camp {select_camp.get()}").pack()

                        def logout_login():
                            global main_window

                            volunteer_read = open("volunteer_database.txt", "r")

                            volunteer_list = []
                            for line2 in volunteer_read:
                                line_string2 = line2.split("%")
                                volunteer_list.append(line_string2)

                            volunteer_read.close()

                            volunteer_list = [updated_user if num[1] == str(user_id) else num for num in volunteer_list]

                            clear_file = open("volunteer_database.txt", "w")
                            clear_file.close()

                            for entry in volunteer_list:
                                with open("volunteer_database.txt", "a") as volunteer_write:
                                    updated_user_string = "%".join(entry)
                                    volunteer_write.write(updated_user_string)
                            volunteer_write.close()

                            update_details_toplevel.destroy()
                            volunteer_entry_screen.destroy()
                            main_window.destroy()
                            Login.main()

                        update_details_toplevel_button = Button(update_details_toplevel, text="Proceed",
                                                                command=logout_login)
                        update_details_toplevel_button.pack()

                        cancel_details_toplevel_button = Button(update_details_toplevel, text="Cancel",
                                                                command=update_details_toplevel.destroy)
                        cancel_details_toplevel_button.pack()

                    createvolunteerSubmit()

            log_out_info = Label(form_frame, text="Please log out and log back in to see updated details")
            log_out_info.pack()

            emergency_submit_button = Button(form_frame, text="Submit", command=newvolunteerVerify)
            emergency_submit_button.pack()

        select_camp_table_button = Button(volunteer_entry_screen, text="Edit Details", command=volunteerEntry)
        select_camp_table_button.pack()
        back_button = Button(volunteer_entry_screen, text="Cancel", command=volunteer_entry_screen.destroy)
        back_button.pack()

    campTable()

    volunteer_entry_screen.mainloop()


def run_camp_lead():
    global main_window

    main_window = Tk()
    main_window.title("Portal Homepage")

    screen_width = main_window.winfo_screenwidth()
    screen_height = main_window.winfo_screenheight()
    window_height = screen_height
    window_width = 900

    center_x = int(screen_width / 2 - window_width / 2)
    center_y = int(screen_height / 2 - window_height / 2)
    main_window.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

    Label(main_window, text="LAMSA", font=("TkDefaultFont", 80, "bold")).pack()
    Label(main_window, text=f"Welcome to Your Portal, {user_name}.\nYou are the Camp Lead of Camp {camp_id}\n", font=("TkDefaultFont", 22)).pack()

    volunteers_button = Button(main_window, text="Volunteer List", command=volunteers_portal)
    volunteers_button.pack()
    accommodation_button = Button(main_window, text="Accommodation Blocks", command=accommodation_portal)
    accommodation_button.pack()
    ration_button = Button(main_window, text="Ration Stalls", command=ration_portal)
    ration_button.pack()
    toilets_button = Button(main_window, text="Toilet Blocks", command=toilets_portal)
    toilets_button.pack()
    medical_button = Button(main_window, text="Medical Dispensaries", command=medical_portal)
    medical_button.pack()
    layout_button = Button(main_window, text="Camp Layout", command=camp_layout)
    layout_button.pack()
    settings_button = Button(main_window, text="Settings", command=Settings)
    settings_button.pack()
    Label(main_window, text="\n").pack()
    exit_button = Button(main_window, text="Log Out", command=lambda: [main_window.destroy(), Login.main()])
    exit_button.pack()

    main_window.mainloop()
