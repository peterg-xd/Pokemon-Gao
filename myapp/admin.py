from django.contrib import admin
from .models import Expense, Category, Income, Source

# Register your models here.

class ExpenseAdmin(admin.ModelAdmin):
    list_display = ('amount', 'description', 'owner', 'category', 'date')
    search_fields = ('amount', 'description', 'category', 'date',)
    list_per_page = 10

class IncomeAdmin(admin.ModelAdmin):
    list_display = ('amount', 'description', 'owner', 'source', 'date')
    search_fields = ('amount', 'description', 'source', 'date',)
    list_per_page = 10

admin.site.register(Expense, ExpenseAdmin)
admin.site.register(Category)
admin.site.register(Income, IncomeAdmin)
admin.site.register(Source)
