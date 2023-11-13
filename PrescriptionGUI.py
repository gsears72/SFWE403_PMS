import customtkinter as ctk 
import tkinter.messagebox as tkmb
#from TESTING import *
#from SFWE403_PMS_Model import *
import PrescriptionView as PCV



def open_PerscriptionGUI():
    # Selecting GUI theme - dark, light , system (for system default) 
    ctk.set_appearance_mode("dark") 
    
    # Selecting color theme - blue, green, dark-blue 
    ctk.set_default_color_theme("blue") 

    app = ctk.CTkToplevel() 
    app.geometry("540x200") #1920x1280 is full screen
    app.title("Prescription Managment")

    label = ctk.CTkLabel(app,text = "Precription Managment Screen")
    label.grid(row = 0, column = 1)

    firstName = ctk.CTkEntry(master=app, text = "Customer First Name", row = 1, column = 1)
    lastName = ctk.CTkEntry(master=app, text = "Customer Last Name", row =  2, column = 1)
    #Function for add prescription

    #button functions
    def open_AddPrescription():
        print("This is a test piece")
        #PCV.Open_Add_Prescription(firstName, lastName)
        #app.withdraw()

    def open_FillPrescription():
        print("This is a test piece")
        #PCV.Open_Fill_PrescriptionView()
        #app.withdraw()


    AddPrescriptionButton = ctk.CTkButton(
        text="Add Prescription",
        width = 150,
        height = 100,
        master = app,
        command = open_AddPrescription
    )

    # FillPrescriptionLabel = ctk.CTkLabel(master=app, text="Enter the customer name")
    # FillPrescriptionEntry = ctk.CTkEntry(master=app, width=300)

    FillPrescriptionButton = ctk.CTkButton(
        text="Fill Prescription",
        width = 150,
        height = 100,
        master= app,
        command = open_FillPrescription
    )


    AddPrescriptionButton.grid(row = 3, column = 0, pady = 20, padx = 20)
    FillPrescriptionButton.grid(row = 3, column = 2, pady = 20)
    #Add A changePassword button
    #Add a back button
    app.mainloop()
