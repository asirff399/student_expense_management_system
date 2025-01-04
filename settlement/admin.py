from django.contrib import admin
from .models import Settlement

# Register your models here.
class SettlementAdmin(admin.ModelAdmin):
    list_display = ['settlement','payee','payer','due_date','amount','payment_status']

admin.site.register(Settlement,SettlementAdmin)