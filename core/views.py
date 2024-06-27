from django.shortcuts import render
from .models import Estacionamiento, Acceso
# Create your views here.

def homePage(request):
    return render(request, 'core/inicio.html')

def estadisticas(request):
    lista_entradas = Acceso.objects.all()

    lunes, martes, miercoles, jueves, viernes, sabado, domingo = ([], [], [] , [], [], [], [])

    cantidad_autos = [0,0,0,0,0,0,0]
    cantidad_motos = [0,0,0,0,0,0,0]

    def verificar_tipo_auto(vehiculo, acceso, lugar_lista):
        if acceso == "0":
            if vehiculo == "A":
                cantidad_autos[lugar_lista] += 1
            else:
                cantidad_motos[lugar_lista] += 1
        # elif acceso == "1":
        #     if vehiculo == "A":
        #         cantidad_autos[lugar_lista] -= 1
        #     else:
        #         cantidad_motos[lugar_lista] -= 1


    for entrada in lista_entradas:
        if entrada.fecha.weekday() == 0:
            lunes.append(entrada)
            verificar_tipo_auto(entrada.vehiculo, entrada.acceso, 0)
        elif entrada.fecha.weekday() == 1:
            martes.append(entrada)
            verificar_tipo_auto(entrada.vehiculo, entrada.acceso, 1)
        elif entrada.fecha.weekday() == 2:
            miercoles.append(entrada)
            verificar_tipo_auto(entrada.vehiculo, entrada.acceso, 2)
        elif entrada.fecha.weekday() == 3:
            jueves.append(entrada)
            verificar_tipo_auto(entrada.vehiculo, entrada.acceso, 3)
        elif entrada.fecha.weekday() == 4:
            viernes.append(entrada)
            verificar_tipo_auto(entrada.vehiculo, entrada.acceso, 4)
        elif entrada.fecha.weekday() == 5:
            sabado.append(entrada)
            verificar_tipo_auto(entrada.vehiculo, entrada.acceso, 5)
        elif entrada.fecha.weekday() == 6:
            domingo.append(entrada)
            verificar_tipo_auto(entrada.vehiculo, entrada.acceso, 6)
        
    print("Autos: ",cantidad_autos)
    print("motos: ",cantidad_motos)

    return render(request, 'core/estadisticas.html')

def mapa_estacionamientos(request):
    estacionamientos_A = Estacionamiento.objects.filter(nombre__startswith="A")
    estacionamientos_B = Estacionamiento.objects.filter(nombre__startswith="B")
    estacionamientos_C = Estacionamiento.objects.filter(nombre__startswith="C")
    estacionamientos_D = Estacionamiento.objects.filter(nombre__startswith="D")
    estacionamientos_E = Estacionamiento.objects.filter(nombre__startswith="E")
    estacionamientos_F = Estacionamiento.objects.filter(nombre__startswith="F")
    estacionamientos_M = Estacionamiento.objects.filter(nombre__startswith="M")
    cantidad_ocupados = Estacionamiento.objects.filter(ocupado=0).count()

    data = {
        "A" : estacionamientos_A,
        "B" : estacionamientos_B,
        "C" : estacionamientos_C,
        "D" : estacionamientos_D,
        "E" : estacionamientos_E,
        "F" : estacionamientos_F,
        "M" : estacionamientos_M,
        "cantidad" : cantidad_ocupados
        
    }

    return render(request, 'core/mapa_estacionamientos.html',data)