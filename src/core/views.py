from django.http import HttpResponse
from django.shortcuts import render

def saludar(request):
	return HttpResponse("Hola desde Django Version JL!")

def saludar_con_etiqueta(request):
	return HttpResponse("<h1> Esta es la etiqueta que le llaman título de mi App! </h1>")

def saludar_con_parametros(request, nombre: str, apellido:str):
	nombre = nombre.capitalize()
	apellido = apellido.capitalize()
	return HttpResponse(f"{apellido}, {nombre}")

def index(request):
	return render(request, "core/index.html")

# Create your views here.
