from rest_framework import serializers
from comentarios.api.serializers import ComentarioSerializer
from avaliacoes.api.serializers import AvalicaoSerializer
from atracoes.api.serializers import AtracaoSerializer
from enderecos.api.serializers import EnderecoSerializer
from core.models import PontoTuristico


class PontoTuristicoSerializer(serializers.ModelSerializer):
    atracoes = AtracaoSerializer(many=True)
    comentarios = ComentarioSerializer(many=True)
    avaliacoes = AvalicaoSerializer(many=True)
    endereco = EnderecoSerializer()
    descricao_completa = serializers.SerializerMethodField()

    class Meta:
        model = PontoTuristico
        fields = ['id','nome','descricao','aprovado','foto',
                'atracoes','comentarios','avaliacoes','endereco',
                'descricao_completa','descricao_completa2']
    

    def get_descricao_completa(self,obj):
        return '%s - %s' % (obj.nome, obj.descricao)