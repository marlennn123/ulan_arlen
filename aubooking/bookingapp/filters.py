from django_filters.rest_framework import DjangoFilterBackend, FilterSet
from .models import Hotel


class HotelFilter(FilterSet):
    filter_backends = (DjangoFilterBackend,)

    class Meta:
        model = Hotel
        fields = ('name', 'in_stock')