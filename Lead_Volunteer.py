from tkinter import *
from tkinter import ttk

camp_id = 1

def volunteers_portal():
    pass


def accommodation_portal():

    accommodations = open("accommodations.txt", "r+")

    blocks_list = []
    for line in accommodations:
        line_string = line.split(",")
        if line_string[0] == str(camp_id):
            blocks_list.append(line_string)

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
        block_occ = StringVar()
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

        new_block_occupancy_label = Label(new_accommodation_screen, text="Block Occupancy: ")
        new_block_occupancy_label.pack()
        new_block_occupancy_entry = Entry(new_accommodation_screen, textvariable=block_occ)
        new_block_occupancy_entry.pack()

        location_list = ["North Wing", "East Wing", "South Wing", "West Wing"]
        block_location.set("Select Camp Area")
        new_block_location_label = Label(new_accommodation_screen, text="Block Location: ")
        new_block_location_label.pack()
        new_block_location_entry = OptionMenu(new_accommodation_screen, block_location, *location_list)
        new_block_location_entry.pack()

        def summary():
            accommodation_summary = Toplevel()

            accommodation_summary.title("Accommodation Block Summary")

            label_1 = Label(accommodation_summary, text="Please check that you are happy with the entry below:")
            label_1.pack()

            summary_label = Label(accommodation_summary, text=f"""
            Block Name: {block_name.get()} \n 
            Block Capacity: {block_cap.get()} \n 
            Block Occupancy: {block_occ.get()} \n 
            Block Location: {block_location.get()}""")
            summary_label.pack()

            def edit_command():
                accommodation_summary.destroy()

            def submit_command():
                new_accommodation[2] = block_name.get()
                new_accommodation[3] = str(block_cap.get())
                new_accommodation[4] = str(block_occ.get())
                new_accommodation[6] = str(int(new_accommodation[3]) - int(new_accommodation[4]))
                if int(new_accommodation[6]) > 0:
                    new_accommodation[5] = "VACANT"
                else:
                    new_accommodation[5] = "FULL"
                new_accommodation[7] = block_location.get()

                new_accommodation_string = ','.join(new_accommodation)

                accommodations.close()

                accommodations_append = open("accommodations.txt", "a")
                accommodations_append.write(new_accommodation_string + ",\n")
                accommodations_append.close()

                accommodation_summary.destroy()
                new_accommodation_screen.destroy()
                accommodation_window.destroy()
                main_window.destroy()
                main()

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
                    int(block_occ.get())
                    check_status[3] = "1"
                except ValueError:
                    new_block_occupancy_reentry_1 = Label(error_frame, text="Please enter an integer for occupancy")
                    new_block_occupancy_reentry_1.pack()
                if check_status[3] == "1" and check_status[1] == "1":
                    try:
                        if int(block_occ.get()) <= int(block_cap.get()):
                            check_status[4] = "1"
                        else:
                            new_block_occupancy_reentry_2 = Label(error_frame, text="Please enter an occupancy lower than capacity")
                            new_block_occupancy_reentry_2.pack()
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

        view_existing_blocks_screen.title("View/Update Blocks")

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
        block_occ = StringVar()
        block_location = StringVar()

        id_select_label = Label(update_block_screen_id, text="Please choose a block ID to update")
        id_select_label.pack()
        block_id.set("Select ID")
        id_select_option = OptionMenu(update_block_screen_id, block_id, *id_list)
        id_select_option.pack()

        def update_run():

            update_block_screen = Toplevel()
            update_block_screen.title("Update Block")

            id = int(block_id.get())
            x = id - 1

            update_accommodation = [blocks_list[x][0], id, blocks_list[x][2], blocks_list[x][3], blocks_list[x][4], blocks_list[x][5], blocks_list[x][6], blocks_list[x][7]]

            new_block_intro_label = Label(update_block_screen, text="To update this Accommodation Block, please fill in the form below.")
            new_block_intro_label.pack()

            new_block_id_label = Label(update_block_screen, text=f"The ID Number of this Accommodation Block is {id}")
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

            new_block_occupancy_label = Label(update_block_screen, text="Block Occupancy: ")
            new_block_occupancy_label.pack()
            new_block_occupancy_entry = Entry(update_block_screen, textvariable=block_occ)
            new_block_occupancy_entry.insert(END, f"{blocks_list[x][4]}")
            new_block_occupancy_entry.pack()

            location_list = ["North Wing", "East Wing", "South Wing", "West Wing"]
            block_location.set(f"{blocks_list[x][7]}")
            new_block_location_label = Label(update_block_screen, text="Block Location: ")
            new_block_location_label.pack()
            new_block_location_entry = OptionMenu(update_block_screen, block_location, *location_list)
            new_block_location_entry.pack()

            def summary():
                accommodation_summary = Toplevel()

                accommodation_summary.title("Accommodation Block Summary")

                label_1 = Label(accommodation_summary, text="Please check that you are happy with the entry below:")
                label_1.pack()

                summary_label = Label(accommodation_summary, text=f"""
                        Block Name: {block_name.get()} \n 
                        Block Capacity: {block_cap.get()} \n 
                        Block Occupancy: {block_occ.get()} \n 
                        Block Location: {block_location.get()}""")
                summary_label.pack()

                def edit_command():
                    accommodation_summary.destroy()

                def submit_command():
                    update_accommodation[1] = str(block_id.get())
                    update_accommodation[2] = block_name.get()
                    update_accommodation[3] = str(block_cap.get())
                    update_accommodation[4] = str(block_occ.get())
                    update_accommodation[6] = str(int(update_accommodation[3]) - int(update_accommodation[4]))
                    if int(update_accommodation[6]) > 0:
                        update_accommodation[5] = "VACANT"
                    else:
                        update_accommodation[5] = "FULL"
                    update_accommodation[7] = block_location.get()

                    new_accommodation_string = ','.join(update_accommodation) + ","

                    accommodations.close()

                    accommodations_read = open("accommodations.txt", "r")

                    lines = accommodations_read.readlines()

                    list_relevant_lines = []
                    for i in lines:
                        if i[0] == str(camp_id):
                            list_relevant_lines.append(i)

                    for i in list_relevant_lines:
                        lines.remove(i)

                    list_relevant_lines[int(x)] = new_accommodation_string + "\n"

                    for i in list_relevant_lines:
                        lines.append(i)

                    with open('accommodations.txt', 'w') as file1:
                        file1.writelines(lines)

                    accommodation_summary.destroy()
                    update_block_screen.destroy()
                    accommodation_window.destroy()
                    main_window.destroy()
                    main()

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
                        int(block_occ.get())
                        check_status[2] = "1"
                    except ValueError:
                        new_block_occupancy_reentry_1 = Label(error_frame,
                                                              text="Please enter an integer for occupancy")
                        new_block_occupancy_reentry_1.pack()
                    if check_status[2] == "1" and check_status[1] == "1":
                        try:
                            if int(block_occ.get()) <= int(block_cap.get()):
                                check_status[3] = "1"
                            else:
                                new_block_occupancy_reentry_2 = Label(error_frame,
                                                                      text="Please enter an occupancy lower than capacity")
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

        id_done = Button(update_block_screen_id, text="Done", command=update_run)
        id_done.pack()

        update_block_screen_id.mainloop()

    def generate_accommodation_window():
        global accommodation_window
        accommodation_window = Toplevel()

        accommodation_window.title("Accommodation Portal")

        accommodation_label = Label(accommodation_window, text="Accommodation Portal", font=("Avenir", 22))
        accommodation_label.pack()

        view_block_button = Button(accommodation_window, text="View/Update Blocks", command=view_existing_blocks, width=30, height=2, borderwidth=5)
        view_block_button.pack()

        add_block_button = Button(accommodation_window, text="Add New Block", command=add_new_block, width=30, height=2, borderwidth=5)
        add_block_button.pack()

        camp_layout_button = Button(accommodation_window, text="View Camp Layout", command=camp_layout, width=30, height=2, borderwidth=5)
        camp_layout_button.pack()

        accommodation_window.mainloop()

    generate_accommodation_window()


