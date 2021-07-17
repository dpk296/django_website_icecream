from django.db import models
# it will create database table which are present in the models class
class Buy(models.Model):
    item=models.CharField(max_length=120)
    quantity=models.CharField(max_length=120)
    status=models.CharField(max_length=120)
    username=models.CharField(max_length=100)
