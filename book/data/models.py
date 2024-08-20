from django.db import models
from data.models import *
# Create your models here.
class Author(models.Model):
    name=models.CharField(max_length=30)
    age=models.IntegerField()
    rate=models.IntegerField()



class Book(models.Model):
    title=models.CharField(max_length=30)
    price=models.IntegerField()
    genre=models.CharField(max_length=50)
    author=models.ForeignKey('Author',on_delete=models.CASCADE)







    def __str__(self):
        return self.title
