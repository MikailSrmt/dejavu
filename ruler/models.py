import datetime

from django.db import models
from django.utils import timezone
# Create your models here.


class Intervals(models.Model):
    interval_name = models.CharField(max_length=200)
    interval_date = models.DateTimeField('date published')

    def was_recorded_recently(self):
        return self.interval_date >= timezone.now() - datetime.timedelta(days=1)

    def __str__(self):
        return self.interval_name


class IntervalApply(models.Model):
    interval_name = models.ForeignKey(Intervals, on_delete=models.CASCADE)
    interval_description = models.CharField(max_length=200)
    interval_counter = models.IntegerField(default=0)

    def __str__(self):
        return self.interval_name
