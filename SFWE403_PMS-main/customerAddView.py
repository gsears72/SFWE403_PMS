import tkinter as tk
from models.Customer import Customer
from models.Staff import PharmacyManager

manager = PharmacyManager("test")
customer = Customer()

window = tk.Tk()
window.geometry("500x500") 
window.title("Add Customer") 

button = tk.Button(
    text="Add",
    width=20,
    height=5,
    bg="blue",
    fg="yellow",
)
# labels are text
label = tk.Label(window,text="Add Customer") 
label1 = tk.Label(window,text="First Name") 
label2 = tk.Label(window,text="Last Name") 
label3 = tk.Label(window,text="DOB in yyyy-mm-dd") 

success = tk.Label(window,text="Successfully Added!", fg="green")  
failure = tk.Label(window,text="Failed to Add!", fg = "red") 
#These are the input fields
firstNameIn = tk.Entry(fg="yellow", bg="gray", width=50)
lastNameIn = tk.Entry(fg="yellow", bg="gray", width=50)
bDayIn = tk.Entry(fg="yellow", bg="gray", width=50)
adressIn = tk.Entry(fg="yellow", bg="gray", width=50)
phoneIn = tk.Entry(fg="yellow", bg="gray", width=50)
emailIn = tk.Entry(fg="yellow", bg="gray", width=50)
insuranceIn = tk.Entry(fg="yellow", bg="gray", width=50)
#this adds inputs to window
label.pack(pady=20)
label1.pack()
firstNameIn.pack() 
label2.pack()
lastNameIn.pack() 
label3.pack()
bDayIn.pack() 
adressIn.pack() 
phoneIn.pack() 
emailIn.pack() 
insuranceIn.pack() 
button.pack(pady = 20)

def handle_click(event): 
    # this gets info from input and puts into class
    customer.first_name = firstNameIn.get()
    customer.last_name = lastNameIn.get()
    customer.date_of_birth = bDayIn.get()
    customer.address = adressIn.get()
    customer.phone = phoneIn.get()
    customer.email = emailIn.get()
    customer.insurance = insuranceIn.get()
    #this adds the customer to database and checks if it worked
    test = manager.createPatient(customer)
    if test:
        failure.pack_forget() #removes from screen
        success.pack(pady = 20) #adds to screen 
        #clears input fields
        clear_text(firstNameIn)
        clear_text(lastNameIn)
        clear_text(bDayIn)
        clear_text(adressIn)
        clear_text(phoneIn)
        clear_text(emailIn)
        clear_text(insuranceIn)
    else:
        success.pack_forget()
        failure.pack(pady = 20) 

def clear_text(text):
   text.delete(0, tk.END)

button.bind("<Button-1>", handle_click) #connects function handle_click to button 

window.mainloop() #constant loop for gui 
