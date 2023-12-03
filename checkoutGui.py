import customtkinter as tk
from models.Customer import Customer
from models.Staff import Cashier
import receiptGUI as rGUI
from controllers.LogController import TransactionLog 

def open_checkoutView(cartHome, cashierWindow, total, cashier, userID):
    # Selecting GUI theme - dark, light , system (for system default) 
    tk.set_appearance_mode("dark") 
    
    # Selecting color theme - blue, green, dark-blue 
    tk.set_default_color_theme("blue") 

    window = tk.CTkToplevel()
    window.geometry("500x500") 
    window.title("Checkout Cart") 

    window.columnconfigure(0, weight = 0)
    window.columnconfigure(1, weight = 0)
    window.rowconfigure(0, weight = 0)
    window.rowconfigure(1, weight = 0)
    window.rowconfigure(2, weight = 0)
    window.rowconfigure(3, weight = 0)
    window.rowconfigure(4, weight = 0)
    window.rowconfigure(5, weight = 0)
    window.rowconfigure(6, weight = 0)

    button = tk.CTkButton(
        text="Pay",
        width=200,
        height=50,
        font = ("Fira Code", 15),
        master = window
    )

    back = tk.CTkButton(
        master=window,
        text="Go Back",
        width=200,
        height=50,
    )
    # labels are text
    label = tk.CTkLabel(master = window, text="Total Cost: ${}".format(total), font=("Fira Code", 25))

    success = tk.CTkLabel(master = window,text="payment completed!")  
    failure = tk.CTkLabel(master = window,text="Failed to complete transaction!") 

    cardNum = tk.CTkLabel(master = window,text="Card Number:") 
    name = tk.CTkLabel(master = window,text="Name on Card:") 
    cvc = tk.CTkLabel(master = window,text="CVC:")   
    expDate = tk.CTkLabel(master = window,text="Expiration Date:") 
   
    #These are the input fields
    cardNumIn = tk.CTkEntry(master = window, width=200)
    expDateIn = tk.CTkEntry(master = window, width=200)
    nameIn = tk.CTkEntry(master = window, width=200)
    cvcIn = tk.CTkEntry(master = window, width=200)

    #this adds inputs to window
    label.grid(columnspan = 2, column = 0, row = 0, pady=10, padx = 4)
    name.grid(column = 0, row = 1, pady=4, padx = 4)
    nameIn.grid(column = 1, row = 1, pady=4, padx = 4)
    cardNum.grid(column = 0, row = 2, pady=4, padx = 4)
    cardNumIn.grid(column = 1, row = 2, pady=4, padx = 4)
    expDate.grid(column = 0, row = 3, pady=4, padx = 4)
    expDateIn.grid(column = 1, row = 3, pady=4, padx = 4)
    cvc.grid(column = 0, row = 4, pady=4, padx = 4)
    cvcIn.grid(column = 1, row = 4, pady=4, padx = 4)
    button.grid(column = 1, row = 5, pady=4, padx = 4)
    back.grid(column = 0, row = 5, pady=4, padx = 4)

    def handle_click(event): 
        # this gets info from input and puts into class
        cart = cashier.fetchCart()
        cashier.updateInventory(cart)
        total = cashier.calculateTotal()
        try:
            TransactionLog(userID,total)
            rGUI.open_receiptView(cartHome, cashierWindow, window, total, cashier)
            window.withdraw()
        except Exception as e:
            success.grid_remove()
            failure.grid(columnspan = 2, row = 6, pady = 4) 
            print(e)

    def clear_text(text):
        text.delete(0, tk.END)

    def closeWindow(self):
        cartHome.deiconify()
        window.destroy()

    button.bind("<Button-1>", handle_click) #connects function handle_click to button 
    back.bind("<Button-1>", closeWindow)

#window.mainloop() #constant loop for gui 
