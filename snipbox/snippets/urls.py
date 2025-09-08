from django.urls import path
from .views import SnippetView


urlpatterns = [
    path('snippets/', SnippetView.as_view(), name='snippet'),
]