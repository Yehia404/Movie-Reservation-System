from django.shortcuts import render , redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.views.generic import (
ListView,
CreateView,
UpdateView,
DeleteView
)
from .models import customer,contact,booking
from django.urls import reverse_lazy, reverse
from django.http import JsonResponse

# Create your views here.


def authenticate(email=None,password=None,**kwargs):
    try:
        Customer=customer.objects.get(email=email,password=password)
        return Customer
    except customer.DoesNotExist:
        return None
    




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
    if request.method == 'POST':
        # Get the form data
        day=request.POST['day']
        time=request.POST['time']
        Movie="Creed 3"
        price=request.POST['price']

        # Create a new Customer object and save it to the database
        Booking = booking(Day=day,time=time,movieName=Movie,price=price)
        Booking.save()
        Booking.Customer.add(Customer)
        msg="Happy Movie, Seats were booked successfully"
        # Redirect to a success page
        return render(request,'reserve/home.html',{
            "msg":msg
        })

    # If the request method is GET, just show the signup form
    return render(request, 'reserve/seats.html')

# -----------------------------------------------------------------------------------------

def shazamseat(request):
    if request.method == 'POST':
        # Get the form data
        day=request.POST['day']
        time=request.POST['time']
        Movie="Shazam! Fury Of The Kings"
        price=request.POST['price']

        # Create a new Customer object and save it to the database
        Booking = booking(Day=day,time=time,movieName=Movie,price=price)
        Booking.save()
        Booking.Customer.add(Customer)
        msg="Happy Movie, Seats were booked successfully"
        # Redirect to a success page
        return render(request,'reserve/home.html',{
            "msg":msg
        })

    # If the request method is GET, just show the signup form
    return render(request, 'reserve/shseats.html')

# --------------------------------------------------------------------------------
def wickseat(request):
    if request.method == 'POST':
        # Get the form data
        day=request.POST['day']
        time=request.POST['time']
        Movie="John Wick Chapter: 4"
        price=request.POST['price']

        # Create a new Customer object and save it to the database
        Booking = booking(Day=day,time=time,movieName=Movie,price=price)
        Booking.save()
        Booking.Customer.add(Customer)
        msg="Happy Movie, Seats were booked successfully"
        # Redirect to a success page
        return render(request,'reserve/home.html',{
            "msg":msg
        })

    # If the request method is GET, just show the signup form
    return render(request, 'reserve/jseats.html')
#--------------------------------------------------------------------------------------
def avatarseat(request):
    if request.method == 'POST':
        # Get the form data
        day=request.POST['day']
        time=request.POST['time']
        Movie="Avatar: The Way of Water"
        price=request.POST['price']

        # Create a new Customer object and save it to the database
        Booking = booking(Day=day,time=time,movieName=Movie,price=price)
        Booking.save()
        Booking.Customer.add(Customer)
        msg="Happy Movie, Seats were booked successfully"
        # Redirect to a success page
        return render(request,'reserve/home.html',{
            "msg":msg
        })

    # If the request method is GET, just show the signup form
    return render(request, 'reserve/avseats.html')


    



def login(request):
    if request.method== "POST":
        email = request.POST["email"]
        password = request.POST["password"]
        user=authenticate(email=email,password=password)
        
    
        if user is not None:
            global Customer
            Customer=user
            msg=f"Hello {Customer.firstName} {Customer.lastName}"
            return  render(request,'reserve/home.html',{
                "msg":msg
            })
        else:
            msg="Invalid Email or Password"
            return render(request,'reserve/Login.html',{
            "msg": msg
             })
    
    return render(request,'reserve/Login.html/')





def register(request):
    return render(request,'reserve/Register.html')
def contact_us(request):
    if request.method == 'POST':
        # Get the form data
        name = request.POST['name']
        email = request.POST['email']
        phone_number = request.POST['phonenumber']
        message = request.POST['message']

        # Create a new Customer object and save it to the database
        Contact = contact(name=name,email=email,phoneNumber=phone_number,message=message)
        Contact.save()
        msg="Contact Form Submitted"
        # Redirect to a success page
        return render(request,'reserve/home.html',{
            "msg":msg
        })

    # If the request method is GET, just show the signup form
    return render(request, 'reserve/contact.html')







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