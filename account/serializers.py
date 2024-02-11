from django.contrib.auth.models import User
from .models import Profile
from rest_framework import serializers
from django.contrib.auth import authenticate


class UserProfileSerializer(serializers.ModelSerializer):
    """
    Serializer to fetch the user profile object
    """
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name',
                  'last_name', 'last_login', 'date_joined']
        extra_kwargs = {
            'id': {'read_only': True},
            'date_joined': {'read_only': True},
            'last_login': {'read_only': True}
        }


class ProfileSerializer(serializers.ModelSerializer):
    """
    Serializer for the user profile object
    """
    user = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(), write_only=True)
    interested_in = serializers.StringRelatedField(many=True)

    class Meta:
        model = Profile
        fields = ['user', 'image', 'interested_in']
        extra_kwargs = {
            'interested_in': {'required': False},
            'image': {'required': False}
        }


class ProfileWriteSerializer(serializers.ModelSerializer):
    """
    Serializer for the user profile object
    """

    class Meta:
        model = Profile
        fields = ['user', 'image', 'interested_in']
        extra_kwargs = {
            'interested_in': {'required': False},
            'image': {'required': False}
        }


class UserAllSerializer(serializers.ModelSerializer):
    """
    Serializer for the user profile object
    """
    profile = ProfileSerializer()

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name',
                  'last_name', 'last_login', 'date_joined', 'profile']


class AuthSerializer(serializers.Serializer):
    """
    Serializer for the user authentication object
    """
    username = serializers.CharField()
    password = serializers.CharField(
        style={'input_type': 'password'},
        trim_whitespace=False
    )

    def validate(self, attrs):
        username = attrs.get('username')
        password = attrs.get('password')

        user = authenticate(
            request=self.context.get('request'),
            username=username,
            password=password
        )

        if not user:
            msg = ('Unable to authenticate with provided credentials')
            raise serializers.ValidationError(msg, code='authentication')

        attrs['user'] = user
        return
