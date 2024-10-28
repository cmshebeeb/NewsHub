from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Article(models.Model):
    category = models.CharField(max_length=100)
    title = models.CharField(max_length=200)
    content = models.TextField()

    def __str__(self):
        return self.title
    
class UserPreferences(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    category = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.user.username} - {self.category}"