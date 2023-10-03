import mysql.connector
import InventoryController
import prescription

mydb = mysql.connector.connect(
        host = 'mysql-145311-0.cloudclusters.net',
        port = '18166',
        user = 'admin',
        passwd = 'FcCZds4d',
        db = 'PMS'
    )

mycursor = mydb.cursor()

def Login():
    
    userID = input("User ID\n")
    Password = input("password\n")

    mycursor.execute("SELECT * FROM PMS_Staff WHERE StaffID = %s and password = %s",(userID,Password))
    
    pswdreturn = mycursor.fetchone()
    
    if pswdreturn == None:
        print("Login Error\n")
        return False, False, False
    else:
        print("Login Success")
        return True, pswdreturn[1],pswdreturn[2]
        






if __name__ == '__main__':
    inventory = InventoryController.inventoryController()
    P = prescription.Prescription('1111111', "101", "2023-09-28", "2024-03-01", "NyQuil", "2", "2", "2", "take medicine", "dr. sharon")
    loggedIn = False
    while loggedIn != True:
        loginResult=Login()
        if loginResult[0] == True:
            loggedIn=loginResult[0]
    
    while loggedIn == True:
        
        rolereturn = loginResult[2]
        if rolereturn == "manager":
            mangerAction = input("Inventory, Reports, User Management, Log Out\n")
            if (mangerAction == "Inventory"):
                inventory.addPrescription(P)
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
            
            
            
        elif rolereturn == "Pharmacist":
            pharmacistAction = input("Add Prescription, Fill Prescription, Check Out")
            if (pharmacistAction == "Add Prescription"):
                print()
            elif (pharmacistAction == "Fill Prescription"):
                print()
            elif (pharmacistAction == "Log Out"):
                loggedIn = False
            else:
                print("error")

            
        
            
        
    
    
    
    
    
        
    
