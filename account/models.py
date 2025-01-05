from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Student(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    class_no = models.PositiveIntegerField(null=True)
    roll_no = models.PositiveIntegerField(null=True)
    college = models.CharField(max_length=100)
    semester = models.PositiveIntegerField(null=True)
    default_payment_methods = models.CharField(max_length=100)  

    def __str__(self):
        return self.user.get_full_name()
