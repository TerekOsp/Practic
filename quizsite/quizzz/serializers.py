from rest_framework import serializers
from .models import Users


class UsersSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField()
    name = serializers.CharField(max_length=50)
    email = serializers.CharField(max_length=50)
    password = serializers.CharField(max_length=20)
    phone = serializers.CharField(max_length=20)

    def create(self, validated_data):
        return Users.objects.create(**validated_data)
