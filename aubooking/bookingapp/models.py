from django.db import models
from django.contrib.auth.models import AbstractUser, User
from phonenumber_field import modelfields


# class CustomUser(AbstractUser):
#     username = models.CharField(max_length=32, unique=True)
#     email = models.EmailField()
#     phone_number = modelfields.PhoneNumberField()


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    age = models.PositiveSmallIntegerField()
    phone_number = modelfields.PhoneNumberField()
    country = models.CharField(max_length=40)
    photo = models.ImageField(upload_to='media/user_photo/')

    def __str__(self):
        return self.user.username


class Hotel(models.Model):
    name = models.CharField(40)
    description = models.TextField()
    address = models.CharField(40)
    city = models.CharField(30)
    country = models.CharField(30)

    def __str__(self):
        return self.name


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    parent = models.ForeignKey('self', on_delete=models.CASCADE)
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, related_name='comment')
    grade = models.IntegerField(choices=[(i, str(i)) for i in range(1, 6)])


class Image(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    image = models.ImageField()


class Room(models.Model):
    hotel = models.CharField(max_length=40)
    room_number = models.ImageField()
    capacity = models.CharField(max_length=40)
    price_per_night = models.IntegerField()

    def __str__(self):
        return f'{self.hotel.name} - {self.room_number}'


class Booking(models.Model):
    user = models.CharField(max_length=40)
    room = models.IntegerField()
    check_in_date = models.IntegerField()
    check_out_date = models.IntegerField()
    total_price = models.IntegerField()
    STATUS_CHOICES = (
        ('occupied', 'Occupied'),
        ('available', 'Available'),

    )
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='available')