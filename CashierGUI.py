import customtkinter as tk
import addCustomerView as acv
import updateCustomerView as ucv
import deleteCustomerView as dcv
import changePassView as cpv
import cartGUI as cartv

from controllers.LogController import LogoutLog

import controllers.Expiration as exp 
from tkinter import messagebox


def open_cashierView(app, currentId, currentPassword):

    CashierHome = tk.CTkToplevel()
    CashierHome.geometry("700x200")
    CashierHome.title("Cashier Homepage")

    def OpenAddWindow():
        acv.open_addCustomerView(CashierHome)
        CashierHome.withdraw()

    def OpenCartWindow():
        cartv.open_cartView(CashierHome, currentId)
        CashierHome.withdraw()

    def OpenUpdateWindow():
        ucv.open_updateCustomerView(CashierHome)
        CashierHome.withdraw()

    def OpenDeleteWindow():
        dcv.open_deleteCustomerView(CashierHome)
        CashierHome.withdraw()

    def LogOut():
        LogoutLog(currentId)
        app.deiconify()
        CashierHome.destroy()

    def ChangePassword():
        cpv.open_passView(CashierHome, currentId, currentPassword)
        CashierHome.withdraw()

    AddCustomerButton = tk.CTkButton(
        master = CashierHome,
        text = "Add Customer",
        width = 200,
        height = 50,
        #bg = "blue",
        #fg = "yellow",
        #font = 10,
        command = OpenAddWindow
    )

    UpdateCustomerButton = tk.CTkButton(
        master = CashierHome,
        text = "Update Customer",
        width = 200,
        height = 50,
        #bg = "blue",
        #fg = "yellow",
        #font = 10,
        command = OpenUpdateWindow
    )

    DeleteCustomerButton = tk.CTkButton(
        master = CashierHome,
        text = "Delete Customer",
        width = 200,
        height = 50,
        #bg = "blue",
        #fg = "yellow",
        #font = 10,
        command = OpenDeleteWindow
    )

    CheckoutButton = tk.CTkButton(
        master = CashierHome,
        text = "Checkout",
        width = 200,
        height = 50,
        #bg = "blue",
        #fg = "yellow",
        #font = 10,
        command = OpenCartWindow
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

    changePassword = tk.CTkButton(
        master = CashierHome,
        text = "Change Password",
        width = 200,
        height = 50,
        #bg = "blue",
        #fg = "yellow",
        #font = 10,
        command = ChangePassword
    )

    app.withdraw()
    AddCustomerButton.grid(row = 0, column = 0, padx=10, pady=10)
    UpdateCustomerButton.grid(row = 0, column = 20, padx=10, pady=10)
    DeleteCustomerButton.grid(row = 0, column = 40, padx=10, pady=10)
    CheckoutButton.grid(row = 50, column = 20,  padx=10, pady=10)
    LogOutButton.grid(row = 50, column = 40,  padx=10, pady=10)    
    changePassword.grid(row = 50, column = 0,  padx=10, pady=10)   

    messagebox.showwarning("WARNING: The following medications are EXPIRED.", exp.Expired())


    #CashierHome.mainloop()
