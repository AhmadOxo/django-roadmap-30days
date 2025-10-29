from django.urls import path, include
from rest_framework import routers
from blog.api_views import PostViewSet


router = routers.DefaultRouter()
router.register(r'posts', PostViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
]