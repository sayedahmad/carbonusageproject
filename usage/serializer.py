from rest_framework import serializers

from .models import Usage, UsageType


class UsageTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = UsageType
        fields = ('__all__')


class UsageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usage
        fields = ('__all__')
