from rest_framework import serializers
from .models import Notes

class NoteSerializers(serializers.ModelSerializer):
    class Meta:
        model = Notes
        fields = ['id', 'title', 'content', 'last_update']
        read_only_fields = ['last_update']