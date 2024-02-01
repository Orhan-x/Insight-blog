from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name="posts"),
    path('home/', views.home, name="posts"),
    path('post/create/', views.create_post, name="create-post"),
]