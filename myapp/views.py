from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import Category, Expense
from django.contrib import messages
from django.core.paginator import Paginator
import json
from django.http import JsonResponse

def search_expenses(request):
    if request.method == 'POST':
        search_str = json.loads(request.body).get('searchText')

        expenses=Expense.objects.filter(
            amount__istartswith=search_str, owner=request.user) | Expense.objects.filter(
            date__istartswith=search_str, owner=request.user) | Expense.objects.filter(
            description__icontains=search_str, owner=request.user) | Expense.objects.filter(
            category__icontains=search_str, owner=request.user)
        
        data=expenses.values()
        return JsonResponse(list(data), safe=False)

# Create your views here.

@login_required(login_url='/authentication/sign-in.html')
def index(request):
    return render(request, 'dashboard.html')
    
@login_required(login_url='/authentication/sign-in.html')
def dashboard(request):
    return render(request, 'dashboard.html')



def expenses(request):  
    categories = Category.objects.all()
    expenses = Expense.objects.filter(owner=request.user)
    paginator = Paginator(expenses, 5)
    page_number = request.GET.get('page')
    page_obj = Paginator.get_page(paginator, page_number)
    context = {
        'expenses': expenses,
        'page_obj': page_obj
    }
    return render(request, 'expenses.html', context) 

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
    
        if not amount.isnumeric():
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
        return redirect('expenses')


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
            return render(request, 'add_expense.html', context)
    
        if not amount.isnumeric():
            messages.error(request, 'Amount must be a value')
            return render(request, 'edit_expense.html', context)
        
        if not description:
            messages.error(request, 'Description is required')
            return render(request, 'edit_expense.html', context)
    
        if date:
            expense.date = date
        expense.owner = request.user
        expense.amount = amount
        expense.category = expense.category
        expense.description = description
        expense.save()

        messages.success(request, "Expense updated succesfully")
        return redirect('expenses')
    

def delete_expense(request, id):
    expense = Expense.objects.get(pk=id)
    expense.delete()
    messages.success(request, "Expense deleted")
    return redirect('expenses')