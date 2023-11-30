import customtkinter as tk
import addCustomerView as acv
import updateCustomerView as ucv
import deleteCustomerView as dcv
from controllers.LogController import *
import controllers.Expiration as exp 
from tkinter import messagebox
#import PrescriptionGUI as pg


def open_phramacistGUI(PharmacistHome,id):

    window = tk.CTkToplevel()
    window.geometry("750x500")
    window.title("Pharmacist Homepage")

    def OpenUpdateWindow():
        ucv.open_updateCustomerView(window)
        window.withdraw()

    def OpenDeleteWindow():
        dcv.open_deleteCustomerView(window)
        window.withdraw()

    def OpenAddWindow():
        acv.open_addCustomerView(window)
        window.withdraw()

    def OpenPrescriptionGUI():
        InventoryLog(id)
        pass
        #pg.open_PerscriptionGUI()
        #PharmacistHome.withdraw()

    def LogOut():
        LogoutLog(id)
        PharmacistHome.deiconify()
        window.destroy()

    AddCustomerButton = tk.CTkButton(
        master = window,
        text = "Add Customer",
        width = 200,
        height = 50,
        command = OpenAddWindow
    )

    UpdateCustomerButton = tk.CTkButton(
        master = window,
        text = "Update Customer",
        width = 200,
        height = 50,
        command = OpenUpdateWindow
    )

    DeleteCustomerButton = tk.CTkButton(
        master = window,
        text = "Delete Customer",
        width = 200,
        height = 50,
        command = OpenDeleteWindow
    )

    FillPrescriptionButton = tk.CTkButton(
        master = window,
        text = "Fill Prescription", 
        width = 200, 
        height = 50, 
        command = OpenPrescriptionGUI 
    )

    NewPrescriptionButton = tk.CTkButton(
        master = window,
        text = "Enter New Prescription", 
        width = 200,
        height = 50, 
        #bg = "blue", 
        #fg = "yellow", 
        #font = 10,
        command = OpenPrescriptionGUI 

    )

    CheckAvailabilityButton = tk.CTkButton(
        master = window,
        text = "Check Med Availability", 
        width = 200,
        height = 50,
        #command = open checkavailability view 
    )

    CheckoutButton = tk.CTkButton(
        master = window,
        text = "Checkout", 
        width = 200,
        height = 50,
        #command = open checkout view 
    )

    LogOutButton = tk.CTkButton(
        master = window,
        text = "Log Out",
        width = 200,
        height = 50,
        #bg = "blue",
        #fg = "yellow",
        #font = 10,
        command = LogOut
    )


    PharmacistHome.withdraw()
    AddCustomerButton.grid(row = 0, column = 0, padx=10, pady=10)
    UpdateCustomerButton.grid(row = 0, column = 20, padx=10, pady=10)
    DeleteCustomerButton.grid(row = 0, column = 40, padx=10, pady=10)
    FillPrescriptionButton.grid(row = 50, column = 0, padx=10, pady=10)
    NewPrescriptionButton.grid(row = 50, column = 20, padx=10, pady=10)
    CheckAvailabilityButton.grid(row = 50, column = 40, padx=10, pady=10)
    CheckoutButton.grid(row = 100, column = 20,  padx=10, pady=10)
    LogOutButton.grid(row = 100, column = 0,  padx=10, pady=10)  


    messagebox.showwarning("WARNING: The following medications are EXPIRED.", exp.Expired())

    #window.mainloop()

    
