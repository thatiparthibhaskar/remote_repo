from django.db import models

class Register(models.Model):
    name=models.CharField(max_length=40)
    fname=models.CharField(max_length=40)
    address=models.CharField(max_length=100)
    photo=models.ImageField(upload_to='images/')
    phonenumber=models.IntegerField(max_length=11,null=True)
    email=models.EmailField(max_length=50)


# Create your models here.
