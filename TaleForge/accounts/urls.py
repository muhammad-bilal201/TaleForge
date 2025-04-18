from django.urls import path
from .views import  LogoutView, SignUpView, ProfileView, ProfileUpdateView
urlpatterns = [
     
    path('signup/', SignUpView.as_view(), name='signup'),
    path('profile/<int:pk>/', ProfileView.as_view(), name='profile'),
    path('profile/<int:pk>/edit/', ProfileUpdateView.as_view(), name='profile_edit'),
    path('logout/',LogoutView.as_view(),name='logout')
   
]