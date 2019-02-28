from django.shortcuts import render

from .models import Pergunta
# Create your views here.

def index(request):
    perguntas = Pergunta.objects.all()
    return render(request, 'index.html',{
        "perguntas" : perguntas
    })