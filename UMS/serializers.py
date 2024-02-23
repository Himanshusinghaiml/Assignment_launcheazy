from rest_framework import serializers
from django.contrib.auth.models import User

class UserSignupSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)  # Define password field separately

    class Meta:
        model = User
        fields = ['username', 'password']  # Use lowercase 'username'

    # Override the create method to properly set the password
    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password']
        )
        return user
