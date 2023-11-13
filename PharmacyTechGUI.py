import customtkinter as tk
#import addCustomerView as acv

def open_pharmacistTechGUI(app):
    CashierHome = tk.CTkToplevel()
    CashierHome.geometry("700x200")
    CashierHome.title("Pharmacy Technician Homepage")

    #should add instant check for low stock or expired notifications
    def LogOut():
        app.deiconify()
        CashierHome.destroy()

    AddCustomerButton = tk.CTkButton(
        master = CashierHome,
        text = "Add Customer",
        width = 200,
        height = 50,
        #bg = "blue",
        #fg = "yellow",
        #font = 10,
        #command = acv.open_addCustomerView()
    )

    UpdateCustomerButton = tk.CTkButton(
        master = CashierHome,
        text = "Update Customer",
        width = 200,
        height = 50,
        #bg = "blue",
        #fg = "yellow",
        #font = 10,
        #command = open updatecustomer view 
    )

    DeleteCustomerButton = tk.CTkButton(
        master = CashierHome,
        text = "Delete Customer",
        width = 200,
        height = 50,
        #bg = "blue",
        #fg = "yellow",
        #font = 10,
        #command = open deletecustomer view 
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

    AddCustomerButton.grid(row = 0, column = 0, padx=10, pady=10)
    UpdateCustomerButton.grid(row = 0, column = 20, padx=10, pady=10)
    DeleteCustomerButton.grid(row = 0, column = 40, padx=10, pady=10)
    LogOutButton.grid(row = 0, column = 20, padx=10, pady=10)

    #CashierHome.mainloop()