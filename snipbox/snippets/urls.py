from django.urls import path
from .views import SnippetView, TagList


urlpatterns = [
    path('snippets/', Snippet.as_view({'post': 'create', 'get': 'list'}), name='snippet'),
    path('snippets/<int:pk>/', Snippet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='snippet_detail'),
]