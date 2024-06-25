from rest_framework import serializers
from .models import StatusOrder


class StatusOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = StatusOrder
        fields = ['id', 'nameStatus', 'colorStatus', 'descriptionStatus']