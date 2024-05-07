from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.contrib.auth.models import Group, Permission


class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """
        Creates and saves a User with the given email and password.
        """
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_staff', True)

        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=255, unique=True)
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    password = models.CharField(max_length=255)
    username = models.CharField(max_length=150, unique=True, null=True, blank=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30, null=True, blank=True)
    last_login = models.DateTimeField(auto_now_add=True, null=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name']

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'

    # Исправленные обратные отношения
    groups = models.ManyToManyField(Group, verbose_name='groups', blank=True, related_name='bookingapp_user_groups')
    user_permissions = models.ManyToManyField(
        Permission, verbose_name='user permissions', blank=True, related_name='bookingapp_user_permissions'
    )


class Hotel(models.Model):
    name = models.CharField(max_length=40, verbose_name="name")
    description = models.TextField(verbose_name="description")
    address = models.CharField(max_length=40, verbose_name="address")
    city = models.CharField(max_length=40, verbose_name="city")
    country = models.CharField(max_length=40, verbose_name="country")

    def __str__(self) -> str:
        return f'{self.name}'


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    text = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, related_name='comments')
    grade = models.IntegerField(choices=[(i, str(i)) for i in range(1, 6)])

    def __str__(self) -> str:
        return f'{self.user}'


class Imagehotel(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    image = models.ImageField()


class Room(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, related_name='rooms')
    room_number = models.IntegerField(verbose_name='сколько комнат')
    capacity = models.CharField(max_length=40, verbose_name='для сколько людей')
    price_per_night = models.IntegerField(verbose_name='сколько за сутки?')
    active = models.BooleanField(null=True)

    def __str__(self) -> str:
        return f'{self.room_number} in {self.hotel}'


class Imageroom(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField()


class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='bookings')
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='bookings')
    check_in_date = models.DateTimeField()
    check_out_date = models.DateTimeField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    STATUS_CHOICES = (
        ('occupied', 'occupied'),
        ('available', 'Available'),
    )
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='available')

    def __str__(self) -> str:
        return f'{self.user} - room number: {self.room} - status: {self.status}'
