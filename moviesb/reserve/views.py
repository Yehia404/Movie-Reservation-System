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
    return render(request,'reserve/seats.html')



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
def contact(request):
    return render(request,'reserve/contact.html')
def admin(request):
    return render(request,'reserve/admin.html')

# def book_movie(request):
#     if request.is_ajax() and request.method == 'POST':
#         movie_id = request.POST.get('movie_id')
#         time = request.POST.get('time')
#         seats = request.POST.get('seats')
        
#         # save data to customer model
#         customer = request.user.customer # assuming you have a customer model with a foreign key to the user model
#         customer.movie = movie_id
#         customer.time = time
#         customer.seats = seats
#         customer.save()
        
#         # update seats availability in database
#         # assuming you have a seats model with a foreign key to the movie model
#         movie = Movie.objects.get(id=movie_id)
#         for seat in seats:
#             movie.seats.get(name=seat).available = False
#             movie.seats.get(name=seat).save()
        
#         return JsonResponse({'success': True})
#     else:
#         return JsonResponse({'success': False})


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