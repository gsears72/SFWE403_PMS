import mysql.connector
import customtkinter as ctk 
import tkinter.messagebox as tkmb
#from SFWE403_PMS_Model import *
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
    
def addfinal(cusID, startDate, endDate, medication, quantity, strength, refills, instruct, prescriber):
    pres = prescription(cusID, startDate, endDate, medication, quantity, strength, refills, instruct, prescriber)
    pharmacist.addPrescription(pres)
    #call addprescription with the prescription up there