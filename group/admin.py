from django.contrib import admin
from .models import Group

# Register your models here.
class GroupAdmin(admin.ModelAdmin):
    list_display = ['name','group_type']

admin.site.register(Group,GroupAdmin) 