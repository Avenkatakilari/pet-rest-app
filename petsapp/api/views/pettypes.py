# Dependencies
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import CreateAPIView, ListAPIView,RetrieveAPIView,UpdateAPIView

from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes

from api.models import PetType
from api.serializers import PetTypeSerializer

"""
Author: K V S Aravind
Pet Type CRUD service level 

"""
class CreatePetTypeView(CreateAPIView):
     permission_classes = (IsAuthenticated,)
     queryset = PetType.objects.all()
     serializer_class = PetTypeSerializer

"""
Get Pet Type

"""
class GetPetTypeView(RetrieveAPIView):
     permission_classes = (IsAuthenticated,)
     queryset = PetType.objects.all()
     serializer_class = PetTypeSerializer

"""
List Pet Type

"""
class ListPetTypeView(ListAPIView):
     permission_classes = (IsAuthenticated,)
     serializer_class = PetTypeSerializer
     queryset = PetType.objects.all()

"""
Update Pet Type

"""
class UpdatePetTypeView(UpdateAPIView):
     permission_classes = (IsAuthenticated,)
     serializer_class = PetTypeSerializer
     queryset = PetType.objects.all()




    