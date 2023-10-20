from rest_framework import generics, filters
from .models import Currency
from .serializers import CurrencySerializer


class CurrencyList(generics.ListCreateAPIView):
    queryset = Currency.objects.all()
    serializer_class = CurrencySerializer
    filter_backends = [
        filters.OrderingFilter,
        filters.SearchFilter
    ]
    search_fields = ['name', 'symbol']


class CurrencyDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Currency.objects.all()
    serializer_class = CurrencySerializer
