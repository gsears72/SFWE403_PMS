import customtkinter as tk
import deleteInventoryView as div
import CheckItemAvailabilityView as checkAvail
import generateFinancialReportsView as gfr
from controllers.LogController import *
#import addCustomerView as acv
import controllers.Expiration as exp 
from tkinter import messagebox

def open_managerGUI(app,id):
    CashierHome = tk.CTkToplevel()
    CashierHome.geometry("700x200")
    CashierHome.title("Manager Homepage")

    def LogOut():
        LogoutLog(id)
        app.deiconify()
        CashierHome.destroy()

    def deleteInventory():
        InventoryLog(id)
        div.open_deleteInventory(CashierHome)
        CashierHome.withdraw()

    def financialreports():
        gfr.open_financialreports(CashierHome)
        CashierHome.withdraw()

    def checkItemAvail():
        checkAvail.open_CheckItemAvailability(CashierHome)
        CashierHome.withdraw()

    

    #should add instant check for low stock or expired notifications

    AddUserButton = tk.CTkButton(
        master = CashierHome,
        text = "Add User",
        width = 200,
        height = 50,
        #bg = "blue",
        #fg = "yellow",
        #font = 10,
        #command = acv.open_addCustomerView()
    )

    UpdateUserButton = tk.CTkButton(
        master = CashierHome,
        text = "Update User",
        width = 200,
        height = 50,
        #bg = "blue",
        #fg = "yellow",
        #font = 10,
        #command = open updatecustomer view 
    )

    DeleteUserButton = tk.CTkButton(
        master = CashierHome,
        text = "Delete User",
        width = 200,
        height = 50,
        #bg = "blue",
        #fg = "yellow",
        #font = 10,
        #command = open deletecustomer view 
    )

    UpdateInventory = tk.CTkButton(
        master = CashierHome,
        text = "Update Inventory",
        width = 200,
        height = 50,
        #bg = "blue",
        #fg = "yellow",
        #font = 10,
        #command = open checkout view 
    )

    DeleteInventory = tk.CTkButton(
        master = CashierHome,
        text = "Delete Inventory",
        width = 200,
        height = 50,
        #bg = "blue",
        #fg = "yellow",
        #font = 10,
        command = deleteInventory
    )

    RecoverUserAccount = tk.CTkButton(
        master = CashierHome,
        text = "Recover User Account",
        width = 200,
        height = 50,
        #bg = "blue",
        #fg = "yellow",
        #font = 10,
        #command = open checkout view 
    )

    LogOutButton = tk.CTkButton(
        master = CashierHome,
        text = "Log Out",
        width = 200,
        height = 50,
        #bg = "blue",
        #fg = "yellow",
        #font = 10,
        command = LogOut
    )

    FinancialReports = tk.CTkButton(
        master = CashierHome,
        text = "Financial Reports",
        width = 200,
        height = 50,
        #bg = "blue",
        #fg = "yellow",
        #font = 10,
        command =  financialreports
    )

    CheckItemAvailability = tk.CTkButton(
        master = CashierHome, 
        text = "Check Item Availability",
        width = 200,
        height = 50,
        command =  checkItemAvail
    )

    app.withdraw()


    AddUserButton.grid(row = 0, column = 0, padx=10, pady=10)
    UpdateUserButton.grid(row = 0, column = 20, padx=10, pady=10)
    DeleteUserButton.grid(row = 0, column = 40, padx=10, pady=10)
    UpdateInventory.grid(row = 50, column = 0,  padx=10, pady=10)
    DeleteInventory.grid(row = 50, column = 20,  padx=10, pady=10)
    RecoverUserAccount.grid(row = 50, column = 40,  padx=10, pady=10)
    LogOutButton.grid(row = 100, column = 40,  padx=10, pady=10) 
    FinancialReports.grid(row = 100, column = 0,  padx=10, pady=10)
    CheckItemAvailability.grid(row = 100, column = 20, padx=10, pady=10)

    messagebox.showwarning("WARNING: The following medications are EXPIRED.", exp.Expired())
    messagebox.showwarning("WARNING: The following medications expire within the NEXT 30 DAYS", exp.Expired30Day())

    CashierHome.mainloop()
