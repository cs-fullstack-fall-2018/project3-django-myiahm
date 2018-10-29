from django.db import models
from datetime import datetime

from django.contrib.auth.models import User

class User(models.Model):
    name = models.CharField(max_length=200)
    currentBal = models.DecimalField(max_digits=15, decimal_places=2)
    emergency = models.DecimalField(max_digits=15,decimal_places=2)
    date = models.DateField(default=datetime.now)

    def __str__(self):
        return self.name




class Withdaraw(models.Model):
    name = models.CharField(max_length=200)
    amount = models.DecimalField(max_digits=4, decimal_places=2)
    date = models.DateField(default=datetime.now)
    def __str__(self):
        return self.name


class Deposit(models.Model):
    name = models.CharField(max_length=200)
    amount = models.DecimalField(max_digits=15, decimal_places=2)
    date = models.DateField(default=datetime.now)

    def __str__(self):
        return self.name


