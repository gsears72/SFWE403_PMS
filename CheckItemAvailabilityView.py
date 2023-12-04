import customtkinter as tk
from models.Medicine import Medicine
from models.Staff import PharmacyManager

def open_CheckItemAvailability(app):
    # Selecting GUI theme - dark, light , system (for system default) 
    tk.set_appearance_mode("dark") 

    # Selecting color theme - blue, green, dark-blue 
    tk.set_default_color_theme("blue") 


    medicine = Medicine()
    manager = PharmacyManager()

    window = tk.CTkToplevel()
    window.geometry("500x500") 
    window.title("Check Item Availability") 

    button = tk.CTkButton(
        text="Search",
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
    label = tk.CTkLabel(master = window,text="Search what item's availability you would like to check? (name batchnum)") 
    
    failure = tk.CTkLabel(master = window,text="Item is not available") 
    #These are the input fields
    nameIn = tk.CTkEntry(master = window, width=300)

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
        isAvailable, quantity = manager.checkAvailability(medicine)
       
        if isAvailable:
            failure.pack_forget() #removes from screen  #adds to screen 
            #clears input fields
            clear_text(nameIn)
            quantity = str(quantity).replace(',', '')
            output = "It is available! The pharmacy has " + str(quantity) + " units of " + str(medicine.name)
            success = tk.CTkLabel(master = window,text=output)  
            success.pack(pady = 20)
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
    #window.mainloop() #constant loop for gui 
