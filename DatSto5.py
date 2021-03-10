from termcolor import cprint
import sys

# importing modules
import bin.CreateStudentID

class Main():
    def __init__(self):
        pass
    
    def userInput(self):
        task = input("DatSto5> ").lower()
        self.task = task
        self.main()

    #checking what arguments has been passed
    def main(self):
        if self.task == "quit":
            print("Exiting")
            sys.exit(1)
        
        elif self.task == "newstudent":
            print("Adding new student\n")
            self.newStudent()
            self.userInput()

        elif self.task == "help":
            file = open("assets\\help.txt", "r")
            print(file.read())
            file.close()
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