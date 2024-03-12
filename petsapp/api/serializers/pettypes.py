from rest_framework import serializers
from api.models import PetType

"""
Author: K V S Aravind

"""
# To provide Pets type object serialization and deseraialization

class PetTypeSerializer(serializers.ModelSerializer): 

    class Meta:
         model = PetType
         fields = (
            'id',
            'name',
            'description',
            'creation_date'
         )
