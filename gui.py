'''
import tkinter
import customtkinter as ctk


class SuperClass(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.geometry("500x400")

        self.button = ctk.CTkButton(self, text="Create Toplevel", command=self.create_toplevel)
        self.button.pack(side="top", padx=40, pady=40)

    def create_toplevel(self):
        window = ctk.CTkToplevel(self)
        window.geometry("400x200")

        # create label on CTkToplevel window
        label = ctk.CTkLabel(window)
        label.pack(side="top", fill="both", expand=True, padx=40, pady=40)

        def go_back_to_old_window():
            # Reopen the old window
            self.update()
            self.deiconify()

            # Close the new window
            window.destroy()

        GoBackButton = ctk.CTkButton(master=window, text="Go Back", command=go_back_to_old_window)
        GoBackButton.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)
        GoBackButton.configure(width=100, height=50)




app = SuperClass()
app.mainloop()
'''
import tkinter
import tkinter
import customtkinter as ctk

class MainPage(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.geometry("600x800")

        # Create a button that opens a new window
        self.StockPrice = ButtonWindow(self, "StockPrice", "Window 1")
        self.StockPrice.pack(side="top", padx=40, pady=40)

        # Create a second button that opens a new window
        self.BalanceSheet = ButtonWindow(self, "Balance Sheet", "Window 2")
        self.BalanceSheet.pack(side="top", padx=40, pady=40)

        self.CashFlow = ButtonWindow(self, "Cash Flow Statements", "Window 3")
        self.CashFlow.pack(side="top", padx=40, pady=40)

        self.Price = ButtonWindow(self, "Price", "Window 4")
        self.Price.pack(side="top", padx=40, pady=40)

class ButtonWindow:
    def __init__(self, master, button_text, window_title):
        self.master = master
        self.button_text = button_text
        self.window_title = window_title

        self.button = ctk.CTkButton(self.master, text=self.button_text, command=self.create_toplevel)

    def pack(self, **kwargs):
        self.button.pack(**kwargs)

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

app = MainPage()
app.mainloop()