from django.contrib import admin
from .models import Notes


@admin.register(Notes)
class Notes(admin.ModelAdmin):
    list_display = ('id', 'title', 'created_at')
    search_fields = ('title', 'content')
    list_per_page = 10