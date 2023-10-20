from django.db.models import Count
from rest_framework import generics, filters
from .models import UserProfile
from .serializers import UserProfileSerializer
from rest_framework.permissions import IsAuthenticated
from crypto_tracker_backend.permissions import IsOwnerOrReadOnly


class UserProfileList(generics.ListCreateAPIView):
    queryset = UserProfile.objects.annotate(
        favouritecurrencies_count=Count(
            'user__favouritecurrencies', distinct=True)
    )
    serializer_class = UserProfileSerializer  # the one that creates the fields
    # Here I change what user can see when they are not logged in
    permission_classes = [IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class UserProfileDetailsView(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserProfile.objects.annotate(
        favouritecurrencies_count=Count(
            'user__favouritecurrencies', distinct=True)
    )
    serializer_class = UserProfileSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'id'
