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

def clean_login_database():
    with open("successful_login.txt", 'r') as file1:
        lines = file1.readlines()

    with open("successful_login.txt", 'w') as file1:
        for line in lines:
            if line.strip():
                file1.write(line)
            else:
                pass

    file1.close()


clean_login_database()