from django.db import models


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
    parent = models.
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    rating = models.


