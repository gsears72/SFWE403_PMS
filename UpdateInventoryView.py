import customtkinter as tk
from models.Medicine import Medicine
from models.Staff import PharmacyManager

def open_UpdateInventory(app):
    # Selecting GUI theme - dark, light , system (for system default) 
    tk.set_appearance_mode("dark") 

    # Selecting color theme - blue, green, dark-blue 
    tk.set_default_color_theme("blue") 

    manager = PharmacyManager("test")
    medicine = Medicine()

    window = tk.CTkToplevel()
    window.geometry("500x500") 
    window.title("Update Item") 

    button = tk.CTkButton(
        text="Update",
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
    label = tk.CTkLabel(master = window,text="What item would you like to update? (name batchNum)") 

    success = tk.CTkLabel(master = window,text="Successfully Found!") 
    successUpdate = tk.CTkLabel(master = window, text="Successfuly Updated!!!!") 
    failure = tk.CTkLabel(master = window,text="Failed to Find Item.") 
    failureUpdate = tk.CTkLabel(master = window, text="Failed to update item amount.")
    #These are the input fields
    nameIn = tk.CTkEntry(master = window, width=300)
    updateAmount = tk.CTkEntry(master = window, width=300)
    updateLabel = tk.CTkLabel(master = window, text = "What is this item's new amount?")



    #this adds inputs to window
    label.pack(pady=20)
    nameIn.pack() 
    button.pack(pady = 20)
    back.pack(pady = 20)

    def handle_click(event): 
        # this gets info from input and puts into class
        name = nameIn.get()
        nameSplit = name.split(" ")
        if (len(nameSplit) > 1):
            medicine.name = nameSplit[0]
            medicine.batch = nameSplit[1]
        #this removes the customer from database and checks if it worked
        medicineID = manager.fetchMedicineID(medicine)
        if medicineID:
            failure.pack_forget() #removes from screen
            success.pack(pady = 20) #adds to screen 
            #clears input fields
            clear_text(nameIn)
            nameIn.pack_forget()
            updateAmount.pack()
            updateLabel.pack()
            amount = int(str(updateAmount.get()).strip())
            inventoryUpdated = manager.updateInventory(medicine.name, medicine.batch)
            if inventoryUpdated == True:
                successUpdate.pack()
                clear_text(updateAmount)
                updateAmount.pack_forget()
                updateLabel.pack_forget()

            else:
                failureUpdate.pack()
                clear_text(updateAmount)           


        else:
            success.pack_forget()
            failure.pack(pady = 20) 

    def clear_text(text):
        text.delete(0, tk.END)

    def closeWindow(self):
        app.deiconify()
        window.destroy()

    button.bind("<Button-1>", handle_click) #connects function handle_click to button 
    back.bind("<Button-1>", closeWindow)