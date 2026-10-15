from tkinter import Frame , Label , Button
from Presentation import main_view
from Common.Entities.employee import Employee


class HomeFrame(Frame):
    def __init__(self,window , main_view : main_view):
        super().__init__()


        self.grid_columnconfigure(0, weight=1)


        self.main_view = main_view
        self.current_employee = None
        self.header_label = Label(self)
        self.header_label.grid(row = 0 , column = 0 ,padx= 10 , pady = 10)

        self.employee_management = Button(self, text = "Employee Management")
        # self.employee_management.grid(row = 1 , column = 0 , pady=(0,10) , padx= 10 , sticky="ew")

        self.account_management = Button(self, text="Account Management")
        self.profile_management = Button(self, text="My Profile")
        self.profile_management.grid(row = 3 , column = 0 , pady=(0,10) , padx= 10 , sticky="ew")




        self.logout_button = Button(self , text = "Logout" , command = self.logout_button_clicked)
        self.logout_button.grid(row = 1 , column = 0 , pady=(0,10) , padx= 10 , sticky="ew")

    def set_current_employee(self,current_employee):
        self.current_employee = current_employee

        self.header_label.config(text = f"Wellcome {self.current_employee.get_fullname()}")


    def logout_button_clicked(self):
        self.current_employee = None
        self.main_view.show_frame("login")

