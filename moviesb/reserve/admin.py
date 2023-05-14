from django.contrib import admin
from .models import customer,movie,Seat
# Register your models here.

admin.site.register(customer)
admin.site.register(movie)
admin.site.register(Seat)