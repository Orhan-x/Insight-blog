from django.db import models
from uuid import uuid4
from users.models import User
        
class Post(models.Model):
    id = models.UUIDField(primary_key=True, default = uuid4)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = models.TextField()
    posted_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title