from rest_framework import serializers
from rest_framework.fields import CurrentUserDefault
from .models import PerformanceReport
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('username', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User(
            username=validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.save()
        Token.objects.create(user=user)
        return (user)


class PerformanceReportSerializer(serializers.ModelSerializer):
    employee = serializers.CharField(default=serializers.CurrentUserDefault())
    class Meta:
        model = PerformanceReport
        exclude = ["id"]

class AdminPerformanceReportListSerializer(serializers.ModelSerializer):
    employee = serializers.CharField(default=serializers.CurrentUserDefault())
    class Meta:
        model = PerformanceReport
        fields ="__all__"

class AdminPerformanceReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = PerformanceReport
        fields = "__all__"


class UserObjectSerializer(serializers.ModelSerializer):
    employee = serializers.CharField(default=serializers.CurrentUserDefault())
    class Meta:
        model = PerformanceReport
        fields = ['employee']
