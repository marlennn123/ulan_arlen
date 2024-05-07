from rest_framework import viewsets, permissions, filters
from rest_framework.response import Response
from django.db.models import Avg
from .filters import HotelFilters, BookingFilters, RoomFilters
from .models import Hotel, Comment, Room, Booking
from .serializers import HotelSerializer, CommentSerializer, RoomSerializer, BookingSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter


class HotelViewSet(viewsets.ModelViewSet):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['country', 'city']
    search_fields = ['name']
    filterset_classs = HotelFilters


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class RoomViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    search_fields = ['hotel']
    filterset_class = RoomFilters


class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    filterset_class = BookingFilters