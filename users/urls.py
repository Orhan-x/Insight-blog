from django.urls import path
from . import views

urlpatterns = [
    path("user/register",views.registration, name="register"),
]