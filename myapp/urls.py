from django.urls import path
from . import views

urlpatterns = [ 
    path("", views.index, name = "index"),
    path("dashboard.html/", views.dashboard, name = "dashboard"),
    path("add_expense.html/", views.add_expense, name="add_expense"),
    path("expenses.html/", views.expenses, name = "expenses"),
    path("edit_expense.html/<int:id>", views.edit_expense, name="edit_expense"),
    path("delete_expense/<int:id>", views.delete_expense, name="delete_expense")
]
