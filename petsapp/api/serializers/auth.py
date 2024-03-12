from rest_framework import serializers
from api.models import AppUser
"""
Author: K V S Aravind.
"""
# To store user into database and JSON to object conversion

class AppUserSerializer(serializers.ModelSerializer):
     
      class Meta:
         model = AppUser
         fields = (
            'id',
            'username', 
            'email', 
            'password'            
          )
      def create(self,data):
         user = AppUser.objects.create(
         username=data['username'],
            email=data['email']                  
           )
         user.set_password(data['password'])
         user.save()
         return user    