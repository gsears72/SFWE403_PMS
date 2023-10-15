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
    mycursor.execute("SELECT * FROM PMS_Prescriptions WHERE prescription == %s", (PrescriptionID))
    grabbedPrescription = mycursor.fetchone
    #When found the prescription print the information regarding the prescription for confirmation


    Confirmation = input("Is this the correct prescription(Y/N): ", grabbedPrescription)
    if (Confirmation == 'Y' or Confirmation == 'y'):
        #tofix(Get the amount of a medication from the prescription database.)
        mycursor.execute("SELECT FROM PMS_prescription WHERE precription == %s", (PrescriptionID)) #getting the amound of medication from the prescription
        prescriptionAmount = mycursor.fetchone
        Stop = 0
        
    
    while(Stop != 1):
        numbergot = input("How many did you remove: ")
        if numbergot == prescriptionAmount:
            Stop = 1
            
            #remove the amount from the prescription from the medicine database

            print("Removing"+numbergot+"from system")


        else:
            difference = prescriptionAmount - numbergot
            if (difference > 0):
                print("too few pills got, grab"+difference+"more")
            else:
                print("too many pills grabbed, get rid of"+abs(difference))
