import customtkinter as tk
import controllers.ReportsController as rpc
from tkinter import messagebox

def open_financialreports(app):
    # Selecting GUI theme - dark, light , system (for system default) 
    tk.set_appearance_mode("dark") 

    # Selecting color theme - blue, green, dark-blue 
    tk.set_default_color_theme("blue") 

    window = tk.CTkToplevel()
    window.geometry("500x500") 
    window.title("Generate Financial Report") 

    button = tk.CTkButton(
        text="Generate",
        width=200,
        height=50,
        font = ("Fira Code", 15),
        master = window
    )

    back = tk.CTkButton(
        master=window,
        text="Go Back",
        width=200,
        height=50,
    )
    # labels are text
    label = tk.CTkLabel(master = window,text="What date(s) would you like a report for? (YYYY-MM-DD)") 

    success = tk.CTkLabel(master = window,text="Successfully Generated")  
    failure = tk.CTkLabel(master = window,text="Failed to Generated") 
    #These are the input fields
    startDate = tk.CTkEntry(master = window, width=300, placeholder_text="YYYY-MM-DD")
    endDate = tk.CTkEntry(master = window, width=300,placeholder_text="YYYY-MM-DD")

    #this adds inputs to window
    label.pack(pady=20)
    startDate.pack()
    endDate.pack()
    button.pack(pady = 20)
    back.pack(pady = 20)

    def handle_click(event):
        sDate = startDate.get()
        eDate = endDate.get()
        complete=rpc.SalesReport(sDate,eDate) 
        if (complete == 0):
            messagebox.showinfo("Generation Complete","PDF report created in files")
        else:
            messagebox.showinfo("Failed","Failed to generate PDF")
        

    def clear_text(text):
        text.delete(0, tk.END)

    def closeWindow(self):
        app.deiconify()
        window.destroy()

    button.bind("<Button-1>", handle_click) #connects function handle_click to button 
    back.bind("<Button-1>", closeWindow)
    #window.mainloop() #constant loop for gui 
