from . import views
from .views import UsernameValidationView
from django.urls import path

urlpatterns = [
    path('validate-username', UsernameValidationView.as_view(), name = 'validate_username'),
    path("sign-up.html/", views.sign_up, name = "sign-up"),
    path("sign-in.html/", views.sign_in, name = "sign-in"),
]