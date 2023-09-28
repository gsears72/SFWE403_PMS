import mysql.connector
import PharmacistAddPrescription

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
    loggedIn = False
    while loggedIn != True:
        loginResult=Login()
        if loginResult[0] == True:
            loggedIn=loginResult[0]
    
    while loggedIn == True:
        
        rolereturn = loginResult[2]
        if rolereturn == "Manager":
            mangerAction = input("Invetory, Reports, User Management, Log Out")
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
            
            
            
        elif rolereturn == "Pharmacist":
            pharmacistAction = input("Add Prescription, Fill Prescription, Check Out")
            if (pharmacistAction == "Add Prescription"):
                print("Pharmacist Add PRescription\n")
                PharmacistAddPrescription
            elif (pharmacistAction == "Fill Prescription"):
                print()
            elif (pharmacistAction == "Log Out"):
                loggedIn = False
            else:
                print("error")

            
        
    
    
    
    
    
        
    