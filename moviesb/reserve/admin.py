from django.contrib import admin
from .models import customer,movie,Seat,booking,contact
# Register your models here.

admin.site.register(customer)
admin.site.register(movie)
admin.site.register(Seat)
admin.site.register(booking)
admin.site.register(contact)