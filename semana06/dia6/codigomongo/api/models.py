#from django.db import models
from mongoengine import Document,fields

# Create your models here.
class Alumno(Document):
    nombre = fields.StringField()
    email = fields.EmailField()
    celular = fields.StringField()
    github = fields.StringField()

    