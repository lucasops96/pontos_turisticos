from rest_framework import serializers
from comentarios.api.serializers import ComentarioSerializer
from avaliacoes.api.serializers import AvalicaoSerializer
from atracoes.api.serializers import AtracaoSerializer
from enderecos.api.serializers import EnderecoSerializer
from core.models import PontoTuristico
from atracoes.models import Atracao


class PontoTuristicoSerializer(serializers.ModelSerializer):
    atracoes = AtracaoSerializer(many=True)
    # comentarios = ComentarioSerializer(many=True,read_only=True)
    # avaliacoes = AvalicaoSerializer(many=True,read_only=True)
    endereco = EnderecoSerializer(read_only=True)
    descricao_completa = serializers.SerializerMethodField()

    class Meta:
        model = PontoTuristico
        fields = ['id','nome','descricao','aprovado','foto',
                'atracoes','comentarios','avaliacoes','endereco',
                'descricao_completa','descricao_completa2']
        read_only_fields = ['comentarios','avaliacoes']
    
    def criar_atracoes(self,atracoes,ponto):
        for atracao in atracoes:
            at = Atracao.objects.create(**atracao)
            ponto.atracoes.add(at)

    def create(self, validated_data):
        atracoes = validated_data['atracoes']
        del validated_data['atracoes']
        ponto = PontoTuristico.objects.create(**validated_data)
        self.criar_atracoes(atracoes,ponto)
        
        return ponto

    

    def get_descricao_completa(self,obj):
        return '%s - %s' % (obj.nome, obj.descricao)