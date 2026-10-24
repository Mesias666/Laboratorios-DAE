from django.shortcuts import render, get_object_or_404
from .models import Autor, Entrada

def lista_entradas(request):
    entradas = Entrada.objects.all()
    return render(request, 'blog/lista_entradas.html', {'entradas': entradas})

def lista_autores(request):
    autores = Autor.objects.all()
    return render(request, 'blog/lista_autores.html', {'autores': autores})

def entradas_por_autor(request, autor_id):
    autor = get_object_or_404(Autor, id=autor_id)
    entradas = autor.entradas.all()
    return render(request, 'blog/entradas_autor.html', {'autor': autor, 'entradas': entradas})