def ration_portal():
    ration = open("ration_stall.txt", "r+")

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
        ration_use = StringVar()
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

        new_block_occupancy_label = Label(new_ration_screen, text="Ration Packs Distributed: ")
        new_block_occupancy_label.pack()
        new_block_occupancy_entry = Entry(new_ration_screen, textvariable=ration_use)
        new_block_occupancy_entry.pack()

        location_list = ["North Wing", "East Wing", "South Wing", "West Wing"]
        ration_location.set("Select Stall Area")
        new_block_location_label = Label(new_ration_screen, text="Stall Location: ")
        new_block_location_label.pack()
        new_block_location_entry = OptionMenu(new_ration_screen, ration_location, *location_list)
        new_block_location_entry.pack()

        def summary():
            ration_summary = Toplevel()

            ration_summary.title("Accommodation Block Summary")

            label_1 = Label(ration_summary, text="Please check that you are happy with the entry below:")
            label_1.pack()

            summary_label = Label(ration_summary, text=f"""
                Stall Name: {ration_name.get()} \n 
                Packs Supplied: {ration_supply.get()} \n 
                Packs Distributed: {ration_use.get()} \n 
                Stall Location: {ration_location.get()}""")
            summary_label.pack()

            def edit_command():
                ration_summary.destroy()

            def submit_command():
                new_ration[2] = ration_name.get()
                new_ration[3] = str(ration_supply.get())
                new_ration[4] = str(ration_use.get())
                new_ration[6] = str(int(new_ration[3]) - int(new_ration[4]))
                if int(new_ration[6]) > 0:
                    new_ration[5] = "PACKS REMAINING"
                else:
                    new_ration[5] = "PACKS DEPLETED"
                new_ration[7] = ration_location.get()

                new_ration_string = ','.join(new_ration)

                ration.close()

                ration_append = open("ration_stall.txt", "a")
                ration_append.write(new_ration_string + ",\n")
                ration_append.close()

                ration_summary.destroy()
                new_ration_screen.destroy()
                ration_window.destroy()
                main_window.destroy()
                main()

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
                    int(ration_use.get())
                    check_status[3] = "1"
                except ValueError:
                    new_block_occupancy_reentry_1 = Label(error_frame, text="Please enter an integer for packs distributed")
                    new_block_occupancy_reentry_1.pack()
                if check_status[3] == "1" and check_status[1] == "1":
                    try:
                        if int(ration_use.get()) <= int(ration_supply.get()):
                            check_status[4] = "1"
                        else:
                            new_block_occupancy_reentry_2 = Label(error_frame,
                                                                  text="Please enter an used lower than supplied")
                            new_block_occupancy_reentry_2.pack()
                    except ValueError:
                        pass

            use_check()

            def location_check():
                if ration_location.get() == "Select Stall Area":
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

        view_existing_stalls_screen.title("View/Update Stalls")

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
        ration_use = StringVar()
        ration_location = StringVar()

        id_select_label = Label(update_block_screen_id, text="Please choose a Stall ID to update")
        id_select_label.pack()
        ration_id.set("Select ID")
        id_select_option = OptionMenu(update_block_screen_id, ration_id, *id_list)
        id_select_option.pack()

        def update_run():

            update_block_screen = Toplevel()
            update_block_screen.title("Update Stall")

            id = int(ration_id.get())
            x = id - 1

            update_stall = [ration_list[x][0], id, ration_list[x][2], ration_list[x][3], ration_list[x][4],
                                    ration_list[x][5], ration_list[x][6], ration_list[x][7]]

            new_block_intro_label = Label(update_block_screen,
                                          text="To update this Ration Stall, please fill in the form below.")
            new_block_intro_label.pack()

            new_block_id_label = Label(update_block_screen, text=f"The ID Number of this Ration Stall is {id}")
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

            new_block_occupancy_label = Label(update_block_screen, text="Packs Distributed: ")
            new_block_occupancy_label.pack()
            new_block_occupancy_entry = Entry(update_block_screen, textvariable=ration_use)
            new_block_occupancy_entry.insert(END, f"{ration_list[x][4]}")
            new_block_occupancy_entry.pack()

            location_list = ["North Wing", "East Wing", "South Wing", "West Wing"]
            ration_location.set(f"{ration_list[x][7]}")
            new_block_location_label = Label(update_block_screen, text="Stall Location: ")
            new_block_location_label.pack()
            new_block_location_entry = OptionMenu(update_block_screen, ration_location, *location_list)
            new_block_location_entry.pack()

            def summary():
                ration_summary = Toplevel()

                ration_summary.title("Ration Stall Summary")

                label_1 = Label(ration_summary, text="Please check that you are happy with the entry below:")
                label_1.pack()

                summary_label = Label(ration_summary, text=f"""
                            Stall Name: {ration_name.get()} \n 
                            Packs Supplied: {ration_supply.get()} \n 
                            Packs Distributed: {ration_use.get()} \n 
                            Stall Location: {ration_location.get()}""")
                summary_label.pack()

                def edit_command():
                    ration_summary.destroy()

                def submit_command():
                    update_stall[1] = str(ration_id.get())
                    update_stall[2] = ration_name.get()
                    update_stall[3] = str(ration_supply.get())
                    update_stall[4] = str(ration_use.get())
                    update_stall[6] = str(int(update_stall[3]) - int(update_stall[4]))
                    if int(update_stall[6]) > 0:
                        update_stall[5] = "PACKS AVAILABLE"
                    else:
                        update_stall[5] = "PACKS DEPLETED"
                    update_stall[7] = ration_location.get()

                    new_ration_string = ','.join(update_stall) + ","

                    ration.close()

                    ration_read = open("ration_stall.txt", "r")

                    lines = ration_read.readlines()

                    list_relevant_lines = []
                    for i in lines:
                        if i[0] == str(camp_id):
                            list_relevant_lines.append(i)

                    for i in list_relevant_lines:
                        lines.remove(i)

                    list_relevant_lines[int(x)] = new_ration_string + "\n"

                    for i in list_relevant_lines:
                        lines.append(i)

                    with open('ration_stall.txt', 'w') as file2:
                        file2.writelines(lines)

                    ration_summary.destroy()
                    update_block_screen.destroy()
                    ration_window.destroy()
                    main_window.destroy()
                    main()

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
                        int(ration_use.get())
                        check_status[3] = "1"
                    except ValueError:
                        new_block_occupancy_reentry_1 = Label(error_frame,
                                                              text="Please enter an integer for packs distributed")
                        new_block_occupancy_reentry_1.pack()
                    if check_status[3] == "1" and check_status[1] == "1":
                        try:
                            if int(ration_use.get()) <= int(ration_supply.get()):
                                check_status[4] = "1"
                            else:
                                new_block_occupancy_reentry_2 = Label(error_frame,
                                                                      text="Please enter an used lower than supplied")
                                new_block_occupancy_reentry_2.pack()
                        except ValueError:
                            pass

                use_check()

                def location_check():
                    if ration_location.get() == "Select Stall Area":
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

        id_done = Button(update_block_screen_id, text="Done", command=update_run)
        id_done.pack()

        update_block_screen_id.mainloop()

    def generate_ration_window():
        global ration_window
        ration_window = Toplevel()

        ration_window.title("Ration Portal")

        accommodation_label = Label(ration_window, text="Ration Portal", font=("Avenir", 22))
        accommodation_label.pack()

        view_block_button = Button(ration_window, text="View/Update Stalls", command=view_existing_stalls,
                                   width=30, height=2, borderwidth=5)
        view_block_button.pack()

        add_block_button = Button(ration_window, text="Add New Stall", command=add_new_ration, width=30, height=2,
                                  borderwidth=5)
        add_block_button.pack()

        camp_layout_button = Button(ration_window, text="View Camp Layout", command=camp_layout, width=30,
                                    height=2, borderwidth=5)
        camp_layout_button.pack()

        ration_window.mainloop()

    generate_ration_window()


