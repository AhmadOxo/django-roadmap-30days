from django.urls import path, include
from rest_framework import routers
from blog.api_views import PostViewSet
from notes.api_views import NotesViewSet

router = routers.DefaultRouter()
router.register(r'posts', PostViewSet)
router.register(r'notes', NotesViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
]