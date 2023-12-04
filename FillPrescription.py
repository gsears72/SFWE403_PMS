import mysql.connector
from datetime import date
from datetime import timedelta
from datetime import datetime

mydb = mysql.connector.connect(
        host = 'mysql-145311-0.cloudclusters.net',
        port = '18166',
        user = 'admin',
        passwd = 'FcCZds4d',
        db = 'PMS'
    )
mycursor = mydb.cursor()


if __name__ == '__main__':
    #Enter Customer Name
    #Get Customer ID
    #Find prescriptions with ID 
    #narrow
    I = int(-1)
    customerConfirmation = 'n'
    while((customerConfirmation != 'y') and (customerConfirmation != 'Y')): #Keep looping until correct Customer Found
        #this is stupid. probably doesnt need to be loop but whatever.
        CustomerName = (input("Enter the customers name(Last/First) you are looking for: ")) #Change This to look by customer Name
        CustomerNameSplit = CustomerName.split(' ') 
        CustomerFirst = CustomerNameSplit[1]
        CustomerLast = CustomerNameSplit[0]
        try:
            #search for the prescription SELECT * FROM PMS.PMS_Prescription where prescription = 1111111
            mycursor.execute("SELECT * FROM Customer WHERE firstName = %s, lastName = %s", (CustomerFirst, CustomerLast,))
            grabbedCustomers = mycursor.fetchall() #make sure fetchall() might cause error
            #When found the prescription print the information regarding the prescription for confirmation
            
        except Exception as e:
            print(e)
        
        print("Is this the correct customer: ", grabbedCustomers[0][1] + " " + grabbedCustomers[0][2]+" "+ grabbedCustomers[0][3])
        customerConfirmation = input() #Make Sure RIght Customer

    CustomerID = int(grabbedCustomers[0][0])#Set customer ID once correct Customer Found
    Confirmation = 'n'


    while((Confirmation != 'y') and (Confirmation != 'Y')): #Keep looping until correct prescription Found
        I += 1
        try:
            #search for the prescriptions of the customer
            mycursor.execute("SELECT * FROM PMS_Prescription WHERE CustomerID = %s", (CustomerID,))
            grabbedPrescription = mycursor.fetchall() #make sure fetchall() might cause error
            #When found the prescription print the information regarding the prescription for confirmation
            
        except Exception as e:
            print(e)
        
        print("Is this the correct prescription(Y/N): ", grabbedPrescription[I][4])
        Confirmation = input()
        
        
    PrescriptionID = int(grabbedPrescription[I][0])

    PrescriptionStart = grabbedPrescription[I][2]
    PrescriptionEnd = grabbedPrescription[I][3]
    prescriptionMedName = grabbedPrescription[I][4]
    prescriptionAmount = int(grabbedPrescription[I][5])
    PrescriptionStrength = grabbedPrescription[I][6]
    PrescriptionRefills = grabbedPrescription[I][7]
    PrescriptionInstructions = grabbedPrescription[I][8]
    PrescriptionDoc = grabbedPrescription[I][9]
    Stop = 0
    
    while(Stop != 1):
        numbergot = int(input("How many did you remove: "))
        if numbergot == prescriptionAmount:
            Stop = 1
            mycursor.execute("Select quantity FROM Inventory where medName = %s", (prescriptionMedName,)) #get the amount of the medication currecntly in system
            currentInventory = int(mycursor.fetchall())

            updatedInventory = currentInventory - prescriptionAmount #Calculate the updated inventory when medication removed
            updatedInventory = str(updatedInventory)

            mycursor.execute("UPDATE Inventory SET quantity = %s WHERE, medName = %s", (updatedInventory,), (prescriptionMedName)) #Update the amount of the medication in the inventory

            print("Removing"+numbergot+"from system")
            updatedInventory = int(updatedInventory)
            print("New inventory amount is" + updatedInventory)
            #reduce the amount of refills by 1
            PrescriptionRefills -= 1
            mycursor.execute("UPDATE PMS_Prescription SET refills = %s, WHERE prescription = %s" (PrescriptionRefills,) (PrescriptionID,))


        else:
            difference = prescriptionAmount - numbergot
            if (difference > 0):
                print("too few pills got, grab"+difference+"more")
            else:
                print("too many pills grabbed, get rid of"+abs(difference))

    