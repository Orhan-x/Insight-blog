from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    avatar = models.TextField(default='/media/users/default-avatar.png')
    about = models.TextField(null=True, blank=True, max_length="300")
    email = models.EmailField(null=False, unique=True)

    def save(self, *args, **kwargs):
        self.username = self.username.lower()
        super().save(*args, **kwargs)