from datetime import datetime
from abc import ABC, abstractmethod
import mysql.connector

mydb = mysql.connector.connect(
        host = 'mysql-145311-0.cloudclusters.net',
        port = '18166',
        user = 'admin',
        passwd = 'FcCZds4d',
        db = 'PMS'
    )

mycursor = mydb.cursor()

def canonical_date(date_str):
    try:
        date = datetime.strptime(date_str, '%Y-%m-%d')
    except ValueError:
        try:
            date = datetime.strptime(date_str, '%m/%d/%Y')
        except ValueError:
            try:
                date = datetime.strptime(date_str, '%d-%b-%Y')
            except ValueError:
                return None
    return date.strftime('%Y-%m-%d')

class Staff(ABC):
    @abstractmethod
    def __init__(self, name, birth_date, address, phone_number, email, username, password):
        self.name = name
        self.birth_date = canonical_date(birth_date)
        self.address = address
        self.phone_number = phone_number
        self.email = email
        self.username = username
        self.password = password

    @abstractmethod
    def __str__(self):
        return "Staff Name: {}\nBirth Date: {}\nAddress: {}\nPhone Number: {}\nEmail: {}\nUsername: {}\nPassword: {}".format(self.name, self.birth_date, self.address, self.phone_number, self.email, self.username, self.password)

    @abstractmethod
    def __repr__(self):
        return "Staff('{}', '{}', '{}', '{}', '{}', '{}', '{}')".format(self.name, self.birth_date, self.address, self.phone_number, self.email, self.username, self.password)
    
    @abstractmethod
    def __eq__(self, other):
        return self.name == other.name and self.birth_date == other.birth_date and self.address == other.address and self.phone_number == other.phone_number and self.email == other.email and self.username == other.username and self.password == other.password
    
    @abstractmethod
    def __ne__(self, other):
        return not self.__eq__(other)
    
    @abstractmethod
    def __hash__(self):
        return hash((self.name, self.birth_date, self.address, self.phone_number, self.email, self.username, self.password))
    

    def get_name(self):
        return self.name
    
    def get_birth_date(self):
        return self.birth_date 
    
    def get_address(self):
        return self.address
    
    def get_phone_number(self):
        return self.phone_number
    
    def get_email(self):
        return self.email
    
    def get_username(self):
        return self.username
    
    def get_password(self):
        return self.password
    
    def set_name(self, name):
        self.name = name

    def set_birth_date(self, birth_date):
        self.birth_date = birth_date

    def set_address(self, address):
        self.address = address

    def set_phone_number(self, phone_number):
        self.phone_number = phone_number

    def set_email(self, email):
        self.email = email

    def set_username(self, username):
        self.username = username

    def set_password(self, password):
        self.password = password

    def createPatient(self):
        #print(first_name, ' ', last_name, ' ', DOB.month, "/", DOB.day, "/", DOB.year, ' ',address, ' ',phone, ' ',email, ' ',insurance, sep= '')
        #mycursor.execute("INSERT INTO Customer (lastName, firstName, DOB, Address, phoneNum, email, insurance) VALUES (%s, %s, %s, %s, %s, %s, %s)", (customer.last_name, customer.first_name, customer.date_of_birth, customer.address, customer.phone, customer.email, customer.insurance))
        mydb.commit()

    def loadCustomer(self):
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

    def UpdateCustomer(self):
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

    def enterPrescription(self):
        prescriptionID = input("Enter the prescription ID: ")

        #Get name and split
        customerName = input("\nEnter the name of the customer (first last): ")
        x = customerName.split()
        firstName = x[0]
        lastName = x[1]
        
        mycursor.execute("SELECT Customer_ID FROM Customer WHERE lastName = %s and firstName = %s",(lastName,firstName))
        customerID = mycursor.fetchone()
        customerID = customerID[0]
        

        prescriptionStartDate = input("\nEnter the start date for the medication in the form YYYY/MM/DD: ")
        prescriptionEndDate = input("\nEnter the end date for the prescription in the form YYYY/MM/DD: ")

        prescriptionMedication = input("\n Enter the name of the medication on the prescription: ")

        prescriptionQuantity = input("\nEnter the amount of the medication per refill: ")
        
        mycursor.execute("INSERT INTO PMS_Prescription (prescription, customerID, startDate, endDate, medication, quantity) VALUES (%s, %s, %s, %s, %s, %s )", (prescriptionID, customerID, prescriptionStartDate, prescriptionEndDate, prescriptionMedication, prescriptionQuantity))
        mydb.commit()

    def addPrescription(self, newPrescription):  
        sql = "INSERT INTO PMS_Prescription (prescription, customerID, startDate, endDate, medication, quantity, strength, refills, instructions, prescriber) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        val = (newPrescription.prescription, newPrescription.customerID, newPrescription.startDate, newPrescription.endDate, newPrescription.medication, newPrescription.quantity, newPrescription.strength, newPrescription.refills, newPrescription.instructions, newPrescription.prescriber)
        mycursor.execute(sql, val)
        mydb.commit()

    def removePrescription(self, newPrescription): 
        sql = "DELETE FROM PMS_Prescription WHERE prescription = " +  newPrescription.prescription
        mycursor.execute(sql)
        mydb.commit()

