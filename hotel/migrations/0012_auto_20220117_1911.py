# Generated by Django 3.2.7 on 2022-01-17 13:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0011_userbookings_userdetails'),
    ]

    operations = [
        migrations.DeleteModel(
            name='UserBookings',
        ),
        migrations.DeleteModel(
            name='UserDetails',
        ),
    ]