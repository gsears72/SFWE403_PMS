import customtkinter as tk  
import mysql.connector


def open_recoverAccountView(priorWindow):
    mydb = mysql.connector.connect(
            host = 'mysql-145311-0.cloudclusters.net',
            port = '18166',
            user = 'admin',
            passwd = 'FcCZds4d',
            db = 'PMS'
        )

    mycursor = mydb.cursor()    

    def clear_text(text):
            text.delete(0, tk.END)

    def recoverAccount():
        id = 0
        user = nameIn.get() 
        mycursor.execute("SELECT lockout from PMS_Staff WHERE name = %s and StaffID > %s", (user, id))
        locked = mycursor.fetchone()
        locked = locked[0]
        if locked == 1:
            locked = 0
            mycursor.execute("UPDATE PMS_Staff SET lockout = %s WHERE name = %s", (locked, user))
            success.grid(row = 30, column = 200, padx = 10, pady = 10)
            mydb.commit()
            
        else:
            success.grid(row = 30, column = 200, padx = 10, pady = 10)
            clear_text(nameIn)

    # Selecting GUI theme - dark, light , system (for system default) 
    tk.set_appearance_mode("dark") 
  
    # Selecting color theme - blue, green, dark-blue 
    tk.set_default_color_theme("blue") 

    window = tk.CTkToplevel()
    window.geometry("800x600")
    window.minsize(800, 600)
    window.maxsize(800, 600)
    window.title("Recover Account")

    def closeWindow():
        priorWindow.deiconify()
        window.destroy()

    recoverButton = tk.CTkButton(
        master = window, 
        text = "Load User",
        command = recoverAccount
    )

    back = tk.CTkButton(
        master = window, 
        text = "Back",
        command = closeWindow
    )


    label = tk.CTkLabel(master = window, text = "What is the first and last name of the user you wish to recover?")
    success = tk.CTkLabel(master = window, text = "Successfully Recovered!")

    nameIn = tk.CTkEntry(master = window, width = 300)

    label.grid(row = 0, column = 200, padx = 10, pady = 10)
    nameIn.grid(row = 10, column = 200, padx = 10, pady = 10)
    recoverButton.grid(row = 20, column = 200, padx = 10, pady = 10)
    back.grid(row = 30, column = 200, padx = 10, pady =10)

#window.mainloop()
