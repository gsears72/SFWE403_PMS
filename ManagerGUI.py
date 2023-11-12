grace3
import customtkinter as tk
import addCustomerView as acv
import updateCustomerView as ucv
import deleteCustomerView as dcv
import RecoverUserAccount as recover

ManagerHome = tk.CTk()
ManagerHome.geometry("700x200")
ManagerHome.title("Manager Homepage")

def OpenAddWindow():
    acv.open_addCustomerView()
    ManagerHome.withdraw()

def OpenUpdateWindow():
    ucv.open_updateCustomerView()
    ManagerHome.withdraw()

def OpenDeleteWindow():
    dcv.open_deleteCustomerView()
    ManagerHome.withdraw()


def OpenRecoverWindow():
    recover.open_recoverAccountView()
    ManagerHome.withdraw()
#should add instant check for low stock or expired notifications

AddUserButton = tk.CTkButton(
    master = ManagerHome,
    text = "Add User",
    width = 200,
    height = 50,
    #bg = "blue",
    #fg = "yellow",
    #font = 10,
    #command = acv.open_addCustomerView()
)

UpdateUserButton = tk.CTkButton(
    master = ManagerHome,
    text = "Update User",
    width = 200,
    height = 50,
    #bg = "blue",
    #fg = "yellow",
    #font = 10,
    #command = open updatecustomer view 
)

DeleteUserButton = tk.CTkButton(
    master = ManagerHome,
    text = "Delete User",
    width = 200,
    height = 50,
    #bg = "blue",
    #fg = "yellow",
    #font = 10,
    #command = open deletecustomer view 
)

AddCustomerButton = tk.CTkButton(
    master = ManagerHome,
    text = "Add Customer",
    width = 200,
    height = 50,
    #bg = "blue",
    #fg = "yellow",
    #font = 10,
    command = OpenAddWindow
)

UpdateCustomerButton = tk.CTkButton(
    master = ManagerHome,
    text = "Update Customer",
    width = 200,
    height = 50,
    #bg = "blue",
    #fg = "yellow",
    #font = 10,
    command = OpenUpdateWindow
)

DeleteCustomerButton = tk.CTkButton(
    master = ManagerHome,
    text = "Delete Customer",
    width = 200,
    height = 50,
    #bg = "blue",
    #fg = "yellow",
    #font = 10,
    command = OpenDeleteWindow
)

UpdateInventory = tk.CTkButton(
    master = ManagerHome,
    text = "Update Inventory",
    width = 200,
    height = 50,
    #bg = "blue",
    #fg = "yellow",
    #font = 10,
    #command = open checkout view 
)

DeleteInventory = tk.CTkButton(
    master = ManagerHome,
    text = "Delete Inventory",
    width = 200,
    height = 50,
    #bg = "blue",
    #fg = "yellow",
    #font = 10,
    #command = open checkout view 
)

RecoverUserAccount = tk.CTkButton(
    master = ManagerHome,
    text = "Recover User Account",
    width = 200,
    height = 50,
    #bg = "blue",
    #fg = "yellow",
    #font = 10,
    command = OpenRecoverWindow 
)



AddUserButton.grid(row = 0, column = 0, padx=10, pady=10)
UpdateUserButton.grid(row = 0, column = 20, padx=10, pady=10)
DeleteUserButton.grid(row = 0, column = 40, padx=10, pady=10)

AddCustomerButton.grid(row = 1, column = 0, padx=10, pady=10)
UpdateCustomerButton.grid(row = 1, column = 20, padx=10, pady=10)
DeleteCustomerButton.grid(row = 1, column = 40, padx=10, pady=10)

UpdateInventory.grid(row = 2, column = 0,  padx=10, pady=10)
DeleteInventory.grid(row = 2, column = 20,  padx=10, pady=10)
RecoverUserAccount.grid(row = 2, column = 40,  padx=10, pady=10)

    


ManagerHome.mainloop()

import customtkinter as tk
import addCustomerView as acv
import updateCustomerView as ucv
import deleteCustomerView as dcv
#import addCustomerView as acv


ManagerHome = tk.CTk()
ManagerHome.geometry("700x200")
ManagerHome.title("Manager Homepage")

def OpenAddWindow():
    acv.open_addCustomerView()
    ManagerHome.withdraw()

def OpenUpdateWindow():
    ucv.open_updateCustomerView()
    ManagerHome.withdraw()

def OpenDeleteWindow():
    dcv.open_deleteCustomerView()
    ManagerHome.withdraw()

#should add instant check for low stock or expired notifications

AddUserButton = tk.CTkButton(
    master = ManagerHome,
    text = "Add User",
    width = 200,
    height = 50,
    #bg = "blue",
    #fg = "yellow",
    #font = 10,
    #command = acv.open_addCustomerView()
)

UpdateUserButton = tk.CTkButton(
    master = ManagerHome,
    text = "Update User",
    width = 200,
    height = 50,
    #bg = "blue",
    #fg = "yellow",
    #font = 10,
    #command = open updatecustomer view 
)

DeleteUserButton = tk.CTkButton(
    master = ManagerHome,
    text = "Delete User",
    width = 200,
    height = 50,
    #bg = "blue",
    #fg = "yellow",
    #font = 10,
    #command = open deletecustomer view 
)

AddCustomerButton = tk.CTkButton(
    master = ManagerHome,
    text = "Add Customer",
    width = 200,
    height = 50,
    #bg = "blue",
    #fg = "yellow",
    #font = 10,
    command = OpenAddWindow
)

UpdateCustomerButton = tk.CTkButton(
    master = ManagerHome,
    text = "Update Customer",
    width = 200,
    height = 50,
    #bg = "blue",
    #fg = "yellow",
    #font = 10,
    command = OpenUpdateWindow
)

DeleteCustomerButton = tk.CTkButton(
    master = ManagerHome,
    text = "Delete Customer",
    width = 200,
    height = 50,
    #bg = "blue",
    #fg = "yellow",
    #font = 10,
    command = OpenDeleteWindow
)

UpdateInventory = tk.CTkButton(
    master = ManagerHome,
    text = "Update Inventory",
    width = 200,
    height = 50,
    #bg = "blue",
    #fg = "yellow",
    #font = 10,
    #command = open checkout view 
)

DeleteInventory = tk.CTkButton(
    master = ManagerHome,
    text = "Delete Inventory",
    width = 200,
    height = 50,
    #bg = "blue",
    #fg = "yellow",
    #font = 10,
    #command = open checkout view 
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



AddUserButton.grid(row = 0, column = 0, padx=10, pady=10)
UpdateUserButton.grid(row = 0, column = 20, padx=10, pady=10)
DeleteUserButton.grid(row = 0, column = 40, padx=10, pady=10)

AddCustomerButton.grid(row = 1, column = 0, padx=10, pady=10)
UpdateCustomerButton.grid(row = 1, column = 20, padx=10, pady=10)
DeleteCustomerButton.grid(row = 1, column = 40, padx=10, pady=10)

UpdateInventory.grid(row = 2, column = 0,  padx=10, pady=10)
DeleteInventory.grid(row = 2, column = 20,  padx=10, pady=10)
RecoverUserAccount.grid(row = 2, column = 40,  padx=10, pady=10)

    


ManagerHome.mainloop()
main
