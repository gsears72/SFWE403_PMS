import customtkinter as ctk 
import tkinter.messagebox as tkmb
from SFWE403_PMS_Model import *

def Open_Fill_PrescriptionView():
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







#Set up Fill Prescription
    fillprescription = ctk.CTkFrame(master=windowPres)

    fillprescription.columnconfigure(0, weight = 0)
    fillprescription.columnconfigure(1, weight = 1)
    fillprescription.rowconfigure(0, weight = 0)
    fillprescription.rowconfigure(1, weight = 0)
    fillprescription.rowconfigure(2, weight = 0)
    fillprescription.rowconfigure(3, weight=0)
    fillprescription.rowconfigure(4, weight=0)
#Fill Presciption Button
    FillPresB = ctk.CTkButton(
        master=fillprescription,
        text = "Fill A Prescription",
        font = ("Fira Code", 15),
        width = 200,
        height= 50,
    )

#Potential Text Fields we will need
    #Fill Prescription text field
    LabelCNF = ctk.CTkLabel(master=fillprescription, text="What is the first and last name of the Customer")
    LabelFq1 = ctk.CTkLabel(master=fillprescription, text = "Is this the correct prescription")
    LabelFq2 = ctk.CTkLabel(master=fillprescription, text = "How many did you grab")
    LabelFRM = ctk.CTkLabel(master=fillprescription, text ="Too many pills grabbed")
    labelFRL = ctk.CTkLabel(master=fillprescription, text="Too few pills grabbed")
    labelFRC = ctk.CTkLabel(master=fillprescription, text ="Correct Number grabbed")


  
    
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
    
      #Add prescriptions text field
    LabelCNA = ctk.CTkLabel(master=AddPrescription, text="What is the first and last name of the Customer")
    LabelPID = ctk.CTkLabel(master = AddPrescription, text ="What is the prescription ID")
    LabelPS = ctk.CTkLabel(master= AddPrescription, text = "What is the prescription start date (YYYY/MM/DD)")
    prescriptionEnd = ctk.CTkLabel(master=AddPrescription, text="What is the prescription end date (YYYY/MM/DD)")

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