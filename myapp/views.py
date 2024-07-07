from django.shortcuts import render
from .models import CardItem
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url='/authentication/sign-in.html')
def index(request):
    return render(request, 'dashboard.html')
    
@login_required(login_url='/authentication/sign-in.html')
def dashboard(request):
    return render(request, 'dashboard.html')

