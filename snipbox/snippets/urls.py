from django.urls import path
from .views import SnippetView


urlpatterns = [
    path('snippets/', Snippet.as_view({'post': 'create'}), name='snippet'),
]