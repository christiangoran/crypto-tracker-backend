from rest_framework import permissions, generics
from rest_framework.permissions import IsAuthenticated
from .models import FavouriteCurrencies
from .serializers import FavouriteCurrenciesSerializer


class FavouriteCurrenciesList(generics.ListCreateAPIView):
    serializer_class = FavouriteCurrenciesSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return FavouriteCurrencies.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class FavouriteCurrenciesDetail(generics.RetrieveDestroyAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = FavouriteCurrenciesSerializer

    def get_queryset(self):
        return FavouriteCurrencies.objects.filter(user=self.request.user)
