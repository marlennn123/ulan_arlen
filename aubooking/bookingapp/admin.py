from django.contrib import admin
from .models import UserProfile, Comment, Room, Booking, Hotel


# Register your models here.
admin.site.register(UserProfile)
admin.site.register(Comment)
admin.site.register(Room)
admin.site.register(Booking)
admin.site.register(Hotel)