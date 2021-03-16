#importing
from termcolor import cprint
import sqlite3
import os

databaseName = "Database"
databaseName = databaseName + ".db"
files = os.listdir("assets") #gets all files in directory for checking if file allready exists
    
def createDatabase():
    if str(databaseName) in files:
        cprint("ERROR: File allready exists", "red")
        return("ERROR")
    else: # file does not yet exist, create it.
        conn = sqlite3.connect("assets\\" + str(databaseName))
        c = conn.cursor() #cursor
        
        #creating table
        c.execute("""CREATE TABLE database(
            firstName text,
            lastName text,
            dateOfBirth text,
            classOf integer,
            email text,
            studentID integer
        )""")
    
    conn.commit() #commiting changes
    conn.close() #closing file
    
def printDatabase():
    if str(databaseName) in files:
        conn = sqlite3.connect("assets\\database.db") #connecting to the database
        c = conn.cursor() #cursor
        
        c.execute("SELECT * FROM database") #gets everything from database
        items = c.fetchall() 
        
        print("NAME " + "\t\tDATE OF BIRTH " + "\tCLASS OF " + "\tEMAIL " + "\t\t\tSTUDENT ID")
        print("---- " + "\t\t------------- " + "\t-------- " + "\t----- " + "\t\t\t----------")
        
        for item in items: #prints it 
            print(str(item[0]) + " " + str(item[1]) + "\t" + str(item[2]) + "\t" + str(item[3]) + "\t" + str(item[4]) + "\t\t" + str(item[5]))
            
        conn.close() #closing file
    
    else:
        cprint("ERROR: file does not exist", "red")
        return("Error")

def addUserToDatabase(firstName, lastName, dateOfBirth, classOf, email, studentID):
    if str(databaseName) in files:
        studentInfo = [(firstName, lastName, dateOfBirth, classOf, email, studentID)] #creating list of arguments for student
        
        conn = sqlite3.connect("assets\\database.db") #connecting to the database
        c = conn.cursor() #cursor
        
        c.executemany("INSERT INTO database VALUES (?, ?, ?, ?, ?, ?)", studentInfo) #inserting student into database
        
        conn.commit() #commiting changes
        conn.close() #closing file
    else:
        cprint("ERROR: file does not exist", "red")
        return("Error")
    
def deleteUser(studentID):
    if str(databaseName) in files:
        conn = sqlite3.connect("assets\\database.db")
        c = conn.cursor()

        c.execute("SELECT * FROM database WHERE studentID == ?", (studentID,))
        items = c.fetchall()

        if len(items) == 0:
            cprint("ERROR: Given student ID does not exist in database", "red")
            return("Error")
        else:
            print("Are you Sure you want to delete user: ")

            print("NAME " + "\t\tDATE OF BIRTH " + "\tCLASS OF " + "\tEMAIL " + "\t\t\tSTUDENT ID")
            print("---- " + "\t\t------------- " + "\t-------- " + "\t----- " + "\t\t\t----------")
        
            for item in items: #prints it 
                print(str(item[0]) + " " + str(item[1]) + "\t" + str(item[2]) + "\t" + str(item[3]) + "\t" + str(item[4]) + "\t\t" + str(item[5]))

            sure = input("y/n: ").lower()

            if sure == "y":
                c.execute("DELETE FROM database WHERE studentID = ?", (studentID,)) #deleting user
                print("User deleted")
            else:
                print("User not deleted")
            
        conn.commit() #commiting changes
        conn.close() #closing file

    else:
        cprint("ERROR: file does not exist", "red")
        return("Error")
    
def searchForUser(searchMethod, searchTerm):
    if str(databaseName) in files:
        if searchMethod not in ["first name", "last name", "studentid", "class", "date of birth", "email"]:
            cprint("ERROR: unknown searchMethod input", "red")
            return("ERROR")
        else:
            conn = sqlite3.connect("assets\\database.db")
            c = conn.cursor()
            
            if searchMethod == "first name":
                c.execute("SELECT * FROM database WHERE firstName == ?", (searchTerm,))
            if searchMethod == "last name":
                c.execute("SELECT * FROM database WHERE lastName == ?", (searchTerm,))
            if searchMethod == "studentid":
                c.execute("SELECT * FROM database WHERE studentID == ?", (searchTerm,))
            if searchMethod == "class":
                c.execute("SELECT * FROM database WHERE classOf == ?", (searchTerm,))
            if searchMethod == "date of birth":
                c.execute("SELECT * FROM database WHERE dateOfBirth == ?", (searchTerm,))
            if searchMethod == "email":
                c.execute("SELECT * FROM database WHERE email == ?", (searchTerm,))
            
            items = c.fetchall() 

            if len(items) >= 1:
                print("NAME " + "\t\tDATE OF BIRTH " + "\tCLASS OF " + "\tEMAIL " + "\t\t\tSTUDENT ID")
                print("---- " + "\t\t------------- " + "\t-------- " + "\t----- " + "\t\t\t----------")
            
                for item in items: #prints it 
                    print(str(item[0]) + " " + str(item[1]) + "\t" + str(item[2]) + "\t" + str(item[3]) + "\t" + str(item[4]) + "\t\t" + str(item[5]))

            else:
                print("No users were found")
        
            conn.commit() #commiting changes
            conn.close() #closing file

    else:
        cprint("ERROR: file does not exist", "red")
        return("Error")
    
def checkID(studentID):
    if str(databaseName) in files:
        conn = sqlite3.connect("assets\\database.db")
        c = conn.cursor()
        
        c.execute("SELECT * FROM database WHERE studentID == ?", (studentID,))
        items = c.fetchall()
        
        if items == True:
            cprint("ID allready exists, generating new one", "red")
            return True
        else:
            return False

        conn.commit()
        conn.close()
        
    else:
        cprint("ERROR: file does not exist", "red")
        return("Error")