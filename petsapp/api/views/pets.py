from  rest_framework.mixins import CreateModelMixin,RetrieveModelMixin,UpdateModelMixin,ListModelMixin
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes

from api.serializers import PetSerializer
from api.models import Pet
"""
Author: K V Aravind
Pet CRUD service level logic
This class demos Mixins special abstraction from DRF
"""
class PetRU(GenericAPIView,RetrieveModelMixin,UpdateModelMixin):
    permission_classes = (IsAuthenticated,)
    queryset = Pet.objects.all()
    serializer_class = PetSerializer
 
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self,request,*args,  **kwargs):
        return self.update(request, *args, **kwargs)

class PetCL(GenericAPIView,CreateModelMixin,ListModelMixin):
       permission_classes = (IsAuthenticated,)
       queryset = Pet.objects.all()
       serializer_class = PetSerializer 
       
       def post(self,request,*args, **kwargs):
        return self.create(request, *args, **kwargs)

       def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

