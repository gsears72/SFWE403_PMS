import customtkinter as tk
import addCustomerView as acv
import updateCustomerView as ucv
import deleteCustomerView as dcv
import PrescriptionGUI as pv
from controllers.LogController import *
import controllers.Expiration as exp 
import changePassView as cpv
import cartGUI as cartv
import CheckItemAvailabilityView as cav
from tkinter import messagebox
#import PrescriptionGUI as pg


def open_phramacistGUI(PharmacistHome, currentId, password):

    window = tk.CTkToplevel()
    window.geometry("800x600")
    window.minsize(800, 600)
    window.maxsize(800, 600)
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
        pv.open_PrescriptionGUI(window)
        window.withdraw()
        InventoryLog(id)

    def OpenCartWindow():
        cartv.open_cartView(window, currentId)
        window.withdraw()

    def ChangePassword():
        cpv.open_passView(window, currentId, password)
        window.withdraw()

    def checkAvail():
        cav.open_CheckItemAvailability(window)
        window.withdraw()

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
        command = checkAvail
    )

    CheckoutButton = tk.CTkButton(
        master = window,
        text = "Checkout", 
        width = 200,
        height = 50,
        command = OpenCartWindow
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

    changePassword = tk.CTkButton(
        master = window,
        text = "Change Password",
        width = 200,
        height = 50,
        #bg = "blue",
        #fg = "yellow",
        #font = 10,
        command = ChangePassword
    )

    PharmacistHome.withdraw()
    AddCustomerButton.grid(row = 0, column = 0, padx=10, pady=10)
    UpdateCustomerButton.grid(row = 0, column = 20, padx=10, pady=10)
    DeleteCustomerButton.grid(row = 0, column = 40, padx=10, pady=10)
    FillPrescriptionButton.grid(row = 50, column = 0, padx=10, pady=10)
    NewPrescriptionButton.grid(row = 50, column = 20, padx=10, pady=10)
    CheckAvailabilityButton.grid(row = 50, column = 40, padx=10, pady=10)
    CheckoutButton.grid(row = 100, column = 20,  padx=10, pady=10)
    LogOutButton.grid(row = 100, column = 40,  padx=10, pady=10)  
    changePassword.grid(row = 100, column = 0,  padx=10, pady=10)


    messagebox.showwarning("WARNING: The following medications are EXPIRED.", exp.Expired())

    #window.mainloop()

    
