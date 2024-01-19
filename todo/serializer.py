
from rest_framework import serializers
from django.contrib.auth.hashers import make_password

from .models import ToDoModel, CustomUser


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, style={'input_type': 'password'})
    confirm_password = serializers.CharField(write_only=True, required=True, style={'input_type': 'password'})

    def validate(self, data):
        password = data.get('password')
        confirm_password = data.pop('confirm_password', None)
        if password != confirm_password:
            raise serializers.ValidationError('password do not match')
        return data

    def create(self, validated_data):
        user = CustomUser(
            username=validated_data['username'],
            password=make_password(validated_data['password']),
            roles=validated_data.get('roles', 1)
        )
        validated_data.pop('confrim_password', None)
        user.save()
        return user

    class Meta:
        model = CustomUser
        fields = ('id', 'username', 'password', 'confirm_password')
        extra_kwargs = {
            'password': {'write_only': True, 'required': True},
            'confirm_password': {'write_only': True, 'required': True}
        }


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ToDoModel
        fields = ('id', 'title', 'description', 'completed', 'important')
        extra_kwargs = {
            'description': {'required': False}
        }
