from fastapi import APIRouter,Request,status
from .models import *
from .pydantic_models import Person
from fastapi.responses import JSONResponse
from passlib.context import CryptContext


app=APIRouter()

pwd_context=CryptContext(schemes=['bcrypt'],deprecated='auto')

def verify_password(plain_password,hashed_password):
    return pwd_context.verify(plain_password,hashed_password)

def get_password_hash(password):
    return pwd_context.hash(password)

@app.post('/')
async def registration(data:Person):
    if await Student.exists(phone=data.phone):
        return {'status':False,'message':'Phone number is already exists'}
    elif await Student.exists(email=data.email):
        return {'status':False,'message':'Email is already existe'}
    else:
        user_obj=await Student.create(name=data.name,email=data.email,phone=data.phone,password=data.password)
        return user_obj
    
@app.get('/all/')
async def all_student():
    user_obj=await Student.all()
    return user_obj

