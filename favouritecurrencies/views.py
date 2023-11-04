from rest_framework import permissions, generics
from rest_framework.permissions import IsAuthenticated
from .models import FavouriteCurrencies
from .serializers import FavouriteCurrenciesSerializer


class FavouriteCurrenciesList(generics.ListCreateAPIView):
    serializer_class = FavouriteCurrenciesSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # this makes sure that only the logged in user can see their own favourites
        return FavouriteCurrencies.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        # This makes sure that the favourite currency is connected with the user who created it.
        serializer.save(user=self.request.user)


class FavouriteCurrenciesDetail(generics.RetrieveDestroyAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = FavouriteCurrenciesSerializer

    def get_queryset(self):
        # This  overrides the queryset so that  a user only sees their favourites
        return FavouriteCurrencies.objects.filter(user=self.request.user)
