import random
import sqlite3
import os

import bin.DatabaseEditor

class CreateStudent():
    def __init__(self, firstName, lastName, dateOfBirth):
        self.firstName = firstName
        self.lastName = lastName
        self.dateOfBirth = dateOfBirth

        self.files = os.listdir("assets")
        self.databaseName = "Database.db"

    def createStudentID(self):
        #creating email, ID and then checking if the ID allready exists
        email = self.firstName.capitalize() + self.lastName.capitalize() + "@school.com" #* replace @school.com with school name

        if str(self.databaseName) not in self.files:
            bin.DatabaseEditor.createDatabase()
            print("File did not exist, created new one.")
            return("File created")

        studentID = str(self.createID())
        self.studentID = studentID

        print(f"Name: {self.lastName}, {self.firstName}")
        print(f"Date of birth: {self.dateOfBirth}")
        print(f"Class of: {self.dateOfBirth[-4:]}")
        print(f"Email: {email}")
        print(f"Student ID: {self.studentID}")

        wishToSave = input("\nDo you wish to save the student ID to the database? Y/N ").lower()

        if wishToSave == "y":
            bin.DatabaseEditor.addUserToDatabase(self.firstName, self.lastName, self.dateOfBirth, self.dateOfBirth[-4:], email, self.studentID) #calling function in another file

        elif wishToSave == "n":
            None
        else:
            print("ERROR: Invalid input, try again.")

    def createID(self):
        studentID = ""
        self.studentID = studentID
        for i in range(6):
            num = random.randint(0, 9)

            #If the first number == 0
            if len(studentID) == 0 and num == 0:
                while True:
                    num = random.randint(0, 9)
                    if num != 0:
                        break

            self.studentID += str(num)
        IdAlreadyExists = bin.DatabaseEditor.checkID(self.studentID) # Checks the id
        if IdAlreadyExists == False:
            return self.studentID # if the id is not a duplicate it gets returned to the createStudentId method
        else:
            self.createID()


def main(fName, lName, dateOfBirth):
    newUser = CreateStudent(fName, lName, dateOfBirth)
    newUser.createStudentID()

if __name__ == "__main__":
    main("John", "Doe", "00/00/0000")