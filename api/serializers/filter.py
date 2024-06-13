from ..models import Filter

from rest_framework import serializers

class FilterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Filter
        fields = '__all__'