from django.contrib.auth.models import AbstractUser
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.utils.translation import gettext_lazy as _

class User(AbstractUser):
    # You can add extra fields here if needed
    is_customer = models.BooleanField(default=False)
    is_fundi = models.BooleanField(default=False)
    is_contractor = models.BooleanField(default=False)
    is_professional = models.BooleanField(default=False)
    is_hardware = models.BooleanField(default=False)

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = PhoneNumberField(_("phone number"), blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=False)  
    location = models.CharField(max_length=255, blank=True, null=False) 
    organization_name = models.CharField(max_length=255, blank=True, null=True)  # optional

class Fundi(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Add fundi specific fields here

class Contractor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    certifications = models.FileField(upload_to='certifications/')
    portfolio_images = models.ImageField(upload_to='portfolio/')
    # add other fields if needed

class Professional(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    certifications = models.FileField(upload_to='certifications/')
    portfolio_images = models.ImageField(upload_to='portfolio/')
    # add other fields if needed

class Hardware(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # add hardware supplier specific fields
