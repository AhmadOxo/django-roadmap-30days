from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Notes
from .serializers import NoteSerializers


class NotesViewSet(viewsets.ModelViewSet):
    serializer_class = NoteSerializers
    permission_classes = [IsAuthenticated]
    queryset = Notes.objects.all()

    
    def get_queryset(self):
        return Notes.objects.filter(user=self.request.user).order_by('-last_update')
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)