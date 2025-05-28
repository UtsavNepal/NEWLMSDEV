from .models import User
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class RegistrationSerializer(serializers.Serializer):
    user_name = serializers.CharField(write_only=True)
    email = serializers.EmailField(write_only=True)
    password = serializers.CharField(write_only=True)
    role = serializers.CharField(write_only=True)

    def validate(self, data):
        # Ensure userId is not in the data
        if 'userId' in self.initial_data:
            raise serializers.ValidationError("userId cannot be provided during registration.")
        return data
class LoginSerializer(serializers.Serializer):
    user_name = serializers.CharField(write_only=True)
    password = serializers.CharField(write_only=True)