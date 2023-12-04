import customtkinter as tk
import deleteInventoryView as div
import addCustomerView as acv
import updateCustomerView as ucv
import deleteCustomerView as dcv
import addStaffView as asv
import updateStaffView as usv
import deleteStaffView as dsv
import generateFinancialReportsView as gfr
import UpdateInventoryView as uiv
import CheckItemAvailabilityView as checkAvail
from controllers.LogController import *
import cartGUI as cartv
#import addCustomerView as acv
import controllers.Expiration as exp 
from tkinter import messagebox
from models.Staff import PharmacyManager

def open_managerGUI(app, id):
    ManagerHome = tk.CTkToplevel()
    ManagerHome.geometry("700x400")
    ManagerHome.title("Manager Homepage")

    manager = PharmacyManager()
    app.withdraw()

    def LogOut():
        LogoutLog(id)
        app.deiconify()
        ManagerHome.destroy()

    def deleteInventory():
        InventoryLog(id)
        div.open_deleteInventory(ManagerHome)
        ManagerHome.withdraw()

    def financialreports():
        gfr.open_financialreports(ManagerHome)
        ManagerHome.withdraw()

    def OpenCartWindow():
        cartv.open_cartView(ManagerHome, id)
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

    def checkItemAvail():
        checkAvail.open_CheckItemAvailability(ManagerHome)
        ManagerHome.withdraw()

    def updateInventory():
        uiv.open_UpdateInventory(ManagerHome)
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
        #bg = "blue",
        #fg = "yellow",
        #font = 10,
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
        #command = open checkout view 
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
   
    CheckItemAvailability = tk.CTkButton(
        master = ManagerHome, 
        text = "Check Item Availability",
        width = 200,
        height = 50,
        command =  checkItemAvail
    )

    AddUserButton.grid(row = 0, column = 0, padx=10, pady=10)
    UpdateUserButton.grid(row = 0, column = 20, padx=10, pady=10)
    DeleteUserButton.grid(row = 0, column = 40, padx=10, pady=10)

    UpdateInventory.grid(row = 50, column = 0,  padx=10, pady=10)
    DeleteInventory.grid(row = 50, column = 20,  padx=10, pady=10)
    RecoverUserAccount.grid(row = 50, column = 40,  padx=10, pady=10)

    AddCustomerButton.grid(row = 100, column = 0, padx=10, pady=10)
    UpdateCustomerButton.grid(row = 100, column = 20, padx=10, pady=10)
    DeleteCustomerButton.grid(row = 100, column = 40, padx=10, pady=10)

    LogOutButton.grid(row = 150, column = 40,  padx=10, pady=10) 
    FinancialReports.grid(row = 150, column = 0,  padx=10, pady=10)

    CheckItemAvailability.grid(row = 150, column = 20, padx=10, pady=10)


    messagebox.showwarning("WARNING: The following medications are EXPIRED.", exp.Expired())
    messagebox.showwarning("WARNING: The following medications expire within the NEXT 30 DAYS", exp.Expired30Day())
    messagebox.showwarning("WARNING: The following medications are low in stock", manager.LowStock())

