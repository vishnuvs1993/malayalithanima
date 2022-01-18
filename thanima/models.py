from django.db import models
from django.db.models.base import Model
from django.db.models.fields import IntegerField,BigIntegerField




# Create your models here.

class UserDetails(models.Model):
    first_name=models.CharField(max_length=30)
    second_name=models.CharField(max_length=20)
    password=models.CharField(max_length=40)
    email=models.EmailField()
    age=models.IntegerField()
    mobile=models.BigIntegerField()
    profile=models.CharField(max_length=100)



class UserBookings(models.Model):
    token=models.CharField(max_length=100,default=None)
    booking_hotel_name=models.CharField(max_length=30)
    booking_user_name=models.CharField(max_length=30)
    booking_check_in_date=models.DateField()
    booking_check_out_date=models.DateField()
    booking_check_in_time=models.TimeField()
    booking_check_out_time=models.TimeField()
    booking_fare_single=models.IntegerField()
    booking_fare_double=models.IntegerField()
    booking_room_countings=models.IntegerField()
    booking_person_countings=models.IntegerField()
    booking_room_type=models.CharField(max_length=30)
    booking_room_fare=models.IntegerField()
    booking_user_email=models.EmailField()
    booking_user_mobile=models.BigIntegerField()

 






