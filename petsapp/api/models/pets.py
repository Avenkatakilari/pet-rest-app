from django.db import models
from api.models import AppUser
from .pettypes import PetType


# Create your models here.

class Pet(models.Model):
 
  id = models.AutoField(
     primary_key=True
    )
  name = models.TextField(
    max_length=25,
    null=False,
    blank=False
  )
  
  description = models.TextField(
    max_length=255,
    null=False,
    blank=False
  )

  creation_date = models.DateTimeField(
    auto_now_add=True
   )
   
  city = models.TextField(
    max_length=25,
    null=True,
    blank=False 
  )

  state = models.TextField(
    max_length=25,
    null=True,
    blank=False 
  )

  phone = models.TextField(
    max_length=10,
    null=False,
    blank=True
  )
  
  user = models.ForeignKey(AppUser,on_delete=models.CASCADE, blank=True,
    null=True)
  pettype = models.ForeignKey(PetType,on_delete=models.CASCADE, blank=True,
   null=True)
