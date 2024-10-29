from django.urls import path, include
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('preferences/', views.preferences, name='preferences'),
    path('profile/', views.profile, name='profile'),
    path('logout/', views.logout_view, name='logout'),
    path('password_change/', include('django.contrib.auth.urls')),
    path('password_reset/', include('django.contrib.auth.urls')),
    path('admin/show_queries/<int:article_id>/', views.show_queries, name='show_queries'),  # Ensure this line is present
]
