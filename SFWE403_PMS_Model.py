import mysql.connector
import Customer

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
        

def Login1(userID,Password):
    
   # userID = input("User ID\n")
    # Password = input("password\n")

    mycursor.execute("SELECT * FROM PMS_Staff WHERE StaffID = %s and password = %s",(userID,Password))
    
    pswdreturn = mycursor.fetchone()
    
    if pswdreturn == None:
        #print("Login Error\n")
        #return False, False, False
        return
    else:
        #print("Login Success")
        #return True, pswdreturn[1],pswdreturn[2]
        return
    
def customerDistroy():
    firstName =input("Patient first name\n")
    lastName =input("Patient last name\n")
    
    mycursor.execute(("DELETE FROM Customer WHERE firstName = %s and lastName = %s"),(firstName,lastName))
    
def addCustomer(customer):
    #print(first_name, ' ', last_name, ' ', DOB.month, "/", DOB.day, "/", DOB.year, ' ',address, ' ',phone, ' ',email, ' ',insurance, sep= '')
    mycursor.execute("INSERT INTO Customer (lastName, firstName, DOB, Address, phoneNum, email, insurance) VALUES (%s, %s, %s, %s, %s, %s, %s)", (customer.last_name, customer.first_name, customer.date_of_birth, customer.address, customer.phone, customer.email, customer.insurance))
    mydb.commit()

def loadCustomer():
    customer1 = Customer.customer()
    customer1.first_name = input("Enter first name:")
    customer1.last_name = input("Enter last name:")
    customer1.date_of_birth = input("Enter DOB as YYYY-MM-DD")
    #DOB = datetime.strptime(date_of_birth, '%Y/%m/%d')
    customer1.address = input("Enter address:")
    customer1.phone = input("Enter phone number:")
    customer1.email = input("Enter email address:")
    customer1.insurance = input("Enter insurance information:")
    return customer1
   
def CreateUserAccounts():
    role = input("Enter role (Manager, Pharmacist, Pharmacist technician, Cashier):")
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
    customerID=input("Enter Customer ID\n")
    toUpdate = input("What would you like to update? (First, Last, DOB, Address, Phone, Email, Insurance)\n")

    if toUpdate == "First" or toUpdate =="first":
        newInfo = input("What is the updated First Name?")
        command = "UPDATE Customer set firstName = %s where Customer_ID = %s"
    elif toUpdate == "Last" or toUpdate =="last":
        newInfo = input("What is the updated Last Name?")
        command = "UPDATE Customer set lastName = %s where Customer_ID = %s"
    elif toUpdate == "DOB" or toUpdate =="dob":
        newInfo = input("What is the updated DOB?")
        command = "UPDATE Customer set DOB = %s where Customer_ID = %s"
    elif toUpdate == "Address" or toUpdate == "address":
        newInfo = input("What is the updated Address?")
        command = "UPDATE Customer set Address = %s where Customer_ID = %s"
    elif toUpdate == "Phone" or toUpdate =="phone":
        newInfo = input("What is the updated Phone Number?")
        command = "UPDATE Customer set phoneNumber = %s where Customer_ID = %s"
    elif toUpdate == "Email" or toUpdate == "email":
        newInfo = input("What is the updated Email?")
        command = "UPDATE Customer set email = %s where Customer_ID = %s"
    elif toUpdate == "Insurance" or toUpdate == "insurance":
        newInfo = input("What is the Insurance?")
        command = "UPDATE Customer set insurance = %s where Customer_ID = %s"
    else:
        print("Invalid Input")
        
    mycursor.execute(command,(newInfo,customerID))
    mydb.commit()


def LookUPCustomerID():
    customerName = input("\nEnter the name of the customer (first last): ")
    x = customerName.split()
    firstName = x[0]
    lastName = x[1]
    
    mycursor.execute("SELECT Customer_ID FROM Customer WHERE lastName = %s and firstName = %s",(lastName,firstName))
    customerID = mycursor.fetchone()
    customerID = customerID[0]

    return customerID