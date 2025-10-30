from django.urls import path, include
from rest_framework import routers
from blog.api_views import PostViewSet
from notes.api_views import NotesViewSet
from accounts.api_views import UserProfileViewSet


router = routers.DefaultRouter()
router.register(r'posts', PostViewSet)
router.register(r'notes', NotesViewSet)
router.register(r'profiles', UserProfileViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
]