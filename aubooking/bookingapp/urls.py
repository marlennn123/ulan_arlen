from django.urls import path, include
from .views import *

urlpatterns = [
    path('accounts/', include('allauth.urls')),
    path('hotel/', HotelViewSet.as_view({'get': 'list', 'post': 'create'}), name='hotel_list'),
    path('hotel/<int:pk', HotelViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='hotel_detail'),

    path('comment/', CommentViewSet.as_view({'get': 'list', 'post': 'create'}), name='comment_list'),
    path('comment/<int:pk', CommentViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='comment_detail'),

    path('roomViewSet/', RoomViewSet.as_view({'get': 'list', 'post': 'create'}), name='room_list'),
    path('roomViewSet/<int:pk', RoomViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='room_detail'),

    path('booking/', BookingViewSer.as_view({'get': 'list', 'post': 'create'}), name='booking_list'),
    path('booking/<int:pk', BookingViewSer.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='booking_detail'),
]