from tkinter import Frame, Label, Entry, Button
from Presentation.Component.password_entry import PasswordEntry


class RegisterFrame(Frame):
    def __init__(self, window, main_view):
        super().__init__(window)

        self.main_view = main_view

        self.grid_columnconfigure(1, weight=1)

        self.firstname_label = Label(self, text="First Name")
        self.firstname_label.grid(row=0, column=0, pady=10, padx=10, sticky="e")

        self.firstname_entry = Entry(self)
        self.firstname_entry.grid(row=0, column=1, pady=10, padx=(0, 10), sticky="ew")

        self.lastname_label = Label(self, text="Last Name")
        self.lastname_label.grid(row=1, column=0, pady=(0, 10), padx=(0, 10), sticky="e")

        self.lastname_entry = Entry(self)
        self.lastname_entry.grid(row=1, column=1, pady=(0, 10), padx=(0, 10), sticky="ew")

        self.username_label = Label(self, text="Username")
        self.username_label.grid(row=2, column=0, pady=(0, 10), padx=(0, 10), sticky="e")

        self.username_entry = Entry(self)
        self.username_entry.grid(row=2, column=1, pady=(0, 10), padx=(0, 10), sticky="ew")

        self.password_label = Label(self, text="Password")
        self.password_label.grid(row=3, column=0, pady=(0, 10), padx=(0, 10), sticky="e")

        self.password_entry = PasswordEntry(self)
        self.password_entry.grid(row=3, column=1, pady=(0, 10), padx=(0, 10), sticky="ew")

        self.register_button = Button(self, text="Register")
        self.register_button.grid(row=4, column=1, pady=(0, 10), padx=(0, 10), sticky="w")

        self.back_button = Button(self, text="Back to Login Page", command=self.back_button_clicked)
        self.back_button.grid(row=5, column=1, pady=(0, 10), padx=(0, 10), sticky="w")

    def back_button_clicked(self):
        self.main_view.show_frame("login")
