from forms.serializers import FileFormSerializer
from rest_framework.generics import ListCreateAPIView

from .mixins import SerializerByMethod
from .models import File
from .serializer import FileSerializer


class FileView(SerializerByMethod, ListCreateAPIView):
    serializer_map = {
        "GET": FileSerializer,
        "POST": FileFormSerializer,
    }
    queryset = File.objects.all()