def toilets_portal():
    pass


def medical_portal():
    pass


def camp_layout():

    accommodation_file = open("accommodations.txt", "r")
    ration_file = open("ration_stall.txt", "r")
    toilet_file = open("toilets.txt", "r")
    medical_file = open("medical.txt", "r")

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

    camp_summary_window = Toplevel()
    camp_summary_window.title("Camp Layout")

    screen_width = main_window.winfo_screenwidth()
    screen_height = main_window.winfo_screenheight()
    window_height = screen_height
    window_width = 750

    center_x = int(screen_width / 2 - window_width / 2)
    center_y = int(screen_height / 2 - window_height / 2)
    camp_summary_window.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

    north_frame = Frame(camp_summary_window, highlightbackground="orange", highlightthickness=3)
    north_frame.pack()
    north_frame.place(relx=0.5, rely=0.02, anchor=N)

    north_label = Label(north_frame, text="North Wing", font=("Avenir", 22, "bold", "underline"))
    north_label.pack()

    north_accom_label = Label(north_frame, text="Accommodation Blocks", font=("Avenir", 16, "bold", "underline"))
    north_accom_label.pack()

    for i in accom_north:
        accom_north_label = Label(north_frame, text=f"{i[2]} ({i[4]} occupants)")
        accom_north_label.pack()

    north_ration_label = Label(north_frame, text="Ration Stalls", font=("Avenir", 16, "bold", "underline"))
    north_ration_label.pack()

    for i in ration_north:
        ration_north_label = Label(north_frame, text=f"Hello {i[2]}")
        ration_north_label.pack()

    north_toilet_label = Label(north_frame, text="Toilet Blocks", font=("Avenir", 16, "bold", "underline"))
    north_toilet_label.pack()

    for i in toilet_north:
        toilet_north_label = Label(north_frame, text=f"Hello {i[2]}")
        toilet_north_label.pack()

    north_medical_label = Label(north_frame, text="Medical Dispensaries", font=("Avenir", 16, "bold", "underline"))
    north_medical_label.pack()

    for i in medical_north:
        medical_north_label = Label(north_frame, text=f"Hello {i[2]}")
        medical_north_label.pack()

    east_frame = Frame(camp_summary_window, highlightbackground="orange", highlightthickness=3)
    east_frame.pack()
    east_frame.place(relx=0.98, rely=0.5, anchor=E)

    east_label = Label(east_frame, text="East Wing", font=("Avenir", 22, "bold", "underline"))
    east_label.pack()

    east_accom_label = Label(east_frame, text="Accommodation Blocks", font=("Avenir", 16, "bold", "underline"))
    east_accom_label.pack()

    for x in accom_east:
        accom_east_label = Label(east_frame, text=f"{x[2]} ({x[4]} occupants)")
        accom_east_label.pack()

    east_ration_label = Label(east_frame, text="Ration Stalls", font=("Avenir", 16, "bold", "underline"))
    east_ration_label.pack()

    for x in ration_east:
        ration_east_label = Label(east_frame, text=f"Hello {x[2]}")
        ration_east_label.pack()

    east_toilet_label = Label(east_frame, text="Toilet Blocks", font=("Avenir", 16, "bold", "underline"))
    east_toilet_label.pack()

    for x in toilet_east:
        toilet_east_label = Label(east_frame, text=f"Hello {x[2]}")
        toilet_east_label.pack()

    east_medical_label = Label(east_frame, text="Medical Dispensaries", font=("Avenir", 16, "bold", "underline"))
    east_medical_label.pack()

    for x in medical_east:
        medical_east_label = Label(east_frame, text=f"Hello {x[2]}")
        medical_east_label.pack()

    south_frame = Frame(camp_summary_window, highlightbackground="orange", highlightthickness=3)
    south_frame.pack()
    south_frame.place(relx=0.5, rely=0.98, anchor=S)

    south_label = Label(south_frame, text="South Wing", font=("Avenir", 22, "bold", "underline"))
    south_label.pack()

    south_accom_label = Label(south_frame, text="Accommodation Blocks", font=("Avenir", 16, "bold", "underline"))
    south_accom_label.pack()

    for y in accom_south:
        accom_south_label = Label(south_frame, text=f"{y[2]} ({y[4]} occupants)")
        accom_south_label.pack()

    south_ration_label = Label(south_frame, text="Ration Stalls", font=("Avenir", 16, "bold", "underline"))
    south_ration_label.pack()

    for y in ration_south:
        ration_south_label = Label(south_frame, text=f"Hello {y[2]}")
        ration_south_label.pack()

    south_toilet_label = Label(south_frame, text="Toilet Blocks", font=("Avenir", 16, "bold", "underline"))
    south_toilet_label.pack()

    for y in toilet_south:
        toilet_south_label = Label(south_frame, text=f"Hello {y[2]}")
        toilet_south_label.pack()

    south_medical_label = Label(south_frame, text="Medical Dispensaries", font=("Avenir", 16, "bold", "underline"))
    south_medical_label.pack()

    for y in medical_south:
        medical_south_label = Label(south_frame, text=f"Hello {y[2]}")
        medical_south_label.pack()

    west_frame = Frame(camp_summary_window, highlightbackground="orange", highlightthickness=3)
    west_frame.pack()
    west_frame.place(relx=0.02, rely=0.5, anchor=W)

    west_label = Label(west_frame, text="West Wing", font=("Avenir", 22, "bold", "underline"))
    west_label.pack()

    west_accom_label = Label(west_frame, text="Accommodation Blocks", font=("Avenir", 16, "bold", "underline"))
    west_accom_label.pack()

    for z in accom_west:
        accom_west_label = Label(west_frame, text=f"{z[2]} ({z[4]} occupants)")
        accom_west_label.pack()

    west_ration_label = Label(west_frame, text="Ration Stalls", font=("Avenir", 16, "bold", "underline"))
    west_ration_label.pack()

    for z in ration_west:
        ration_west_label = Label(west_frame, text=f"Hello {z[2]}")
        ration_west_label.pack()

    west_toilet_label = Label(west_frame, text="Toilet Blocks", font=("Avenir", 16, "bold", "underline"))
    west_toilet_label.pack()

    for z in toilet_west:
        toilet_west_label = Label(west_frame, text=f"Hello {z[2]}")
        toilet_west_label.pack()

    west_medical_label = Label(west_frame, text="Medical Dispensaries", font=("Avenir", 16, "bold", "underline"))
    west_medical_label.pack()

    for z in medical_west:
        medical_west_label = Label(west_frame, text=f"Hello {z[2]}")
        medical_west_label.pack()

    camp_summary_window.mainloop()


