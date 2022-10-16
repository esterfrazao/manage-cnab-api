from rest_framework import serializers

from .models import ModelFileForm


class FileFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = ModelFileForm
        fields = ["file"]

    def create(self, validated_data):
        return super().create(validated_data)
