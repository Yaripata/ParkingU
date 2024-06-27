from django.shortcuts import render
from .models import Estacionamiento, Acceso
from datetime import date
# Create your views here.

def homePage(request):
    salidas = Acceso.objects.filter(acceso=1).count()
    entradas = Acceso.objects.filter(acceso=0).count()

    estacionamientos_A = Estacionamiento.objects.filter(nombre__startswith="A").count()
    estacionamientos_B = Estacionamiento.objects.filter(nombre__startswith="B").count()
    estacionamientos_C = Estacionamiento.objects.filter(nombre__startswith="C").count()
    estacionamientos_D = Estacionamiento.objects.filter(nombre__startswith="D").count()
    estacionamientos_E = Estacionamiento.objects.filter(nombre__startswith="E").count()
    estacionamientos_F = Estacionamiento.objects.filter(nombre__startswith="F").count()
    estacionamientos_M = Estacionamiento.objects.filter(nombre__startswith="M").count()

    data = {
        "cantidad_actual" : entradas - salidas,
        "cantidad_A" : estacionamientos_A,
        "cantidad_B" : estacionamientos_B,
        "cantidad_C" : estacionamientos_C,
        "cantidad_D" : estacionamientos_E,
        "cantidad_E" : estacionamientos_D,
        "cantidad_F" : estacionamientos_F,
        "cantidad_M" : estacionamientos_M,
    }

    return render(request, 'core/inicio.html', data)

def estadisticas(request):
    lista_entradas = Acceso.objects.all()
    semana = [[], [], [] , [], [], [], []]
    lunes, martes, miercoles, jueves, viernes, sabado, domingo = semana

    cantidad_autos = [0,0,0,0,0,0,0]
    cantidad_motos = [0,0,0,0,0,0,0]
    disp_hora_actual = [0]*17
    disp_hora_anterior = [0]*17

    dia_actual = date.today().weekday()
    if dia_actual == 0:
        dia_anterior = 6
    elif dia_actual >= 1:
        dia_anterior = dia_actual - 1

    def verificar_tipo_auto(vehiculo, acceso, lugar_lista):
        if acceso == "0":
            if vehiculo == "A":
                cantidad_autos[lugar_lista] += 1
            else:
                cantidad_motos[lugar_lista] += 1

    def contar_hora(lista, entrada):
        hora = entrada.fecha.time().hour
        match hora:
            case 6:
                lista[0] += 1
            case 7:
                lista[1] += 1
            case 8:
                lista[2] += 1
            case 9:
                lista[3] += 1
            case 10:
                lista[4] += 1
            case 11:
                lista[5] += 1
            case 12:
                lista[6] += 1
            case 13:
                lista[7] += 1
            case 14:
                lista[8] += 1
            case 15:
                lista[9] += 1
            case 16:
                lista[10] += 1
            case 17:
                lista[11] += 1
            case 18:
                lista[12] += 1
            case 19:
                lista[13] += 1
            case 20:
                lista[14] += 1
            case 21:
                lista[15] += 1
            case 22:
                lista[16] += 1

    for entrada in lista_entradas:
        if entrada.fecha.weekday() == 0:
            lunes.append(entrada)
            verificar_tipo_auto(entrada.vehiculo, entrada.acceso, 0)
            if dia_actual == 0:
                contar_hora(disp_hora_actual, entrada)
            elif dia_anterior == 0:
                contar_hora(disp_hora_anterior, entrada)
        elif entrada.fecha.weekday() == 1:
            martes.append(entrada)
            verificar_tipo_auto(entrada.vehiculo, entrada.acceso, 1)
            if dia_actual == 1:
                contar_hora(disp_hora_actual, entrada)
            elif dia_anterior == 1:
                contar_hora(disp_hora_anterior, entrada)
        elif entrada.fecha.weekday() == 2:
            miercoles.append(entrada)
            verificar_tipo_auto(entrada.vehiculo, entrada.acceso, 2)
            if dia_actual == 2:
                contar_hora(disp_hora_actual, entrada)
            elif dia_anterior == 2:
                contar_hora(disp_hora_anterior, entrada)
        elif entrada.fecha.weekday() == 3:
            jueves.append(entrada)
            verificar_tipo_auto(entrada.vehiculo, entrada.acceso, 3)
            if dia_actual == 3:
                contar_hora(disp_hora_actual, entrada)
            elif dia_anterior == 3:
                contar_hora(disp_hora_anterior, entrada)
        elif entrada.fecha.weekday() == 4:
            viernes.append(entrada)
            verificar_tipo_auto(entrada.vehiculo, entrada.acceso, 4)
            if dia_actual == 4:
                contar_hora(disp_hora_actual, entrada)
            elif dia_anterior == 4:
                contar_hora(disp_hora_anterior, entrada)
        elif entrada.fecha.weekday() == 5:
            sabado.append(entrada)
            verificar_tipo_auto(entrada.vehiculo, entrada.acceso, 5)
            if dia_actual == 5:
                contar_hora(disp_hora_actual, entrada)
            elif dia_anterior == 5:
                contar_hora(disp_hora_anterior, entrada)
        elif entrada.fecha.weekday() == 6:
            domingo.append(entrada)
            verificar_tipo_auto(entrada.vehiculo, entrada.acceso, 6)
            if dia_actual == 6:
                contar_hora(disp_hora_actual, entrada)
            elif dia_anterior == 6:
                contar_hora(disp_hora_anterior, entrada)

    data = {
        "motos" : cantidad_motos,
        "autos" : cantidad_autos,
        "disp_actual" : disp_hora_actual,
        "disp_anterior" : disp_hora_anterior,
        "lunes_combinado" : cantidad_motos[0] + cantidad_autos[0],
        "martes_combinado" : cantidad_motos[1] + cantidad_autos[1],
        "miercoles_combinado" : cantidad_motos[2] + cantidad_autos[2],
        "jueves_combinado" : cantidad_motos[3] + cantidad_autos[3],
        "viernes_combinado" : cantidad_motos[4] + cantidad_autos[4],
        "sabado_combinado" : cantidad_motos[5] + cantidad_autos[5],
        "domingo_combinado" : cantidad_motos[6] + cantidad_autos[6],
    }

    return render(request, 'core/estadisticas.html', data)

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

def control(request):
    
    return render(request, 'core/mapa_estacionamientos.html',data)