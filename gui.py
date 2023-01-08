from tkinter import *
import tkinter
import customtkinter as ctk
from customtkinter import CTkFrame
from functions import stockSearch, profilePull

def split_into_lines(long_string, max_words_per_line):
    words = long_string.split()
    lines = []
    current_line = []
    
    for word in words:
       
        if len(current_line) == max_words_per_line:
            lines.append(current_line)
            current_line = []

        current_line.append(word)

    lines.append(current_line)

    return '\n'.join([' '.join(line) for line in lines])
search_term = ""

def open_main_page():
    global search_term
    search_term = SearchEntry.get()
    root.destroy()
    main_page = MainPage(search_term)
    main_page.mainloop()

class MainPage(ctk.CTk):
    def __init__(self, search_term):
        super().__init__()
        self.search_term = search_term

        self.search_term_label = ctk.CTkLabel(self, text=f"Analyzing...", font=('arial', 30))
        self.search_term_label.place(x=15, y=10)

        self.CompanyName = stockSearch(self.search_term)
        self.CompanyNameLabel = ctk.CTkLabel(self, text=f"{self.CompanyName}", font=('arial', 30))
        self.CompanyNameLabel.place(x=15, y=50)
        #self.search_term.configure(font=('Arial',40))
        
        self.com_description = profilePull(self.search_term)
        self.com_description = split_into_lines(self.com_description, 20)
        
        self.textFrame = CTkFrame(self, width = 400, height = 100)
        self.textFrame.place(relx=0.5, rely=0.4, anchor=tkinter.CENTER)
        self.textbox = ctk.CTkTextbox(self.textFrame, width=450, height = 400)
        self.textbox.grid(row = 0, column=0)
        self.textbox.insert("0.0", f"{self.com_description}")  # insert at line 0 character 0
        self.text = self.textbox.get("0.0", "end")  # get text from line 0 character 0 till the end

        self.textbox.configure(state="disabled")  # configure textbox to be read-only
        
        self.geometry("500x800")

        self.StockPrice = ButtonWindow(self, "StockPrice", "Window 1")
        self.BalanceSheet = ButtonWindow(self, "Balance Sheet", "Window 2")
        self.CashFlow = ButtonWindow(self, "Cash Flow Statements", "Window 3")
        self.Price = ButtonWindow(self, "Price", "Window 4")

        self.StockPrice.pack(side='bottom', padx=20, pady=20)
        self.BalanceSheet.pack(side='bottom', padx=20, pady=20)
        self.CashFlow.pack(side='bottom', padx=20, pady=20)
        self.Price.pack(side='bottom', padx=20, pady=20)

class ButtonWindow:
    def __init__(self, master, button_text, window_title):
        self.master = master
        self.button_text = button_text
        self.window_title = window_title

        self.button = ctk.CTkButton(self.master, text=self.button_text, command=self.create_toplevel)

    def pack(self, **kwargs):
        self.button.pack(**kwargs)

    def grid(self, **kwargs):
        self.button.grid(**kwargs)

    def create_toplevel(self):
        window = ctk.CTkToplevel(self.master)
        window.geometry("400x200")
        window.title(self.window_title)

        # create label on CTkToplevel window
        label = ctk.CTkLabel(window, text=self.window_title)
        label.pack(side="top", fill="both", expand=True, padx=40, pady=40)

        def go_back_to_old_window():
            # Reopen the old window
            self.master.update()
            self.master.deiconify()

            # Close the new window
            window.destroy()

        GoBackButton = ctk.CTkButton(master=window, text="Go Back", command=go_back_to_old_window)
        GoBackButton.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)
        GoBackButton.configure(width=100, height=50)

root = ctk.CTk()
root.geometry("600x300")
root.title("Stock App")


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


root.mainloop()
       
