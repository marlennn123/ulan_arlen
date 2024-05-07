from .models import *
from rest_framework import serializers
from django.db.models import Avg


class HotelSerializer(serializers.ModelSerializer):
    rating = serializers.SerializerMethodField()

    class Meta:
        model = Hotel
        fields = ['name', 'description', 'address', 'city', 'country', 'rating']

    def get_rating(self, obj):
        rating = obj.comment.aggregate(Avg('grade'))['grade__avg']
        return rating if rating is not None else 0


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = '__all__'


class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'


