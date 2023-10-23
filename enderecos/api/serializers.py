from rest_framework import serializers
from enderecos.models import Endereco

class EnderecoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Endereco
        fields = ['linha1']