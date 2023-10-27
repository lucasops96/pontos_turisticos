from rest_framework import serializers

from atracoes.api.serializers import AtracaoSerializer
from enderecos.api.serializers import EnderecoSerializer
from core.models import PontoTuristico


class PontoTuristicoSerializer(serializers.ModelSerializer):
    atracoes = AtracaoSerializer(many=True)
    endereco = EnderecoSerializer()

    class Meta:
        model = PontoTuristico
        fields = ['id','nome','descricao','aprovado','foto',
                'atracoes','comentarios','avaliacoes','endereco']