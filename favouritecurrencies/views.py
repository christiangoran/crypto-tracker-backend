from rest_framework import generics, permissions, viewsets
from crypto_tracker_backend.permissions import IsOwnerOrReadOnly
from .models import FavouriteCurrencies
from .serializers import FavouriteCurrenciesSerializer


class FavouriteCurrenciesList(generics.ListCreateAPIView):
    queryset = FavouriteCurrencies.objects.all()
    serializer_class = FavouriteCurrenciesSerializer
    permission_classes = [

        permissions.IsAuthenticatedOrReadOnly
    ]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class FavouriteCurrenciesDetail(generics.RetrieveDestroyAPIView):
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = FavouriteCurrenciesSerializer
    queryset = FavouriteCurrencies.objects.all()
