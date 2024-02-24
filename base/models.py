from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Enforce user association
    title = models.CharField(max_length=255, unique=False)  # Descriptive title
    description = models.TextField(default="")  # Empty default
    like_count = models.PositiveIntegerField(default=0)  # Non-negative like count
    share_count = models.PositiveIntegerField(default=0)  # Non-negative share count
    created_at = models.DateTimeField(auto_now_add=True)  # Auto-set creation date
    
    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['created_at']
