# Generated by Django 3.2.7 on 2022-01-17 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('thanima', '0004_userbookings'),
    ]

    operations = [
        migrations.AddField(
            model_name='userbookings',
            name='token',
            field=models.CharField(default=None, max_length=100),
        ),
    ]
