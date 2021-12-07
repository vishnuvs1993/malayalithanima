# Generated by Django 3.2.7 on 2021-11-24 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('thanima', '0001_initial'),
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
    ]
