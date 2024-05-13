from django.shortcuts import render
from .models import CardItem
from django.contrib.auth.models import User

# Create your views here.

def index(request):
    return render(request, 'dashboard.html')

def dashboard(request):
    return render(request, 'dashboard.html')

