import customtkinter as tk
import addCustomerView as acv
import updateCustomerView as ucv
import deleteCustomerView as dcv
#import addCustomerView as acv



PharmacyTechHome = tk.CTk()
PharmacyTechHome.geometry("700x200")
PharmacyTechHome.title("Pharmacy Technician Homepage")

def OpenAddWindow():
    acv.open_addCustomerView()
    PharmacyTechHome.withdraw()

def OpenUpdateWindow():
    ucv.open_updateCustomerView()
    PharmacyTechHome.withdraw()

def OpenDeleteWindow():
    dcv.open_deleteCustomerView()
    PharmacyTechHome.withdraw()

#should add instant check for low stock or expired notifications

AddCustomerButton = tk.CTkButton(
    master = PharmacyTechHome,
    text = "Add Customer",
    width = 200,
    height = 50,
    #bg = "blue",
    #fg = "yellow",
    #font = 10,
    command = OpenAddWindow
)

UpdateCustomerButton = tk.CTkButton(
    master = PharmacyTechHome,
    text = "Update Customer",
    width = 200,
    height = 50,
    #bg = "blue",
    #fg = "yellow",
    #font = 10,
    command = OpenUpdateWindow
)

DeleteCustomerButton = tk.CTkButton(
    master = PharmacyTechHome,
    text = "Delete Customer",
    width = 200,
    height = 50,
    #bg = "blue",
    #fg = "yellow",
    #font = 10,
    command = OpenDeleteWindow
)

CheckoutButton = tk.CTkButton(
    master = PharmacyTechHome,
    text = "Checkout",
    width = 200,
    height = 50,
    #bg = "blue",
    #fg = "yellow",
    #font = 10,
    #command = OpenDeleteWindow
)

EnterPrescriptionButton = tk.CTkButton(
    master = PharmacyTechHome,
    text = "Enter Prescription",
    width = 200,
    height = 50,
    #bg = "blue",
    #fg = "yellow",
    #font = 10,
    #command = OpenDeleteWindow
)

AddCustomerButton.grid(row = 0, column = 0, padx=10, pady=10)
UpdateCustomerButton.grid(row = 0, column = 20, padx=10, pady=10)
DeleteCustomerButton.grid(row = 0, column = 40, padx=10, pady=10)
EnterPrescriptionButton.grid(row = 2, column = 0, padx=10, pady=10)
CheckoutButton.grid(row = 2, column = 20, padx=10, pady=10)


PharmacyTechHome.mainloop()