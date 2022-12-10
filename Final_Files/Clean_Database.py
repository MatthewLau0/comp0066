def clean_volunteer_database():
    with open("volunteer_database.txt", 'r') as file:
        lines = file.readlines()

    with open("volunteer_database.txt", 'w') as file:
        for line in lines:
            if line[0] == "N":
                pass
            else:
                if line.strip():
                    file.write(line)

    file.close()


clean_volunteer_database()