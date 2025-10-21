from django.contrib import admin
from .models import Notes, Comment

@admin.register(Notes)
class NotesAdmin(admin.ModelAdmin):
    list_display = ['title', 'user', 'created_at', 'last_update']
    list_filter = ['created_at', 'user']
    search_fields = ['title', 'content']

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['note', 'author', 'published_at']
    list_filter = ['published_at']