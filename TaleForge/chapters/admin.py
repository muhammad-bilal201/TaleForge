from django.contrib import admin
from mptt.admin import MPTTModelAdmin
from .models import Chapter, Vote

@admin.register(Chapter)
class ChapterAdmin(MPTTModelAdmin):
    list_display = ['title', 'story', 'author', 'status', 'votes', 'created_at']
    list_filter = ['status', 'created_at', 'story']
    search_fields = ['title', 'content', 'author__username', 'story__title']
    date_hierarchy = 'created_at'
    ordering = ['-created_at']
    readonly_fields = ['created_at', 'updated_at', 'votes']
    fieldsets = (
        (None, {
            'fields': ('title', 'content', 'author', 'story', 'parent', 'status')
        }),
        ('Meta', {
            'fields': ('votes', 'created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )

@admin.register(Vote)
class VoteAdmin(admin.ModelAdmin):
    list_display = ['user', 'chapter', 'vote_type', 'created_at']
    list_filter = ['vote_type', 'created_at']
    search_fields = ['user__username', 'chapter__title']
    date_hierarchy = 'created_at'
    ordering = ['-created_at']
