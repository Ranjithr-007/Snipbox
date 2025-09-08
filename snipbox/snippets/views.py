from django.shortcuts import render
from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from .models import Snippet, Tag
from .serializers import SnippetSerializer

# Create your views here.

class Snippet(viewsets.ViewSet):
    permission_classes = [permissions.IsAuthenticated]

    def list(self, request):
        snippets = Snippet.objects.filter(user=request.user)
        serializer = SnippetSerializer(snippets, many=True)
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