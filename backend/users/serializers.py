from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import User

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 
                 'phone_number', 'user_type', 'college_name', 'student_id', 
                 'is_verified', 'profile_picture', 'created_at']
        read_only_fields = ['id', 'created_at', 'is_verified']


class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=8)
    password_confirm = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'password_confirm', 
                 'first_name', 'last_name', 'phone_number', 'user_type', 
                 'college_name', 'student_id']

    def validate(self, attrs):
        if attrs['password'] != attrs['password_confirm']:
            raise serializers.ValidationError("Passwords don't match")
        return attrs

    def create(self, validated_data):
        validated_data.pop('password_confirm')
        user = User.objects.create_user(**validated_data)
        return user
