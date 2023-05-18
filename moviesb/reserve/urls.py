from django.urls import path
from . import views
from .views import (
CustomerListView,
CustomerCreateView,
CustomerUpdateView,
CustomerDeleteView
)

urlpatterns = [
    path('', views.home,name="home"),
    path('movies/',views.movies,name="movies"),
    path('creed/',views.creed,name="creed"),
    path('shazam/',views.shazam,name="shazam"),
    path('avatar/',views.avatar,name="avatar"),
    path('johnwick/',views.wick,name="wick"),
    path('antman/',views.ant,name="ant"),
    path('maneater/',views.maneater,name="maneater"),
    path('seats/',views.seats,name="seats"),
    path('login/',views.login,name="login"),
    path('register/',views.register,name="register"),
    path('contact/',views.contact_us,name="contact"),
    



    path('home/admin/', views.admin,name="admin-home"),
    path('reserve/list/',CustomerListView.as_view(),name="customers-list"),
    path('reserve/create/',CustomerCreateView.as_view(),name="customers-create"),
    path('reserve/update/<int:pk>',CustomerUpdateView.as_view(),name="customers-update"),
    path('reserve/delete/<int:pk>',CustomerDeleteView.as_view(),name="customers-delete")
]