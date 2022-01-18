from dataclasses import fields
from rest_framework import serializers
from rest_framework import UserBookings


class UserBookingsSerializer(serializers.ModelSerializer):

    class Meta:
        model= UserBookings
        fields='__all__'
