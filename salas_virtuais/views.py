from django.shortcuts import render, redirect
from .models import Sala
from .models import CATEGORIAS

# Create your views here.
def index(request):
    salas = Sala.objects.all().order_by('-data_criacao')
    context = {
        'salas': salas
    }
    return render(request, 'index.html', context)

def criar_sala(request):
    categorias = CATEGORIAS
    context = {
        'categorias': categorias
    }
    return render(request, 'criar_sala.html', context)