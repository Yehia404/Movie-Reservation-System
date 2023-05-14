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
        return f"{self.firstName} {self.lastName}"
    
    def get_absolute_url(self):
        return reverse('home')
    
    
    
class movie(models.Model):
    movieName=models.CharField(max_length=100)
    bookedSeats=models.ManyToManyField('Seat',null=True,blank=True)

    def __str__(self) -> str:
        return self.movieName
    

class Seat(models.Model):
    seatNo=models.CharField(max_length=2,validators=[MinLengthValidator(2)])
    occupied=models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.seatNo

