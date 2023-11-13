import mysql.connector
import customtkinter as ctk 
import tkinter.messagebox as tkmb
from SFWE403_PMS_Model import *

mydb = mysql.connector.connect(
        host = 'mysql-145311-0.cloudclusters.net',
        port = '18166',
        user = 'admin',
        passwd = 'FcCZds4d',
        db = 'PMS'
    )
mycursor = mydb.cursor()

def Open_Fill_Prescription(self, firstName, lastName):
    #Select Theme
    ctk.set_appearance_mode("dark")

    #Select Color Theme
    ctk.set_default_color_theme("blue")

    #Setting up general Window
    windowPres = ctk.CTkToplevel
    windowPres.geometry = ("800x800")
    windowPres.title("Prescription Manager")

    windowPres.columnconfigure(0, weight = 0)
    windowPres.columnconfigure(1, weight = 2)
    windowPres.rowconfigure(0, weight = 0)
    windowPres.rowconfigure(1, weight = 0)
    windowPres.rowconfigure(2, weight = 0)
    windowPres.rowconfigure(3, weight = 0)
    windowPres.rowconfigure(4, weight = 0)

    confirmationFrame = ctk.CTkFrame(master = windowPres, row = 0, column = 0)


    mycursor.execute("SELECT * FROM Customer WHERE firstName = %s, lastName = %s", (firstName, lastName))
    grabbedCustomers = mycursor.fetchall() #make sure fetchall() might cause error
    
    LabelFq1 = ctk.CTkLabel(master=confirmationFrame, text = "Is this the correct Customer", row = 1, column = 0)
    ConfirmB1 = ctk.CTkButton(master = confirmationFrame, text = "Yes", row = 2, column = 0, command= fill_prescription2)
    
    def fill_prescription2():

        LabelFq2 = ctk.CTkLabel(master = windowPres, text = "Is this the correct Prescription", )



    
#Fill Presciption Button
    FillPresB = ctk.CTkButton(
        master=windowPres,
        text = "Fill A Prescription",
        font = ("Fira Code", 15),
        width = 200,
        height= 50,
    )

#Potential Text Fields we will need
    #Fill Prescription text field)
   
    LabelFq2 = ctk.CTkLabel(master=windowPres, text = "How many did you grab")
    LabelFRM = ctk.CTkLabel(master=windowPres, text ="Too many pills grabbed")
    labelFRL = ctk.CTkLabel(master=windowPres, text="Too few pills grabbed")
    labelFRC = ctk.CTkLabel(master=windowPres, text ="Correct Number grabbed")


    #Add prescriptions text field
    LabelCNA = ctk.CTkLabel(master=AddPrescription, text="What is the first and last name of the Customer")
    LabelPID = ctk.CTkLabel(master = AddPrescription, text ="What is the prescription ID")
    LabelPS = ctk.CTkLabel(master= AddPrescription, text = "What is the prescription start date (YYYY/MM/DD)")
    prescriptionEnd = ctk.CTkLabel(master=AddPrescription, text="What is the prescription end date (YYYY/MM/DD)")
    
    #General Text Fields
    success = ctk.CTkLabel(master=windowPres,text="Successfully Added!")  
    failure = ctk.CTkLabel(master=windowPres,text="Failed to Load Customer!")


#Entry Fields
    #entry for fill prescription
    nameInFF = ctk.CTkEntry(master=fillprescription, width=300)
    nameInFL = ctk.CTkEntry(master=fillprescription, width= 300)
    confirmationF = ctk.CTkEntry(master=fillprescription, width = 300)
    numInF = ctk.CTkEntry(master=fillprescription, width=300)

    #entry for add prescription 
    #prescriptionID, customerName, prescriptionStartDate,prescriptionEndDate, prescriptionMedication, prescriptionQuantity


    


def Open_Add_Prescription():
#Set up Add prescription frame stuff
    AddPrescription=ctk.CTkToplevel

    AddPrescription.columnconfigure(0, weight = 0)
    AddPrescription.columnconfigure(1, weight = 1)
    AddPrescription.rowconfigure(0, weight = 0)
    AddPrescription.rowconfigure(1, weight = 0)
    AddPrescription.rowconfigure(2, weight = 0)
    AddPrescription.rowconfigure(3, weight=0)
    AddPrescription.rowconfigure(4, weight=0)

    #button for Add prescription
    AddPresB = ctk.CTkButton(
        master=AddPrescription,
        text = "Add A Prescription",
        font = ("Fira Code", 15),
        width = 200,
        height= 50,
    )

    prescriptionIDA = ctk.CTkEntry(master=AddPrescription, width=300)
    nameInA = ctk.CTkEntry(master=AddPrescription, width= 300)
    prescriptionStart = ctk.CTkEntry(master=AddPrescription, width = 300)
    prescriptionEnd = ctk.CTkEntry(master = AddPrescription, width = 300)
    precriptionMedication = ctk.CTkEntry(master=AddPrescription, width=300)
    prescriptionQuantity = ctk.CTkEntry(master=AddPrescription, width=300)