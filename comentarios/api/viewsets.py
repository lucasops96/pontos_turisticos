from rest_framework import viewsets
from comentarios.models import Comentario
from .serializers import ComentarioSerializer

class ComentarioViewSet(viewsets.ModelViewSet):
    queryset = Comentario.objects.all()
    serializer_class = ComentarioSerializer