from django.db import models

# Create your models here.
class data101(models.Model):
    datetime=models.CharField(max_length=100)
    close=models.FloatField(default=True)
    high=models.FloatField(default=True)
    low=models.FloatField(default=True)
    open=models.FloatField(default=True)
    volume=models.IntegerField(default=True)
    instrument=models.CharField(max_length=100,null=True)
