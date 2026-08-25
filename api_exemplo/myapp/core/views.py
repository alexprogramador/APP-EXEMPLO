from django.shortcuts import render
from rest_framework import viewsets
from .models import Pessoa
from .serializers import PessoaSerializer

# Create your views here.
class PessoaViewSet(viewsets.ModelViewSet):
    queryset = Pessoa.objects.all()
    serializer_class = PessoaSerializer
from django.http import JsonResponse
import json

def pessoas(request):
    if request.method == "POST":
        data = json.loads(request.body)

        nome = data["nome"]
        idade = data["idade"]

        return JsonResponse({"mensagem": "Pessoa criada"})