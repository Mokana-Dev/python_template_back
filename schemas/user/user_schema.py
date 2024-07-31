from pydantic import BaseModel, EmailStr
from typing import Optional
from ..auth.login_schema import LoginSchema


class UserAdminSchema(LoginSchema):
    pass


class UserFilterSchema(BaseModel):
    email: str


class CreateUserPersonalInfoSchema(BaseModel):
    first_name: str
    last_name: str
    email: EmailStr
    phone_number: Optional[str] = None
    address: Optional[str] = None
    date_of_birth: str
    user_admin: LoginSchema
