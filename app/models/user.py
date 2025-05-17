# app/models/user.py
from sqlalchemy import Column, Integer, String, Date, Boolean, func
from app.database import Base
import enum


class Status(enum.StrEnum):
    ACTIVE = "active"
    INACTIVE = "inactive"
    BANNED = "banned"


class Role(enum.IntEnum):
    USER = 101
    ADMIN = 111


class User(Base):
    __tablename__ = "users"
    user_id = Column(Integer, primary_key=True, index=True)
    user_email = Column(String, nullable=False, unique=True)
    user_password = Column(String, nullable=False)
    user_first_name = Column(String, nullable=False)
    user_last_name = Column(String, nullable=False)
    user_birthday = Column(Date)
    user_status = Column(String, default=Status.INACTIVE)
    user_is_verify_email = Column(Boolean, default=False)
    user_native_language = Column(String, nullable=False, default="en")
    user_role = Column(Integer, default=Role.USER)
    user_has_bill = Column(Boolean, nullable=False, default=False)
    user_on_boarding = Column(Boolean, nullable=False, default=False)
    user_updated_at = Column(Date, default=func.now())
    user_created_at = Column(Date, default=func.now())
