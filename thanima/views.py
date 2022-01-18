from dataclasses import fields
import json
from lib2to3.pgen2 import token
from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from . models import *
from random import random
from django.core.files.storage import FileSystemStorage
from hotel.models import * 
from django.core.mail import send_mail
from smtplib import SMTP
import smtplib
import _json
from django.core.serializers import serialize
from django.views.generic import View
from django.contrib.auth.tokens import default_token_generator
import random


def index(request):
     
    k_obj=HotelDetails.objects.all().filter(district='01')
           
    return render(request,'home.html',{'k14':k_obj})


def fsignup(request):
    try:
        user_mail=request.POST['u_email']
        obj1=UserDetails.objects.filter(email=user_mail).exists()
        if obj1==False:
            user_first=request.POST['u_first_name']
            user_second=request.POST['u_second_name']
            user_password=request.POST['u_password']
            user_age=request.POST['u_age']
            user_phone=request.POST['u_phone_number']
            user_file=request.FILES['u_file']
            file_name=str(random())+user_file.name
            file_obj=FileSystemStorage()
            file_obj.save(file_name,user_file)
            user_obj=UserDetails(first_name=user_first,second_name=user_second,password=user_password,email=user_mail,age=user_age,mobile=user_phone,profile=file_name)
            user_obj.save()
            return render(request,'home.html')
    except Exception as error:
        print(error)
    return render(request,'customerlogin.html')

def flogin(request):
    try:
        if request.method=='POST':
            login_email=request.POST['l_email']
            login_password=request.POST['l_password']
            login_obj=UserDetails.objects.get(email=login_email,password=login_password)
          
            request.session['user_session']=login_obj.id
            session_obj=request.session['user_session']
            user_obj1=UserDetails.objects.get(id=session_obj)
            print(user_obj1.first_name)
            print(user_obj1.profile)
            return render(request,'home.html',{'display':user_obj1})
    except Exception as error:
        print(error)        
     

    return render(request,'home.html',{"msg":"plese check your email and password"})


def demo(request):
    return render(request,'demo.html')


def place14(request):
   
    
    k_obj=HotelDetails.objects.all().filter(district='01')
    k_obj1=list(k_obj)
  
    
    
   
    return render(request,'kl14.html',{'k14':k_obj1})  


def alappy(request):
    return render(request,'alapuzhabackwater.html')   


def trail(request):
    return render(request,'trail.html')      

def logout(request):
    del request.session['user_session']
    print("sucess")
    return render(request,'home.html')    

def booknow(request):
    try:
        if request.method=='POST':
            print("enter")
            token1=str(random.random()).split('.')
            token2=token1[1]
            hotel_name_booking=request.POST['book_hotel_name'] 
            print(hotel_name_booking)
            user_name_booking=request.POST['book_user_name']
            check_in_date_booking=request.POST['book_check_in_date'] 
            
            check_out_date_booking=request.POST['book_check_out_date']
            print(check_out_date_booking)
            check_in_time_booking=request.POST['book_check_in_time']
            check_out_time_booking=request.POST['book_check_out']
            single_booking=request.POST['book_single']
            double_booking=request.POST['book_double']
            room_count_booking=int(request.POST['book_room_count'])
          
            person_count_booking=request.POST['book_person_count']
            print(person_count_booking)
            room_type_booking=request.POST['book_room_type']
            room_fare_booking=request.POST['book_room_fare']
            user_email_booking=request.POST['book_user_email']
           
            user_mobile_booking=int(request.POST['book_user_mobile'])
         
            booking_obj=UserBookings(booking_hotel_name= hotel_name_booking,booking_user_name=user_name_booking, booking_check_in_date=
            check_in_date_booking, booking_check_out_date=check_out_date_booking, booking_check_in_time=check_in_time_booking,
            booking_check_out_time=check_out_time_booking,booking_fare_single= single_booking,booking_fare_double= double_booking,
            booking_room_countings=room_count_booking,booking_person_countings=person_count_booking, booking_room_type= room_type_booking,
            booking_room_fare= room_fare_booking,booking_user_email= user_email_booking, booking_user_mobile=user_mobile_booking,token=token1[1])
            
            hotel_details_obj=HotalAvalilibity.objects.get(hotel_name=hotel_name_booking)
           
            
            if hotel_details_obj.avl_single_room>=room_count_booking and hotel_details_obj.avl_double_room>=room_count_booking:
                
               

                 booking_obj.save()
                 
                 if room_type_booking=='single room':
                     hotel_details_obj.avl_single_room=hotel_details_obj.avl_single_room-room_count_booking
                     print(hotel_details_obj.avl_single_room)
                     obj2=HotalAvalilibity.objects.get(hotel_name= hotel_name_booking)
                     print(obj2)
                     obj2.avl_single_room= hotel_details_obj.avl_single_room
                     obj2.save()
                     if obj2.avl_single_room<=4 :
                         print("this is working")

                         h_obj2=HotelDetails.objects.get( hotel_name=obj2.hotel_name)
                         print("this is hotel",h_obj2.email)
                         send_mail(
                     'malayalithanima hotelbooked info',
                     'your rooms avalalibilty is too low,please verify it...',
                      'malayalithanimademo@gmail.com',
                     [h_obj2.email],
                     
                     fail_silently=False

                 )
                     else:
                         print("its ok")    

                    
                 elif room_type_booking=='double room':
                     hotel_details_obj.avl_double_room=hotel_details_obj.avl_double_room-room_count_booking
                     print("double room",hotel_details_obj.avl_double_room)
                     obj3=HotalAvalilibity.objects.get(hotel_name= hotel_name_booking)
                     print(obj3)
                     obj3.avl_double_room= hotel_details_obj.avl_double_room
                     obj3.save()


                     if obj3.avl_double_room<=4 :
                         print("this is working")

                         h_obj2=HotelDetails.objects.get( hotel_name=obj3.hotel_name)
                         print("this is hotel",h_obj2.email)
                         send_mail(
                     'malayalithanima hotelbooked info',
                     'your rooms avalalibilty is too low,please verify it...',
                      'malayalithanimademo@gmail.com',
                     [h_obj2.email],
                     
                     fail_silently=False

                 )
                     else:
                         print("its ok")     
                     

                 else:
                     print("something wrong")      
                   


                 send_mail(
                    
                     'malayalithanima hotelbooked info',
                     f'Dear Mr.{user_name_booking}\n warm greetings from  {hotel_name_booking}!!!\n Check In-{check_in_date_booking} \n Check-Out-{ check_out_date_booking}\n Room Type-{room_type_booking}\n Room Fare-{room_fare_booking}\n Cancel Policy: \n cancel by 3pm day prior to arrival to avoid one night room and tax penalty. \n Polices for coporate rates and group room blocks may vary \n Thank you for using our app for cancelation "http://127.0.0.1:8000/cancel/{token2}" ',

                     'malayalithanimademo@gmail.com',
                     [user_email_booking],
                     fail_silently=False

                 )
                
                 
                 
                 return JsonResponse({'msg':'saved successfully'})  
            else:
                return JsonResponse({'msg':'no rooms are avaliable'})
            
                
           
    except Exception as error:
        print(error)    
        
    return render(request,'kl14.html')




def fcancel(request,token2):
    obj2=UserBookings.objects.get(token=token2)

    return render(request,'cancel.html',{'display':obj2})

  


