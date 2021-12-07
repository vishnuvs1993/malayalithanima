from os import name
from django.urls import path
from . import  views

urlpatterns = [
    path('h_signup/',views.hsignup,name='h_signup'),
    path('hotel_details/',views.hotel_statics,name="hotel_details"),
    path('h_login/',views.flogin,name="h_login"),
    path('logout/',views.logout,name="logout"),
    path('hotel_avl/',views.fhotal_avl,name="hotel_avl")
]