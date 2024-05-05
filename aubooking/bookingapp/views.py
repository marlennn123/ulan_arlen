from rest_framework import viewsets, permissions
from rest_framework.response import Response
from django.db.models import Avg
from .models import UserProfile, Hotel, Comment, Room, Booking
from .serializers import UserProfileSerializer, HotelSerializer, CommentSerializer, RoomSerializer, BookingSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter


class UserPrfileViewSer(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer


class HotelViewSet(viewsets.ModelViewSet):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['country', 'city']
    search_fields = ['name']


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class RoomViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    filter_backends = ['active']


class BookingViewSer(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
