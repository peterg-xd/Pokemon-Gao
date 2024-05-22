from django.shortcuts import render
from django.views import View
from django.http import JsonResponse
import json
from django.contrib.auth.models import User
from validate_email import validate_email

# Create your views here.

class UsernameValidationView(View): 
    def post(self, request):
        data = json.loads(request.body)
        username = data['username']

        if not str(username).isalnum():
            return JsonResponse({'username_error': 'username should only contain alphanumeric characters'}, status=400)
        if User.objects.filter(username=username).exists():
            return JsonResponse({'username_error': 'username in use, choose another one'}, status=409)
        
        return JsonResponse({'username_valid': True})
    

class EmailValidationView(View): 
    def post(self, request):
        data = json.loads(request.body)
        email = data['email']

        if not validate_email(email):
            return JsonResponse({'email_error': 'email is Invalid'}, status=400)
        if User.objects.filter(email=email).exists():
            return JsonResponse({'email_error': 'email in use, choose another one'}, status=409)
        
        return JsonResponse({'email_valid': True})

    
def sign_up(request): 
    return render(request, 'sign-up.html')

def sign_in(request):
    return render(request, 'sign-in.html')