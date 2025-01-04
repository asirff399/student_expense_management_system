from django.db import models
from .constants import SPLITE_TYPE
from category.models import Category
from account.models import Student
from group.models import Group

# Create your models here.
class Expenses(models.Model):
    amount = models.DecimalField(max_digits=10,decimal_places=2)
    category = models.ForeignKey(Category,on_delete=models.SET_NULL,null=True)
    splite_type = models.CharField(max_length=20,choices=SPLITE_TYPE)
    date = models.DateField()
    receipt_image = models.CharField(max_length=100)
    paid_by = models.ForeignKey(Student,on_delete=models.CASCADE)
    group = models.ForeignKey(Group,on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.amount} - {self.category.name}'

