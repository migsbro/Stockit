from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse

# Create your models here.
class User(AbstractUser):
    phone_number = models.CharField(max_length=45, null=False)
    street_address = models.CharField(max_length=45, null=False)
    city = models.CharField(max_length=45, null=False)
    state = models.CharField(max_length=25, null=True)
    zipcode = models.CharField(max_length=5, null=True)


    @property
    def name(self):
        return self.first_name + " " + self.last_name
    
    @property
    def address(self):
        return self.street_address + ", " + self.city + ", " + self.state + " " + self.zipcode

    def get_absolute_url(self):
        return reverse("home:home")