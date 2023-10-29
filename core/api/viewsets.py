from django.http import HttpResponse
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from core.models import PontoTuristico
from .serializers import PontoTuristicoSerializer
from rest_framework.filters import SearchFilter

class PontoTuristicoViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    # queryset = PontoTuristico.objects.filter(aprovado=True)
    serializer_class = PontoTuristicoSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [SearchFilter]
    search_fields = ['nome', 'descricao','endereco__linha1']
    # lookup_field = 'nome'

    def get_queryset(self):
        id = self.request.query_params.get('id',None)
        nome = self.request.query_params.get('nome',None)
        descricao = self.request.query_params.get('descricao',None)
        queryset = PontoTuristico.objects.filter(aprovado=True)

        if id:
            queryset = PontoTuristico.objects.filter(pk=id)
        
        if nome:
            queryset = queryset.filter(nome__icontains=nome)
        
        if descricao:
            queryset = queryset.filter(descricao__icontains=descricao)

        return queryset
        
    
    def list(self, request, *args, **kwargs):
        return super(PontoTuristicoViewSet,self).list(request,*args, **kwargs)
    
    def create(self,request, *args, **kwargs):
        return super(PontoTuristicoViewSet,self).create(request,*args, **kwargs)
    
    def destroy(self, request, *args, **kwargs):
        return super(PontoTuristicoViewSet,self).destroy(request,*args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        return super(PontoTuristicoViewSet,self).retrieve(request,*args, **kwargs)

    def update(self, request, *args, **kwargs):
        return super(PontoTuristicoViewSet,self).update(request,*args, **kwargs) 
    
    def partial_update(self, request, *args, **kwargs):
        return super(PontoTuristicoViewSet,self).partial_update(request,*args, **kwargs)

    @action(methods=['get'],detail=True)
    def denunciar(self, request, pk=None):
        pass
    
    @action(methods=['get'],detail=False)
    def teste(self,request):
        pass

    @action(methods=['post'],detail=True)
    def associa_atracoes(self,request,pk):
        atracoes = request.data['ids']

        ponto = PontoTuristico.objects.get(pk=pk)

        ponto.atracoes.set(atracoes)

        ponto.save()

        return HttpResponse('OK')