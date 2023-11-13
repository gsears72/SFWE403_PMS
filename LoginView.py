
import customtkinter as ctk 
import CashierGUI as cgui
from models.Staff import User
from tkinter import messagebox


from models.Login import LoginLib
from controllers.LoginController import *

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")


class LoginGUI(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("400x320")
        self.title("PMS Login")
        self.currentPassword = ""
        self.currentId = 0
        self.frame = ctk.CTkFrame(self) 
        self.frame.pack(pady=20,padx=40,fill='both',expand=True) 
        
        self.label = ctk.CTkLabel(self.frame,text='PMS Login System') 
        self.label.pack(pady=12,padx=10)

        def clear_text(text, text2, text3):
            text.delete(0, ctk.END)
            text2.delete(0, ctk.END)
            text3.delete(0, ctk.END)
        
        def loginstrike():
            Loginstrike(self.user_entry.get())
            
        def loginlogic():
            #logindata = LoginLib( UserID = self.user_entry.get(self), Password = self.user_pass.get(self))
            id = self.user_entry.get()
            password = self.user_pass.get()
            secret = self.user_secret.get()
            result = Login(id,password,secret)
            ################################
            currentId = result[0]
            currentPassword = result[3]
            ################################################################
            if result != None and result[4] == 0 :
                Resetstrike(id)
                #write code here
                match result[2]:
                    case "manager":
                        clear_text(self.user_entry, self.user_pass, self.user_secret)
                        messagebox.showinfo("Success","Login Successful")
                        #load manager gui
                    case "pharmacist":
                        clear_text(self.user_entry, self.user_pass, self.user_secret)
                        #load pharmacist gui
                    case "cashier": #load cashier gui
                        clear_text(self.user_entry, self.user_pass, self.user_secret)
                        cgui.open_cashierView(app, currentId, currentPassword)
                        app.withdraw()
                    case "technitian":
                        clear_text(self.user_entry, self.user_pass, self.user_secret)
                #messagebox.showinfo("Success","Login Successful")
                return result[2]
            elif result == None:
                loginstrike()
                messagebox.showinfo("Failed","Login Failed, please check ID, Password, or Secret")
            elif result[4] == 1:
                messagebox.showinfo("Lock Out","This account has been Lock, Please contact a manager")
                  
        self.user_entry= ctk.CTkEntry(self.frame,placeholder_text="User ID") 
        self.user_entry.pack(pady=12,padx=10) 
        
        self.user_pass= ctk.CTkEntry(self.frame,placeholder_text="Password",show="*") 
        self.user_pass.pack(pady=12,padx=10)
        
        self.user_secret= ctk.CTkEntry(self.frame,placeholder_text="Secret",show="*") 
        self.user_secret.pack(pady=12,padx=10)
               
        self.button = ctk.CTkButton(self.frame,text='Login',command=loginlogic) 
        self.button.pack(pady=12,padx=10) 
        
        
if __name__=='__main__':
    app = LoginGUI()
    app.mainloop()
        