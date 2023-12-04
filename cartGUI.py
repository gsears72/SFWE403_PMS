from tkinter import Frame
import customtkinter as tk
from models.Medicine import Medicine
from models.Staff import Cashier
import checkoutGui as cg

def open_cartView(cashierWindow, userID):
# Selecting GUI theme - dark, light , system (for system default) 
    tk.set_appearance_mode("dark") 
    
    # Selecting color theme - blue, green, dark-blue 
    tk.set_default_color_theme("blue") 

    cashier = Cashier()
    medicine = Medicine()
    rows = []

    window = tk.CTkToplevel()
    table = Frame(window)
    window.geometry("500x500") 
    window.title("Add to Cart") 

    window.columnconfigure(0, weight = 0)
    window.columnconfigure(1, weight = 0)
    window.columnconfigure(2, weight = 0)
    window.columnconfigure(3, weight = 0)
    window.columnconfigure(4, weight = 0)
    window.rowconfigure(0, weight = 0)
    window.rowconfigure(1, weight = 0)
    window.rowconfigure(2, weight = 0)
    window.rowconfigure(3, weight = 0)
    window.rowconfigure(4, weight = 0)
    window.rowconfigure(5, weight = 0)

    button = tk.CTkButton(
        master=window,
        text="Add to Cart",
        width=150,
        height=50,
    )

    back = tk.CTkButton(
        master=window,
        text="Go Back",
        width=150,
        height=50,
    )

    checkOutB = tk.CTkButton(
        master=window,
        text="Check Out",
        width=150,
        height=50,
    )

    # labels are text
    label = tk.CTkLabel(master=window,text="Shopping Cart", font=("Fira Code", 25)) 
    label1 = tk.CTkLabel(master=window,text="Name") 
    label2 = tk.CTkLabel(master=window,text="Quantity") 
    # the cart headers
    nameL = tk.CTkLabel(master=window,text="name") 
    quantityL = tk.CTkLabel(master=window,text="quantity") 
    strengthL = tk.CTkLabel(master=window,text="strength") 
    priceL = tk.CTkLabel(master=window,text="price") 

    success = tk.CTkLabel(master=window,text="Successfully Added!")  
    failure = tk.CTkLabel(master=window,text="Failed to Add!") 
    #These are the input fields
    nameIn = tk.CTkEntry(master=window, width=300)
    quantityIn = tk.CTkEntry(master=window, width=300)

    #this adds inputs to window
    label.grid(columnspan=5, row=0, padx=1, pady=1)
    label1.grid(column=0, row=9, padx=5, pady=5)
    nameIn.grid(column=1, columnspan=4, row=9, padx=5, pady=5) 
    label2.grid(column=0, row=10, padx=5, pady=5)
    quantityIn.grid(column=1, columnspan=4, row=10, padx=5, pady=5) 

    button.grid(column = 1, columnspan=2, row=11, padx=5, pady=5)
    back.grid(column = 0, row=11, padx=5, pady=5)
    checkOutB.grid(column = 3, columnspan=2, row=11, padx=5, pady=5)

    def handle_click(event): 
        
        medicine.name = nameIn.get()
        medicine.quantity = int(quantityIn.get())
        try:
            item = cashier.fetchItem(medicine.name)
            newMed = loadMedicine(item, medicine)
        
            cashier.addCart(newMed) 
            items = cashier.fetchCart()

            nameL.grid(column=0, row=1, padx=3, pady=5)
            quantityL.grid(column=1, row=1, padx=3, pady=5) 
            strengthL.grid(column=2, row=1, padx=3, pady=5)
            priceL.grid(column=3, row=1, padx=3, pady=5) 
            failure.grid_remove()
            clear_text(nameIn)
            clear_text(quantityIn)
            buildTable(items)
        except:
            clear_text(nameIn)
            clear_text(quantityIn)
            failure.grid(row = 8, columnspan = 4, pady = 4)

    def clear_text(text):
        text.delete(0, tk.END)

    def buildTable(items):
        count = 0
        for med in items:
            #row is of type medicine
            temp = count+2
            newRow = Row(med.name, med.quantity, med.strength, med.price, temp, med)
            newRow.generate()
            count = count + 1   

    def loadMedicine(item, medicine):
        newMedicine = Medicine()
        newMedicine.name = medicine.name
        newMedicine.quantity = medicine.quantity
        newMedicine.expDate = item[5]
        newMedicine.strength = item[3] 
        newMedicine.batch = item[4] 
        newMedicine.price = item[6] 
        return newMedicine

    def updateCart(rows):
        for row in rows:
            newQuantity = row.qLabel.get()
            cashier.updateCart(row.med, newQuantity)

    def checkOut(event):
        updateCart(rows)
        total = cashier.calculateTotal()
        cg.open_checkoutView(window, cashierWindow, total, cashier, userID)
        window.withdraw()
        
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
            self.qLabel = tk.CTkEntry(master=window, width=50)
            self.strLabel = tk.CTkLabel(master=window, text="{}".format(self.strength))
            self.priceLabel = tk.CTkLabel(master=window, text="${}".format(self.price))
            self.tempButton = tk.CTkButton(
                master = window,
                text = "Remove",
                width = 50,
                height = 25,
            )

        def removeRow(self, event):
            try:
                cashier.removeItemCart(self.med)
                self.nameLabel.grid_remove()
                self.qLabel.grid_remove()
                self.strLabel.grid_remove()
                self.priceLabel.grid_remove()
                self.tempButton.grid_remove()
                rows.remove(self)
            except Exception as e:
                print(e)

        def generate(self): #generates a row on the grid
            self.nameLabel.grid(row = self.rowIndex, column = 0)
            self.qLabel.insert(0, self.quantity)
            self.qLabel.grid(row = self.rowIndex, column = 1)
            self.strLabel.grid(row = self.rowIndex, column = 2)
            self.priceLabel.grid(row = self.rowIndex, column = 3)
            self.tempButton.grid(row = self.rowIndex, column = 4)
            self.tempButton.bind("<Button-1>", self.removeRow)
            try:
                rows.append(self)
            except Exception as e:
                print(e)

    def closeWindow(self):
        cashierWindow.deiconify() #makes the previous window visible 
        window.destroy()

    button.bind("<Button-1>", handle_click) #connects function handle_click to button 
    checkOutB.bind("<Button-1>", checkOut)
    back.bind("<Button-1>", closeWindow)

    #window.mainloop() #constant loop for gui 