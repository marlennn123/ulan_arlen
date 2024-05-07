from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth import get_user_model
from .models import *

User = get_user_model()


class CustomUserAdmin(BaseUserAdmin):
    ordering = ('email',)
    list_display = ('email', 'first_name', 'last_name')
    list_filter = ["is_staff"]

    fieldsets = [
        (None, {"fields": ["email", "password"]}),
        (
            "Other info",
            {
                "fields": [
                    "first_name",
                    "last_name",
                    "is_active",
                    "is_staff",
                ],
            },
        ),
    ]
    add_fieldsets = [
        (
            None,
            {
                "fields": [
                    "email",
                    "first_name",
                    "last_name",
                    "password1",
                    "password2",
                    "is_active",
                    "is_staff",
                ]
            },
        ),
    ]


admin.site.register(Hotel)
admin.site.register(Comment)
admin.site.register(Imagehotel)
admin.site.register(Room)
admin.site.register(Imageroom)
admin.site.register(Booking)