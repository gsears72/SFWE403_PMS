import mysql.connector

mydb = mysql.connector.connect(
        host = 'mysql-145311-0.cloudclusters.net',
        port = '18166',
        user = 'admin',
        passwd = 'FcCZds4d',
        db = 'PMS'
    )

mycursor = mydb.cursor()

def CreateUserAccounts():
    role = input("Enter role (Manager, Pharmacist):")
    name = input("Enter full name:")
    password = input("Create password:")

    mycursor.execute("INSERT INTO PMS_Staff (role, name, password) VALUES (%s, %s, %s)", (role, name, password))
    mydb.commit()

if __name__ == '__main__':
   
   CreateUserAccounts()

   mycursor.execute("SELECT * FROM PMS_Staff")
   for x in mycursor:
      print(x)
