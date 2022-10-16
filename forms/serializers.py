from files.models import File
from files.serializer import FileSerializer
from rest_framework import serializers

from .models import ModelFileForm
from .parser import CNABParser


class FileFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = ModelFileForm
        fields = ["file"]

    def create(self, validated_data: dict):
        parser = CNABParser(validated_data.get("file"))

        for item in parser.transactions:
            serializer = FileSerializer(data=item)
            if serializer.is_valid():
                serializer.save()
                print("salvou")
            else:
                print(serializer.errors)

        return super().create(validated_data)
