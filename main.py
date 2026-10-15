import os
from dotenv import load_dotenv
from Presentation.main_view import MainView
from BusinessLogic.user_business_logic import UserBusinessLogic
from DataAccess.Repositories.SQLServer.employee_repository import SQLServerEmployeeRepository
from DataAccess.Services.rabbitmq_sms_service import RabbitMQSmsService

load_dotenv()

sql_server_host = os.getenv("SQLSERVER_HOST", ".")
sql_server_database = os.getenv("SQLSERVER_DATABASE")


repository = SQLServerEmployeeRepository(sql_server_host, sql_server_database)
sms_service = RabbitMQSmsService()
user_business = UserBusinessLogic(repository, sms_service)

MainView(user_business)