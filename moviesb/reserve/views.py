from django.shortcuts import render , redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
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
def creed(request):
    return render(request,'reserve/creed.html')
def shazam(request):
    return render(request,'reserve/shazam.html')
def avatar(request):
    return render(request,'reserve/avatar.html')
def wick(request):
    return render(request,'reserve/wick.html')
def ant(request):
    return render(request,'reserve/antman.html')
def maneater(request):
    return render(request,'reserve/maneater.html')
def seats(request):
    return render(request,'reserve/seats.html')



def login(request):

    # email = request.POST["email"]
    # password = request.POST["password"]
    
    # customers=customer.objects.all()
    # for obj in customers:
    #     if obj.email == email and obj.password == password :
    #         return render(request,'reserve/home.html/<int:pk>')

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