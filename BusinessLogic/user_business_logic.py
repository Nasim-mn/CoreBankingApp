from datetime import datetime
from hashlib import md5
from Common.Enums.employee_status import EmployeeStatus
from Common.DTOs.response import Response
from Common.Repositories.iemployee_repository import IEmployeeRepository
from Common.Services.isms_service import ISmsService


class UserBusinessLogic:
    def __init__(self, employee_repository: IEmployeeRepository, sms_service: ISmsService):
        self.employee_repository = employee_repository
        self.sms_service = sms_service

    def login(self, username: str, password: str):
        if len(username) < 3 or len(password) < 6:
            return Response(False, "Invalid structure username or password.")

        password_hashed = md5(password.encode()).hexdigest()
        employee = self.employee_repository.get_by_username_password(username, password_hashed)

        if employee:
            match employee.status:
                case EmployeeStatus.Active:
                    message = f"Welcome {employee.get_fullname()}"
                    if not self._send_login_sms(employee):
                        message += " (SMS notification could not be sent)"
                    return Response(True, message, employee)
                case EmployeeStatus.Pending:
                    return Response(False, "Your account is pending(call to administrator).", employee)
                case EmployeeStatus.Deactive:
                    return Response(False, "Your account was deactivated.", employee)
                case _:
                    return Response(False, "Unknown account status.", employee)
        else:
            return Response(False, "Invalid username or password")

    def _send_login_sms(self, employee) -> bool:
        now = datetime.now().strftime("%Y-%m-%d %H:%M")
        content = (
            f"Dear {employee.get_fullname()}, a login to your Core Banking account "
            f"was recorded at {now}. If this was not you, contact support immediately."
        )
        # An SMS failure must never block a valid login.
        return self.sms_service.send(employee.mobile, content)