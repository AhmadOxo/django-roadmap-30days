from django.urls import path
from . import views
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularSwaggerView,
    SpectacularRedocView,
)

urlpatterns = [
    path('', views.PostListView.as_view(), name='post_list'),
    path('posts/create/', views.post_create, name='post_create'),
    path('posts/p/<slug:slug>/', views.post_detail, name='post_detail'),
    path('posts/p/<slug:slug>/edit/', views.post_update, name='post_update'),
    path('posts/p/<slug:slug>/delete/', views.post_delete, name='post_delete'),
    path('category/<slug:category_slug>/', views.PostsByCategoryView.as_view(), name='posts_by_category'),
    path('search/', views.SearchView.as_view(), name='search'),
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]