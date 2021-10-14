from rest_framework import serializers

from .models import Usage, Usage_type


class UsageTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usage_type
        fields = ('__all__')


class UsageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usage
        fields = ('__all__')
