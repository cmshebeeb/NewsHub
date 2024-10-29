from django.db import models
from django.contrib.auth.models import User

class Article(models.Model):
    category = models.CharField(max_length=100)
    title = models.CharField(max_length=200)
    content = models.TextField()

    def save(self, *args, **kwargs):
        self.category = self.category.capitalize()
        super(Article, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

class UserPreferences(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    category = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.user.username} - {self.category}"

class Query(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    user_query = models.CharField(max_length=200)

    def __str__(self):
        return self.user_query
