from django.shortcuts import render
from django.http import HttpResponse

def inicio_view(request):
  return HttpResponse("Bienvenidos")

from django.template import Template, Context
from django.http import HttpResponse

def cursos_view(request):
  #return HttpResponse("Estos son mis cursos")
  return render(request, "AppCoder/padre.html")

def cursos_view(xx):
    nombre = "Mariano Manuel"
    apellido = "Barracovich"
    diccionario = {
        'nombre': nombre,
        'apellido': apellido,
        "nacionalidad": "argentino"
    }  # Para enviar al contexto

    ruta = "C:/Users/nazareno/Desktop/Code/Proyecto_final/ProyectoFinal2/AppCoder/templates/AppCoder/padre.html"
    mi_archivo = open(ruta, "r")

    # "Método django - versión 1"
    plantilla = Template(mi_archivo.read())  # Se carga en memoria nuestro documento, template1
    contexto = Context(diccionario)  # Le doy al contexto mi nombre y apellido
    documento = plantilla.render(contexto)  # Aqui renderizamos la plantilla en documento

    return HttpResponse(documento)