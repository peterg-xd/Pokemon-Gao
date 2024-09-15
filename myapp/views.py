from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import Category, Expense, Income, Source
from django.contrib import messages
from django.core.paginator import Paginator
import json
from django.http import JsonResponse
from userpreferences.models import UserPreference
from django.db.models import Q

def search_expenses(request):
    if request.method == 'POST':
        search_str = json.loads(request.body).get('searchText')

        expenses = Expense.objects.filter(
            Q(amount__istartswith=search_str) |
            Q(date__istartswith=search_str) |
            Q(description__icontains=search_str) |
            Q(category__icontains=search_str),
            owner=request.user
        )
        
        data=expenses.values()
        return JsonResponse(list(data), safe=False)

def search_income(request):
    if request.method == 'POST':
        search_str = json.loads(request.body).get('incomeSearchText')

        incomes = Income.objects.filter(
            Q(amount__istartswith=search_str) |
            Q(date__istartswith=search_str) |
            Q(description__icontains=search_str) |
            Q(source__icontains=search_str),
            owner=request.user
        )
        
        data=incomes.values()
        return JsonResponse(list(data), safe=False)

# Create your views here.

@login_required(login_url='/authentication/sign-in.html')
def index(request):
    return render(request, 'dashboard.html')
    
@login_required(login_url='/authentication/sign-in.html')
def dashboard(request):
    return render(request, 'dashboard.html')


@login_required(login_url='/authentication/sign-in.html')
def transactions(request):  
    categories = Category.objects.all()
    expenses = Expense.objects.filter(owner=request.user)
    expense_paginator = Paginator(expenses, 5)
    expense_page_number = request.GET.get('page')
    expense_page_obj = Paginator.get_page(expense_paginator, expense_page_number)

    incomes = Income.objects.filter(owner=request.user)
    income_paginator = Paginator(incomes, 5)
    income_page_number = request.GET.get('page')
    income_page_obj = Paginator.get_page(income_paginator, income_page_number)

    currency = "None"
    if UserPreference.objects.filter(user = request.user).exists():
        currency = UserPreference.objects.get(user=request.user).currency
    context = {
        'expenses': expenses,
        'incomes': incomes,
        'expense_page_obj': expense_page_obj,
        'income_page_obj': income_page_obj,
        'currency': currency
    }
    return render(request, 'transactions.html', context) 

@login_required(login_url='/authentication/sign-in.html')
def add_expense(request): 
    categories = Category.objects.all()
    context = {
        'categories': categories,
        'values': request.POST
    }
    if request.method == 'GET':
        return render(request, 'add_expense.html', context)

    if request.method == 'POST':
        amount = request.POST['amount']
        description = request.POST['description']
        date = request.POST['expense_date']
        category = request.POST['category']

        if not amount:
            messages.error(request, 'Amount is required')
            return render(request, 'add_expense.html', context)
    
        if not is_number(amount):
            messages.error(request, 'Amount must be a value')
            return render(request, 'add_expense.html', context)
        
        if not description:
            messages.error(request, 'Description is required')
            return render(request, 'add_expense.html', context)
    
        if not date:
            Expense.objects.create(owner=request.user, amount=amount, category=category, description=description)
        else:
            Expense.objects.create(owner=request.user, amount=amount, date=date, category=category, description=description)
        messages.success(request, "Expense saved successfully")
        return redirect('transactions')
    
@login_required(login_url='/authentication/sign-in.html')
def add_income(request): 
    sources = Source.objects.all()
    context = {
        'sources': sources,
        'values': request.POST
    }
    if request.method == 'GET':
        return render(request, 'add_income.html', context)

    if request.method == 'POST':
        amount = request.POST['amount']
        description = request.POST['description']
        date = request.POST['income_date']
        source = request.POST['source']

        if not amount:
            messages.error(request, 'Amount is required')
            return render(request, 'add_income.html', context)
    
        if not is_number(amount):
            messages.error(request, 'Amount must be a value')
            return render(request, 'add_income.html', context)
        
        if not description:
            messages.error(request, 'Description is required')
            return render(request, 'add_income.html', context)
    
        if not date:
            Income.objects.create(owner=request.user, amount=amount, source=source, description=description)
        else:
            Income.objects.create(owner=request.user, amount=amount, date=date, source=source, description=description)
        messages.success(request, "Income saved successfully")
        return redirect('transactions')

@login_required(login_url='/authentication/sign-in.html')
def edit_expense(request, id):
    expense = Expense.objects.get(pk=id)
    categories = Category.objects.all()

    context = {
        'expense': expense,
        'values': expense,
        'categories': categories
    }
    if request.method == 'GET':
        return render(request, "edit_expense.html", context)
    elif request.method == 'POST':
        amount = request.POST['amount']
        description = request.POST['description']
        date = request.POST['expense_date']
        category = request.POST['category']

        if not amount:
            messages.error(request, 'Amount is required')
            return render(request, 'edit_expense.html', context)
    
        if not is_number(amount):
            messages.error(request, 'Amount must be a value')
            return render(request, 'edit_expense.html', context)
        
        if not description:
            messages.error(request, 'Description is required')
            return render(request, 'edit_expense.html', context)
    
        if date:
            expense.date = date
        expense.owner = request.user
        expense.amount = amount
        expense.category = category
        expense.description = description
        expense.save()

        messages.success(request, "Expense updated successfully")
        return redirect('transactions')
    
@login_required(login_url='/authentication/sign-in.html')
def edit_income(request, id):
    income = Income.objects.get(pk=id)
    sources = Source.objects.all()

    context = {
        'income': income,
        'values': income,
        'sources': sources
    }
    if request.method == 'GET':
        return render(request, "edit_income.html", context)
    elif request.method == 'POST':
        amount = request.POST['amount']
        description = request.POST['description']
        date = request.POST['income_date']
        source = request.POST['source']

        if not amount:
            messages.error(request, 'Amount is required')
            return render(request, 'edit_income.html', context)
    
        if not is_number(amount):
            messages.error(request, 'Amount must be a value')
            return render(request, 'edit_income.html', context)
        
        if not description:
            messages.error(request, 'Description is required')
            return render(request, 'edit_income.html', context)
    
        if date:
            income.date = date
        income.owner = request.user
        income.amount = amount
        income.source = source
        income.description = description
        income.save()

        messages.success(request, "Income updated successfully")
        return redirect('transactions')

def delete_expense(request, id):
    expense = Expense.objects.get(pk=id)
    expense.delete()
    messages.success(request, "Expense deleted")
    return redirect('transactions')

def delete_income(request, id):
    income = Income.objects.get(pk=id)
    income.delete()
    messages.success(request, "Income deleted")
    return redirect('transactions')

def is_number(s):
    try:
        # Attempt to convert the string to a float
        float(s)  
        return True
    except ValueError:
        return False