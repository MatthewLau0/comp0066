VOLUNTEER = 0
CAMP_LEAD = 1
ADMIN = 2

class Database:

    def __init__(self):
        self.volunteers = {}
        self.camps = []
        '''
        volunteers = {
        username1: [role, active (bool), password, phone number, camp, availability (str)]
        }
        '''
    def accept_volunteer(self, name, role, phone, camp, availability):
        volunteer = Volunteer(role, password, phone, camp, availability, True) #creating a user
        self.volunteers[name] = user

    def deactivate_volunteer(self, name):
        volunteer = self.volunteers[name]  #getting a user from database 'users' by name
        volunteer.set_activity(False)

    def reactivate_volunteer(self, name):
        volunteer = self.volunteers[name]
        volunteer.set_activity(True)

    def delete_volunteer(self, name):
        del self.volunteers[name]

class Volunteer:

    def __init__(self, role, phone, camp, availability, active):
        self.role = role
        self.phone = phone
        self.camp = camp
        self.availability = availability
        self.active = active

    def set_activity(self, active):
       self.active = active

    def set_role(self, role):
        self.role = role

    def set_camp(self, camp):
        self.camp = camp


def main():
    database = Database()

    while(True):
        # Login
        name = input("Enter your name: ")
        password = input("Enter your password: ")
        if (database.volunteers[name].password == password):
            role = database.volunteers[name].role
            break

    while (True):

        if (role == VOLUNTEER):
            #MENU for volunteer

            print("0. Quit \n"
              "1. \n")

        elif (role == CAMP_LEAD):
            #MENU for CAMP LEAd

            print("0. Quit \n"
              "1.  \n")

        elif (role == ADMIN):
            #MENU for ADMIN

            print("0. Quit \n"
              "1. Accept Volunteer \n"
              "2. Reactivate Volunteer \n"
              "3. Deactivate Volunteer \n"
              "4. Delete Volunteer \n"
              "5. Assign Role \n"
              "6. Create Emergency Plan \n")

        choice = int(input("Select your choice: "))

        if (choice == 0):
            break

        elif(choice == 1):
            database.accept_volunteer(name)

        elif(choice == 2):
            database.reactivate_volunteer(name)

        elif(choice == 3):
            database.deactivate_volunteer(name)

        elif(choice == 4):
            database.delete_volunteer(name)

        elif(choice == 5):
            print("0. Volunteer \n"
                  "1. Camp Lead")

            role = int(input("Input new role: "))
            if role not in [0,1]:
                print("Role not applicable")
                continue
            database.volunteers[name].set_role(role)

        elif(choice == 6):
            #call the function to create emergency plan

        else:
            print("Invalid choice. \n")


# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^