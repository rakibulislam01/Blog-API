from django.contrib.contenttypes.models import ContentType
from django.contrib.auth import get_user_model
from rest_framework.serializers import (HyperlinkedIdentityField,
                                        CharField,
                                        EmailField,
                                        ModelSerializer,
                                        SerializerMethodField,
                                        ValidationError)

User = get_user_model()


class UserCreateSerializer(ModelSerializer):
    email = EmailField(label="Email address")
    email2 = EmailField(label="Confirm email")

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'email2',
            'password',
        ]
        extra_kwargs = {
            "password": {
                "write_only": True
            }
        }

    def validate_email(self, value):
        data = self.get_initial()
        email1 = data.get("email2")
        email2 = value

        if email1 != email2:
            raise ValidationError("Email must match.")

        user_qs = User.objects.filter(email=email2)

        if user_qs.exists():
            raise ValidationError("This user email already exists.")
        return value

    def validate_email2(self, value):
        data = self.get_initial()
        email1 = data.get("email")
        email2 = value

        if email1 != email2:
            raise ValidationError("Email must match.")
        return value

    def create(self, validated_data):
        username = validated_data['username']
        email = validated_data['email']
        password = validated_data['password']
        user_obj = User(
            username=username,
            email=email
        )
        user_obj.set_password(password)
        user_obj.save()
        return validated_data


class UserLoginSerializer(ModelSerializer):
    token = CharField(allow_blank=True, read_only=True)
    username = CharField()
    email = EmailField(label="Email address")

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password',
            'token',
        ]
        extra_kwargs = {
            "password": {
                "write_only": True
            }
        }
