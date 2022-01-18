from django.db import models

# Create your models here.

class HotelDetails(models.Model):
    first_name=models.CharField(max_length=40)
    last_name=models.CharField(max_length=20)
    password=models.CharField(max_length=40)
    email=models.EmailField()
    hotel_name=models.CharField(max_length=40)
    hotel_description=models.CharField(max_length=256)
    price_single=models.IntegerField()
    price_double=models.IntegerField()
    age=models.IntegerField()
    mobile=models.BigIntegerField()
    district=models.CharField(max_length=40)
    ower_profile=models.CharField(max_length=100)
    hotel_picture1=models.CharField(max_length=100)
    hotel_picture2=models.CharField(max_length=100)
    hotel_picture3=models.CharField(max_length=100)


class HotalAvalilibity(models.Model):
    hotel_name=models.CharField(max_length=30)
    owner_name=models.CharField(max_length=30)
    today_date=models.DateField()
    avl_single_room=models.IntegerField()
    avl_double_room=models.IntegerField()
    email=models.EmailField()
    mobile=models.BigIntegerField()  
    
# class Demo(models.Model):
#     username=models.CharField(max_length=100)       
#  

# class UserDetails(models.Model):
#     first_name=models.CharField(max_length=30)
#     second_name=models.CharField(max_length=20)
#     password=models.CharField(max_length=40)
#     email=models.EmailField()
#     age=models.IntegerField()
#     mobile=models.BigIntegerField()
#     profile=models.CharField(max_length=100)



# class UserBookings(models.Model):
#     booking_hotel_name=models.CharField(max_length=30)
#     booking_user_name=models.CharField(max_length=30)
#     booking_check_in_date=models.DateField()
#     booking_check_out_date=models.DateField()
#     booking_check_in_time=models.TimeField()
#     booking_check_out_time=models.TimeField()
#     booking_fare_single=models.IntegerField()
#     booking_fare_double=models.IntegerField()
#     booking_room_countings=models.IntegerField()
#     booking_person_countings=models.IntegerField()
#     booking_room_type=models.CharField(max_length=30)
#     booking_room_fare=models.IntegerField()
#     booking_user_email=models.EmailField()
#     booking_user_mobile=models.BigIntegerField()
    
        
        
  
