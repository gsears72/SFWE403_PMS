import customtkinter as tk
import addCustomerView as acv
import updateCustomerView as ucv
import deleteCustomerView as dcv
import addStaffView as asv
import updateStaffView as usv
import deleteStaffView as dsv
#import addCustomerView as acv


ManagerHome = tk.CTk()
ManagerHome.geometry("700x200")
ManagerHome.title("Manager Homepage")

def OpenAddStaffWindow():
    asv.open_addStaffView()
    ManagerHome.withdraw()

def OpenUpdateStaffWindow():
    usv.open_updateStaffView()
    ManagerHome.withdraw()

def OpenDeleteStaffWindow():
    dsv.open_deleteStaffView()
    ManagerHome.withdraw()

def OpenAddCustomerWindow():
    acv.open_addCustomerView()
    ManagerHome.withdraw()

def OpenUpdateCustomerWindow():
    ucv.open_updateCustomerView()
    ManagerHome.withdraw()

def OpenDeleteCustomerWindow():
    dcv.open_deleteCustomerView()
    ManagerHome.withdraw()

#should add instant check for low stock or expired notifications

AddStaffButton = tk.CTkButton(
    master = ManagerHome,
    text = "Add User",
    width = 200,
    height = 50,
    #bg = "blue",
    #fg = "yellow",
    #font = 10,
    command = OpenAddStaffWindow
)

UpdateStaffButton = tk.CTkButton(
    master = ManagerHome,
    text = "Update User",
    width = 200,
    height = 50,
    #bg = "blue",
    #fg = "yellow",
    #font = 10,
    command = OpenUpdateStaffWindow
)

DeleteStaffButton = tk.CTkButton(
    master = ManagerHome,
    text = "Delete User",
    width = 200,
    height = 50,
    #bg = "blue",
    #fg = "yellow",
    #font = 10,
    command = OpenDeleteStaffWindow
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



AddStaffButton.grid(row = 0, column = 0, padx=10, pady=10)
UpdateStaffButton.grid(row = 0, column = 20, padx=10, pady=10)
DeleteStaffButton.grid(row = 0, column = 40, padx=10, pady=10)

AddCustomerButton.grid(row = 1, column = 0, padx=10, pady=10)
UpdateCustomerButton.grid(row = 1, column = 20, padx=10, pady=10)
DeleteCustomerButton.grid(row = 1, column = 40, padx=10, pady=10)

UpdateInventory.grid(row = 2, column = 0,  padx=10, pady=10)
DeleteInventory.grid(row = 2, column = 20,  padx=10, pady=10)
RecoverUserAccount.grid(row = 2, column = 40,  padx=10, pady=10)


ManagerHome.mainloop()