def settings():
    pass



def main():
    global main_window


    main_window = Tk()
    main_window.minsize(320, 435)
    main_window.maxsize(320, 435)

    main_window.title("Portal Homepage")

    portal_welcome = Label(main_window, text="Welcome to Your Portal!", height=2, font=('Avenir', 25, "bold", "underline"))
    portal_welcome.pack()

    volunteers_button = Button(main_window, text="Volunteers List", command=volunteers_portal, width=30, height=2)
    volunteers_button.pack()
    accommodation_button = Button(main_window, text="Accommodation Blocks", command=accommodation_portal, width=30, height=2)
    accommodation_button.pack()
    ration_button = Button(main_window, text="Ration Stalls", command=ration_portal, width=30, height=2)
    ration_button.pack()
    toilets_button = Button(main_window, text="Toilet Blocks", command=toilets_portal, width=30, height=2)
    toilets_button.pack()
    medical_button = Button(main_window, text="Medical Dispensaries", command=medical_portal, width=30, height=2)
    medical_button.pack()
    layout_button = Button(main_window, text="Camp Layout", command=camp_layout, width=30, height=2)
    layout_button.pack()
    settings_button = Button(main_window, text="Settings", command=settings, width=30, height=2)
    settings_button.pack()
    exit_button = Button(main_window, text="Log Out", command=exit, width=30, height=2)
    exit_button.pack()

    main_window.mainloop()

if __name__ == '__main__':
    main()
