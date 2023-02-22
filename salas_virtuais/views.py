from django.shortcuts import render, redirect
from .models import Sala
from .forms import SalaForm

# Create your views here.
def index(request):
    salas = Sala.objects.all().order_by('-data_criacao')
    context = {
        'salas': salas
    }
    return render(request, 'index.html', context)

def criar_sala(request):
    form = SalaForm()
    if request.method == 'POST':
        form = SalaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {
        'form': form,
    }
    return render(request, 'criar_sala.html', context)