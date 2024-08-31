from . import views
from .views import UsernameValidationView, EmailValidationView, RegistrationView, VerificationView, LoginView, LogoutView
from django.urls import path
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('validate-username', csrf_exempt(UsernameValidationView.as_view()), name = 'validate_username'),
    path('validate-email', csrf_exempt(EmailValidationView.as_view()), name = 'validate_email'),
    path('sign-up.html/', RegistrationView.as_view(), name = "sign-up"),
    path('sign-in.html/', LoginView.as_view(), name = "sign-in"),
    path('activate/<uidb64>/<token>', VerificationView.as_view(), name = "activate"),
    path('logout', LogoutView.as_view(), name = "logout"),
]