import customtkinter as tk
import models.Staff as Staff
from models.Staff import PharmacyManager
from models.Staff import Pharmacist
from models.Staff import PharmacistTechnician
from models.Staff import Cashier


def open_deleteStaffView():
    # Selecting GUI theme - dark, light , system (for system default) 
    tk.set_appearance_mode("dark") 
    
    # Selecting color theme - blue, green, dark-blue 
    tk.set_default_color_theme("blue") 

    staff = Staff.User()
    manager = Staff.PharmacyManager("test")

    window = tk.CTkToplevel()
    window.geometry("500x500") 
    window.title("Remove Staff") 

    button = tk.CTkButton(
        text="Delete",
        width=200,
        height=50,
        font = ("Fira Code", 15),
        master = window
    )
    # labels are text
    label = tk.CTkLabel(master = window,text="What staff would you like to remove? (full name:[first last])") 

    success = tk.CTkLabel(master = window,text="Successfully Removed!")  
    failure = tk.CTkLabel(master = window,text="Failed to Remove!") 
    #These are the input fields
    nameIn = tk.CTkEntry(master = window, width=300)

    #this adds inputs to window
    label.pack(pady=20)
    nameIn.pack() 
    button.pack(pady = 20)

    def handle_click(event): 
        # this gets info from input and puts into class
        name = nameIn.get()

        #this removes the staff from database and checks if it worked
        test = manager.removeStaff(name)
        if test:
            failure.pack_forget() #removes from screen
            success.pack(pady = 20) #adds to screen 
            #clears input fields
            clear_text(nameIn)
        else:
            success.pack_forget()
            failure.pack(pady = 20) 

    def clear_text(text):
        text.delete(0, tk.END)

    button.bind("<Button-1>", handle_click) #connects function handle_click to button 

#window.mainloop() #constant loop for gui 