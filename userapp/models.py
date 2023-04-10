from django.db import models
from Adminapp.models import *
# Create your models here.

class Register(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    email = models.EmailField(max_length=20)
    phone = models.CharField(max_length=10)

class Booking(models.Model):
    venueid = models.ForeignKey(Venuedb, on_delete=models.CASCADE)
    venue = models.CharField(max_length=30, default='')
    userid = models.ForeignKey(Register, on_delete=models.CASCADE)
    selected_service = models.CharField(max_length=20, default='')
    service_name = models.CharField(max_length=10,default='')
    date_time = models.DateTimeField()
    purpose = models.CharField(max_length=20)
    service_amount = models.IntegerField(default=0)
    status = models.IntegerField(default=0)
    total = models.IntegerField(default=0)

class Confirmation(models.Model):
    userid = models.ForeignKey(Register, on_delete=models.CASCADE)
    bookingid = models.ForeignKey(Booking, on_delete=models.CASCADE)