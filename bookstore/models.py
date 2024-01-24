from django.db import models

# Create your models here.
class Author(models.Model):
    
    name = models.CharField(max_length = 30)
    email = models.EmailField(unique = True)
    bio = models.TextField()
    
    def __str__(self):
        return self.name
    
class Category(models.Model):
    
    Categories  = (
        ('Cyber security','Cyber security'),
        ('Front-end','Front-end'),
        ('Back-end','Back-end'),
        ('Big Data','Big Data'),
        ('AI','AI'),
        ('Data Engineer','Data Engineer'),
        ('Data Analysis','Data Analysis'),
    )
    name = models.CharField(max_length = 40,null=True, choices = Categories)
    
    
class Post(models.Model):
    pass


class Comment(models.Model):
    pass