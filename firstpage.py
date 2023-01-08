from tkinter import *
import tkinter
import customtkinter as ctk
from customtkinter import CTkFrame

root = ctk.CTk()
root.geometry("600x300")
root.title("Stock App")

#Creating the label with Investistock at the top
NameFrame = CTkFrame(root, width = 800, height = 100, fg_color='#1F1F1F')
NameFrame.place(x=300, y=0, anchor=tkinter.N)
NameLabel = ctk.CTkLabel(master=root, text="InvestIStock", bg_color='#1F1F1F', font=('Arial',40))
NameLabel.place(x=185, y=20)

#Creating search bar 
NameFrame = CTkFrame(root, width = 400, height = 70)
NameFrame.place(x=300, y=120, anchor=tkinter.N)
entry = ctk.CTkEntry(NameFrame, placeholder_text="Enter Company Ticket Symbol", width=200)
entry.pack(side="top", padx=40, pady=40)


root.mainloop()
