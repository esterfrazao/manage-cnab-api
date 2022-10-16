from rest_framework import serializers

from .models import File
from .parser import CNABParser


class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = "__all__"


class FileFormSerializer(serializers.Serializer):
    file = serializers.FileField(write_only=True)
    message = serializers.CharField(read_only=True)

    def create(self, validated_data: dict):
        parser = CNABParser(validated_data.get("file"))

        for item in parser.transactions:
            serializer = FileSerializer(data=item)
            serializer.is_valid(raise_exception=True)
            serializer.save()

        return {"message": "File successfully parsed!"}
