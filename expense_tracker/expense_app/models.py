from django.db import models


class User(models.Model):
    name = models.CharField(max_length=200)
    currentBal = models.DecimalField(max_digits=15, decimal_places=2)
    emergency = models.DecimalField(max_digits=15,decimal_places=2)
    date = models.DateField()

    def __str__(self):
        return self.name
