from typing import Optional
from ninja import Schema
from pydantic_core.core_schema import FieldValidationInfo
from pydantic import field_validator
import uuid
import datetime

class RegisterSchema(Schema):
    email: str
    password: str
    password_confirm: str
    first_name: str = None
    last_name: Optional[str] = None
    username: str

    @field_validator("password_confirm")
    def validate_password(cls, v, values):
        if v != values.data["password"]:
            raise ValueError("Passwords do not match")
        return v
    
    @field_validator("username")
    def validate_username(cls, v):
        assert v.isalnum(), "Username must be alphanumeric"
        return v
    

class LoginSchema(Schema):
    username: str
    password: str


class LoginResponseSchema(Schema):
    message: str
    token: str


class UserSchema(Schema):
    id: uuid.UUID
    email: str
    first_name: str
    last_name: str
    created_at: datetime.datetime
    