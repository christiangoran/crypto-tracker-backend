from rest_framework import generics, permissions, viewsets
from crypto_tracker_backend.permissions import IsOwnerOrReadOnly
from .models import FavouriteCurrencies
from .serializers import FavouriteCurrenciesSerializer


class FavouriteCurrenciesList(generics.ListCreateAPIView):
    serializer_class = FavouriteCurrenciesSerializer
    permission_classes = [

        permissions.IsAuthenticatedOrReadOnly
    ]

    def get_queryset(self):
        # this makes sure that only the logged in user can see their own favourites
        return FavouriteCurrencies.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        # This makes sure that the favourite currency is connected with the user who created it.
        serializer.save(user=self.request.user)


class FavouriteCurrenciesDetail(generics.RetrieveDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = FavouriteCurrenciesSerializer

    def get_queryset(self):
        return FavouriteCurrencies.objects.filter(user=self.request.user)

    def get_object(self):

        queryset = self.filter_queryset(self.get_queryset())

        obj = queryset.get(pk=self.kwargs.get('pk'))
        self.check_object_permissions(self.request, obj)
        return obj
