'''
main window with custom tkinter
'''

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
    GoBackButton.configure(width=200, height=50)
    GoBackButton.pack()

    # Display the new window
    new_window.mainloop()

# Use CTkButton instead of tkinter Button
OpenNewWindowButton = ctk.CTkButton(master=root, text="Open New Window", command=open_new_window)
OpenNewWindowButton.configure(width=200, height=50)
OpenNewWindowButton.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

root.mainloop()