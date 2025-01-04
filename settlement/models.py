from django.db import models
from .constants import PAYMENT_TYPE,SETTLEMENT_METHOD
from account.models import Student

# Create your models here.
class Settlement(models.Model):
    amount = models.DecimalField(max_digits=10,decimal_places=2)
    payment_status = models.CharField(max_length=20,choices=PAYMENT_TYPE)
    settlement = models.CharField(max_length=20,choices=SETTLEMENT_METHOD)
    due_date = models.DateField()
    payer = models.ForeignKey(Student,on_delete=models.CASCADE,related_name='settlement_made')
    payee = models.ForeignKey(Student,on_delete=models.CASCADE,related_name='settlement_recived') 

    def __str__(self):
        return f'{self.payee} - {self.payer} - {self.amount} - {self.payment_status}'
