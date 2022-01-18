from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from . models import *
from random import random
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.models import User, auth

# Create your views here.

def hsignup(request):
    try:
        c_email=request.POST['c_email']
        hotel_obj=HotelDetails.objects.filter(email=c_email).exists()
        if hotel_obj==False:
            c_firstname=request.POST['c_first_name']
            c_lastname=request.POST['c_second_name']
            c_password=request.POST['c_password']
            c_hotelname=request.POST['c_hotel_name']
            c_hotel_description=request.POST['c_hotel_description']
            c_single=request.POST['c_single_room']
            c_double=request.POST['c_double_room']
            c_dict1=request.POST['dict']
            print(c_dict1)
            cage=request.POST['c_age']
            c_mobile=request.POST['c_phone_number']
            c_file=request.FILES['u_file']
            c_filename=str(random())+c_file.name
            file_obj=FileSystemStorage()
            file_obj.save(c_filename,c_file)
            c_file1=request.FILES['u_file1']
            c_filename1=str(random())+c_file1.name
            file_obj1=FileSystemStorage()
            file_obj1.save(c_filename1,c_file1)
            c_file2=request.FILES['u_file2']
            c_filename2=str(random())+c_file1.name
            file_obj2=FileSystemStorage()
            file_obj2.save(c_filename2,c_file2)
            c_file3=request.FILES['u_file3']
            c_filename3=str(random())+c_file3.name
           

            file_obj3=FileSystemStorage()
            file_obj3.save(c_filename3,c_file3)
            hotel_obj1=HotelDetails(first_name=c_firstname,last_name=c_lastname,password=c_password,email=c_email,hotel_name=c_hotelname,
            hotel_description=c_hotel_description,price_single=c_single,price_double=c_double,district=c_dict1,age=cage,mobile=c_mobile,
            ower_profile= c_filename,hotel_picture1=c_filename1, hotel_picture2=c_filename2,hotel_picture3=c_filename3)
            hotel_obj1.save()
            k_obj=HotelDetails.objects.all().filter(district='01')
           
            
            return render(request,'hotel_management.html',{'k_obj':k_obj}) 
    except Exception as error:
        print(error)        
       

    return render(request,'hotel_owner.html')
def hotel_statics(request):
    
    return render(request,'hotel_management.html')

def flogin(request):
    try:
        if request.method=='POST':
            hotel_email=request.POST['h_email']
            hotel_password=request.POST['h_password']
            login_obj=HotelDetails.objects.get(email=hotel_email,password=hotel_password)
           
            request.session['hotel_session']=login_obj.id
            session_obj=request.session['hotel_session']
            user_obj1=HotelDetails.objects.get(id=session_obj)
           
            return render(request,'hotel_management.html',{'display':user_obj1})
    except Exception as error:
        print(error)        
     

    return render(request,'hotel_management.html',{"msg":"plese check your email and password"})

            
def logout(request):
    del request.session['hotel_session']
    print("sucess")
    return render(request,'hotel_management.html')



def fhotal_avl(request):
    hotelname=request.POST['a_hotelname']
    val_obj=HotalAvalilibity.objects.filter(hotel_name=hotelname).exists()
    if val_obj==False:
        print("enter the function")
       
        ownername=request.POST['a_ownername']
        todaydate=request.POST['a_todaydate']
        avlsingleroom=request.POST['a_singleroom_number']
        avldoubleroom=request.POST['a_doubleroom_number']
        owner_email=request.POST['a_email']
        owner_mobile=request.POST['a_mobile']
        s_obj=HotalAvalilibity(hotel_name= hotelname, owner_name=ownername,today_date= todaydate, avl_single_room= avlsingleroom,avl_double_room= avldoubleroom, email=  owner_email,mobile= owner_mobile)
        s_obj.save()
        print("saved sucess")
        return render(request,'hotel_management.html',{'msg':'update sucessfully'})
    elif val_obj==True:
        hotelname=request.POST['a_hotelname']
        ownername=request.POST['a_ownername']
        todaydate=request.POST['a_todaydate']
        avlsingleroom=request.POST['a_singleroom_number']
        avldoubleroom=request.POST['a_doubleroom_number']
        owner_email=request.POST['a_email']
        owner_mobile=request.POST['a_mobile']
                    
        print("error")

        session_obj=request.session['hotel_session']
        user_obj1=HotelDetails.objects.get(id=session_obj)
        
        user_obj2=HotalAvalilibity.objects.get(hotel_name=user_obj1.hotel_name)
        print(user_obj2.id)
        avl_obj=HotalAvalilibity(id=user_obj2.id,hotel_name=hotelname,owner_name=ownername,today_date=todaydate,avl_single_room=avlsingleroom,avl_double_room=avldoubleroom,
        email=owner_email,mobile=owner_mobile)
            
        avl_obj.save()
        print("update sucess")
        return render(request,'hotel_management.html',{'msg':'update sucessfully'})


    return render(request,'hotel_management.html',{'msg':'update sucessfully'})
    
            


     

   