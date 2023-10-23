from rest_framework import serializers
from avaliacoes.models import Avalicao


class AvalicaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Avalicao
        fields = ['id','usuario','comentario','nota','data']