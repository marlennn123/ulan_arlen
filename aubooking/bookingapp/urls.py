from django.urls import path, include
from .views import *

urlpatterns = [
    path('accounts/', include('allauth.urls')),

    path('hotels/', HotelViewSet.as_view({'get': 'list', 'post': 'create'}), name='hotel_list'),
    path('hotel/<int:pk>/', HotelViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='hotel_detail'),

    path('comments/', CommentViewSet.as_view({'get': 'list', 'post': 'create'}), name='comment_list'),
    path('comment/<int:pk>/', CommentViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='comment_detail'),

    path('rooms/', RoomViewSet.as_view({'get': 'list', 'post': 'create'}), name='room_list'),
    path('room/<int:pk>/', RoomViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='room_detail'),

    path('booking/', BookingViewSet.as_view({'get': 'list', 'post': 'create'}), name='booking_list'),
    path('booking/<int:pk>/', BookingViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='booking_detail'),
]