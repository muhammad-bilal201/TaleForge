from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('username', 'email')

class ProfileUpdateForm(UserChangeForm):
    password = None  # Remove password field
    
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'bio', 'avatar')