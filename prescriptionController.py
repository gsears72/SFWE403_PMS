import mysql.connector
import customtkinter as ctk 
import tkinter.messagebox as tkmb
from SFWE403_PMS_Model import *
from models.Prescription import prescription
from models.Staff import Pharmacist

# mydb = mysql.connector.connect(
#         host = 'mysql-145311-0.cloudclusters.net',
#         port = '18166',
#         user = 'admin',
#         passwd = 'FcCZds4d',
#         db = 'PMS'
#     )
# mycursor = mydb.cursor()

pharmacist = Pharmacist()

def fillfinal(name, removeNum):
    pharmacist.updateInventoryP(name, removeNum)
    # mycursor.execute("SELECT * FROM PMS_Prescription WHERE prescription = %s", (prescriptionID,))
    # prescriptionInfo= mycursor.fetchone()

    # prescriptionMedName = prescriptionInfo[0][4]
    # mycursor.execute("Select quantity FROM Inventory where medName = %s", (prescriptionMedName,)) #get the amount of the medication currecntly in system
    # currentInventory = mycursor.fetchall()

    # updatedInventory = str(int(currentInventory[0][0]) - int(prescriptionInfo[0][5]))
    # mycursor.execute("UPDATE Inventory SET quantity = %s WHERE medName = %s", (updatedInventory,prescriptionMedName)) #Update the amount of the medication in the inventory
    # mydb.commit()

    # PrescriptionRefills = prescriptionInfo[0][7]
    # PrescriptionRefills -= 1
    # PrescriptionRefills = str(PrescriptionRefills)
    # mycursor.execute("UPDATE PMS_Prescription SET refills = %s WHERE prescription = %s", (PrescriptionRefills, prescriptionID))
    # mydb.commit()

def addfinal(cusID, startDate, endDate, medication, quantity, strength, refills, instruct, prescriber):
    pres = prescription(cusID, startDate, endDate, medication, quantity, strength, refills, instruct, prescriber)
    pharmacist.addPrescription(pres)
    #call addprescription with the prescription up there