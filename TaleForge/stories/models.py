from django.db import models

# Create your models here.
from django.db import models
from accounts.models import CustomUser

class Story(models.Model):
    GENRE_CHOICES = [
        ('MOR', 'MORAL'),
        ('FAN', 'Fantasy'),
        ('SCI', 'Sci-Fi'),
        ('HOR', 'Horror'),
        ('ROM', 'Romance'),
        ('MYS', 'Mystery'),
        ('HIS', 'Historical'),
    ]
    
    title = models.CharField(max_length=200)
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    genre = models.CharField(max_length=3, choices=GENRE_CHOICES)
    summary = models.TextField()
    cover_image = models.ImageField(upload_to='story_covers/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_completed = models.BooleanField(default=False)
    
    def __str__(self):
        return self.title