from django.db import models


# Create your models here.


class Person(models.Model):
    Name = models.CharField(max_length=20)
    Age= models.IntegerField()
    track= models.CharField(max_length=20)
