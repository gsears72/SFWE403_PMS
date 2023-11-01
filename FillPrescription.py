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
    PrescriptionID = input("Enter the prescription ID you are looking for: ")

    #search for the prescription
    mycursor.execute("SELECT * FROM PMS_Prescriptions WHERE prescription == %s, customerID = 3", (PrescriptionID))
    grabbedPrescription = mycursor.fetchone
    #When found the prescription print the information regarding the prescription for confirmation
    
    PrescriptionID = int(PrescriptionID)

    Confirmation = input("Is this the correct prescription(Y/N): ", grabbedPrescription)
    if (Confirmation == 'Y' or Confirmation == 'y'):
        #tofix(Get the amount of a medication from the prescription database.)
        mycursor.execute("SELECT quantity FROM PMS_prescription WHERE precription == %s", (PrescriptionID)) #getting the amound of medication from the prescription
        prescriptionAmount = int(mycursor.fetchone)
        
        mycursor.execute("SELECT medication FROM PMS_prescription WHERE precription == %s", (PrescriptionID)) #Getting the name of the medciation from the prescription
        prescriptionMedName = mycursor.fetchone
        Stop = 0
        
    
        while(Stop != 1):
            numbergot = int(input("How many did you remove: "))
            if numbergot == prescriptionAmount:
                Stop = 1
                mycursor.execute("Select quantity FROM Inventory where medName = %s", (prescriptionMedName)) #get the amount of the medication currecntly in system
                currentInventory = int(mycursor.fetchone)

                updatedInventory = currentInventory - prescriptionAmount #Calculate the updated inventory when medication removed
                updatedInventory = str(updatedInventory)

                mycursor.execute("UPDATE Inventory SET quantity = %s WHERE medName = %s", (updatedInventory), (prescriptionMedName)) #Update the amount of the medication in the inventory

                print("Removing"+numbergot+"from system")
                updatedInventory = int(updatedInventory)
                print("New inventory amount is" + updatedInventory)


            else:
                difference = prescriptionAmount - numbergot
                if (difference > 0):
                    print("too few pills got, grab"+difference+"more")
                else:
                    print("too many pills grabbed, get rid of"+abs(difference))
    else: 
        print("Error")