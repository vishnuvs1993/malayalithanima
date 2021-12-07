from django.db import models

# Create your models here.



class AdminDetails(models.Model):
    first_name=models.CharField(max_length=30)
    second_name=models.CharField(max_length=20)
    password=models.CharField(max_length=40)
    email=models.EmailField()
    age=models.IntegerField()
    mobile=models.BigIntegerField()
    profile=models.CharField(max_length=100)


class EventDetails(models.Model):
    event_pic1=models.CharField(max_length=60)
    event_name1=models.CharField(max_length=40)
    event_discription1=models.CharField(max_length=255)

    event_pic2=models.CharField(max_length=60)
    event_name2=models.CharField(max_length=40)
    event_discription2=models.CharField(max_length=255)

    event_pic3=models.CharField(max_length=60)
    event_name3=models.CharField(max_length=40)
    event_discription3=models.CharField(max_length=255)

    event_pic4=models.CharField(max_length=60)
    event_name4=models.CharField(max_length=40)
    event_discription4=models.CharField(max_length=255)

    event_pic5=models.CharField(max_length=60)
    event_name5=models.CharField(max_length=40)
    event_discription5=models.CharField(max_length=255)

    event_pic6=models.CharField(max_length=60)
    event_name6=models.CharField(max_length=40)
    event_discription6=models.CharField(max_length=255)