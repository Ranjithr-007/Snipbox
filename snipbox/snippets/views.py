from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from .models import Snippet
from .serializers import SnippetSerializer

# Create your views here. 
class SnippetView(viewsets.ViewSet):
    pass

