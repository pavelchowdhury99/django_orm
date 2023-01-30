from django.db import models
from datetime import datetime


# Create your models here.
class SampleTable(models.Model):
    char_field = models.CharField(max_length=200)
    int_field = models.IntegerField(default=1)
    date_field = models.DateField(default=datetime.now().date())
    bool_field = models.BooleanField(default=True)
