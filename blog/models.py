from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    
    title = models.CharField(max_length=120)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    publish_at = models.DateTimeField(auto_now=True)
    is_updated = models.BooleanField(default=False)
    
    def save(self, *args, **kwargs):
        
        if self.pk : 
            try:
                old_instance = Post.objects.get(pk = self.pk)
                if old_instance.title != self.title or old_instance.content != self.content:
                    self.is_updated = True
            except Post.DoesNotExist:
                pass
        super().save(self, *args, **kwargs)
        
            