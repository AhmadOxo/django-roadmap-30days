from rest_framework import serializers
from django.contrib.auth.models import User
from blog.models import Post

class UserProfileSerializer(serializers.ModelSerializer):
    post_count = serializers.SerializerMethodField()
    avatar = serializers.ImageField(source='profile.avatar', read_only=True)
    bio = serializers.CharField(source='profile.bio', read_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'post_count', 'avatar', 'bio']

    def get_post_count(self, obj):
        return obj.post_set.count()