from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from core.models import PontoTuristico

from .serializers import PontoTuristicoSerializer


class PontoTuristicoViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    # queryset = PontoTuristico.objects.filter(aprovado=True)
    serializer_class = PontoTuristicoSerializer

    def get_queryset(self):
        return PontoTuristico.objects.filter(aprovado=True)
    
    def list(self, request, *args, **kwargs):
        return Response({'teste':123})
    
    def create(self,request, *args, **kwargs):
        return Response({'Hello':request.data['nome']})
    
    def destroy(self, request, *args, **kwargs):
        pass

    def retrieve(self, request, *args, **kwargs):
        pass

    def update(self, request, *args, **kwargs):
        pass 
    
    def partial_update(self, request, *args, **kwargs):
        pass

    @action(methods=['get'],detail=True)
    def denunciar(self, request, pk=None):
        pass
    
    @action(methods=['get'],detail=False)
    def teste(self,request):
        pass