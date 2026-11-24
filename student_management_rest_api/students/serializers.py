from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Student

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=8)

    class Meta:
        model = User
        fields = ["id", "username", "email", "password"]

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class StudentSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source="owner.username")

    class Meta:
        model = Student
        fields = [
            "id", "owner", "name", "email", "roll_number",
            "course", "age", "created_at"
        ]
        read_only_fields = ["id", "owner", "created_at"]

    def validate_age(self, value):
        if value < 16 or value > 100:
            raise serializers.ValidationError("Age must be between 16 and 100.")
        return value
