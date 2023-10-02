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
   date_of_birth = input("Enter DOB as MM/DD/YYYY")
   DOB = datetime.strptime(date_of_birth, '%m/%d/%Y')
   address = input("Enter address:")
   phone = input("Enter phone number:")
   email = input("Enter email address:")
   insurance = input("Enter insurance information:")
   
   #print(first_name, ' ', last_name, ' ', DOB.month, "/", DOB.day, "/", DOB.year, ' ',address, ' ',phone, ' ',email, ' ',insurance, sep= '')

   mycursor.execute("INSERT INTO Customer (lastName, firstName, DOB, Address, phoneNum, email, insurance) VALUES (%s, %s, %s, %s, %s, %s, %s)", (last_name, first_name, DOB, address, phone, email, insurance))
   mydb.commit()


def UpdateCustomer():
   #field is the information field that is being updated

   customerinfo = input("please enter the first and last name and DOB of the patient profile you wish to update (first last yyyy/mm/dd) ")
   customer = customerinfo.split()
   first = customer[0]
   last = customer[1]
   dob = customer[2]
   #query that will give the corresponding customer id and assign it to the variable ID
   mycursor.execute("SELECT Customer_ID FROM Customer WHERE lastName = %s and firstName = %s and DOB = %s", (last, first, dob))
   id = mycursor.fetchone()
   ID = str(id[0])
   


   valid = False
   while valid == False:
      field = input("Please enter the information field you wish to update (first, last, DOB, address, phoneNum, email, insurance) ")

      if field == 'first':
         valid = True
         updatedField = input("Please enter the updated information ")
         mycursor.execute("UPDATE Customer SET firstName = %s WHERE Customer_ID = %s", (updatedField, ID))
         mydb.commit()
      elif field == 'last':
         valid = True
         updatedField = input("Please enter the updated information ")
         mycursor.execute("UPDATE Customer SET lastName = %s WHERE Customer_ID = %s", (updatedField, ID))
         mydb.commit()
      elif field == 'DOB':
         valid = True
         updatedField = input("Please enter the updated information ")
         mycursor.execute("UPDATE Customer SET DOB = %s WHERE Customer_ID = %s", (updatedField, ID))
         mydb.commit()
      elif field == 'email':
         valid = True
         updatedField = input("Please enter the updated information ")
         mycursor.execute("UPDATE Customer SET email = %s WHERE Customer_ID = %s", (updatedField, ID))
         mydb.commit()
      elif field == 'phoneNum':
         valid = True
         updatedField = input("Please enter the updated information ")
         mycursor.execute("UPDATE Customer SET phoneNum = %s WHERE Customer_ID = %s", (updatedField, ID))
         mydb.commit()
      elif field == 'email':
         valid = True
         updatedField = input("Please enter the updated information ")
         mycursor.execute("UPDATE Customer SET email = %s WHERE Customer_ID = %s", (updatedField, ID))
         mydb.commit()
      elif field == 'insurance':
         valid = True
         updatedField = input("Please enter the updated information ")
         mycursor.execute("UPDATE Customer SET insurance = %s WHERE Customer_ID = %s", (updatedField, ID))
         mydb.commit()
      else:
         print("no field found, please try again\n")   



if __name__ == '__main__':
   #all of this code is bascially to test that things are working 
   AddCustomer()

   mycursor.execute("SELECT * FROM Customer")
   for x in mycursor:
      print(x)
 
   UpdateCustomer()

   mycursor.execute("SELECT * FROM Customer")
   for x in mycursor:
      print(x)





