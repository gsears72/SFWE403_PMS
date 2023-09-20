import mysql.connector

mydb = mysql.connector.connect(
        host = 'mysql-145311-0.cloudclusters.net',
        port = '18166',
        user = 'admin',
        passwd = 'FcCZds4d',
        db = 'PMS'
    )

mycursor = mydb.cursor()

def Login(userID):
    
    password = input("password\n")
    
    mycursor.execute("SELECT pasword FROM PMS_STAFF WHERE ID = %d",userID)
    pswdreturn = mycursor.fetchone()
    
    if pswdreturn == password:
        print("Login Success")
        return True
    else:
        print("Login Error\n")
        return False






if __name__ == '__main__':
    userID = input("User ID\n")
    loggedIn = False
    while loggedIn != True:
        loggedIn=Login(userID)
    
    while loggedIn == True:
        mycursor.execute("SELECT role FROM PMS_STAFF WHERE ID = %d",userID)
        rolereturn = mycursor.fetchone()
        if rolereturn == "Manager":
            mangerAction = input("Invetory, Reports, User Management, Log Out")
            if (mangerAction == "Inventory"):
                print()
            elif (mangerAction == "Reports"):
                print()
            elif (mangerAction == "User Management"):
                print()
            elif (mangerAction == "Log Out"):
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

            
        
    
    
    
    
    
        
    