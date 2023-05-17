from django.db import models

# Create your models here.
class Student(models.Model):
    sid=models.IntegerField()
    sname=models.CharField(max_length=100,primary_key=True)
    email=models.EmailField()
    sage=models.IntegerField()


    def __str__(self):
        return str(self.sid)