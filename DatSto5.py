from termcolor import cprint
import sys

# importing modules
import bin.CreateStudentID
import bin.DatabaseEditor

class Main():
    def __init__(self):
        pass
    
    def userInput(self):
        task = input("DatSto5> ").lower()
        self.task = task
        self.main()

    #checking what arguments has been passed
    def main(self):
        if self.task == "exit":
            print("Exiting")
            sys.exit(1)
        
        elif self.task == "newuser":
            print("Adding new student\n")
            self.newStudent()
            self.userInput()

        elif self.task == "help":
            file = open("assets\\help.txt", "r")
            print(file.read())
            file.close()
            self.userInput()

        elif self.task == "printdata":
            bin.DatabaseEditor.printDatabase()
            self.userInput()
        
        elif self.task == "deluser":
            try:
                studentID = input("DatSto5> Student ID: ")
            except ValueError:
                cprint("Error: Student ID given is not an integer")   
                self.userInput()

            bin.DatabaseEditor.deleteUser(studentID)
            self.userInput()

        elif self.task == "usersearch":
            operations = ["first name", "last name", "studentid", "class", "date of birth", "email"]

            print("\nSearch user from: ")
            print("First name")
            print("Last name")
            print("StudentID")
            print("Class")
            print("Date of birth")
            print("Email")

            searchMethod = input("Search method: ")

            if searchMethod not in operations:
                cprint("Error: searchMethod given is not valid!", "red")
                self.userInput()
            
            searchTerm = str(input("Search term: "))

            bin.DatabaseEditor.searchForUser(searchMethod, searchTerm)
            self.userInput()

            
    def newStudent(self):
        fName = str(input("DatSto5> First name: "))
        Lname = str(input("DatSto5> Last name: "))
        birthDate = str(input("DatSto5> Date of birth (dd/mm/yyyy): "))

        if len(birthDate) != 10 or birthDate[2] != "/" or birthDate[5] != "/":
            cprint("DatSto5> ERROR: Date of birth missing / or invalid length, use format: dd/mm/yyyy", "red")
            sys.exit(1)
        print()
       
        bin.CreateStudentID.main(fName, Lname, birthDate) #calling CreateStudentID


if __name__ == "__main__":
    user = Main()
    user.userInput()    