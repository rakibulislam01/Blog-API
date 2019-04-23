from rest_framework.serializers import (ModelSerializer,
                                        HyperlinkedIdentityField,
                                        SerializerMethodField)
from blogApp.models import Post
from comments.api.serializers import CommentSerializer
from comments.models import Comment


class PosCreateUpdateSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = [
            'title',
            'content',
            'publish'
        ]


url_field_name = HyperlinkedIdentityField(
    view_name='detail',
    lookup_field='pk',
)


class PostDetailSerializer(ModelSerializer):
    user = SerializerMethodField()
    url = url_field_name
    html = SerializerMethodField()
    comments = SerializerMethodField()

    class Meta:
        model = Post
        fields = [
            'url',
            'id',
            'user',
            'title',
            'slug',
            'content',
            'publish',
            'image',
            'html',
            'comments',
        ]

    def get_user(self, obj):
        return str(obj.user.username)

    def get_html(self, obj):
        return obj.get_markdown()

    def get_image(self, obj):
        try:
            image = obj.image.url
        except:
            image = None
        return image

    def get_comments(self, obj):
        c_qs = Comment.objects.filter_by_instance(obj)
        comments = CommentSerializer(c_qs, many=True).data
        return comments


class PostListSerializer(ModelSerializer):
    url = url_field_name
    user = SerializerMethodField()

    # delete_url = HyperlinkedIdentityField(
    #     view_name='delete',
    #     lookup_field='pk',
    # )

    class Meta:
        model = Post
        fields = [
            'url',
            'user',
            'id',
            'title',
            'slug',
            'content',
            'publish',
            # 'delete_url'
        ]

    def get_user(self, obj):
        return str(obj.user.username)
