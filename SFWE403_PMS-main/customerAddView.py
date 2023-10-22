import tkinter as tk
from models.Customer import Customer

window = tk.Tk()
window.geometry("400x400") 
window.title("Add Customer") 


label = tk.Label(window,text="Add Customer") 
entry = tk.Entry(fg="yellow", bg="gray", width=50)
entry1 = tk.Entry(fg="yellow", bg="gray", width=50)
entry2 = tk.Entry(fg="yellow", bg="gray", width=50)
entry3 = tk.Entry(fg="yellow", bg="gray", width=50)
entry4 = tk.Entry(fg="yellow", bg="gray", width=50)
label.pack(pady=20)
entry.pack() 
entry1.pack() 
entry2.pack() 
entry3.pack() 
entry4.pack() 

window.mainloop()