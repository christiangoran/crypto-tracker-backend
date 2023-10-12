from rest_framework import generics, permissions
from .models import CurrencyPost
from .serializers import CurrencyPostSerializer


class CurrencyPostList(generics.ListCreateAPIView):
    queryset = CurrencyPost.objects.all()
    serializer_class = CurrencyPostSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly
    ]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
