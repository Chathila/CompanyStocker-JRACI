'''
main window with custom tkinter
'''

import tkinter
from tkinter import *
import customtkinter as ctk
from customtkinter import CTkToplevel

ctk.set_appearance_mode("System") 
ctk.set_default_color_theme("dark-blue")  

#creating ctkinter window
root = ctk.CTk() 
root.geometry("500x700")
root.title("Stock App")


def button_function():
    # Create a new window using CTkToplevel
    new_window = ctk.CTkToplevel()
    new_window.geometry("500x700")
    new_window.title("New Window")

    # Display the new window
    new_window.mainloop()

# Use CTkButton instead of tkinter Button
StockPriceButton = ctk.CTkButton(master=root, text="Check Stock Prices", command=button_function)
StockPriceButton.configure(width=200, height=50)
StockPriceButton.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

root.mainloop()