from django.urls import path
from . import views
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [ 
    path("", views.index, name = "index"),
    path("dashboard.html/", views.dashboard, name = "dashboard"),
    path("transactions.html/", views.transactions, name = "transactions"),
    path("add_expense.html/", views.add_expense, name="add_expense"),
    path("edit_expense.html/<int:id>", views.edit_expense, name="edit_expense"),
    path("delete_expense/<int:id>", views.delete_expense, name="delete_expense"),
    path("search_expenses", csrf_exempt(views.search_expenses), name="search_expenses"),
    path("add_income.html/", views.add_income, name="add_income"),
    path("edit_income.html/<int:id>", views.edit_income, name="edit_income"),
    path("delete_income/<int:id>", views.delete_income, name="delete_income"),
    path("search_income", csrf_exempt(views.search_income), name="search_income"),
]
