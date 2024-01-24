from django.db import models

# Create your models here.
class Usr(models.Model):
    name = models.CharField(max_length = 30)
    email = models.EmailField()
    passwd = models.CharField(min_length = 10)
    is_active = models.BooleanField(default=False)
    
    
    
class Post(models.Model):
    image = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=None)
    author = models.ForeignKey()
    
class Order(models.Model):
    pass