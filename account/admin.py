from django.contrib import admin
from account.models import Student

# Register your models here.
class AccountAdmin(admin.ModelAdmin):
    list_display = ['user','college','semester','default_payment_methods']