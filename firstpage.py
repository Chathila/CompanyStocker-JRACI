from tkinter import *
import tkinter
import customtkinter as ctk
from customtkinter import CTkFrame
from secondpage import MainPage

root = ctk.CTk()
root.geometry("600x300")
root.title("Stock App")

def open_main_page():
    root.withdraw()
    main_page = MainPage()
    main_page.mainloop()

#Creating the label with Investistock at the top
NameFrame = CTkFrame(root, width = 800, height = 300, fg_color='#1F1F1F')
NameFrame.place(relx=0.5, y=0, anchor=tkinter.CENTER)
NameLabel = ctk.CTkLabel(master=root, text="CompanyStocker", bg_color='#1F1F1F', font=('Arial',40))
NameLabel.place(x=150, y=20)

#Creating search bar 
NameFrame = CTkFrame(root, width = 400, height = 100)
NameFrame.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)
SearchEntry = ctk.CTkEntry(NameFrame, placeholder_text="Enter Company Ticket Symbol", width=200)
SearchEntry.pack(side="top", padx=40, pady=50)
SearchEntry.place(x=100, rely=0.2)

#Adding search button
search_button = ctk.CTkButton(root, text="Search", command=open_main_page)
search_button.place(relx=0.5, rely=0.57, anchor=tkinter.CENTER)
search_button.configure(height=20, width=80)

#def traversing_to_second_page():


root.mainloop()
