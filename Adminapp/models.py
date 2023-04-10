from django.db import models

# Create your models here.
class managerdb(models.Model):
    name=models.CharField(max_length=25)
    address=models.CharField(max_length=50)
    phone=models.IntegerField()
    venuename=models.CharField(max_length=25)
    email=models.CharField(max_length=25)
    password=models.CharField(max_length=12)
    image=models.ImageField(upload_to="Manager")

class Venuedb(models.Model):
    venue_name=models.CharField(max_length=500)
    address=models.CharField(max_length=700)
    manager=models.CharField(max_length=100, default='')
    description=models.CharField(max_length=20)
    price=models.CharField(max_length=10)
    phone=models.IntegerField()
    email=models.CharField(max_length=20)
    venue_img=models.ImageField(upload_to='Venue', default='null.jpg')

class Contactdb(models.Model):
    name=models.CharField(max_length=30)
    c_email=models.CharField(max_length=20)
    message=models.CharField(max_length=500) 

class Servicedb(models.Model):
    sname=models.CharField(max_length=30)
    cost=models.CharField(max_length=30)
    service_image=models.ImageField(upload_to='Service', default='null.jpg')       


     
