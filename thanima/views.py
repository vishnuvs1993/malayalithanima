from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from . models import *
from random import random
from django.core.files.storage import FileSystemStorage
from hotel.models import * 


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
            booking_room_fare= room_fare_booking,booking_user_email= user_email_booking, booking_user_mobile=user_mobile_booking)
            
            hotel_details_obj=HotalAvalilibity.objects.get(hotel_name=hotel_name_booking)
            if hotel_details_obj.avl_single_room>=room_count_booking and hotel_details_obj.avl_double_room>=room_count_booking:

            
                 booking_obj.save()

                 return JsonResponse({'msg':'saved successfully'})  
            else:
                return JsonResponse({'msg':'no rooms are avaliable'})

           
    except Exception as error:
        print(error)    
        
    return render(request,'kl14.html')