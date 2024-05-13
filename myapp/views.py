from django.shortcuts import render, HttpResponse
from .models import CardItem

# Create your views here.

def index(request):
    return render(request, 'index.html')

def dashboard(request):
    return render(request, 'dashboard.html')

def sign_in(request):
    return render(request, 'sign-in.html')