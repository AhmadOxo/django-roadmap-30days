from django.contrib import admin
from .models import * # The Star means "All" or everything That's there


@admin.register(Notes)
class Notes(admin.ModelAdmin):
    list_display = ('id', 'title', 'created_at', 'last_update')
    search_fields = ('title', 'content')
    list_per_page = 10

admin.site.register(Comment)