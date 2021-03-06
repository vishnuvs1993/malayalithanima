# Generated by Django 3.2.7 on 2022-01-17 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0010_auto_20220117_1856'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserBookings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('booking_hotel_name', models.CharField(max_length=30)),
                ('booking_user_name', models.CharField(max_length=30)),
                ('booking_check_in_date', models.DateField()),
                ('booking_check_out_date', models.DateField()),
                ('booking_check_in_time', models.TimeField()),
                ('booking_check_out_time', models.TimeField()),
                ('booking_fare_single', models.IntegerField()),
                ('booking_fare_double', models.IntegerField()),
                ('booking_room_countings', models.IntegerField()),
                ('booking_person_countings', models.IntegerField()),
                ('booking_room_type', models.CharField(max_length=30)),
                ('booking_room_fare', models.IntegerField()),
                ('booking_user_email', models.EmailField(max_length=254)),
                ('booking_user_mobile', models.BigIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='UserDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('second_name', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=40)),
                ('email', models.EmailField(max_length=254)),
                ('age', models.IntegerField()),
                ('mobile', models.BigIntegerField()),
                ('profile', models.CharField(max_length=100)),
            ],
        ),
    ]
