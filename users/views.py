from django.shortcuts import render
from django.db.models import Q
from ninja import Router
from typing import Union
from django.contrib.auth import get_user_model, authenticate

from users.schemas import RegisterSchema, LoginSchema, LoginResponseSchema, UserSchema
from core.schemas import SuccessMessageResponseSchema

from users.helpers import TokenAuth

# Create your views here.

router = Router()

User = get_user_model()

@router.post("/register", response=SuccessMessageResponseSchema)
def register(request, input: RegisterSchema):
    first_name = input.first_name if hasattr(input, "first_name") else None
    last_name = input.last_name if hasattr(input, "last_name") else None
    email = input.email if hasattr(input, "email") else None
    password = input.password if hasattr(input, "password") else None
    username = input.username if hasattr(input, "username") else None
    
    user = User.objects.create_user(email=email, password=password, first_name=first_name, last_name=last_name, username=username)

    return {"message": "User created successfully"}

@router.post("/login", response=Union[LoginResponseSchema, SuccessMessageResponseSchema])
def login(request, input: LoginSchema):
    username = input.username
    password = input.password
    user = authenticate(request, username=username, password=password)
    if not user:
        return {"message": "Invalid username or password"}
    else:
        return {"message": "Login successful", "token": user.get_auth_token()}
    
@router.get("/me", auth=TokenAuth(), response=UserSchema)
def me(request):
    print(request.auth)
    return request.auth