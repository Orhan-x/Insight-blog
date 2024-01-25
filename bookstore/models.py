from datetime import timezone
from django.db import models

# Create your models here.
class Author(models.Model):
    
    name = models.CharField(max_length = 30)
    email = models.EmailField(unique = True)
    bio = models.TextField()
    
    def __str__(self):
        return self.name
class User(models.Model):
    name = models.CharField(max_length = 40)
    email = models.EmailField(unique = True)
    bio = models.TextField()
    password = models.CharField(max_length = 30)
    
class Category(models.Model):
    
    CATEGORIES  = (
        ('Cyber security','Cyber security'),
        ('Front-end','Front-end'),
        ('Back-end','Back-end'),
        ('Big Data','Big Data'),
        ('AI','AI'),
        ('Data Engineer','Data Engineer'),
        ('Data Analysis','Data Analysis'),
    )
    name = models.CharField(max_length = 40,null=True, choices = CATEGORIES)
    def __str__(self):
        return self.name
    
    
class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    
class Post(models.Model):
    #to add image
    title =  models.CharField(max_length = 100, null=True)
    author = models.ForeignKey(Author,null=True, on_delete=models.CASCADE)
    pub_date = models.DateTimeField(auto_now_add=True, null=True)
    content = models.TextField(null=True)
    categories = models.ManyToManyField(Category)
    tags = models.ManyToManyField(Tag)


class Comment(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    content = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    