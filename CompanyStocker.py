from tkinter import *
import tkinter
import customtkinter as ctk
from customtkinter import CTkFrame
from functions import stockSearch, profilePull, stockPrice, incomePull_final, balancePull_final, cashflowPull_final

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

        # self.search_term_label = ctk.CTkLabel(self, text=f"Analyzing...", font=('arial', 30))
        # self.search_term_label.place(x=15, y=10)

        self.CompanyName = stockSearch(self.search_term)
        self.CompanyNameLabel = ctk.CTkLabel(self, text=f"{self.CompanyName}", font=('arial', 27))
        self.CompanyNameLabel.place(x=15, y=20)
        #self.search_term.configure(font=('Arial',40))
        self.ShowStock = stockPrice(self.search_term)
        self.ShowStockLabel = ctk.CTkLabel(self, text=f"Stock Price: ${self.ShowStock}USD", font=('arial', 20))
        self.ShowStockLabel.place(x=15, y=65)
        
        self.com_description = profilePull(self.search_term)
        self.com_description = split_into_lines(self.com_description, 20)
        
        self.textFrame = CTkFrame(self, width = 400, height = 100)
        self.textFrame.place(relx=0.5, rely=0.4, anchor=tkinter.CENTER)
        self.textbox = ctk.CTkTextbox(self.textFrame, width=450, height = 400)
        self.textbox.grid(row = 0, column=0)
        self.textbox.insert("0.0", f"{self.com_description}") 
        self.text = self.textbox.get("0.0", "end") 
        self.textbox.configure(state="disabled")  
        
        self.geometry("500x800")


        self.BalanceSheet = ButtonWindow(self, "Balance Sheet", "Balance Sheet")
        self.CashFlow = ButtonWindow(self, "Cash Flow Statements", "Cash Flow Statements")
        self.IncomeStatements = ButtonWindow(self, "Income Statements", "Income Statements")

        self.BalanceSheet.pack(side='bottom', padx=20, pady=20)
        self.CashFlow.pack(side='bottom', padx=20, pady=20)
        self.IncomeStatements.pack(side='bottom', padx=20, pady=20)

#class Chart:
#    def __init__(self):
#        self.chart_button = ctk.CTkButton(self, text = "Show Graph", command=lambda: grapher(f"{search_term}"), width=200, height=50, font=("arial", 15))

class ButtonWindow:
    def __init__(self, master, button_text, window_title):
        self.master = master
        self.button_text = button_text
        self.window_title = window_title

        self.button = ctk.CTkButton(self.master, text=self.button_text, command=self.create_toplevel, width=200, height=50, font=("arial", 15))

    def pack(self, **kwargs):
        self.button.pack(**kwargs)

    def grid(self, **kwargs):
        self.button.grid(**kwargs)

    def create_toplevel(self):
        if self.button_text == "Balance Sheet":
            window = BalanceSheetWindow(self.master, search_term)
        elif self.button_text == "Cash Flow Statements":
            window = CashFlowWindow(self.master, search_term)
        elif self.button_text == "Income Statements":
            window = IncomeStatementWindow(self.master, search_term)
        else:
            window = ctk.CTkToplevel(self.master)
            window.title(self.window_title)
        def go_back_to_old_window():
            # Reopen the old window
            self.master.update()
            self.master.deiconify()

            # Close the new window
            window.destroy()

        GoBackButton = ctk.CTkButton(master=window, text="Go Back", command=go_back_to_old_window)
        GoBackButton.place(relx=0.5, rely=0.9, anchor=tkinter.CENTER)
        GoBackButton.configure(width=100, height=50)

        
class BalanceSheetWindow(tkinter.Toplevel):
    def __init__(self, master, search_term):
        super().__init__(master)
        self.search_term = search_term
        self.balance_label = ctk.CTkLabel(self, text=f"Balance Sheet", font=('arial', 20))
        self.balance_label.place(x=15, y=50)

        self.CompanyName = stockSearch(self.search_term)
        self.CompanyNameLabel = ctk.CTkLabel(self, text=f"{self.CompanyName}", font=('arial', 27))
        self.CompanyNameLabel.place(x=15, y=10)
        
        self.balancedata = balancePull_final(self.search_term)

        self.geometry("500x800")

        self.textFrame = CTkFrame(self, width = 400, height = 100)
        self.textFrame.place(relx=0.5, rely=0.47, anchor=tkinter.CENTER)
        self.textbox = ctk.CTkTextbox(self.textFrame, width=450, height = 570)
        self.textbox.grid(row = 0, column=0)
        self.textbox.insert("0.0", f"{self.balancedata}") 
        self.text = self.textbox.get("0.0", "end") 
        self.textbox.configure(state="disabled")  


class CashFlowWindow(tkinter.Toplevel):
    def __init__(self, master, search_term):
        super().__init__(master)
        self.search_term = search_term
        self.cash_label = ctk.CTkLabel(self, text=f"Cash Flow Statement", font=('arial', 20))
        self.cash_label.place(x=15, y=50)

        self.CompanyName = stockSearch(self.search_term)
        self.CompanyNameLabel = ctk.CTkLabel(self, text=f"{self.CompanyName}", font=('arial', 27))
        self.CompanyNameLabel.place(x=15, y=10)
        
        self.cashflowdata = cashflowPull_final(self.search_term)

        self.geometry("500x800")

        self.textFrame = CTkFrame(self, width = 400, height = 100)
        self.textFrame.place(relx=0.5, rely=0.47, anchor=tkinter.CENTER)
        self.textbox = ctk.CTkTextbox(self.textFrame, width=450, height = 570)
        self.textbox.grid(row = 0, column=0)
        self.textbox.insert("0.0", f"{self.cashflowdata}") 
        self.text = self.textbox.get("0.0", "end") 
        self.textbox.configure(state="disabled") 


class IncomeStatementWindow(tkinter.Toplevel):
    def __init__(self, master, search_term):
        super().__init__(master)
        self.search_term = search_term
        self.income_label = ctk.CTkLabel(self, text=f"Income Statement", font=('arial', 20))
        self.income_label.place(x=15, y=50)

        self.CompanyName = stockSearch(self.search_term)
        self.CompanyNameLabel = ctk.CTkLabel(self, text=f"{self.CompanyName}", font=('arial', 27))
        self.CompanyNameLabel.place(x=15, y=10)
        
        self.incomedata = incomePull_final(self.search_term)

        self.geometry("500x800")

        self.textFrame = CTkFrame(self, width = 400, height = 100)
        self.textFrame.place(relx=0.5, rely=0.47, anchor=tkinter.CENTER)
        self.textbox = ctk.CTkTextbox(self.textFrame, width=450, height = 570)
        self.textbox.grid(row = 0, column=0)
        self.textbox.insert("0.0", f"{self.incomedata}") 
        self.text = self.textbox.get("0.0", "end") 
        self.textbox.configure(state="disabled") 

        

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
SearchEntry = ctk.CTkEntry(NameFrame, placeholder_text="Enter Company Ticker Symbol", width=200)
SearchEntry.pack(side="top", padx=40, pady=50)
SearchEntry.place(x=100, rely=0.2)

#Adding search button
search_button = ctk.CTkButton(root, text="Search", command=open_main_page)
search_button.place(relx=0.5, rely=0.57, anchor=tkinter.CENTER)
search_button.configure(height=20, width=80)


root.mainloop()