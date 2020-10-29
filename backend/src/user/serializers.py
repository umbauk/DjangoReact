from django.contrib.auth import authenticate
from django.contrib.auth.models import update_last_login
from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken

from .models import User


class UserRegistrationSerializer(serializers.ModelSerializer):

    token = serializers.CharField(max_length=255, read_only=True)
    id = serializers.CharField(max_length=255, read_only=True)

    class Meta:
        model = User
        fields = ('email', 'password', 'first_name', 'last_name', 'token', 'id')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        refresh = RefreshToken.for_user(user)
        jwt_token = str(refresh.access_token)
        update_last_login(None, user)
        return {
            'id': user.id,
            'token': jwt_token,
            'email': user.email,
            'first_name': user.first_name,
            'last_name': user.last_name,
        }


class UserLoginSerializer(serializers.Serializer):

    email = serializers.CharField(max_length=255)
    password = serializers.CharField(max_length=128, write_only=True)
    id = serializers.CharField(max_length=255, read_only=True)
    token = serializers.CharField(max_length=255, read_only=True)

    def validate(self, data):
        email = data.get("email", None)
        password = data.get("password", None)
        user = authenticate(email=email, password=password)
        if user is None:
            raise serializers.ValidationError(
                'A user with this email and password is not found.'
            )
        try:
            refresh = RefreshToken.for_user(user)
            jwt_token = str(refresh.access_token)
            update_last_login(None, user)
        except User.DoesNotExist:
            raise serializers.ValidationError(
                'User with given email and password does not exists'
            )

        return {
            'email': user.email,
            'id': user.id,
            'token': jwt_token
        }


# class UserSerializerWithToken(serializers.ModelSerializer):
#
#     token = serializers.SerializerMethodField()
#     password = serializers.CharField(write_only=True)
#
#     def create(self, validated_data):
#         password = validated_data.pop('password', None)
#         instance = self.Meta.model(**validated_data)
#         if password is not None:
#             instance.set_password(password)
#         instance.save()
#         return instance
#
#     class Meta:
#         model = User
#         fields = ('token', 'username', 'password')
