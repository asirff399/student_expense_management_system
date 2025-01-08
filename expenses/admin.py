from django.contrib import admin
from .models import Expenses

# Register your models here.
class ExpensesAdmin(admin.ModelAdmin):
    list_display = ['amount','category','split_type','date','receipt_image','paid_by','group']

admin.site.register(Expenses,ExpensesAdmin)