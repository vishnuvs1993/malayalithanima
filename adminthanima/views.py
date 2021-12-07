from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpResponse,JsonResponse

from thanima.models import UserBookings
from . models import *
from random import random
from django.core.files.storage import FileSystemStorage
from hotel.models import *
from thanima.models import *

# Create your views here.


def signup(request):

    
    try:    
        user_mail=request.POST['u_email']
        obj1=AdminDetails.objects.filter(email=user_mail).exists()
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
            admin_obj=AdminDetails(first_name=user_first,second_name=user_second,password=user_password,email=user_mail,age=user_age,mobile=user_phone,profile=file_name)
            admin_count=AdminDetails.objects.all().count()
            if admin_count<3:
                admin_obj.save()
                return render(request,'a_home.html')
          
    except Exception as error:
        print(error)
  

    

    return render(request,'a_signup.html',)


def ahome(request):
    return render(request,'a_home.html')    


def login(request):

    try:
        if request.method=='POST':
            login_email=request.POST['l_email']
            login_password=request.POST['l_password']
            login_obj=AdminDetails.objects.get(email=login_email,password=login_password)
           
            request.session['admin_session']=login_obj.id
            session_obj=request.session['admin_session']
            user_obj1=AdminDetails.objects.get(id=session_obj)
            print(user_obj1.first_name)
            print(user_obj1.profile)
            return render(request,'a_home.html',{'display':user_obj1})
    except Exception as error:
        print(error)        
     

    return render(request,'home.html',{"msg":"plese check your email and password"})

def logout(request):

    return render(request,'a_sinup.html')    


def event_add(request):
    try:
        if request.method=='POST':
            a_file1=request.FILES['a_file1']
            a_filename1=str(random())+a_file1.name
            file_obj1=FileSystemStorage()
            file_obj1.save(a_filename1,a_file1)
            a_event_name1=request.POST['a_event1']
            a_event_info1=request.POST['a_event_description1']

            a_file2=request.FILES['a_file2']
            a_filename2=str(random())+a_file2.name
            file_obj2=FileSystemStorage()
            file_obj2.save(a_filename2,a_file2)
            a_event_name2=request.POST['a_event2']
            a_event_info2=request.POST['a_event_description2']

            
            a_file3=request.FILES['a_file3']
            a_filename3=str(random())+a_file3.name
            file_obj3=FileSystemStorage()
            file_obj3.save(a_filename3,a_file3)
            a_event_name3=request.POST['a_event3']
            a_event_info3=request.POST['a_event_description3']

            a_file4=request.FILES['a_file4']
            a_filename4=str(random())+a_file4.name
            file_obj4=FileSystemStorage()
            file_obj4.save(a_filename4,a_file4)
            a_event_name4=request.POST['a_event4']
            a_event_info4=request.POST['a_event_description4']

            a_file5=request.FILES['a_file5']
            a_filename5=str(random())+a_file5.name
            file_obj5=FileSystemStorage()
            file_obj5.save(a_filename5,a_file5)
            a_event_name5=request.POST['a_event5']
            a_event_info5=request.POST['a_event_description5']

            a_file6=request.FILES['a_file6']
            a_filename6=str(random())+a_file6.name
            file_obj6=FileSystemStorage()
            file_obj6.save(a_filename6,a_file6)
            a_event_name6=request.POST['a_event6']
            a_event_info6=request.POST['a_event_description6']

            event_obj=EventDetails(event_pic1= a_filename1,event_name1=a_event_name1, event_discription1=a_event_info1, event_pic2= a_filename2,event_name2= a_event_name2, event_discription2=a_event_info2,event_pic3= a_filename3,event_name3= a_event_name3,  event_discription3=a_event_info3,event_pic4= a_filename4, event_name4= a_event_name4, event_discription4= a_event_info4,event_pic5=a_filename5,event_name5=a_event_name5, event_discription5=
            a_event_info5, event_pic6= a_filename6, event_name6= a_event_name6, event_discription6= a_event_info6)
            event_obj.save()
            return render(request,'a_home.html')
    except Exception as error:
        print(error)
    return render(request,'a_home.html')


def u_booking(request):
    return render(request,'user_bookings.html')    

def user_b_details(request):
    print("fewfwf")
    user_b_obj=UserBookings.objects.all()
    user_b_obj=[{'user_id':i.id,'user_name':i.booking_user_name,'booked_hotel_name':i.booking_hotel_name,'user_check_in_date':i.booking_check_in_date,'user_check_out_date':i.booking_check_out_date,'user_check_in_time':i.booking_check_in_time,'user_check_out_time':i.booking_check_out_time,'user_fare_single':i.booking_fare_single,'user_fare_double':i.booking_fare_double,'user_room_countings':i.booking_room_countings,'user_person_countings':i.booking_person_countings,'user_room_type':i.booking_room_type,'user_room_fare':i.booking_room_fare,'user_email':i.booking_user_email,'user_mobile':i.booking_user_mobile}for i in user_b_obj]
    print(user_b_obj)
    return JsonResponse({'display_u_booking':user_b_obj})



def fadmin(request):
    return render(request,'registration/profile.html')    