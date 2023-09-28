import mysql.connector
from datetime import datetime 

mydb = mysql.connector.connect(
        host = 'mysql-145311-0.cloudclusters.net',
        port = '18166',
        user = 'admin',
        passwd = 'FcCZds4d',
        db = 'PMS'
    )

mycursor = mydb.cursor()    

def AddCustomer():
   first_name = input("Enter first name:")
   last_name = input("Enter last name:")
   date_of_birth = input("Enter DOB as YYYY-MM-DD")
   #DOB = datetime.strptime(date_of_birth, '%Y/%m/%d')
   address = input("Enter address:")
   phone = input("Enter phone number:")
   email = input("Enter email address:")
   insurance = input("Enter insurance information:")
   
   #print(first_name, ' ', last_name, ' ', DOB.month, "/", DOB.day, "/", DOB.year, ' ',address, ' ',phone, ' ',email, ' ',insurance, sep= '')

   mycursor.execute("INSERT INTO Customer (lastName, firstName, DOB, Address, phoneNum, email, insurance) VALUES (%s, %s, %s, %s, %s, %s, %s)", (last_name, first_name, date_of_birth, address, phone, email, insurance))
   mydb.commit()





if __name__ == '__main__':
   
   AddCustomer()

   mycursor.execute("SELECT * FROM Customer")
   for x in mycursor:
      print(x)
 


