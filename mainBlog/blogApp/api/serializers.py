from rest_framework.serializers import ModelSerializer, HyperlinkedIdentityField
from blogApp.models import Post


class PosCreateUpdateSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = [
            'title',
            'content',
            'publish'
        ]


class PostDetailSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = [
            'id',
            'title',
            'slug',
            'content',
            'publish'
        ]

    url_field_name = HyperlinkedIdentityField(
        view_name='detail',
        lookup_field='pk',
    )


class PostListSerializer(ModelSerializer):

    # delete_url = HyperlinkedIdentityField(
    #     view_name='delete',
    #     lookup_field='pk',
    # )

    class Meta:
        model = Post
        fields = [
            'url_field_name',
            'user',
            'id',
            'title',
            'slug',
            'content',
            'publish',
            # 'delete_url'
        ]
