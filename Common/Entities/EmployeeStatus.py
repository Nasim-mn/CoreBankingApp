from DataAccess.models.base import Base
from sqlalchemy import Integer , String , Date , DateTime
from sqlalchemy.orm import Mapped, mapped_column, Relationship


class EmployeeStatus(Base):
    __tablename__ = 'EmployeeStatus'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    Title: Mapped[str] = mapped_column(String(50), nullable=False)
