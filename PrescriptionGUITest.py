import customtkinter as ctk 
import tkinter.messagebox as tkm
import mysql.connector
import time
import PrescriptionView as PCV
from datetime import date
from datetime import timedelta
from datetime import datetime


mydb = mysql.connector.connect(
        host = 'mysql-145311-0.cloudclusters.net',
        port = '18166',
        user = 'admin',
        passwd = 'FcCZds4d',
        db = 'PMS'
    )
mycursor = mydb.cursor()

# def open_PrescriptionGUI
# Selecting GUI theme - dark, light , system (for system default) 
ctk.set_appearance_mode("dark") 
    
# Selecting color theme - blue, green, dark-blue 
ctk.set_default_color_theme("blue") 

app = ctk.CTkToplevel() 
app.geometry("540x200") #1920x1280 is full screen
app.title("Prescription Managment")

presHome = ctk.CTkButton(
            master = app,
            width=75,
            height = 50,
            text = "Home",
            #command = home
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



#firstnamel = ctk.CTkLabel(master=app, text = "First Name")
#firstnamel.grid(row = 1, column = 0)
#lastnamel = ctk.CTkLabel(master=app, text = "Last Name")
#lastnamel.grid(row = 2, column = 0)
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

firstName.bind("<FocusIn>", temp_text1)
lastName.bind("<FocusIn>", temp_text2)

def open_AddPrescription():
    app.geometry("500x800")
    firstN = firstName.get()
    lastN = lastName.get()

    if(firstN == "Input First Name"): #if no name input clear for now, should break back to homepage
        firstName.delete(0, "end")
    if (lastN == "Input Last Name"):
        lastName.delete(0, "end")

    
    def temp_text3(e):
        presID.delete(0, "end")
    
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
        pid = presID.get()
        psd = presStart.get()
        ped = presEnd.get()
        pmn = presMed.get()
        pq = presNum.get()
        ps = presStr.get()
        pr = presRefil.get()
        pi = presInstruction.get()
        pdn = presDoc.get()
        print(pid, firstN, lastN, psd, ped, pmn, pq, ps, pr, pi, pdn)#send all variables above to add prescription call
        PCV.addfinal(pid, firstN, lastN, cusID, psd, ped, pmn, pq, ps, pr, pi, pdn)
        app.withdraw()

   
    firstName.configure(state="disabled") #prevents editing in the first name/ last name when in the add prescription GUI
    lastName.configure(state ="disabled")
    
    AddPrescriptionButton.grid_forget() #temporarily close the buttons
    FillPrescriptionButton.grid_forget()
    
    #TO DO: REINSTATE THESE BUTTONS/LABEL AFTER

    label.grid_forget() #temporarily closes the current label
    
    label1 = ctk.CTkLabel(master=app, text = "Adding Prescription") #new label for this function
    label1.grid(row = 0, column = 0, padx = 10)
    

    #prescription ID
    presID = ctk.CTkEntry(master=app)
    presID.grid(row = 1, column = 1)
    presID.insert(0, "Enter ID")
    presID.bind("<FocusIn>", temp_text3)
       
    
    #Name Fields
    firstName.grid(row = 2, column = 1) #move them down so text fields align
    lastName.grid(row = 3, column = 1)
    
    #get Customer ID, put it in an entry field and disable editing

    cusID = ctk.CTkEntry(master = app)
    cusID.grid(row = 4, column = 1)
    
    mycursor.execute("SELECT * FROM Customer WHERE firstName = %s and lastName = %s", (firstN, lastN))
    grabbedCustomers = mycursor.fetchone() #make sure fetchall() might cause error
    cusIDt = grabbedCustomers[0]
    cusID.insert(0,cusIDt)
    cusID.configure(state = "disabled")
    
    #prescription Start Date
    presStart = ctk.CTkEntry(master = app)
    presStart.grid(row = 5, column = 1)
    presStart.insert(0, "Enter Start Date(YYYY/MM/DD)")
    presStart.bind("<FocusIn>", temp_text4)
        #Create a remove func


    #prescription End Date
    presEnd = ctk.CTkEntry(master = app)
    presEnd.grid(row = 6, column = 1)
    presEnd.insert(0, "Enter End Date(YYYY/MM/DD)")
    presEnd.bind("<FocusIn>", temp_text5)
        #Create a remove func

    
    #prescription Medication
    presMed = ctk.CTkEntry(master = app)
    presMed.grid(row = 7, column = 1)
    presMed.insert(0, "Enter Name")
    presMed.bind("<FocusIn>", temp_text6)
        #Create a remove func
    
    #prescription Quantity
    presNum = ctk.CTkEntry(master = app)
    presNum.grid(row = 8, column = 1)
    presNum.insert(0, "Enter Quantity")
    presNum.bind("<FocusIn>", temp_text7)
        #CREATE A REMOVE FUNC
    
    #prescriptionStrength
    presStr = ctk.CTkEntry(master=app)
    presStr.grid(row = 9, column = 1)
    presStr.insert(0, "Enter Strength")
    presStr.bind("<FocusIn>", temp_text8)
        #CREATE A REMOVE FUNC

#prescriptionRefills
    presRefil = ctk.CTkEntry(master=app)
    presRefil.grid(row = 10, column = 1)
    presRefil.insert(0, "Number of Refills")
    presRefil.bind("<FocusIn>", temp_text9)
        #Create a remove func

#Instructions
    presInstruction = ctk.CTkEntry(master=app)
    presInstruction.grid(row=11, column = 1)
    presInstruction.insert(0, "Instructions")
    presInstruction.bind("<FocusIn>", temp_text10)
        #Text Wraping here
        
    
    #Pharmacist/Doctor Name
    presDoc = ctk.CTkEntry(master = app)
    presDoc.grid(row = 12, column =1)
    presDoc.insert(0, "Doctor's Name")
    presDoc.bind("<FocusIn>", temp_text11)
        #Create the remove function

    #Confirm and Deny Button
    confirmationB = ctk.CTkButton(master = app, text = "Add Prescription", width = 100, height = 20, command = addPresFinal)
    confirmationB.grid(row = 5, column = 2)
    denyB = ctk.CTkButton(master = app, text = "Cancel", width = 100, height = 20)
    denyB.grid(row = 10, column = 2)
    
    
    
    
    #PCV.Open_Add_Prescription(firstName, lastName)
    

def open_FillPrescription():
    
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
        firstName.grid_forget()
        lastName.grid_forget()
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
           PCV.fillfinal(presID)
           
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
    
    presGrabbed = ctk.CTkEntry(master = app)
    
    
    firstN.set(firstName.get())
    CustomerFirst = firstName.get()
    
    
    CustomerLast = lastName.get()

    AddPrescriptionButton.grid_forget()
    FillPrescriptionButton.grid_forget()
    label.grid_forget()
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
    
    PresInstr.set("This is some test text")
    
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

    presConfirm1 = ctk.CTkButton(
        master = app,
        text = "Correct Customer",
        width = 150,
        height = 100,
        command = open_fill2
        )
    
    presConfirm1.grid(row = 13, column = 0)


AddPrescriptionButton = ctk.CTkButton(
    text="Add Prescription",
    width = 150,
    height = 100,
    master = app,
    command = open_AddPrescription
)

    # FillPrescriptionLabel = ctk.CTkLabel(master=app, text="Enter the customer name")
    # FillPrescriptionEntry = ctk.CTkEntry(master=app, width=300)

FillPrescriptionButton = ctk.CTkButton(
    text="Fill Prescription",
    width = 150,
    height = 100,
    master= app,
    command = open_FillPrescription
)


AddPrescriptionButton.grid(row = 4, column = 0, pady = 20, padx = 20)
FillPrescriptionButton.grid(row = 4, column = 2, pady = 20)
#Add A changePassword button
#Add a back button
app.mainloop()
