
from os import name
from django.urls import path
from . import  views

urlpatterns = [
    path('home/',views.index,),
    path('signup/',views.fsignup,name='signup'),
    path('demo1',views.demo),
    path('login/kasaragod/',views.place14,name='kasaragod'),
    path('alapuzhabackwater',views.alappy),
    path('trail',views.trail),
    path('login/',views.flogin,name="login"),
    path('logout/',views.logout,name="logout"),
    path('login/user_booking/',views.booknow,name="user_booking"),
    path('cancel/<token2>',views.fcancel,name="cancel"),
   
   
    
]