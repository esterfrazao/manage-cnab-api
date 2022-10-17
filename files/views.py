from rest_framework.generics import ListCreateAPIView

from .mixins import SerializerByMethod
from .models import File
from .serializer import FileFormSerializer, FileSerializer


class FileView(SerializerByMethod, ListCreateAPIView):
    serializer_class = FileFormSerializer
    serializer_map = {
        "GET": FileSerializer,
        "POST": FileFormSerializer,
    }
    queryset = File.objects.all()
