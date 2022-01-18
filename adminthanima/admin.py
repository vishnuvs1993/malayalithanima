from django.contrib import admin
from . models import *
from hotel.models import *
from thanima.models import *
from django.contrib.sessions.models import Session

# Register your models here.

admin.site.register(AdminDetails),
admin.site.register(UserBookings),
admin.site.register(HotelDetails),
admin.site.register(HotalAvalilibity),
admin.site.register(Session),
admin.site.register(UserDetails)



