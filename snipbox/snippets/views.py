from rest_framework import viewsets, permissions, status, generics
from rest_framework.response import Response
from .models import Snippet, Tag
from .serializers import SnippetSerializer,SnippetListSerializer, TagSerializer
from django.shortcuts import get_object_or_404


class SnippetView(viewsets.ViewSet):
    permission_classes = [permissions.IsAuthenticated]
    
    def list(self, request):
        snippets = Snippet.objects.filter(user=request.user)
        serializer = SnippetListSerializer(snippets, many=True, context={'request': request})
        return Response({
            "total_count": snippets.count(),
            "snippets": serializer.data
        })

    def create(self, request):
        serializer = SnippetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def retrieve(self, request, pk=None):
        snippet = get_object_or_404(Snippet, pk=pk, user=request.user)
        serializer = SnippetSerializer(snippet)
        return Response(serializer.data)
    
    def update(self, request, pk=None):
        snippet = get_object_or_404(Snippet, pk=pk, user=request.user)
        serializer = SnippetSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        snippet = get_object_or_404(Snippet, pk=pk, user=request.user)
        snippet.delete()
        return self.list(request)

class TagList(generics.ListAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = [permissions.IsAuthenticated]

class TagDetails(generics.RetrieveAPIView):
    serializer_class = SnippetSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, pk):
        tag = get_object_or_404(Tag, pk=pk)
        snippets = Snippet.objects.filter(tag=tag, user=request.user)
        serializer = SnippetSerializer(snippets, many=True)
        return Response(serializer.data)