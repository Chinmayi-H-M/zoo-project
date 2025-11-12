from django.db import models


class Animals(models.Model):
    name=models.CharField(max_length=20)
    species=models.CharField(max_length=10)
    scientific_name=models.CharField(max_length=20)
    habitat=models.CharField(max_length=40)
    age=models.BigIntegerField()

class Donaters(models.Model):
    name=models.CharField()
    donated_amount=models.FloatField(max_length=10, unique=True)
    date_donated=models.DateField()
    email=models.CharField(max_length=40)
    phone=models.BigIntegerField()

class Caretakers(models.Model):
    name=models.TextField()
    experiance_years=models.CharField(max_length=10)
    shift_time=models.TimeField()
    assigned_animals=models.CharField(max_length=40)
    phone=models.BigIntegerField()



