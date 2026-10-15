from ttkbootstrap import Frame, Label, Entry, Button, Checkbutton
from ttkbootstrap.dialogs import Messagebox

try:
    from ttkbootstrap.widgets import ToastNotification  # newer ttkbootstrap
except ImportError:
    from ttkbootstrap.toast import ToastNotification  # older ttkbootstrap

from Presentation.Component.password_entry import PasswordEntry
from Presentation.Component.captcha_widget import CaptchaWidget

from BusinessLogic.user_business_logic import UserBusinessLogic


class LoginFrame(Frame):
    def __init__(self, main_window, main_view, user_business: UserBusinessLogic):
        super().__init__(main_window)

        self.main_view = main_view
        self.user_business = user_business

        self.grid_columnconfigure(1, weight=1)

        self.username_label = Label(self, text="Username")
        self.username_label.grid(row=0, column=0, pady=10, padx=10, sticky="e")

        self.username_entry = Entry(self)
        self.username_entry.grid(row=0, column=1, pady=10, padx=(0, 10), sticky="ew")

        self.password_label = Label(self, text="Password")
        self.password_label.grid(row=1, column=0, pady=(0, 10), padx=10, sticky="e")

        self.password_entry = PasswordEntry(self)
        self.password_entry.grid(row=1, column=1, pady=(0, 10), padx=(0, 10), sticky="ew")

        self.captcha_label = Label(self, text="Captcha")
        self.captcha_label.grid(row=2, column=0, pady=(0, 10), padx=10, sticky="ne")

        self.captcha = CaptchaWidget(self)
        self.captcha.grid(row=2, column=1, pady=(0, 10), padx=(0, 10), sticky="ew")

        self.remember_me_button = Checkbutton(self, text="Remember Me?")
        self.remember_me_button.grid(row=3, column=1, pady=(0, 10), padx=(0, 10), sticky="w")

        self.login_button = Button(self, text="Login", bootstyle="primary", command=self.login_button_clicked)
        self.login_button.grid(row=4, column=1, pady=(0, 10), padx=(0, 10), sticky="w")

        self.register_button = Button(self, text="Register", bootstyle="secondary", command=self.register_button_clicked)
        self.register_button.grid(row=5, column=1, pady=(0, 10), padx=(0, 10), sticky="w")

    def login_button_clicked(self):
        # 1) Captcha first, so wrong captcha never reaches the database.
        if not self.captcha.is_valid():
            Messagebox.show_warning("Captcha is incorrect. Please try again.", "Captcha", parent=self)
            self.captcha.refresh()
            return

        username = self.username_entry.get()
        password = self.password_entry.get_value()

        response = self.user_business.login(username, password)

        if response.success:
            self.show_toast("Login Successful", response.message, "success")
            self.captcha.refresh()
            self.password_entry.clear()
            home_frame = self.main_view.show_frame("home")
            home_frame.set_current_employee(response.data)
        else:
            Messagebox.show_error(response.message, "Login Failed", parent=self)
            self.captcha.refresh()

    def register_button_clicked(self):
        self.main_view.show_frame("register")

    @staticmethod
    def show_toast(title: str, message: str, style: str):
        ToastNotification(title=title, message=message, duration=3000, bootstyle=style).show_toast()