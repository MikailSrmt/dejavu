from django.db import models
# Create your models here.


class Intervals(models.Model):
    interval_name = models.CharField(max_length=200)
    interval_date = models.DateTimeField('date published')


class IntervalApply(models.Model):
    interval_name = models.ForeignKey(Intervals, on_delete=models.CASCADE)
    interval_description = models.CharField(max_length=200)
    interval_counter = models.IntegerField(default=0)
