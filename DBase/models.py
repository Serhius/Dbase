# -*- coding: utf-8 -*-
from django.db import models

class DBase(models.Model):
    class Meta():
        db_table = "dbase"
    number = models.CharField(max_length = 20)
    oper = models.CharField(max_length = 4)
    date = models.DateField(blank=True)
    time = models.TimeField()
    stat = models.CharField(max_length = 5)
    reason = models.CharField(max_length = 5)