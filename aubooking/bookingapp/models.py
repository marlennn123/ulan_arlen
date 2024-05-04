from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    age = models.IntegerField()
    country = models.CharField(max_length=40)
    photo = models.ImageField()
    phone_number = models.IntegerField()


class Hotel(models.Model):
    name = models.CharField(40)
    description = models.TextField()
    address = models.CharField(40)
    city = models.CharField(30)
    country = models.CharField(30)


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    created_date = models.DateTimeField
    parent = models.ForeignKey('self', on_delete=models.CASCADE)
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    rating = models.IntegerField(choices=[(i, str(i)) for i in range(1, 6)])


class Image(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    image = models.ImageField()


class Room(models.Model):
    hotel = models.CharField(max_length=40)
    room_number = models.ImageField()
    capacity = models.CharField(max_length=40)
    price_per_night = models.IntegerField()


class Booking(models.Model):
    user = models.CharField(max_length=40)
    room = models.IntegerField()
    check_in_date = models.IntegerField()
    check_out_date = models.IntegerField()
    total_price = models.IntegerField()
    STATUS_CHOICES = (
        ('occupied', 'occupied'),
        ('available', 'Available'),

    )
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='available')