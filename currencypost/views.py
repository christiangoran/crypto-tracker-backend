from rest_framework import generics, permissions
from .models import CurrencyPost
from .serializers import CurrencyPostSerializer
from crypto_tracker_backend.permissions import IsOwnerOrReadOnly


class CurrencyPostList(generics.ListCreateAPIView):
    queryset = CurrencyPost.objects.all()
    serializer_class = CurrencyPostSerializer
    permission_classes = [
        # This permission class will allow only authenticated users to edit the post.
        permissions.IsAuthenticatedOrReadOnly
    ]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class CurrencyPostDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    This class handles the http GET, PUT and DELETE requests.
    """
    queryset = CurrencyPost.objects.all()
    serializer_class = CurrencyPostSerializer
    permission_classes = [IsOwnerOrReadOnly]

    def perform_update(self, serializer):
        serializer.save()
