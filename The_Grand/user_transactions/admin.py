from django.contrib import admin
from .models import reviews,rooms,user_booking,restaurant

# Register your models here.
admin.site.register(reviews)
admin.site.register(rooms)
admin.site.register(user_booking)
admin.site.register(restaurant)
