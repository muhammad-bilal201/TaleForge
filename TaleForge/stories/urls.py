from django.urls import path
from .views import StoryListView, StoryDetailView, StoryCreateView, StoryUpdateView

urlpatterns = [
    path('', StoryListView.as_view(), name='home'),
    path('story/<int:pk>/', StoryDetailView.as_view(), name='story_detail'),
    path('story/new/', StoryCreateView.as_view(), name='story_create'),
    path('story/<int:pk>/edit/', StoryUpdateView.as_view(), name='story_edit'),
]