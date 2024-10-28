from django.contrib import admin
from .models import Article, UserPreferences

admin.site.register(Article)
admin.site.register(UserPreferences)
