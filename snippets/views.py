from snippets.models import Snippet
from snippets.serializers import SnippetSerializer
from snippets.serializers import UserSerializer
from rest_framework import generics
from django.contrib.auth.models import User
from rest_framework import permissions
from snippets.permissions import IsOwnerOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from snippets.permissions import IsOwnerOrReadOnly


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class SnippetList(generics.ListCreateAPIView):
    """
    Returns a list of all snippets.
    """
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter,]
    search_fields = ['title', 'code']
    ordering_fields = ('title', 'owner')
    filter_fields = ('title', 'code', 'linenos', 'owner')
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]



