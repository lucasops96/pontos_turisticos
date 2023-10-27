from django.db import models
from atracoes.models import Atracao
from comentarios.models import Comentario
from avaliacoes.models import Avalicao
from enderecos.models import Endereco

class DocIdentificacao(models.Model):
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.description

class PontoTuristico(models.Model):
    nome = models.CharField(max_length=150)
    descricao = models.TextField()
    aprovado = models.BooleanField(default=False)

    atracoes = models.ManyToManyField(Atracao)
    comentarios = models.ManyToManyField(Comentario)
    avaliacoes = models.ManyToManyField(Avalicao)
    endereco = models.ForeignKey(Endereco, on_delete=models.CASCADE,null=True, blank=True)
    foto = models.ImageField(upload_to='pontos_turisticos',null=True,blank=True)
    doc_identificacao = models.OneToOneField(DocIdentificacao, on_delete=models.CASCADE,null=True,blank=True)

    @property
    def descricao_completa2(self):
        return f'{self.nome} - {self.aprovado}'

    def __str__(self):
        return self.nome