class PharmacyManager(Staff):
    def __init__(self, name):
        pass
    def __str__(self):
        pass
    
    def __repr__(self):
        pass
    
    def __eq__(self, other):
        pass
    
    def __ne__(self, other):
        pass
    
    def __hash__(self):
        pass

    def createPharmacyAccount(self):
        role = input("Enter role (Manager, Pharmacist, Pharmacist technician, Cashier):")
        name = input("Enter full name:")
        password = input("Create password:")

        mycursor.execute("INSERT INTO PMS_Staff (role, name, password) VALUES (%s, %s, %s)", (role, name, password))
        mydb.commit()

    def removePatient(self):
        firstName = input("Patient first name\n")
        lastName = input("Patient last name\n")
        mycursor.execute(("DELETE FROM Customer WHERE firstName = %s and lastName = %s"),(firstName,lastName))

    def recoverStaffAccount(self):
        pass

    def orderMedication(self):
        pass

    def updateInventory(self):
        medName = input("Enter Item Name \n")        
        newInfo = input("What is new quantity for this item?\n")
        command = "UPDATE Inventory set quantity = %s where medName = %s"
            
        mycursor.execute(command,(newInfo,medName))
        mydb.commit()

    def removeItem(self):
        medName = input("Enter Item Name to be removed\n")        
        sql = (("DELETE FROM Inventory WHERE medName = %s"),(medName))
        mycursor.execute(sql)
        mydb.commit()

    def generateFinancialReport(self):
        pass

    def generateInventoryReport(self):
        pass

    
    

class Pharmacist(Staff):
    def __init__(self, name):
        pass
    
    def __str__(self):
        pass
    
    def __repr__(self):
        pass
    
    def __eq__(self, other):
        pass
    
    def __ne__(self, other):
        pass
    
    def __hash__(self):
        pass

    def removePatient(self):
        firstName =input("Patient first name\n")
        lastName =input("Patient last name\n")        
        mycursor.execute(("DELETE FROM Customer WHERE firstName = %s and lastName = %s"),(firstName,lastName))
        
    def checkAvailability(self):
        pass

    def fillPrescription(self):
        # log()
        pass

    def log(self, Prescription):
        f = open("log.txt", "a")
        f.write(("prescription name: %s\nfilled by: %s\npatients name: %s\ndate: %s\nmedicine: %s\nquantity: %s"), (Prescription.prescription,Prescription.prescriber,Prescription.customerID,Prescription.startDate,Prescription.medication,Prescription.quantity))
        f.write("\n")
        f.close()

    
    
        

class PharmacistTechnician(Staff):
    def __init__(self, name, birth_date, address, phone_number, email, username, password, pharmacy):
        pass    
    
    def __str__(self):
        pass
    
    def __repr__(self):
        pass
    
    def __eq__(self, other):
        pass
    
    def __ne__(self, other):
        pass
    
    def __hash__(self):
        pass
    
    

class Cashier(Staff):
    def __init__(self, name, birth_date, address, phone_number, email, username, password):
        pass
    
    def __str__(self):
        pass
    
    def __repr__(self):
        pass
    
    def __eq__(self, other):
        pass
    
    def __ne__(self, other):
        pass
    
    def __hash__(self):
        pass
    
    
    
    

    


    