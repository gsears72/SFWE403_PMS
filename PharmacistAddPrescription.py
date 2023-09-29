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
    
