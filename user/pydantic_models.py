from pydantic import BaseModel

class Person(BaseModel):
    name:str
    email:str
    phone:int
    password:str

class data(BaseModel):
    id:int

class delete_data(BaseModel):
    id:int

class update(BaseModel):
    id:int
    name:str
    email:str
    phone:int