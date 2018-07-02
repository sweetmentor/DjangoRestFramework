from django.db import models

# Create your models here.
class Vehicle(models.Model):
    registration = models.CharField(max_length=15, blank=False, null=False)
    make = models.CharField(max_length=30, blank=False, null=False)
    model = models.CharField(max_length=30, blank=False, null=False)
    year = models.IntegerField(default=2018, blank=False, null=False)

    def __str__(self):
        return self.registration