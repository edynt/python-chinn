from pydantic import BaseModel
from datetime import date


class UserCreate(BaseModel):
    user_email: str
    user_password: str
    user_first_name: str
    user_last_name: str
    user_birthday: date


class UserResponse(UserCreate):
    user_id: int
    user_email: str
    user_password: str
    user_first_name: str
    user_last_name: str
    user_birthday: date
    user_status: str
    user_is_verify_email: bool
    user_native_language: str
    user_role: int
    user_has_bill: bool
    user_on_boarding: bool
    user_updated_at: date
    user_created_at: date

    model_config = {"from_attributes": True}
