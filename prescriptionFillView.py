import customtkinter as ctk
import prescriptionController as pcv
import mysql.connector
import time

mydb = mysql.connector.connect(
        host = 'mysql-145311-0.cloudclusters.net',
        port = '18166',
        user = 'admin',
        passwd = 'FcCZds4d',
        db = 'PMS'
    )
mycursor = mydb.cursor()

def open_FillPrescription(priorWindow, fName, lName):
        # Selecting GUI theme - dark, light , system (for system default) 
        ctk.set_appearance_mode("dark") 
            
        # Selecting color theme - blue, green, dark-blue 
        ctk.set_default_color_theme("blue") 

        app = ctk.CTkToplevel() 
        app.geometry("800x600")
        app.minsize(800, 600)
        app.maxsize(800, 600)
        app.title("Prescription Managment")

        def open_fill2():
            
            app.geometry("500x500")
            customerDOBb.grid_forget()
            presConfirm1.grid_forget()

            #Prescription ID
            presIDb.grid(row = 1, column = 1)

            #CustomerID
            customerIDb.grid(row = 4, column = 1)

            #prescription Start
            presStartb.grid(row = 5, column = 1)

            #prescription End        
            presEndb.grid(row = 6, column = 1)

            #prescription Medication
            presMedb.grid(row = 7, column = 1)
            
            #prescription Quantitiy    
            PresNumb.grid(row = 8, column = 1)
        
            #prescription Strength
            PresStrb.grid(row = 9, column = 1)

            #prescription Refills
            PresRefilb.grid(row = 10, column = 1)

            #prescritpion Instructions
            PresInstrb.grid(row = 11, column = 1)

            #Prescription Doctor
            PresDocb.grid(row = 12, column = 1)

            
            presGCon.grid(row = 13, column = 0)
    
        def check1():
            #display current number to grab
            app.geometry("500x500")
            firstName.grid_forget()
            lastName.grid_forget()
            presGCon.grid_forget()
            presIDb.grid_forget()
            customerIDb.grid_forget()
            presStartb.grid_forget()
            presEndb.grid_forget()
            presMedb.grid_forget()
            PresNumb.grid_forget()
            PresStrb.grid_forget()
            PresRefilb.grid_forget()
            PresInstrb.grid_forget()
            PresDocb.grid_forget()
            label2.grid_forget()
            
            presGLabel = ctk.CTkLabel(master = app, textvariable = PresNum)
            presGLabel.grid(row = 0, column = 0)
            presGLabel2 = ctk.CTkLabel(master = app, text = "How many pills did you grab:")
            presGLabel2.grid(row = 1, column = 0)
            
            presGrabbed.grid(row = 2, column = 1)

            presGCon2.grid(row = 3, column = 0)
            #presIDb.grid_forget()
            #customerIDb.grid_forget()
            #presStartb.grid_forget()

        def check2():
            presGCon2.grid_forget
            textback = ctk.StringVar()
            correct = ctk.CTkLabel(master = app, textvariable = textback)
            amountGrabbed = int(presGrabbed.get())
            if(amountGrabbed == PresNum.get()):
                textback.set("Correct Number Grabbed")
                presGCon.grid_forget()
                correct.grid(row = 3, column = 1)
                pcv.fillfinal(grabbedPrescription[0][4], grabbedPrescription[0][7])
            elif(amountGrabbed > PresNum.get()):
                textback.set("Too Many Grabbed")
                correct.grid(row = 3, column = 1)
                time.sleep(3)
                open_fill2
            else:
                textback.set("Too Few grabbed")
                correct.grid(row = 3, column = 1)
                time.sleep(3)
                open_fill2
            priorWindow.deiConify()
            app.destroy()


        app.geometry("500x400")

        amountText = ctk.StringVar()
        firstN = ctk.StringVar()
        lastN = ctk.StringVar()
        customerDOB = ctk.StringVar()
        customerID = ctk.IntVar()
        presStart = ctk.StringVar()
        presEnd = ctk.StringVar()
        presID = ctk.StringVar()
        PresMed = ctk.StringVar()
        PresNum = ctk.IntVar()
        PresStr = ctk.StringVar()
        PresRefil = ctk.StringVar()
        PresInstr = ctk.StringVar()
        PresDoc = ctk.StringVar()
        amountGrabbed = 0
        
        presGrabbed = ctk.CTkEntry(master = app)
        
        #firstN.set(fName)
        CustomerFirst = fName
        CustomerLast = lName

        label2 = ctk.CTkLabel(master=app, text = "Is this the correct Prescription")
        label2.grid(row = 0, column = 0)

        try:
            #search for the prescription SELECT * FROM PMS.PMS_Prescription where prescription = 1111111
            mycursor.execute("SELECT * FROM Customer WHERE firstName = %s and lastName = %s", (CustomerFirst, CustomerLast))
            grabbedCustomers = mycursor.fetchone() #make sure fetchall() might cause error
            #When found the prescription print the information regarding the prescription for confirmation
                
        except Exception as e:
            print(e)

        firstN.set(grabbedCustomers[1])
        lastN.set(grabbedCustomers[2])
        customerDOB.set(str(grabbedCustomers[3]))

        CustomerID=int(grabbedCustomers[0])
        customerID.set(CustomerID)

        mycursor.execute("SELECT * FROM PMS_Prescription WHERE CustomerID = %s", (CustomerID,))
        grabbedPrescription = mycursor.fetchall() #make sure fetchall() might cause error

        
        presID.set(grabbedPrescription[0][0])
        presIDb = ctk.CTkLabel(master = app, textvariable = presID)
        customerIDb = ctk.CTkLabel(master = app, textvariable=customerID)
        presStart.set(grabbedPrescription[0][2])
        presStartb = ctk.CTkLabel(master = app, textvariable = presStart)
        presEnd.set(grabbedPrescription[0][3])
        presEndb = ctk.CTkLabel(master = app, textvariable = presEnd)
        PresMed.set(grabbedPrescription[0][4])
        presMedb = ctk.CTkLabel(master = app, textvariable = PresMed)
        PresNum.set(int(grabbedPrescription[0][5]))
        PresNumb = ctk.CTkLabel(master = app, textvariable = PresNum)
        PresStr.set(grabbedPrescription[0][6])
        PresStrb = ctk.CTkLabel(master = app, textvariable = PresStr)
        PresRefil.set(grabbedPrescription[0][7])
        PresRefilb = ctk.CTkLabel(master = app, textvariable = PresRefil)
        PresInstr.set(grabbedPrescription[0][8])
        PresInstrb = ctk.CTkLabel(master = app, textvariable = PresInstr)
        PresDoc.set(grabbedPrescription[0][9])
        PresDocb = ctk.CTkLabel(master = app, textvariable = PresDoc)
        
        firstName = ctk.CTkEntry(master=app)
        lastName = ctk.CTkEntry(master=app)
        firstName.grid(row = 1, column = 1)
        firstName.insert(0, fName)
        lastName.grid(row = 2, column = 1)
        lastName.insert(0, lName)

        firstName.configure(state="disabled") #prevents editing in the first name/ last name when in the add prescription GUI
        lastName.configure(state ="disabled")
        
        firstName.grid(row = 2, column = 1)
        firstName.configure(state = "disabled")
        lastName.grid(row = 3, column = 1)
        lastName.configure(state = "disabled")

        customerDOBb = ctk.CTkLabel(master = app, textvariable = customerDOB)
        customerDOBb.grid(row = 4, column = 1)
        #customerDOBb.insert(0, textvariable =customerDOB)
        #PCV.Open_Fill_PrescriptionView()
        #app.withdraw()

        presGCon = ctk.CTkButton(
                master = app,
                width=150,
                height = 100,
                text = "Correct Prescription",
                command = check1
            )
        
        presGCon2 = ctk.CTkButton(
                master = app,
                width=150,
                height = 100,
                text = "Next",
                command = check2
            )
        
        presConfirm1 = ctk.CTkButton(
            master = app,
            text = "Correct Customer",
            width = 150,
            height = 100,
            command = open_fill2
            )
        
        presConfirm1.grid(row = 13, column = 0)