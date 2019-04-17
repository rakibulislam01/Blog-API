from rest_framework.serializers import ModelSerializer
from blogApp.models import Post


class PostSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = [
            'id',
            'title',
            'slug',
            'content',
            'publish'
        ]
