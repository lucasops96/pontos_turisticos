from rest_framework import viewsets
from avaliacoes.models import Avalicao
from .serializers import AvalicaoSerializer


class AvaliacaoViewSet(viewsets.ModelViewSet):
    queryset = Avalicao.objects.all()
    serializer_class = AvalicaoSerializer