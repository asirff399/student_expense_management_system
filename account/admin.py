from django.contrib import admin
from .models import Student

# Register your models here.
class StudentAdmin(admin.ModelAdmin):
    list_display = ['user','college','semester','default_payment_methods']

admin.site.register(Student,StudentAdmin) 