from django.shortcuts import render
from django.views.generic import (
ListView,
CreateView,
UpdateView,
DeleteView
)
from .models import customer
from django.urls import reverse_lazy
# Create your views here.

def home(request):
    return render(request,'reserve/home.html')
def movies(request):
    return render(request,'reserve/movie.html')
def booking(request):
    return render(request,'reserve/booking.html')
def seats(request):
    return render(request,'reserve/seats.html')
def login(request):
    return render(request,'reserve/Login.html')
def register(request):
    return render(request,'reserve/Register.html')
def contact(request):
    return render(request,'reserve/contact.html')
def admin(request):
    return render(request,'reserve/admin.html')



class CustomerListView(ListView):
    model= customer
    context_object_name='customers'
    
class CustomerCreateView(CreateView):
    model= customer
    fields=['firstName','lastName','email','phoneNumber','password']

class CustomerUpdateView(UpdateView):
    model= customer    
    fields=['firstName','lastName','email','phoneNumber','password']

class CustomerDeleteView(DeleteView):
    model= customer    
    context_object_name='customers'  
    success_url= reverse_lazy('admin-home')