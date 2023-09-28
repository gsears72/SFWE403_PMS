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

def sendToDataBase(self):
    mycursor.execute("INSERT INTO Prescription (PID, CFN, CLN, PSD, PED, PM, PQ) VALUES (%s, %s, %s, %s, %s, %s, %s)", (last_name, first_name, date_of_birth, address, phone, email, insurance))
    mydb.commit()
        
        #if not already in database add as prescription
            #Recheck to see if prescription was entered correctly, IF yes send succesful addition if not throw error
            #checkDataBase(prescriptionID, customerName, prescriptionStartDate, PrescriptionEndDate, prescriptionMedication, prescriptionQuantity)
            
        

#def checkDataBase(self, PID,CN, PSD, PED, PM, PQ):
        #if(True): #yes it exists in data base
            #return 0
        #else: #does not exist in data base
#             return 1


class PharmacistAddPresceription:
    #Debug to make sure we entered this file
    print("Entered Pharmacist Add PRescription")

    #Get prescription ID    
    prescriptionID = input("Enter the prescription ID: ")

    #Get name and split
    customerName = input("\nEnter the name of the customer (first, last): ")
    x = customerName.split()
    firstName = x[0]
    lastName = x[1]

    prescriptionStartDate = input("\nEnter the start date for the medicaiton in the form MM/DD/YY: ")
    prescriptionEndDate = input("\nEnter the end date for the prescription in the form MM/DD/YY: ")

    prescriptionMedication = input("\n Enter the name of the medication on the prescription: ")

    prescriptionQuantity = input("\nEnter the amount of the medication per refill: ")

    #Call checkDataBase to see if Prescription already exists
        #if it does pull up something that is the same pull up error

        #else call sendToDataBase
   

   
    mycursor.execute("SELECT * FROM Prescription")
    for x in mycursor:
         print(x)
    