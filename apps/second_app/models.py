from __future__ import unicode_literals
from datetime import datetime
from django.db import models
from ..user_app.models import userReg
# class event_manager(models.Manager):
#     def manager(self,request):

class active(models.Model):
    title=models.CharField(max_length=200)
    start=models.DateField(auto_now_add=False)
    fin=models.TimeField(auto_now=False)
    description=models.CharField(max_length=200)
    activity=models.ForeignKey(userReg,related_name='active')
    join=models.ManyToManyField(userReg,related_name='joiner')
    # objects=event_manager()