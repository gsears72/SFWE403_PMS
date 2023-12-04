import customtkinter as ctk
import prescriptionController as pcv
import mysql.connector

mydb = mysql.connector.connect(
        host = 'mysql-145311-0.cloudclusters.net',
        port = '18166',
        user = 'admin',
        passwd = 'FcCZds4d',
        db = 'PMS'
    )
mycursor = mydb.cursor()

def open_AddPrescription(priorWindow, firstN, lastN):
        #Selecting GUI theme - dark, light , system (for system default) 
        ctk.set_appearance_mode("dark") 
            
        # Selecting color theme - blue, green, dark-blue 
        ctk.set_default_color_theme("blue") 

        window = ctk.CTkToplevel()
        window.geometry("800x600")
        window.minsize(800, 600)
        window.maxsize(800, 600) 
        window.title("Add Prescription") 
            
        firstName = ctk.CTkEntry(master=window)
        lastName = ctk.CTkEntry(master=window)
        firstName.grid(row = 1, column = 1)
        firstName.insert(0, firstN)
        lastName.grid(row = 2, column = 1)
        lastName.insert(0, lastN)

        def temp_text4(e):
            presStart.delete(0, "end")

        def temp_text5(e):
            presEnd.delete(0,"end")

        def temp_text6(e):
            presMed.delete(0, "end")

        def temp_text7(e):
            presNum.delete(0, "end")

        def temp_text8(e):
            presStr.delete(0, "end")

        def temp_text9(e):
            presRefil.delete(0, "end")

        def temp_text10(e):
            presInstruction.delete(0, "end")

        def temp_text11(e):
            presDoc.delete(0, "end")

        def addPresFinal():
            #Confirm that the medications exist, if yes continue if not make an error message and end
            psd = presStart.get()
            ped = presEnd.get()
            pmn = presMed.get()
            pq = presNum.get()
            ps = presStr.get()
            pr = presRefil.get()
            pi = presInstruction.get()
            pdn = presDoc.get()
            print( firstN, lastN, psd, ped, pmn, pq, ps, pr, pi, pdn)#send all variables above to add prescription call
            #cusID, startDate, endDate, medication, quantity, strength, refills, instruct, prescriber
            pcv.addfinal(cusIDt, psd, ped, pmn, pq, ps, pr, pi, pdn)
            priorWindow.deiconify()
            window.destroy()

        def closeWindow():
            priorWindow.deiconify()
            window.destroy()

        firstName.configure(state="disabled") #prevents editing in the first name/ last name when in the add prescription GUI
        lastName.configure(state ="disabled")
        
        label1 = ctk.CTkLabel(master=window, text = "Adding Prescription") #new label for this function
        label1.grid(row = 0, column = 0, padx = 10)
        

        #prescription ID
        # presID = ctk.CTkEntry(master=app)
        # presID.grid(row = 1, column = 1)
        # presID.insert(0, "Enter ID")
        # presID.bind("<FocusIn>", temp_text3)
        
        
        #Name Fields
        firstName.grid(row = 2, column = 1) #move them down so text fields align
        lastName.grid(row = 3, column = 1)
        
        #get Customer ID, put it in an entry field and disable editing

        cusID = ctk.CTkEntry(master = window)
        cusID.grid(row = 4, column = 1)
        
        try:
            mycursor.execute("SELECT * FROM Customer WHERE firstName = %s and lastName = %s", (firstN, lastN))
            grabbedCustomers = mycursor.fetchone() #make sure fetchall() might cause error
            cusIDt = grabbedCustomers[0]
            cusID.insert(0,cusIDt)
            cusID.configure(state = "disabled")
        except Exception as e:
            print(e)
        #prescription Start Date
        presStart = ctk.CTkEntry(master = window)
        presStart.grid(row = 5, column = 1)
        presStart.insert(0, "Enter Start Date(YYYY/MM/DD)")
        presStart.bind("<FocusIn>", temp_text4)
            #Create a remove func


        #prescription End Date
        presEnd = ctk.CTkEntry(master = window)
        presEnd.grid(row = 6, column = 1)
        presEnd.insert(0, "Enter End Date(YYYY/MM/DD)")
        presEnd.bind("<FocusIn>", temp_text5)
            #Create a remove func

        
        #prescription Medication
        presMed = ctk.CTkEntry(master = window)
        presMed.grid(row = 7, column = 1)
        presMed.insert(0, "Enter Name")
        presMed.bind("<FocusIn>", temp_text6)
            #Create a remove func
        
        #prescription Quantity
        presNum = ctk.CTkEntry(master = window)
        presNum.grid(row = 8, column = 1)
        presNum.insert(0, "Enter Quantity")
        presNum.bind("<FocusIn>", temp_text7)
            #CREATE A REMOVE FUNC
        
        #prescriptionStrength
        presStr = ctk.CTkEntry(master=window)
        presStr.grid(row = 9, column = 1)
        presStr.insert(0, "Enter Strength")
        presStr.bind("<FocusIn>", temp_text8)
            #CREATE A REMOVE FUNC

    #prescriptionRefills
        presRefil = ctk.CTkEntry(master=window)
        presRefil.grid(row = 10, column = 1)
        presRefil.insert(0, "Number of Refills")
        presRefil.bind("<FocusIn>", temp_text9)
            #Create a remove func

    #Instructions
        presInstruction = ctk.CTkEntry(master=window)
        presInstruction.grid(row=11, column = 1)
        presInstruction.insert(0, "Instructions")
        presInstruction.bind("<FocusIn>", temp_text10)
            #Text Wraping here
            
        #Pharmacist/Doctor Name
        presDoc = ctk.CTkEntry(master = window)
        presDoc.grid(row = 12, column =1)
        presDoc.insert(0, "Doctor's Name")
        presDoc.bind("<FocusIn>", temp_text11)
            #Create the remove function

        #Confirm and Deny Button
        confirmationB = ctk.CTkButton(master = window, text = "Add Prescription", width = 100, height = 20, command = addPresFinal)
        confirmationB.grid(row = 5, column = 2)
        denyB = ctk.CTkButton(master = window, text = "Cancel", width = 100, height = 20, command = closeWindow)
        denyB.grid(row = 10, column = 2)
        
        #PCV.Open_Add_Prescription(firstName, lastName)
        