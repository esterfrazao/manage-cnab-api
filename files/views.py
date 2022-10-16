from forms.serializers import FileFormSerializer
from rest_framework.generics import ListCreateAPIView

from .models import File
from .serializer import FileSerializer


class FileView(ListCreateAPIView):
    serializer_class = FileFormSerializer
    queryset = File.objects.all()
