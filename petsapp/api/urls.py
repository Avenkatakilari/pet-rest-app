from django.urls import path

from . import views
from .views import RegisterView
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.views import TokenRefreshView
from rest_framework_simplejwt.views import TokenVerifyView


urlpatterns = [
    path('register',RegisterView.as_view()),
    path('token', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh_token', TokenRefreshView.as_view(), name='token_refresh'),
    path('verify', TokenVerifyView.as_view(), name='token_verify'),
    path('hello',views.HelloView.as_view(), name='hello'),
    path('pet/<int:pk>',views.PetRU.as_view(), name='pet_object_retrieve_update'),
    path('pet',views.PetCL.as_view(), name='pet_object_retrieve_update'),
    path('pet-type/list',views.ListPetTypeView.as_view(),name="create_pet_type"),
    path('pet-type',views.CreatePetTypeView.as_view(),name="list_pet_type"),
    path('pet-type/update/<int:pk>',views.UpdatePetTypeView.as_view(),name="update-pet-type"),
    path('pet-type/<int:pk>',views.GetPetTypeView.as_view(),name="list_pet_type"),

]