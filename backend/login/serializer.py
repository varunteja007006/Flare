from rest_framework import serializers
from django.contrib.auth.models import User

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "email", "password", "first_name", "last_name"]
    
    def validate(self, attrs):
        email = attrs.get("email")
        username = attrs.get("username")

        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError(
                {"error_message": "Email address already exists."}
            )

        if User.objects.filter(username=username).exists():
            raise serializers.ValidationError(
                {"error_message": "Username already exists."}
            )

        return attrs


# For use with user profile in employee
class UserDataSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ["username", "email"]
