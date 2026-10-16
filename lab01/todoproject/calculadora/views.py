from django.http import HttpResponse

def sumar(request, numero1, numero2):
    resultado = numero1 + numero2
    return HttpResponse(f"La suma de {numero1} + {numero2} = {resultado}")


def restar(request, numero1, numero2):
    resultado = numero1 - numero2
    return HttpResponse(f"La resta de {numero1} - {numero2} = {resultado}")


def multiplicar(request, numero1, numero2):
    resultado = numero1 * numero2
    return HttpResponse(f"La multiplicación de {numero1} x {numero2} = {resultado}")