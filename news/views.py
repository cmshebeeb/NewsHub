from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from .forms import UserRegisterForm, SearchForm, UserPreferencesForm
from .models import Article, UserPreferences
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator



def index(request):
    form = SearchForm()
    query = request.GET.get('query')
    category = request.GET.get('category')
    categories = Article.objects.values_list('category', flat=True).distinct().order_by('category')
    
    if query:
        articles = Article.objects.filter(title__icontains=query).order_by('id')
    elif category and category != "All News":
        articles = Article.objects.filter(category=category).order_by('id')
    else:
        if request.user.is_authenticated:
            user_pref = UserPreferences.objects.filter(user=request.user).first()
            if user_pref and user_pref.category:
                articles = Article.objects.filter(category=user_pref.category).order_by('id')
            else:
                articles = Article.objects.all().order_by('id')
        else:
            articles = Article.objects.all().order_by('id')
    
    paginator = Paginator(articles, 5)  # Show 5 articles per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'news/index.html', {
        'page_obj': page_obj, 
        'form': form, 
        'category': category if category else 'All News',
        'categories': categories
    })
    

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

def logout_view(request):
    logout(request)
    return redirect('index')

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
def profile(request):
    return render(request, 'news/profile.html')



