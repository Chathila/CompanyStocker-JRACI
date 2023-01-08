'''
main window with custom tkinter


import tkinter
import customtkinter as ctk

ctk.set_appearance_mode("System")  # Modes: system (default), light, dark
ctk.set_default_color_theme("dark-blue")  # Themes: blue (default), dark-blue, green

root = ctk.CTk()  # create CTk window like you do with the Tk window
root.geometry("500x700")
root.title("Stock App")

def open_new_window():
    # Create a new window
    new_window = ctk.CTkToplevel()
    new_window.geometry("500x700")
    new_window.title("New Window")

    # Create a button to go back to the old window
    def go_back_to_old_window():
        # Reopen the old window
        root.update()
        root.deiconify()

        # Close the new window
        new_window.destroy()

    GoBackButton = ctk.CTkButton(master=new_window, text="Go Back", command=go_back_to_old_window)
    GoBackButton.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)
    GoBackButton.configure(width=100, height=50)


    # Display the new window
    new_window.mainloop()

# Use CTkButton instead of tkinter Button
OpenNewWindowButton = ctk.CTkButton(master=root, text="Open New Window", command=open_new_window)
OpenNewWindowButton.configure(width=200, height=50)
OpenNewWindowButton.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

root.mainloop()
'''

import tkinter
import customtkinter as ctk

class ExampleApp(ctk.CTk):
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


app = ExampleApp()
app.mainloop()