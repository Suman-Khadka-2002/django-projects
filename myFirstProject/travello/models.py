from django.db import models

# Create your models here.

class Destination(models.Model):
    # id : int  # database will automatically create id as primary key
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='pics')
    desc = models.TextField()
    price = models.IntegerField
    offer = models.BooleanField(default=False)  # for special offer