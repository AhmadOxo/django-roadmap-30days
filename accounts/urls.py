from . import views
from django.urls import path


app_name = 'user'

urlpatterns = [
    path('profile/<str:username>/', views.profile_view, name='profile'),
    path('profile/<str:username>/edit/', views.profile_edit, name='profile_edit'),
]