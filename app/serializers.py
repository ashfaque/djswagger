from rest_framework import serializers
import datetime
from app.models import *


class SwaggerTestCreateSerializer(serializers.ModelSerializer):
    created_by = serializers.CharField(default=serializers.CurrentUserDefault())
    class Meta:
        model = SwaggerTest
        fields = '__all__'


class SwaggerTestEditSerializer(serializers.ModelSerializer):
    updated_by = serializers.CharField(default=serializers.CurrentUserDefault())
    updated_at = serializers.DateTimeField(default=datetime.datetime.now())
    class Meta:
        model = SwaggerTest
        fields = '__all__'


class SwaggerTestDeleteSerializer(serializers.ModelSerializer):
    deleted_by = serializers.CharField(default=serializers.CurrentUserDefault())
    is_deleted = serializers.BooleanField(default=True)
    deleted_at = serializers.DateTimeField(default=datetime.datetime.now())

    class Meta:
        model = SwaggerTest
        fields = '__all__'
