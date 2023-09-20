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
    pswdreturn = mycursor.fetchall()
    
    if pswdreturn == password:
        print("Login Success")
        return True
    else:
        print("Login Error\n")
        return False






if __name__ == '__main__':
    userID = input("User ID\n")
    
    while Login == True:
        mycursor.execute("SELECT role FROM PMS_STAFF WHERE ID = %d",userID)
        rolereturn = mycursor.fetchall()
        if rolereturn == "Manager":
            input("Invetory, Reports, User Management")
            
        elif rolereturn == "Pharmasist":
            
        
    
    
    
    
    
        
    