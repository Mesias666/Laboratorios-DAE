import math
from django.shortcuts import render

def index(request):
    context = {
        'titulo': "Formulario",
    }
    return render(request, 'encuesta/formulario.html', context)

def enviar(request):
    context = {
        'titulo': "Respuesta",
        'nombre': request.POST['nombre'],
        'clave': request.POST['password'],
        'educacion': request.POST['educacion'],
        'nacionalidad': request.POST['nacionalidad'],
        'idiomas': request.POST.getlist('idiomas'),
        'correo': request.POST['email'],
        'website': request.POST['sitioweb'],
    }
    return render(request, 'encuesta/respuesta.html', context)

def cilindro(request):
    return render(request, 'encuesta/cilindro.html')

def volumen(request):
    diametro = float(request.POST['diametro'])
    altura = float(request.POST['altura'])
    radio = diametro / 2
    vol = math.pi * radio ** 2 * altura
    return render(request, 'encuesta/volumen.html', {'volumen': vol})