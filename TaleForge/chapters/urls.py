from django.urls import path
from .views import ChapterCreateView, ChapterDetailView, vote_chapter

urlpatterns = [
    path('chapter/<int:story_pk>/new/', ChapterCreateView.as_view(), name='chapter_create'),
    path('chapter/<int:story_pk>/new/<int:parent_pk>/', ChapterCreateView.as_view(), name='chapter_create_with_parent'),
    path('chapter/<int:pk>/', ChapterDetailView.as_view(), name='chapter_detail'),
    path('chapter/<int:pk>/vote/<str:vote_type>/', vote_chapter, name='chapter_vote'),

]