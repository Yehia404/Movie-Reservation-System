from django.db import models
from django.urls import reverse
from django.core.validators import MinLengthValidator
# Create your models here.

class customer(models.Model):
    firstName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phoneNumber= models.CharField(max_length=11,validators=[MinLengthValidator(11)])
    password = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name
    
    def get_absolute_url(self):
        return reverse('admin-home')