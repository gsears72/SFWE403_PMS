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


def rolecallback(choice):
  return choice   
    
def open_addStaffView(ManagerHome):
    # Selecting GUI theme - dark, light , system (for system default) 
    tk.set_appearance_mode("dark") 
        
    # Selecting color theme - blue, green, dark-blue 
    tk.set_default_color_theme("blue") 

    #staff = Staff.User()
    #manager = Staff.PharmacyManager("test")

    window = tk.CTkToplevel()
    window.geometry("500x500") 
    window.title("Add Staff") 

    window.columnconfigure(0, weight = 0)
    window.columnconfigure(1, weight = 2)
    window.rowconfigure(0, weight = 2)
    window.rowconfigure(1, weight = 0)
    window.rowconfigure(2, weight = 0)
    window.rowconfigure(3, weight = 0)
    window.rowconfigure(4, weight = 0)
    window.rowconfigure(5, weight = 0)
    window.rowconfigure(6, weight = 0)
    window.rowconfigure(7, weight = 0)
    window.rowconfigure(8, weight = 0)
    window.rowconfigure(9, weight = 0)

    # frame = tk.CTkFrame(master=window) 
    # frame.pack(pady=20,padx=40,fill='both',expand=True) 

    button = tk.CTkButton(
        master=window,
        text="Add Staff",
        width=200,
        height=50,
        # bg="blue",
        # fg="yellow",
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
    label = tk.CTkLabel(master=window,text="Add Staff", font=("Fira Code", 25)) 
    label1 = tk.CTkLabel(master=window,text="Full Name") 
    label2 = tk.CTkLabel(master=window,text="Role") 
    label3 = tk.CTkLabel(master=window,text="Password") 
    label4 = tk.CTkLabel(master=window,text="High School") 

    success = tk.CTkLabel(master=window,text="Successfully Added!")  
    failure = tk.CTkLabel(master=window,text="Failed to Add!") 

    #These are the input fields
    fullNameIn = tk.CTkEntry(master=window, width=300)
    roleIn = tk.CTkComboBox(master=window,
                                     values=['manager', 'pharmacist', 'technician', 'cashier'],
                                     command=rolecallback)
    roleIn.set("cashier")
    passwordIn = tk.CTkEntry(master=window, width=300)
    highSchoolIn = tk.CTkEntry(master=window, width=300)

    #this adds inputs to window
    label.grid(columnspan=2, row=0, padx=5, pady=5)
    label1.grid(column=0, row=1, padx=5, pady=5)
    fullNameIn.grid(column=1, row=1, padx=5, pady=5) 
    label2.grid(column=0, row=2, padx=5, pady=5)
    roleIn.grid(column=1, row=2, padx=5, pady=5) 
    label3.grid(column=0, row=3, padx=5, pady=5)
    passwordIn.grid(column=1, row=3, padx=5, pady=5)
    label4.grid(column=0, row=4, padx=5, pady=5) 
    highSchoolIn.grid(column=1, row=4, padx=5, pady=5) 
    button.grid(columnspan=2, row=8, padx=5, pady=5)
    back.grid(columnspan=2, row=9, padx=5, pady=5)

    def handle_click(event): 
        # this gets info from input and puts into class
        fullName = fullNameIn.get()
        role = roleIn.get()
        password = passwordIn.get()
        highSchool = highSchoolIn.get()

        #this adds the staff to database and checks if it worked
        if (role == "manager"):
            mycursor.execute("INSERT INTO PMS_Staff (role, name, password, highschool) VALUES (%s, %s, %s, %s)", (role, fullName, password, highSchool))
            mydb.commit()
            failure.grid_remove() #removes from screen
            success.grid(columnspan=2, row=9, padx=5, pady=5) #adds to screen 
            #clears input fields
            clear_text(fullNameIn)
            clear_text(passwordIn)
            clear_text(highSchoolIn)


        elif (role == "pharmacist"):
            mycursor.execute("INSERT INTO PMS_Staff (role, name, password, highschool) VALUES (%s, %s, %s, %s)", (role, fullName, password, highSchool))
            mydb.commit()
            failure.grid_remove() #removes from screen
            success.grid(columnspan=2, row=9, padx=5, pady=5) #adds to screen 
            #clears input fields
            clear_text(fullNameIn)
            clear_text(passwordIn)
            clear_text(highSchoolIn)

        elif (role == "technician"):
            mycursor.execute("INSERT INTO PMS_Staff (role, name, password, highschool) VALUES (%s, %s, %s, %s)", (role, fullName, password, highSchool))
            mydb.commit()
            failure.grid_remove() #removes from screen
            success.grid(columnspan=2, row=9, padx=5, pady=5) #adds to screen 
            #clears input fields
            clear_text(fullNameIn)
            clear_text(passwordIn)
            clear_text(highSchoolIn)

        elif (role == "cashier"):
            mycursor.execute("INSERT INTO PMS_Staff (role, name, password, highschool) VALUES (%s, %s, %s, %s)", (role, fullName, password, highSchool))
            mydb.commit()
            failure.grid_remove() #removes from screen
            success.grid(columnspan=2, row=9, padx=5, pady=5) #adds to screen 
            #clears input fields
            clear_text(fullNameIn)
            clear_text(passwordIn)
            clear_text(highSchoolIn)

        else:
            success.grid_remove()
            failure.grid(columnspan=2, row=9, padx=5, pady=5)

    def closeWindow(self):
        ManagerHome.deiconify()
        window.destroy()

    def clear_text(text):
        text.delete(0, tk.END)

    button.bind("<Button-1>", handle_click) #connects function handle_click to button 
    back.bind("<Button-1>", closeWindow)

#window.mainloop() #constant loop for gui