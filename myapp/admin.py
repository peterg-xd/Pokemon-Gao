from django.contrib import admin
from .models import Expense, Category

# Register your models here.

class ExpenseAdmin(admin.ModelAdmin):
    list_display = ('amount', 'description', 'owner', 'category', 'date')
    search_fields = ('amount', 'description', 'category', 'date',)
    list_per_page = 10

admin.site.register(Expense, ExpenseAdmin)
admin.site.register(Category)
