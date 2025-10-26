from django.urls import path
from . import views


urlpatterns = [
    path('', views.PostListView.as_view(), name='post_list'),
    path('posts/create/', views.post_create, name='post_create'),
    path('posts/p/<slug:slug>/', views.post_detail, name='post_detail'),
    path('posts/p/<slug:slug>/edit/', views.post_update, name='post_update'),
    path('posts/p/<slug:slug>/delete/', views.post_delete, name='post_delete'),
    path('posts/c/<slug:category_slug>/', views.PostsByCategoryView.as_view(), name='posts_by_category'),
    path('search/', views.SearchView.as_view(), name='search'),
]