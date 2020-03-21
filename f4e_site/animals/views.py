from .models import Snippet
from .serializers import SnippetSerializer
from rest_framework import generics


class SnippetList(generics.ListAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer


class SnippetDetail(generics.ListAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer