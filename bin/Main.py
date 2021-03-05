from termcolor import cprint
import argparse
import sys

# importing modules
import bin.CreateStudentID

class Main():
    def __init__(self):
        parser = argparse.ArgumentParser(description="A student database manager") #making parser

        parser.add_argument("-q", "--quit", action="store_true", help="Quits the program") #* quit
        parser.add_argument("-ns", "--newStudent", action="store_true", help="Adds a new student to the database") #* new student

        args = parser.parse_args()

        self.args = args

    #checking what arguments has been passed
    def main(self):
        if self.args.quit:
            print("Exiting")
            sys.exit(1)
        
        if self.args.newStudent:
            print("Adding new student\n")
            self.newStudent()
    
    def newStudent(self):
        fName = str(input("First name: "))
        Lname = str(input("Last name: "))
        birthDate = str(input("Date of birth (dd/mm/yyyy): "))

        if len(birthDate) != 10 or birthDate[2] != "/" or birthDate[5] != "/":
            cprint("ERROR: Date of birth missing / or invalid length, use format: dd/mm/yyyy", "red")
            sys.exit(1)
        print()
       
        CreateStudentID.main(fName, Lname, birthDate) #calling CreateStudentID


if __name__ == "__main__":
    user = Main()
    user.main()    