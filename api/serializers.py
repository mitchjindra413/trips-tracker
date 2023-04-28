from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from django.core import exceptions

class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'username', 'password')
    
    def validate(self, data):
        user = User(**data)
        password = user.get("password")

        try:
            validate_password(password, user)
        except exceptions.ValidationError as e:
            serializer_errors = serializers.as_serializer_error(e)
            raise exceptions.ValidationError(
                {'password': serializer_errors['non_field_errors']}
            )

    
    def create(self, validatedData):
        user = User.objects.create_user(
            email=validatedData["email"],
            password=validatedData["password"],
            username=validatedData["username"]
        )

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'username')
