#this file is essentially only for starting the main module without having to type python name.py -arguments
#importing
import os

#importing modules
import bin.Main

class StudentDatabase():
    def __init__(self):
        pass
    
    def startTask(self):
        print()
        task = str(input("StDat: ")) # Getting input for arguments
        path = os.path.abspath(os.getcwd())
        path = path + "\\bin\\"
        print(path)


    
if __name__ == "__main__":
    user = StudentDatabase()
    user.startTask()