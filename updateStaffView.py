import customtkinter as tk
import models.Staff as Staff
from models.Staff import PharmacyManager
from models.Staff import Pharmacist
from models.Staff import PharmacistTechnician
from models.Staff import Cashier


def open_updateStaffView():
    # Selecting GUI theme - dark, light , system (for system default) 
    tk.set_appearance_mode("dark") 
    
    # Selecting color theme - blue, green, dark-blue 
    tk.set_default_color_theme("blue") 

    staff = Staff.User()
    manager = Staff.PharmacyManager("test")

    window = tk.CTkToplevel()
    window.geometry("500x500") 
    window.title("Update Staff") 

    window.columnconfigure(0, weight = 0)
    window.columnconfigure(1, weight = 2)
    window.rowconfigure(0, weight = 0)
    window.rowconfigure(1, weight = 0)
    window.rowconfigure(2, weight = 0)
    window.rowconfigure(3, weight = 0)
    window.rowconfigure(4, weight = 0)
    window.rowconfigure(5, weight = 0)
    window.rowconfigure(6, weight = 0)
    window.rowconfigure(7, weight = 0)
    window.rowconfigure(8, weight = 0)
    window.rowconfigure(9, weight = 0)
    window.rowconfigure(10, weight = 0)
    window.rowconfigure(11, weight = 0)

    button = tk.CTkButton(
        master=window,
        text="Update Staff",
        font=("Fira Code", 15),
        width=200,
        height=50,
    )

    button2 = tk.CTkButton(
        master=window,
        text="Load Staff",
        font=("Fira Code", 15),
        width=200,
        height=50,
    )
    # labels are text
    label = tk.CTkLabel(master=window,text="What is the full name of the staff?")
    label1 = tk.CTkLabel(master=window,text="Full Name")

    success = tk.CTkLabel(master=window,text="Successfully Added!")
    failure = tk.CTkLabel(master=window,text="Failed to Load Customer!")
    #These are the input fields
    fullNameIn = tk.CTkEntry(master=window, width=300)
    staffIDIn = tk.CTkEntry(master=window, width=300)
    roleIn = tk.CTkEntry(master=window, width=300)
    passwordIn = tk.CTkEntry(master=window, width=300)
    highSchoolIn = tk.CTkEntry(master=window, width=300)
    lockoutIn = tk.CTkEntry(master=window, width=300)
    strikeCountIn = tk.CTkEntry(master=window, width=300)

    #this adds inputs to window
    label.grid(columnspan=2, row=0, padx=5, pady=5)
    fullNameIn.grid(columnspan=2, row=1, padx=5, pady=5)
    button2.grid(columnspan=2, row=2, padx=5, pady=5)


    def load(event):
        name = fullNameIn.get()

        try:
            failure.grid_remove()

            staffInfo = manager.fetchStaff(name)
            
            fullNameIn.insert(0, staffInfo[0][2])
            staffIDIn.insert(0, staffInfo[0][1])
            roleIn.insert(0, staffInfo[0][3]) 
            passwordIn.insert(0, staffInfo[0][4])
            highSchoolIn.insert(0, staffInfo[0][5])
            lockoutIn.insert(0, staffInfo[0][6])
            strikeCountIn.insert(0, staffInfo[0][7])

            fullNameIn.grid(columnspan=2, row=3, padx=5, pady=5) 
            staffIDIn.grid(columnspan=2, row=4, padx=5, pady=5) 
            roleIn.grid(columnspan=2, row=5, padx=5, pady=5) 
            passwordIn.grid(columnspan=2, row=6, padx=5, pady=5) 
            highSchoolIn.grid(columnspan=2, row=7, padx=5, pady=5) 
            lockoutIn.grid(columnspan=2, row=8, padx=5, pady=5) 
            strikeCountIn.grid(columnspan=2, row=9, padx=5, pady=5)
            button.grid(columnspan=2, row=10, padx=5, pady=5)
        except Exception as e:
            failure.grid(columnspan=2, row=3, padx=5, pady=5) 
            print(e)

    def update(event): 
        # this gets info from input and puts into class
        staff.name = fullNameIn.get()
        staff.StaffID = staffIDIn.get()
        staff.role = roleIn.get()
        staff.password = passwordIn.get()
        staff.highschool = highSchoolIn.get()
        staff.lockout = lockoutIn.get()
        staff.strikecount = strikeCountIn.get()

        #this adds the customer to database and checks if it worked
        try:
            test = manager.UpdateStaff(staff, staff.name)
        except Exception as e:
            print(e)
        if test:
            failure.grid_remove() #removes from screen
            success.grid(columnspan=2, row=11, padx=5, pady=5)  #adds to screen 
            #clears input fields
            clear_text(fullNameIn)
            clear_text(staffIDIn)
            clear_text(roleIn)
            clear_text(passwordIn)
            clear_text(highSchoolIn)
            clear_text(lockoutIn)
            clear_text(strikeCountIn)
        else:
            success.grid_remove()
            failure.grid(columnspan=2, row=11, padx=5, pady=5) 

    def clear_text(text):
        text.delete(0, tk.END)

    button.bind("<Button-1>", update) #connects function handle_click to button 
    button2.bind("<Button-1>", load)

#window.mainloop() #constant loop for gui 
