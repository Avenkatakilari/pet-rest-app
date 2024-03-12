from django.db import models

# Pet type master data.

class PetType(models.Model):
 
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
  
  class Meta:
    db_table = 'pet_type'