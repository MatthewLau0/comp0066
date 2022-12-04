import tkinter as tk
from tkinter import *
from tkinter import ttk


def volunteers_portal():
    pass


def accommodation_portal():
    accommodations = open("accommodations.txt", "r+")

    blocks_list = []
    for line in accommodations:
        line_list = line.split(",")
        blocks_list.append(line_list)

    def add_new_block():

        new_accommodation_screen = tk.Tk()

        new_accommodation_screen.title("Add New Accommodation Block")

        new_accommodation = ["NA", "NA", "NA", "NA", "NA", "NA", "NA"]

        def new_block_id():
            if len(blocks_list) == 0:
                new_accommodation[0] = "1"
            elif len(blocks_list) >= 1:
                new_accommodation[0] = str((int((blocks_list[-1])[0]) + 1))

        new_block_id()

        block_name = StringVar()
        block_cap = IntVar()
        block_occ = IntVar()
        block_location = StringVar()

        new_block_intro_label = Label(new_accommodation_screen,
                                      text="You are going to make a new emergency plan. Please follow the below instructions")
        new_block_intro_label.pack()

        new_block_id_label = Label(new_accommodation_screen,
                                   text="The index number for your camp is " + new_accommodation[0])
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

        new_block_location_label = Label(new_accommodation_screen, text="Block Location: ")
        new_block_location_label.pack()
        new_block_location_entry = Entry(new_accommodation_screen, textvariable=block_location)
        new_block_location_entry.pack()

        def check_done():
            new_accommodation_screen.destroy()

            new_accommodation[1] = block_name.get()
            new_accommodation[2] = str(block_cap.get())
            new_accommodation[3] = str(block_occ.get())
            new_accommodation[5] = str(int(new_accommodation[2]) - int(new_accommodation[3]))
            if int(new_accommodation[5]) > 0:
                new_accommodation[4] = "VACANT SPACES"
            else:
                new_accommodation[4] = "FULL"
            new_accommodation[6] = block_location.get()

            window = tk.Tk()

            window.title("Summary")

            text = Label(window, text=f"Hello {new_accommodation[1]} and {new_accommodation[2]} and {new_accommodation[3]} and {new_accommodation[4]}")
            text.pack()

            window.mainloop()

        new_block_done = Button(new_accommodation_screen, text="Done", command=check_done)
        new_block_done.pack()

        new_accommodation_screen.mainloop()

        new_accommodation_string = ','.join(new_accommodation)

        accommodations.close()

        accommodations_append = open("accommodations.txt", "a")
        accommodations_append.write(new_accommodation_string + ",\n")
        accommodations_append.close()

    def view_existing_blocks():

        view_existing_blocks_screen = tk.Tk()

        view_existing_blocks_screen.title("Existing Accommodation Blocks")

        game_frame = Frame(view_existing_blocks_screen)
        game_frame.pack()

        my_game = ttk.Treeview(game_frame)

        my_game['columns'] = (
            "Block ID",
            "Block Name",
            "Block Capacity",
            "Block Occupancy",
            "Block Status",
            "Block Space",
            "Block Location"
        )

        my_game.column("#0", width=0, stretch=NO)
        my_game.column("Block ID", anchor=CENTER, width=150)
        my_game.column("Block Name", anchor=CENTER, width=150)
        my_game.column("Block Capacity", anchor=CENTER, width=150)
        my_game.column("Block Occupancy", anchor=CENTER, width=150)
        my_game.column("Block Status", anchor=CENTER, width=150)
        my_game.column("Block Space", anchor=CENTER, width=150)
        my_game.column("Block Location", anchor=CENTER, width=150)

        my_game.heading("#0", text="", anchor=CENTER)
        my_game.heading("Block ID", text="ID", anchor=CENTER)
        my_game.heading("Block Name", text="Name", anchor=CENTER)
        my_game.heading("Block Capacity", text="Capacity", anchor=CENTER)
        my_game.heading("Block Occupancy", text="Occupancy", anchor=CENTER)
        my_game.heading("Block Status", text="Status", anchor=CENTER)
        my_game.heading("Block Space", text="Space", anchor=CENTER)
        my_game.heading("Block Location", text="Location", anchor=CENTER)

        for s in range(0, len(blocks_list)):
            my_game.insert(parent='', index=s, iid=s, values=(
                blocks_list[s][0],
                blocks_list[s][1],
                blocks_list[s][2],
                blocks_list[s][3],
                blocks_list[s][4],
                blocks_list[s][5],
                blocks_list[s][6]
            ))
            s += 1

        my_game.pack()

        view_existing_blocks_screen.mainloop()

    def generate_accommodation_window():
        global accommodation_window
        accommodation_window = tk.Tk()

        accommodation_window.title("Accommodation Portal")

        window_width = 1000
        window_height = 800
        screen_width = accommodation_window.winfo_screenwidth()
        screen_height = accommodation_window.winfo_screenheight()
        center_x = int(screen_width / 2 - window_width / 2)
        center_y = int(screen_height / 2 - window_height / 2)
        accommodation_window.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

        view_block_button = tk.Button(accommodation_window, text="View Existing Blocks", command=view_existing_blocks)
        view_block_button.pack()

        add_block_button = tk.Button(accommodation_window, text="Add New Block", command=add_new_block)
        add_block_button.pack()

        accommodation_window.mainloop()

    generate_accommodation_window()


def ration_portal():
    pass


def toilets_portal():
    pass


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
    main_window = tk.Tk()

    main_window.title("Camp Head Homepage")

    window_width = 800
    window_height = 600
    screen_width = main_window.winfo_screenwidth()
    screen_height = main_window.winfo_screenheight()
    center_x = int(screen_width / 2 - window_width / 2)
    center_y = int(screen_height / 2 - window_height / 2)
    main_window.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

    volunteers_button = tk.Button(main_window, text="Volunteers List", command=volunteers_portal)
    volunteers_button.pack()
    accommodation_button = tk.Button(main_window, text="Accommodation Blocks", command=accommodation_portal)
    accommodation_button.pack()
    ration_button = tk.Button(main_window, text="Ration Stalls", command=ration_portal)
    ration_button.pack()
    toilets_button = tk.Button(main_window, text="Toilet Blocks", command=toilets_portal)
    toilets_button.pack()
    medical_button = tk.Button(main_window, text="Medical Dispensaries", command=medical_portal)
    medical_button.pack()
    exit_button = tk.Button(main_window, text="Log Out", command=exit)
    exit_button.pack()

    main_window.mainloop()


if __name__ == '__main__':
    main()
