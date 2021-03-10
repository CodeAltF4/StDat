import random

class CreateStudent():
    def __init__(self, firstName, lastName, birthDate):
        self.firstName = firstName
        self.lastName = lastName
        self.birthDate = birthDate

    def createStudentID(self):
        #creating email, ID and then checking if the ID allready exists
        email = self.firstName.capitalize() + self.lastName.capitalize() + "@school.com" #* replace @school.com with school name

        studentID = str(self.createID())
        self.studentID = studentID

        print(f"Name: {self.lastName}, {self.firstName}")
        print(f"Date of birth: {self.birthDate}")
        print(f"Class of: {self.birthDate[-4:]}")
        print(f"Email: {email}")
        print(f"Student ID: {self.studentID}")

        wishToSave = input("\nDo you wish to save the student ID to the database? Y/N ").lower()

        if wishToSave == "y":
            file = open("assets\\Database.txt", "a") # driectory

            file.write("\n")
            file.write("Name: " + self.lastName + ", " + self.firstName + "\n")
            file.write("Date of birth: " + self.birthDate + "\n")
            file.write("Class of: " + self.birthDate[-4:] + "\n")
            file.write("Email: " + email + "\n")
            file.write("Student ID: " + self.studentID)
            file.write("\n")
            file.close()

        elif wishToSave == "n":
            None
        else:
            print("ERROR: Invalid input, try again.")

    def createID(self):
        studentID = ""
        self.studentID = studentID
        for i in range(6):
            num = random.randint(0, 9)
            self.studentID += str(num)
        self.checkID() # Checks the id
        return self.studentID # if the id is not a duplicate it gets returned to the createStudentId method

    def checkID(self):
        try:
            f = open("assets\\Database.txt", "rt") # directory
            f.close()
        except FileNotFoundError:
            f = open("assets\\Database.txt", "a") # directory
            f.close()

        f = open("assets\\Database.txt", "rt") # directory
        data = f.readlines()

        for line in data:
            if "Student ID: " + str(self.studentID) in line:
                f.close()
                print("Student is allready exists, creating new one.")

                self.studentID = ""
                for i in range(6):
                    num = random.randint(0, 9)
                    self.studentID += str(num)
                self.checkID()

        return self.studentID

def main(fName, lName, birthDate):
    newUser = CreateStudent(fName, lName, birthDate)
    newUser.createStudentID()

if __name__ == "__main__":
    main()