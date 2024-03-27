from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("Hola, esta es tu aplicacion de calc")

def suma(request, op1, op2):
    return HttpResponse("Este es el resultado de la suma: {}".format(op1 + op2))

def resta(request, op1, op2):
    return HttpResponse("Este es el resultado de la resta: {}".format(op1 - op2))