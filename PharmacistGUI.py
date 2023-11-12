import customtkinter as tk
import addCustomerView as acv
import updateCustomerView as ucv
import deleteCustomerView as dcv



PharmacistHome = tk.CTk()
PharmacistHome.geometry("750x500")
PharmacistHome.title("Pharmacist Homepage")

def OpenAddWindow():
    acv.open_addCustomerView()
    PharmacistHome.withdraw()

def OpenUpdateWindow():
    ucv.open_updateCustomerView()
    PharmacistHome.withdraw()

def OpenDeleteWindow():
    dcv.open_deleteCustomerView()
    PharmacistHome.withdraw()

AddCustomerButton = tk.CTkButton(
    master = PharmacistHome,
    text = "Add Customer",
    width = 200,
    height = 50,
    #bg = "blue",
    #fg = "yellow",
    #font = 10,
    command = OpenAddWindow 
)

UpdateCustomerButton = tk.CTkButton(
    master = PharmacistHome,
    text = "Update Customer",
    width = 200,
    height = 50,
    #bg = "blue",
    #fg = "yellow",
    #font = 10,
    command = OpenUpdateWindow 
)

DeleteCustomerButton = tk.CTkButton(
    master = PharmacistHome,
    text = "Delete Customer",
    width = 200,
    height = 50,
    #bg = "blue",
    #fg = "yellow",
    #font = 10,
    command = OpenDeleteWindow 
)

FillPrescriptionButton = tk.CTkButton(
    master = PharmacistHome,
    text = "Fill Prescription", 
    width = 200, 
    height = 50, 
    #bg = "blue", 
    #fg = "yellow", 
    #font = 10,
    #command = open fillprescription view 
)

NewPrescriptionButton = tk.CTkButton(
    master = PharmacistHome,
    text = "Enter New Prescription", 
    width = 200, 
    height = 50, 
    #bg = "blue", 
    #fg = "yellow", 
    #font = 10,
    #command = open enter new prescription view 
)

CheckAvailabilityButton = tk.CTkButton(
    master = PharmacistHome,
    text = "Check Med Availability", 
    width = 200, 
    height = 50, 
    #bg = "blue", 
    #fg = "yellow", 
    #font = 10,
    #command = open checkavailability view 
)

CheckoutButton = tk.CTkButton(
    master = PharmacistHome,
    text = "Checkout", 
    width = 200, 
    height = 50, 
    #bg = "blue", 
    #fg = "yellow", 
    #font = 10,
    #command = open checkout view 
)

BacktoLoginButton = tk.CTkButton(
    master = PharmacistHome, 
    text = "Exit", 
    width = 100, 
    height = 25, 
)

AddCustomerButton.grid(row = 0, column = 0, padx=10, pady=10)
UpdateCustomerButton.grid(row = 0, column = 20, padx=10, pady=10)
DeleteCustomerButton.grid(row = 0, column = 40, padx=10, pady=10)
FillPrescriptionButton.grid(row = 50, column = 0, padx=10, pady=10)
NewPrescriptionButton.grid(row = 50, column = 20, padx=10, pady=10)
CheckAvailabilityButton.grid(row = 50, column = 40, padx=10, pady=10)
CheckoutButton.grid(row = 100, column = 20,  padx=10, pady=10)
BacktoLoginButton.grid(row = 500, column = 20, padx= 10, pady= 10)


PharmacistHome.mainloop()
