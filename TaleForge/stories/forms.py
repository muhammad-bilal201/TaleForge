from django import forms
from .models import Story

class StoryForm(forms.ModelForm):
    class Meta:
        model = Story
        fields = ['title', 'genre', 'summary', 'cover_image']
        widgets = {
            'summary': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Enter a brief summary of your story...'}),
            'title': forms.TextInput(attrs={'placeholder': 'Enter story title...'}),
        }