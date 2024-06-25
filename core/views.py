from django.shortcuts import render

# Create your views here.

def homePage(request):
    return render(request, 'core/inicio.html')

def estadisticas(request):
    return render(request, 'core/estadisticas.html')

def mapa_estacionamientos(request):
    return render(request, 'core/mapa_estacionamientos.html')