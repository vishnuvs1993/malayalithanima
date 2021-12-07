from os import name
from django.urls import path
from . import  views

urlpatterns = [
   path('a_signup/',views.signup),
   path('a_home/',views.ahome),
   path('login/',views.login,name="login"),
   path('a_logout/',views.logout),
   path('add_event/',views.event_add,name="add_event"),
   path('user_bookings/',views.u_booking,name="user_bookings"),
   path('booking_user/', views.user_b_details,name='booking_user'),
   path('profile',views.fadmin,name="profile")

]