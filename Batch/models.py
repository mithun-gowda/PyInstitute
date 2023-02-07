from django.db import models
from .validators import Minchar,Maxchar
from django.core.validators import MaxLengthValidator
# Create your models here.
class Subject(models.Model):
    sid=models.CharField(max_length=15,primary_key=True)
    subject=models.CharField(max_length=30)

    def __str__(self):
        return self.subject

class Trainer(models.Model):
    tid=models.CharField(max_length=10,primary_key=True,validators=[Minchar])
    name=models.CharField(max_length=40,validators=[Minchar,MaxLengthValidator(20)])
    salary=models.PositiveIntegerField()
    work_exp=models.PositiveIntegerField()
    Date_of_join=models.DateField()
    photo=models.ImageField(upload_to='timages')
    subject=models.ManyToManyField(Subject)

    def __str__(self):
        return self.name

class BatchDB(models.Model):
    bid=models.CharField(max_length=20,primary_key=True)
    Trainer=models.ForeignKey(Trainer,on_delete=models.CASCADE)
    subject=models.ForeignKey(Subject,on_delete=models.CASCADE)
    Time=models.TimeField()
    a=[['201','201'],['301','301'],['302','302'],['501','501'],['502','502'],['webonline','webonline']]
    room_no=models.CharField(max_length=10,choices=a)
    b=[['Online','online'],['offline','offline']]
    mode=models.CharField(max_length=10,choices=b)

    def __str__(self):
        return self.bid + self.subject
