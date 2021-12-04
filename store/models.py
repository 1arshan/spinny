from django.db import models
from  django.contrib.auth.models import User

class Box(models.Model):
    length=models.DecimalField(max_digits=10,decimal_places=2)
    width = models.DecimalField(max_digits=10, decimal_places=2)
    height = models.DecimalField(max_digits=10, decimal_places=2)
    area = models.DecimalField(max_digits=10, decimal_places=2,blank=True)
    volume = models.DecimalField(max_digits=10, decimal_places=2,blank=True)
    created_by=models.ForeignKey(User,on_delete=models.PROTECT,blank=True)
    last_updated=models.DateTimeField(auto_now=True)

