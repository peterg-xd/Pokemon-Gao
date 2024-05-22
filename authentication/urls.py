from . import views
from .views import UsernameValidationView, EmailValidationView
from django.urls import path
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('validate-username', csrf_exempt(UsernameValidationView.as_view()), name = 'validate_username'),
    path('validate-email', csrf_exempt(EmailValidationView.as_view()), name = 'validate_email'),
    path("sign-up.html/", views.sign_up, name = "sign-up"),
    path("sign-in.html/", views.sign_in, name = "sign-in"),
]