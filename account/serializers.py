from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'email')
        # read_only_fields = ('username', 'email')


class CreateUserSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        # call create_user on user object. Without this
        # the password will be stored in plain text.
        user = User.objects.create_user(**validated_data)
        return user

    class Meta:
        model = User
        fields = ('username', 'password', 'first_name',
                  'last_name', 'email', 'activation_token')
        extra_kwargs = {'password': {'write_only': True},
                        'activation_token': {'write_only': True}}


class UserActivationSerializer(serializers.Serializer):
    activation_token = serializers.CharField(max_length=30)
    email = serializers.CharField(max_length=30)
