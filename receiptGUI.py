import customtkinter as tk

def open_receiptView(cartWindow, cashierWindow, checkoutWindow, total, cashier):
    # Selecting GUI theme - dark, light , system (for system default) 
    tk.set_appearance_mode("dark") 
    
    # Selecting color theme - blue, green, dark-blue 
    tk.set_default_color_theme("blue") 

    window = tk.CTkToplevel()
    window.geometry("800x600")
    window.minsize(800, 600)
    window.maxsize(800, 600)
    window.title("Receipt") 

    window.columnconfigure(0, weight = 0)
    window.columnconfigure(1, weight = 0)
    window.columnconfigure(2, weight = 0)
    window.columnconfigure(3, weight = 0)
    window.rowconfigure(0, weight = 0)
    window.rowconfigure(1, weight = 0)
    window.rowconfigure(2, weight = 0)
    window.rowconfigure(3, weight = 0)
    window.rowconfigure(4, weight = 0)
    window.rowconfigure(5, weight = 0)
    window.rowconfigure(6, weight = 0)

    back = tk.CTkButton(
        master=window,
        text="Go Back",
        width=200,
        height=50,
    )
    # labels are text
    label = tk.CTkLabel(master = window, text="Receipt", font=("Fira Code", 25))
    totalLabel = tk.CTkLabel(master = window, text="{}".format(total))
    totallabel2 = tk.CTkLabel(master = window, text="Total: ")

    #this adds inputs to window
    label.grid(columnspan = 4, column = 0, row = 0, pady=10, padx = 4)
    totalLabel.grid(columnspan = 2, column = 1, row = 7, pady=10, padx = 4)
    totallabel2.grid(columnspan = 2, column = 0, row = 7, pady=10, padx = 4)
    back.grid(columnspan = 4, row = 8, pady=4, padx = 4)

    class Row:
        def __init__(self, name, quantity, strength, price, rowIndex, med): #this needs to be a class so that every generated row knows its own index and can be removed later
            #values
            self.name = name
            self.quantity = quantity
            self.strength = strength
            self.price = price
            self.rowIndex = rowIndex
            self.med = med
            #grid stuff
            self.nameLabel = tk.CTkLabel(master=window, text="{}".format(self.name))
            self.qLabel = tk.CTkLabel(master=window,  text="{}".format(self.quantity))
            self.strLabel = tk.CTkLabel(master=window, text="{}".format(self.strength))
            self.priceLabel = tk.CTkLabel(master=window, text="${}".format(self.price))

        def generate(self): #generates a row on the grid
            self.nameLabel.grid(row = self.rowIndex, column = 0, padx=2)
            self.qLabel.grid(row = self.rowIndex, column = 1, padx=2)
            self.strLabel.grid(row = self.rowIndex, column = 2, padx=2)
            self.priceLabel.grid(row = self.rowIndex, column = 3, padx=2)

    def buildTable(items):
        count = 0
        for med in items:
            #row is of type medicine
            temp = count+2
            newRow = Row(med.name, med.quantity, med.strength, med.price, temp, med)
            newRow.generate()
            count = count + 1   

    def clear_text(text):
        text.delete(0, tk.END)

    def closeWindow(self):
        cashierWindow.deiconify()
        checkoutWindow.destroy()
        cartWindow.destroy()
        window.destroy()

    items = cashier.fetchCart()
    buildTable(items)

    back.bind("<Button-1>", closeWindow)

#window.mainloop() #constant loop for gui 
