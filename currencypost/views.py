from rest_framework import generics, permissions
from .models import CurrencyPost
from .serializers import CurrencyPostSerializer
from crypto_tracker_backend.permissions import IsOwnerOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend


class CurrencyPostList(generics.ListCreateAPIView):
    queryset = CurrencyPost.objects.all()
    serializer_class = CurrencyPostSerializer
    permission_classes = [
        # This permission class will allow
        # only authenticated users to edit the post.
        permissions.IsAuthenticatedOrReadOnly
    ]
    filter_backends = [
        DjangoFilterBackend,
    ]
    filterset_fields = [
        'currency']

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
