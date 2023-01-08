from tkinter import *
import tkinter
import customtkinter as ctk
from customtkinter import CTkFrame

root = ctk.CTk()
root.geometry("600x800")
root.title("Stock App")

LoginFrame = CTkFrame(root, width = 800, height = 100, fg_color='#1F1F1F')
LoginFrame.place(x=300, y=0, anchor=tkinter.N)
label = ctk.CTkLabel(master=root, text="InvestIStock", bg_color='#1F1F1F', font=('SF Pro',40))
label.place(x=175, y=20)

root.mainloop()
