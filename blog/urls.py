from django.urls import path, include
from .views import create_post, home

urlpatterns = [
        path('', home, name='posts'),
        path('home/', home, name='posts'),
        path('post/create/', create_post, name="create-post"),  
]
