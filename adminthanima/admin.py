from django.contrib import admin
from . models import *
from hotel.models import *
from thanima.models import *


# Register your models here.

admin.site.register(AdminDetails),
admin.site.register(UserBookings),
admin.site.register(HotelDetails)
admin.site.register(HotalAvalilibity)


