from rest_framework import serializers
from comentarios.api.serializers import ComentarioSerializer
from avaliacoes.api.serializers import AvalicaoSerializer
from atracoes.api.serializers import AtracaoSerializer
from enderecos.api.serializers import EnderecoSerializer
from core.models import PontoTuristico , DocIdentificacao
from atracoes.models import Atracao
from enderecos.models import Endereco

class DocIdentificacaoSerializar(serializers.ModelSerializer):
    class Meta:
        model = DocIdentificacao
        fields = '__all__'

class PontoTuristicoSerializer(serializers.ModelSerializer):
    atracoes = AtracaoSerializer(many=True)
    # comentarios = ComentarioSerializer(many=True,read_only=True)
    # avaliacoes = AvalicaoSerializer(many=True,read_only=True)
    endereco = EnderecoSerializer()
    descricao_completa = serializers.SerializerMethodField()
    doc_identificacao = DocIdentificacaoSerializar()

    class Meta:
        model = PontoTuristico
        fields = ['id','nome','descricao','aprovado','foto',
                'atracoes','comentarios','avaliacoes','endereco',
                'descricao_completa','descricao_completa2','doc_identificacao']
        read_only_fields = ['comentarios','avaliacoes']
    
    def criar_atracoes(self,atracoes,ponto):
        for atracao in atracoes:
            at = Atracao.objects.create(**atracao)
            ponto.atracoes.add(at)

    def create(self, validated_data):
        atracoes = validated_data['atracoes']
        del validated_data['atracoes']

        endereco = validated_data['endereco']
        del validated_data['endereco']

        doc_identi = validated_data['doc_identificacao']
        del validated_data['doc_identificacao']

        ponto = PontoTuristico.objects.create(**validated_data)
        self.criar_atracoes(atracoes,ponto)
        
        end = Endereco.objects.create(**endereco)
        ponto.endereco = end

        doc = DocIdentificacao.objects.create(**doc_identi)
        ponto.doc_identificacao = doc
        
        ponto.save()

        return ponto

    def get_descricao_completa(self,obj):
        return '%s - %s' % (obj.nome, obj.descricao)