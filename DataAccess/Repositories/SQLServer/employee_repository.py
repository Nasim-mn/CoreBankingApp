import pymssql
from Common.Entities.employee import Employee
from Common.Repositories.iemployee_repository import IEmployeeRepository


class SQLServerEmployeeRepository(IEmployeeRepository):
    def __init__(self, server, database):
        self.server = server
        self.database = database

    def get_by_username_password(self, username: str, password: str) -> Employee:
        with pymssql.connect(host=self.server, database=self.database) as connection:
            cursor = connection.cursor()
            cursor.execute("""
Select	Id
,		FirstName
,		LastName
,		Username
,		Password
,		Mobile
,		EmployeeStatusId
From	Employee
Where	Username	=	%s
AND		Password	=	%s""", (username, password))
            row = cursor.fetchone()

            if row:
                employee = Employee(row[0], row[1], row[2], row[3], row[4], row[5], row[6])
                return employee

    def insert(self, employee: Employee):
        pass
