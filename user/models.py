from tortoise.models import Model
from tortoise import Tortoise,fields

class Student(Model):
    id=fields.CharField(10,pk=True)
    name=fields.CharField(220)
    email=fields.CharField(266, unique=True)
    phone=fields.CharField(10)
    password=fields.CharField(225)


Tortoise.init_models(['user.models'],'models')