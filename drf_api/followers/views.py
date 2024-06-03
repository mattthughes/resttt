from rest_framework import generics, permissions
from drf_api.permissions import IsOwnerOrReadOnly
from .models import Followers
from .serializers import FollowerSerializer

# Create your views here.

class FollowerList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = FollowerSerializer
    queryset = Followers.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class FollowerDetail(generics.RetrieveDestroyAPIView):
    serializer_class = FollowerSerializer
    queryset = Followers.objects.all()
    permission_classes = [IsOwnerOrReadOnly]