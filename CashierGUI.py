import customtkinter as tk
import addCustomerView as acv
import updateCustomerView as ucv
import deleteCustomerView as dcv


CashierHome = tk.CTk()
CashierHome.geometry("700x200")
CashierHome.title("Cashier Homepage")

def OpenAddWindow():
    acv.open_addCustomerView()
    CashierHome.withdraw()

def OpenUpdateWindow():
    ucv.open_updateCustomerView()
    CashierHome.withdraw()

def OpenDeleteWindow():
    dcv.open_deleteCustomerView()
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
    #command = open checkout view 
)

BacktoLoginButton = tk.CTkButton(
    master = CashierHome, 
    text = "Exit", 
    width = 100, 
    height = 25, 
)



AddCustomerButton.grid(row = 0, column = 0, padx=10, pady=10)
UpdateCustomerButton.grid(row = 0, column = 20, padx=10, pady=10)
DeleteCustomerButton.grid(row = 0, column = 40, padx=10, pady=10)
CheckoutButton.grid(row = 50, column = 20,  padx=10, pady=10)
BacktoLoginButton.grid(row = 500, column = 20, padx= 10, pady= 10)


CashierHome.mainloop()
