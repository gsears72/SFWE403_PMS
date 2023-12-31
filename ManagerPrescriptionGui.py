import customtkinter as ctk 
#import tkinter.messagebox as tkm
import prescriptionController as pcv
import prescriptionAddView as pav
import prescriptionFillView as pfv

from datetime import date
from datetime import timedelta
from datetime import datetime

def open_PrescriptionManagerGUI(priorWindow):
    # Selecting GUI theme - dark, light , system (for system default) 
    ctk.set_appearance_mode("dark") 
        
    # Selecting color theme - blue, green, dark-blue 
    ctk.set_default_color_theme("blue") 

    app = ctk.CTkToplevel() 
    app.geometry("800x600")
    app.minsize(800, 600)
    app.maxsize(800, 600)
    app.title("Prescription Managment")

    def closeWindow():
        priorWindow.deiconify()
        app.destroy()

    presHome = ctk.CTkButton(
        master = app,
        width=75,
        height = 50,
        text = "Back",
        command = closeWindow
    )
    presHome.grid(row = 0, column = 2)

    label = ctk.CTkLabel(app,text = "Precription Managment Screen")
    label.grid(row = 0, column = 1)

    app.columnconfigure(0, weight = 0)
    app.columnconfigure(1, weight = 0)
    app.columnconfigure(2, weight = 0)

    app.rowconfigure(1, weight = 0)
    app.rowconfigure(2, weight = 0)
    app.rowconfigure(3, weight = 0)
    app.rowconfigure(4, weight = 0)
    app.rowconfigure(5, weight = 0)
    app.rowconfigure(6, weight = 0)
    app.rowconfigure(7, weight = 0)
    app.rowconfigure(8, weight = 0)
    app.rowconfigure(9, weight = 0)
    app.rowconfigure(10, weight = 0)
    app.rowconfigure(11, weight = 0)
    app.rowconfigure(12, weight = 0)
    app.rowconfigure(13, weight = 0)

    def temp_text1(e):
        firstName.delete(0, "end")

    def temp_text2(e):
        lastName.delete(0, "end")

    firstName = ctk.CTkEntry(master=app)
    lastName = ctk.CTkEntry(master=app)
    firstName.grid(row = 1, column = 1)
    firstName.insert(0, "Input First Name")
    lastName.grid(row = 2, column = 1)
    lastName.insert(0,"Input Last Name")

    def OpenAddWindow():
        fName = firstName.get()
        lName = lastName.get()
        pav.open_AddPrescription(app, fName, lName)
        app.withdraw()

    firstName.bind("<FocusIn>", temp_text1)
    lastName.bind("<FocusIn>", temp_text2)

    AddPrescriptionButton = ctk.CTkButton(
        text="Add Prescription",
        width = 150,
        height = 100,
        master = app,
        command = OpenAddWindow
    )

    AddPrescriptionButton.grid(row = 4, column = 0, pady = 20, padx = 20)
    

   