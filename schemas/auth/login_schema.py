from pydantic import BaseModel


class LoginSchema(BaseModel):
    username: str
    password: str


class AccessTokenSchema(BaseModel):
    access_token: str
    expired: str
