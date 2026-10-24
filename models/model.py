from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from database.db import Base


class Student(Base):
    __tablename__ = "students"

    id: Mapped[int] = mapped_column(primary_key=True)
    roll_number: Mapped[str] = mapped_column(String(20), unique=True)
    name: Mapped[str] = mapped_column(String(100))
    maths: Mapped[int]
    physics: Mapped[int]
    chemistry: Mapped[int]
    total: Mapped[int]