import customtkinter as tk
import deleteInventoryView as div
import addInventoryView as aiv
import addCustomerView as acv
import updateCustomerView as ucv
import deleteCustomerView as dcv
import addStaffView as asv
import updateStaffView as usv
import deleteStaffView as dsv
import changePassView as cpv
import RecoverUserAccount as ra
import cartGUI as ocw
import UpdateInventoryView as uiv
import CheckItemAvailabilityView as cav
import ManagerPrescriptionGui as mpgui
import generateFinancialReportsView as gfr
import CheckItemAvailabilityView as cia
from controllers.LogController import *
#import addCustomerView as acv
import controllers.Expiration as exp 
from tkinter import messagebox

from models.Staff import PharmacyManager

def open_managerGUI(app, currentId, password):
    ManagerHome = tk.CTkToplevel()
    ManagerHome.geometry("800x600")
    ManagerHome.minsize(800, 600)
    ManagerHome.maxsize(800, 600)
    ManagerHome.title("Manager Homepage")

    manager = PharmacyManager()
    app.withdraw()

    def LogOut():
        LogoutLog(id)
        app.deiconify()
        ManagerHome.destroy()

    def deleteInventory():
        div.open_deleteInventory(ManagerHome)
        ManagerHome.withdraw()
        InventoryLog(id)

    def updateInventory():
        uiv.open_UpdateInventory(ManagerHome)
        ManagerHome.withdraw()
        InventoryLog(id)

    def addInventory():
        aiv.open_addInventoryView(ManagerHome)
        ManagerHome.withdraw()
        InventoryLog(id)

    def addPrescription():
        mpgui.open_PrescriptionManagerGUI(ManagerHome)
        ManagerHome.withdraw()

    def financialreports():
        gfr.open_financialreports(ManagerHome)
        ManagerHome.withdraw()

    def changePassView():
        cpv.open_passView(ManagerHome, currentId, password)
        ManagerHome.withdraw()

    def OpenAddStaffWindow():
        asv.open_addStaffView(ManagerHome)
        ManagerHome.withdraw()

    def OpenUpdateStaffWindow():
        usv.open_updateStaffView(ManagerHome)
        ManagerHome.withdraw()

    def OpenDeleteStaffWindow():
        dsv.open_deleteStaffView(ManagerHome)
        ManagerHome.withdraw()

    def OpenAddCustomerWindow():
        acv.open_addCustomerView(ManagerHome)
        ManagerHome.withdraw()

    def OpenUpdateCustomerWindow():
        ucv.open_updateCustomerView(ManagerHome)
        ManagerHome.withdraw()

    def OpenDeleteCustomerWindow():
        dcv.open_deleteCustomerView(ManagerHome)
        ManagerHome.withdraw()

    def OpenCartWindow():
        ocw.open_cartView(ManagerHome, currentId)
        ManagerHome.withdraw()

    def checkAvail():
        cav.open_CheckItemAvailability(ManagerHome)
        ManagerHome.withdraw()

    def recoverAccount():
        ra.open_recoverAccountView(ManagerHome)
        ManagerHome.withdraw()
    
    #should add instant check for low stock or expired notifications

    #lowstock = Manager.PharmacyManager.LowStock()

    AddUserButton = tk.CTkButton(
        master = ManagerHome,
        text = "Add Staff",
        width = 200,
        height = 50,
        #bg = "blue",
        #fg = "yellow",
        #font = 10,
        command = OpenAddStaffWindow
    )

    UpdateUserButton = tk.CTkButton(
        master = ManagerHome,
        text = "Update Staff",
        width = 200,
        height = 50,
        #bg = "blue",
        #fg = "yellow",
        #font = 10,
        command = OpenUpdateStaffWindow 
    )

    DeleteUserButton = tk.CTkButton(
        master = ManagerHome,
        text = "Delete Staff",
        width = 200,
        height = 50,
        #bg = "blue",
        #fg = "yellow",
        #font = 10,
        command = OpenDeleteStaffWindow
    )

    UpdateInventory = tk.CTkButton(
        master = ManagerHome,
        text = "Update Inventory",
        width = 200,
        height = 50,
        command = updateInventory
    )

    DeleteInventory = tk.CTkButton(
        master = ManagerHome,
        text = "Delete Inventory",
        width = 200,
        height = 50,
        #bg = "blue",
        #fg = "yellow",
        #font = 10,
        command = deleteInventory
    )

    RecoverUserAccount = tk.CTkButton(
        master = ManagerHome,
        text = "Recover User Account",
        width = 200,
        height = 50,
        #bg = "blue",
        #fg = "yellow",
        #font = 10,
        command = recoverAccount
    )

    LogOutButton = tk.CTkButton(
        master = ManagerHome,
        text = "Log Out",
        width = 200,
        height = 50,
        #bg = "blue",
        #fg = "yellow",
        #font = 10,
        command = LogOut
    )

    FinancialReports = tk.CTkButton(
        master = ManagerHome,
        text = "Financial Reports",
        width = 200,
        height = 50,
        #bg = "blue",
        #fg = "yellow",
        #font = 10,
        command =  financialreports
    )

    AddCustomerButton = tk.CTkButton(
        master = ManagerHome,
        text = "Add Customer",
        width = 200,
        height = 50,
        #bg = "blue",
        #fg = "yellow",
        #font = 10,
        command = OpenAddCustomerWindow
    )

    UpdateCustomerButton = tk.CTkButton(
        master = ManagerHome,
        text = "Update Customer",
        width = 200,
        height = 50,
        #bg = "blue",
        #fg = "yellow",
        #font = 10,
        command = OpenUpdateCustomerWindow
    )

    DeleteCustomerButton = tk.CTkButton(
        master = ManagerHome,
        text = "Delete Customer",
        width = 200,
        height = 50,
        #bg = "blue",
        #fg = "yellow",
        #font = 10,
        command = OpenDeleteCustomerWindow
    )
   
    checkAvailability = tk.CTkButton(
        master = ManagerHome,
        text = "check availability",
        width = 200,
        height = 50,
        command = checkAvail
    )

    AddInventory = tk.CTkButton(
        master = ManagerHome,
        text = "Add Inventory",
        width = 200,
        height = 50,
        command = addInventory
    )

    changePassword = tk.CTkButton(
        master = ManagerHome,
        text = "Change Password",
        width = 200,
        height = 50,
        command = changePassView
    )

    addPrescription = tk.CTkButton(
        master = ManagerHome,
        text = "Add Prescription",
        width = 200,
        height = 50,
        command = addPrescription
    )

    cart = tk.CTkButton(
        master = ManagerHome,
        text = "Cart",
        width = 200,
        height = 50,
        command = OpenCartWindow
    )

    AddUserButton.grid(row = 0, column = 0, padx=30, pady=10)
    UpdateUserButton.grid(row = 0, column = 20, padx=30, pady=10)
    DeleteUserButton.grid(row = 0, column = 40, padx=30, pady=10)

    UpdateInventory.grid(row = 50, column = 0,  padx=10, pady=10)
    DeleteInventory.grid(row = 50, column = 20,  padx=10, pady=10)
    RecoverUserAccount.grid(row = 50, column = 40,  padx=10, pady=10)

    AddCustomerButton.grid(row = 100, column = 0, padx=10, pady=10)
    UpdateCustomerButton.grid(row = 100, column = 20, padx=10, pady=10)
    DeleteCustomerButton.grid(row = 100, column = 40, padx=10, pady=10)

    LogOutButton.grid(row = 150, column = 40,  padx=10, pady=10) 
    FinancialReports.grid(row = 150, column = 0,  padx=10, pady=10)
    checkAvailability.grid(row = 150, column = 20,  padx=10, pady=10)

    AddInventory.grid(row = 200, column = 40,  padx=10, pady=10) 
    changePassword.grid(row = 200, column = 0,  padx=10, pady=10)
    addPrescription.grid(row = 200, column = 20, padx=10, pady=10)

    cart.grid(row = 250, column = 20, padx=10, pady=10)

    messagebox.showwarning("WARNING: The following medications are EXPIRED.", exp.Expired())
    messagebox.showwarning("WARNING: The following medications expire within the NEXT 30 DAYS", exp.Expired30Day())
    messagebox.showwarning("WARNING: The following medications are low in stock", manager.LowStock())

