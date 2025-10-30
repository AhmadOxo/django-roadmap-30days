import django_filters
from .models import Post

class PostFilter(django_filters.FilterSet):
    category = django_filters.CharFilter(field_name='categories__slug')

    class Meta:
        model = Post
        fields = ['category']