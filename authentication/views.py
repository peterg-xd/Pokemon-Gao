from django.shortcuts import render
from django.views import View
from django.http import JsonResponse
import json

# Create your views here.

class UsernameValidationView(View): 
    def post(self, request):
        data = json.loads(request.body)
        username = data['username']

        if not str(username).isalnum():
            return JsonResponse({'username error': 'username should only contain alphanumeric characters'})
        return JsonResponse('username_valid', True)
    
def sign_up(request): 
    return render(request, 'sign-up.html')

def sign_in(request):
    return render(request, 'sign-in.html')