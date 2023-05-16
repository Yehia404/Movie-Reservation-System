from django.contrib import admin
from .models import customer,movie,Seat,booking
# Register your models here.

admin.site.register(customer)
admin.site.register(movie)
admin.site.register(Seat)
admin.site.register(booking)