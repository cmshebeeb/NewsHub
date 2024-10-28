'''
from django.shortcuts import render
from .models import Article

def index(request):
    category = request.GET.get('category')
    print("Available Categories:", Article.objects.values_list('category', flat=True).distinct())
    if category:
        print("Selected Category:", category)
        articles = Article.objects.filter(category=category)
        print("Filtered Articles:", articles)
    else:
        articles = Article.objects.all()
        print("All Articles:", articles)
    return render(request, 'news/index.html', {'articles': articles})
'''
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate,logout
from django.contrib.auth.forms import AuthenticationForm
from .forms import UserRegisterForm
from .models import Article
from django.contrib.auth.decorators import login_required

from .forms import UserPreferencesForm
from .models import UserPreferences

def index(request):
    category = request.GET.get('category')
    if category:
        articles = Article.objects.filter(category=category)
    else:
        articles = Article.objects.all()
    return render(request, 'news/index.html', {'articles': articles, 'category': category})

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            UserPreferences.objects.create(user=user)  # Create UserPreferences instance
            login(request, user)
            return redirect('index')
    else:
        form = UserRegisterForm()
    return render(request, 'news/register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')
    else:
        form = AuthenticationForm()
    return render(request, 'news/login.html', {'form': form})


@login_required
def preferences(request):
    user_pref, created = UserPreferences.objects.get_or_create(user=request.user)  # Ensures an instance exists
    if request.method == 'POST':
        form = UserPreferencesForm(request.POST, instance=user_pref)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = UserPreferencesForm(instance=user_pref)
    return render(request, 'news/preferences.html', {'form': form})


@login_required
def index(request):
    user_pref = UserPreferences.objects.filter(user=request.user).first()
    if user_pref and user_pref.category:
        articles = Article.objects.filter(category=user_pref.category)
    else:
        articles = Article.objects.all()
    return render(request, 'news/index.html', {'articles': articles, 'category': user_pref.category if user_pref else None})


def logout_view(request):
    logout(request)
    return redirect('index')


@login_required
def profile(request):
    return render(request, 'news/profile.html')


