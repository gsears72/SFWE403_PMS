import mysql.connector
from datetime import datetime
from SFWE403_PMS_Model import *

mydb = mysql.connector.connect(
        host = 'mysql-145311-0.cloudclusters.net',
        port = '18166',
        user = 'admin',
        passwd = 'FcCZds4d',
        db = 'PMS'
    )

mycursor = mydb.cursor()
    
if __name__ == '__main__':
    loggedIn = False
    while loggedIn != True:
        loginResult=Login()
        if loginResult[0] == True:
            loggedIn=loginResult[0]
    
    while loggedIn == True:
        rolereturn = str(loginResult[2])
        if rolereturn == "manager":
            mangerAction = input("Invetory, Reports, User Management, Log Out\n")
            if (mangerAction == "Inventory"):
                print("Inventory")
            elif (mangerAction == "Reports"):
                print("Reports")
            elif (mangerAction == "User Management"):
                print("User Management")
            elif (mangerAction == "Log Out"):
                print("Logging Out")
                loggedIn = False 
            else:
                print("error")
            
            
            
        elif rolereturn == "pharmacist":
            pharmacistAction = input("Add Prescription, Fill Prescription, Check Out")
            if (pharmacistAction == "Add Prescription"):
                print()
            elif (pharmacistAction == "Fill Prescription"):
                print()
            elif (pharmacistAction == "Log Out"):
                loggedIn = False
            else:
                print("error")

            
        
    
    
    
    
    
        
    