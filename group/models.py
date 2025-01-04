from django.db import models
from .constants import GROUP_TYPE
from account.models import Student

# Create your models here.
class Group(models.Model):
    name = models.CharField(max_length=100)
    group_type = models.CharField(max_length=30,choices=GROUP_TYPE)
    members =models.ManyToManyField(Student) 

    def __str__(self):
        return self.name
