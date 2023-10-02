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
        
def customerDistroy():
    firstName =input("Patient first name\n")
    lastName =input("Patient last name\n")
    
    mycursor.execute(("DELETE FROM Customer WHERE firstName = %s and lastName = %s"),(firstName,lastName))
    
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
   
def CreateUserAccounts():
    role = input("Enter role (manager, pharmacist, pharmacist technician, cashier):")
    name = input("Enter full name:")
    password = input("Create password:")

    mycursor.execute("INSERT INTO PMS_Staff (role, name, password) VALUES (%s, %s, %s)", (role, name, password))
    mydb.commit()
    
def PharmacistAddPresceription():
    #Debug to make sure we entered this file
    #print("Entered Pharmacist Add Prescription")

    #Get prescription ID    
    prescriptionID = input("Enter the prescription ID: ")

    #Get name and split
    customerName = input("\nEnter the name of the customer (first last): ")
    x = customerName.split()
    firstName = x[0]
    lastName = x[1]
    
    mycursor.execute("SELECT Customer_ID FROM Customer WHERE lastName = %s and firstName = %s",(lastName,firstName))
    customerID = mycursor.fetchone()
    customerID = customerID[0]
    

    prescriptionStartDate = input("\nEnter the start date for the medicaiton in the form YYYY/MM/DD: ")
    prescriptionEndDate = input("\nEnter the end date for the prescription in the form YYYY/MM/DD: ")

    prescriptionMedication = input("\n Enter the name of the medication on the prescription: ")

    prescriptionQuantity = input("\nEnter the amount of the medication per refill: ")
    
    mycursor.execute("INSERT INTO PMS_Prescription (prescription, customerID, startDate, endDate, medication, quantity) VALUES (%s, %s, %s, %s, %s, %s )", (prescriptionID, customerID, prescriptionStartDate, prescriptionEndDate, prescriptionMedication, prescriptionQuantity))
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


def LookUPCustomerID():
    customerName = input("\nEnter the name of the customer (first last): ")
    x = customerName.split()
    firstName = x[0]
    lastName = x[1]
    
    mycursor.execute("SELECT Customer_ID FROM Customer WHERE lastName = %s and firstName = %s",(lastName,firstName))
    customerID = mycursor.fetchone()
    customerID = customerID[0]

    return customerID
    
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

            
        
    
    
    
    
    
        
    
