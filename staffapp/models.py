from django.db import models

from django.contrib.auth.models import User
# Create your models here.

class StaffDB(User):
    mobile=models.PositiveBigIntegerField()
    a=[['Male','Male'],['Female','Female'],['Others','Others']]
    gender=models.CharField(max_length=10,choices=a)