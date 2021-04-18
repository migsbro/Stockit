from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    phone_number = models.CharField(max_length=45, null=False)
    address = models.CharField(max_length=45, null=False)
    city = models.CharField(max_length=45, null=False)
    state = models.CharField(max_length=25, null=True)
    zipcode = models.CharField(max_length=5, null=True)