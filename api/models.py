from django.db import models
from django.contrib.auth.models import  AbstractUser
from datetime import datetime
from django.contrib.auth.models import User
from django.conf import settings

# Create your models here.
# user=get_user_model()
class User(AbstractUser):
    id=models.AutoField(primary_key=True,unique=True)
    username=models.CharField(max_length=255,unique=True)
    confirm_password=models.CharField(max_length=255)
    phone_number=models.IntegerField()
    is_staff=models.BooleanField(default=False)
    def __str__(self):
        return self.username
    
class Store(models.Model):
    id=models.AutoField(primary_key=True,unique=True)
    user=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,null=True,default='')
    medicine=models.CharField(max_length=255)
    price=models.IntegerField()
    quantity=models.IntegerField()
    expiry=models.DateField(default= datetime.now)
    def __str__(self):
        return self.medicine

class Sales(models.Model):
    id=models.AutoField(primary_key=True,unique=True)
    user=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,null=True)
    date =models.CharField(max_length=255)
    items=models.JSONField(max_length=1000,null=True,blank=True)
    total=models.IntegerField(blank=True,null=True)
    def __str__(self):
        return self.items

class Reciepts(models.Model):
    id=models.AutoField(primary_key=True,unique=True)
    user=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,null=True)
    date=models.DateField(default=datetime.now)
    amount=models.IntegerField()
    def __str__(self):
        return self.date

class Trash(models.Model):
    id=models.AutoField(primary_key=True,unique=True)
    user=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,null=True)
    medicine=models.CharField(max_length=255)
    expiry=models.DateField(default= datetime.now)



