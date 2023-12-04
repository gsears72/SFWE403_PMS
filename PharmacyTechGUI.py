import customtkinter as tk
from controllers.LogController import LogoutLog
import addCustomerView as acv
import updateCustomerView as ucv
import cartGUI as ocw
import changePassView as cpv
import ManagerPrescriptionGui as mpgui
import controllers.Expiration as exp 
from tkinter import messagebox

def open_pharmacistTechGUI(app, currentId, password):
    PTHome = tk.CTkToplevel()
    PTHome.geometry("800x600")
    PTHome.minsize(800, 600)
    PTHome.maxsize(800, 600)
    PTHome.title("Pharmacy Technician Homepage")

    #should add instant check for low stock or expired notifications
    def LogOut():
        LogoutLog(id)
        app.deiconify()
        PTHome.destroy()

    def OpenCartWindow():
        ocw.open_cartView(PTHome, currentId)
        PTHome.withdraw()

    def addPrescription():
        mpgui.open_PrescriptionManagerGUI(PTHome)
        PTHome.withdraw()

    def OpenAddCustomerWindow():
        acv.open_addCustomerView(PTHome)
        PTHome.withdraw()

    def OpenUpdateCustomerWindow():
        ucv.open_updateCustomerView(PTHome)
        PTHome.withdraw()

    def changePassView():
        cpv.open_passView(PTHome, currentId, password)
        PTHome.withdraw()

    AddCustomerButton = tk.CTkButton(
        master = PTHome,
        text = "Add Customer",
        width = 200,
        height = 50,
        command = OpenAddCustomerWindow
    )

    UpdateCustomerButton = tk.CTkButton(
        master = PTHome,
        text = "Update Customer",
        width = 200,
        height = 50,
        command = OpenUpdateCustomerWindow
    )

    LogOutButton = tk.CTkButton(
        master = PTHome,
        text = "Log Out",
        width = 200,
        height = 50,
        command = LogOut
    )

    addPrescription = tk.CTkButton(
        master = PTHome,
        text = "Add Prescription",
        width = 200,
        height = 50,
        command = addPrescription
    )

    cart = tk.CTkButton(
        master = PTHome,
        text = "Cart",
        width = 200,
        height = 50,
        command = OpenCartWindow
    )

    changePassword = tk.CTkButton(
        master = PTHome,
        text = "Change Password",
        width = 200,
        height = 50,
        command = changePassView
    )

    app.withdraw()

    AddCustomerButton.grid(row = 0, column = 0, padx=10, pady=10)
    UpdateCustomerButton.grid(row = 0, column = 20, padx=10, pady=10)
    cart.grid(row = 0, column = 40, padx=10, pady=10)
    changePassword.grid(row = 20, column = 0, padx=10, pady=10)
    LogOutButton.grid(row = 20, column = 40, padx=10, pady=10)
    addPrescription.grid(row = 20, column = 20, padx=10, pady=10)

    messagebox.showwarning("WARNING: The following medications are EXPIRED.", exp.Expired())


    #CashierHome.mainloop()

