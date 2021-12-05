from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Box


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'username', 'password', "is_staff", "date_joined")

    def create(self, validated_data):
        user = super(UserSerializer, self).create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user


class BoxSerializer(serializers.ModelSerializer):
    class Meta:
        model = Box
        fields = ["length", "width", "height"]


class BoxNonStaffSerializer(serializers.ModelSerializer):
    class Meta:
        model = Box
        fields = ["length", "width", "height", "area", "volume"]


class BoxStaffSerializer(serializers.ModelSerializer):
    class Meta:
        model = Box
        fields = ["length", "width", "height", "area", "volume", "created_by", "last_updated", "created_date"]


class BoxNonStaffSerializer(serializers.ModelSerializer):
    class Meta:
        model = Box
        fields = ["length", "width", "height", "area", "volume"]
