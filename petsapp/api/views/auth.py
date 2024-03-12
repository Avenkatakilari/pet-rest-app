from django.shortcuts import render
from rest_framework.decorators import api_view
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
from rest_framework import generics
from rest_framework.permissions import AllowAny
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes
from rest_framework.decorators import authentication_classes
from rest_framework.authentication import TokenAuthentication
from rest_framework.views import APIView
from rest_framework.response import Response
from api.models import AppUser
from api.serializers import AppUserSerializer



class RegisterView(generics.CreateAPIView):
    queryset = AppUser.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = AppUserSerializer

class HelloView(APIView):
    permission_classes = (IsAuthenticated,)
    # permission_classes = (AllowAny,)
    def get(self, request):
        content = {'message': 'Hello, World!'}
        return Response(content)