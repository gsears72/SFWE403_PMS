import customtkinter as tk
from models.Staff import User
from models.Staff import PharmacyManager

def open_passView(oldWindow, currentId, currentPassword):
    # Selecting GUI theme - dark, light , system (for system default) 
    tk.set_appearance_mode("dark") 
    
    # Selecting color theme - blue, green, dark-blue 
    tk.set_default_color_theme("blue") 

    user = PharmacyManager("test")

    window = tk.CTkToplevel()
    window.geometry("500x500") 
    window.title("Update Customer") 

    window.columnconfigure(0, weight = 0)
    window.columnconfigure(1, weight = 2)
    window.rowconfigure(0, weight = 2)
    window.rowconfigure(1, weight = 0)
    window.rowconfigure(2, weight = 0)
    window.rowconfigure(3, weight = 0)
    window.rowconfigure(4, weight = 0)
    window.rowconfigure(5, weight = 0)

    label = tk.CTkLabel(master=window,text="current password") 
    label1 = tk.CTkLabel(master=window,text="Change Password", font=("Fira Code", 25)) 
    label2 = tk.CTkLabel(master=window,text="new password") 
    label3 = tk.CTkLabel(master=window,text="new password again") 

    success = tk.CTkLabel(master=window,text="Successfully Changed!")  
    failure = tk.CTkLabel(master=window,text="Failed to Change!") 
    failure2 = tk.CTkLabel(master=window,text="password is incorrect") 
    failure3 = tk.CTkLabel(master=window,text="passwords do not match or password") 

    pass1 = tk.CTkEntry(master=window, width=300)
    pass2 = tk.CTkEntry(master=window, width=300)
    newPass = tk.CTkEntry(master=window, width=300)

    button = tk.CTkButton(
        master=window,
        text="Save Password",
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

    label1.grid(columnspan=2, row=0, padx=2, pady=2)
    label.grid(column=0, row=1, padx=5, pady=5)
    label2.grid(column=0, row=2, padx=5, pady=5)
    label3.grid(column=0, row=3, padx=5, pady=5)

    pass1.grid(column=1, row=1, padx=5, pady=5)
    pass2.grid(column=1, row=2, padx=5, pady=5)
    newPass.grid(column=1, row=3, padx=5, pady=5)

    button.grid(column=1, row=4, padx=5, pady=5)
    back.grid(column=0, row=4, padx=5, pady=5)

    def handle_click(event): 
        valid = False
        matches = False
        passwordIn = newPass.get()
        old1 = pass1.get()
        new2 = pass2.get()
        new = newPass.get()
        if (old1 == currentPassword): #old password is correct
            valid = True
        else:
            valid = False

        if (new2 == new): #new passwords match
            matches = True
        else:
            matches = False
        
        if (valid and matches):
            test = user.changePassword(passwordIn, currentId)
            if test:
                failure.grid_remove() #removes from screen
                failure2.grid_remove()
                failure3.grid_remove()
                success.grid(columnspan=2, row=5, padx=5, pady=5) #adds to screen 
                #clears input fields
                clear_text(newPass)
                clear_text(pass1)
                clear_text(pass2)
            else:
                success.grid_remove()
                failure2.grid_remove()
                failure3.grid_remove()
                clear_text(newPass)
                clear_text(pass1)
                clear_text(pass2)
                failure.grid(columnspan=2, row=5, padx=5, pady=5) 
        elif (valid):
            success.grid_remove()
            failure.grid_remove()
            failure2.grid_remove()
            clear_text(newPass)
            clear_text(pass1)
            clear_text(pass2)
            failure3.grid(columnspan=2, row=5, padx=5, pady=5)
        else:
            success.grid_remove()
            failure.grid_remove()
            failure3.grid_remove()
            clear_text(newPass)
            clear_text(pass1)
            clear_text(pass2)
            failure2.grid(columnspan=2, row=5, padx=5, pady=5)

    def clear_text(text):
        text.delete(0, tk.END)

    def closeWindow(self):
        oldWindow.deiconify()
        window.destroy()

    button.bind("<Button-1>", handle_click) #connects function handle_click to button 
    back.bind("<Button-1>", closeWindow)
