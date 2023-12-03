import customtkinter as tk
import models.Staff as Staff
from models.Staff import PharmacyManager
from models.Staff import Pharmacist
from models.Staff import PharmacistTechnician
from models.Staff import Cashier
import mysql.connector

mydb = mysql.connector.connect(
        host = 'mysql-145311-0.cloudclusters.net',
        port = '18166',
        user = 'admin',
        passwd = 'FcCZds4d',
        db = 'PMS'
    )

mycursor = mydb.cursor()

def open_updateStaffView(ManagerHome):
    # Selecting GUI theme - dark, light , system (for system default) 
    tk.set_appearance_mode("dark") 
    
    # Selecting color theme - blue, green, dark-blue 
    tk.set_default_color_theme("blue") 

    #staff = Staff.User()
    manager = Staff.PharmacyManager()

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

    back = tk.CTkButton(
        master=window,
        text="Go Back",
        width=200,
        height=50,
        # bg="blue",
        # fg="yellow",
    )

    # labels are text
    label = tk.CTkLabel(master=window,text="Full Name")
    label1 = tk.CTkLabel(master=window,text="Staff ID")
    label2 = tk.CTkLabel(master=window,text="Role")
    label3 = tk.CTkLabel(master=window,text="Password")
    label4 = tk.CTkLabel(master=window,text="High School")

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
    back.grid(columnspan=2, row=12, padx=5, pady=5)

    def load(event):
        nameOriginal = fullNameIn.get()

        try:
            failure.grid_remove()

            staffInfo = manager.fetchStaff(nameOriginal)
            
            staffIDIn.insert(0, staffInfo[0][0])
            roleIn.insert(0, staffInfo[0][2]) 
            passwordIn.insert(0, staffInfo[0][3])
            highSchoolIn.insert(0, staffInfo[0][5])
            lockoutIn.insert(0, staffInfo[0][4])
            strikeCountIn.insert(0, staffInfo[0][6])

            button2.destroy()
            fullNameIn.grid(columnspan=2, row=2, padx=5, pady=5)
            #label1.grid(columnspan=2, row=3, padx=5, pady=5)
            #staffIDIn.grid(columnspan=2, row=4, padx=5, pady=5) 
            label2.grid(columnspan=2, row=5, padx=5, pady=5)
            roleIn.grid(columnspan=2, row=6, padx=5, pady=5) 
            label3.grid(columnspan=2, row=7, padx=5, pady=5)
            passwordIn.grid(columnspan=2, row=8, padx=5, pady=5) 
            label4.grid(columnspan=2, row=9, padx=5, pady=5)
            highSchoolIn.grid(columnspan=2, row=10, padx=5, pady=5) 
            button.grid(columnspan=2, row=11, padx=7, pady=5)


        except Exception as e:
            failure.grid(columnspan=2, row=3, padx=5, pady=5) 
            print(e)

    def update(event): 
        # this gets info from input and puts into class
        name = fullNameIn.get()
        StaffID = staffIDIn.get()
        role = roleIn.get()
        password = passwordIn.get()
        highschool = highSchoolIn.get()
        lockout = lockoutIn.get()
        strikecount = strikeCountIn.get()

        #this adds the customer to database and checks if it worked
        try:
            mycursor.execute("UPDATE PMS_Staff set StaffID = %s, name = %s, role = %s, password = %s, lockout = %s, highschool = %s, strikecount = %s where StaffID = %s",(StaffID, name, role, password, lockout, highschool, strikecount, StaffID))
            mydb.commit()
            
            failure.grid_remove() #removes from screen
            success.grid(columnspan=2, row=13, padx=5, pady=5)  #adds to screen 
            #clears input fields
            clear_text(fullNameIn)
            clear_text(staffIDIn)
            clear_text(roleIn)
            clear_text(passwordIn)
            clear_text(highSchoolIn)
            clear_text(lockoutIn)
            clear_text(strikeCountIn)

        except Exception as e:
            success.grid_remove()
            failure.grid(columnspan=2, row=13, padx=5, pady=5) 
            print(e)

    def clear_text(text):
        text.delete(0, tk.END)

    def closeWindow(self):
        ManagerHome.deiconify()
        window.destroy()

    button.bind("<Button-1>", update) #connects function handle_click to button 
    button2.bind("<Button-1>", load)
    back.bind("<Button-1>", closeWindow)

#window.mainloop() #constant loop for gui 
