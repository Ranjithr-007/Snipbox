from django.urls import path
from .views import SnippetView


urlpatterns = [
    path('snippets/', Snippet.as_view({'post': 'create', 'get': 'list'}), name='snippet'),
    path('snippets/<int:pk>/', Snippet.as_view({'get': 'retrieve', 'put': 'update'}), name='snippet_detail'),
]