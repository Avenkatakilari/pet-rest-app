from rest_framework import serializers
from api.models import Pet
from api.serializers import AppUserSerializer
from api.models import AppUser
from .pettypes import PetTypeSerializer
from api.models import PetType


"""
Author : K V S Aravind
"""
# To store pets data and do serialization and deserialization of Pet Object

class PetSerializer(serializers.ModelSerializer):
    user = AppUserSerializer(read_only=True)
    pettype = PetTypeSerializer(read_only=True) 
    
    ### Create Pet ###
    def create(self,validated_data):
     user_data = self.initial_data['user']
     user_instance = AppUser.objects.get(pk=user_data['id'])
     pet_type_data = self.initial_data['pettype']
     pet_type_instance = PetType.objects.get(pk=pet_type_data['id'])
     validated_data['user'] = user_instance
     validated_data['pettype'] = pet_type_instance
     return super().create(validated_data)
     
    class Meta:
         model = Pet
         fields = (
            'id',
            'name',
            'description',
            'creation_date',
            'user',
            'pettype',
            'city',
            'state',
            'phone',
         )
