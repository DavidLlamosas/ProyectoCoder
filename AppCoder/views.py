from django.shortcuts import render
from django.http import HttpResponse
#from .models import Profesor     #Importamos la clase profesor de models aunque tambien podriamos importar todo con *
#COMO VIEWS ESTA DENTRO DE LA CARPETA DE APPCODER Y MODELS TAMBIEN ENTONCES, PODEMOS PONER .models en vez de AppCoder.models
from .models import *

def profe_nuevo(request):
    profeN = Profesor(nombre = "Pepe", apellido="Python", email="pepe@hotmail.com", profesion="Biofísico")   #Siempre colocar por nombre, atributos...
    profeN.save() #En el caso que no se coloquen los nombres aparecera por ID...

    return HttpResponse(f"Hemos guardado al profesor {profeN.nombre}")   #Atributo de profeN, en este caso nombre.

def curso_nuevo(request):
    curso_fav = Curso(nombre= "Python", comision=47765)   #Siempre colocar por nombre, atributos...
    curso_fav.save() #En el caso que no se coloquen los nombres aparecera por ID...

    return HttpResponse(f"Bienvenidos al curso {curso_fav.nombre} comision {curso_fav.comision}") 