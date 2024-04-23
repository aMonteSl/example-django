from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404, HttpResponseRedirect
from .models import Contenido, Comentario
from django.views.decorators.csrf import csrf_exempt
import datetime
from django.template import loader
from django.contrib.auth import logout


# Create your views here.

formulario_contenido = """
<hr>
<form action="" method="POST">
    Introduce el (nuevo) contenido para esta pagina:
    <input type="text" name="valor">
    <input type="submit" value="Enviar">

</form>
"""

formulario_comentario = """
<hr>
<form action="" method="POST">
    Introduce un comentario para esta pagina: <br>
    Titulo: <input type="text" name="titulo"> <br>
    Cuerpo: <input type="text" name="cuerpo"> <br>
    <input type="submit" value="Enviar">

</form>
"""


@csrf_exempt
def exits_user(request):
    return request.user.is_authenticated


@csrf_exempt
def manage_content(request, clave):
    if request.method == "PUT":
        valor = request.body.decode("utf-8")
        actualizar_contenido(request, clave, valor)
    elif request.method == "POST":
        if "valor" in request.POST:
            valor = request.POST["valor"]
            actualizar_contenido(request, clave, valor)
        if "titulo" and "cuerpo" in request.POST:
            titulo = request.POST["titulo"]
            cuerpo = request.POST["cuerpo"]
            c = Contenido.objects.get(clave=clave)
            com_db = Comentario(
                titulo=titulo,
                cuerpo=cuerpo,
                fecha=datetime.datetime.now(),
                contenido=c)
            com_db.save()


@csrf_exempt
def get_content(request, clave):
    # Si el usuario no esta logeado, redirigir a la pagina de login
    if exits_user(request):
        manage_content(request, clave)

    try:
        # Mandar la template contenido.html
        contenido = Contenido.objects.get(clave=clave)
        comentarios = contenido.comentario_set.all()
        template = loader.get_template('contenido.html')
        context = {
            'contenido': contenido,
            'comentarios': comentarios,
            'usuario': request.user.is_authenticated
        }
        return HttpResponse(template.render(context, request))

    except Contenido.DoesNotExist:
        raise Http404("No existe para contenido para " + clave)


def actualizar_contenido(request, clave, valor):
    if request.method in ["PUT", "POST"]:
        try:
            contenido = Contenido.objects.get(clave=clave)
            contenido.valor = valor
            return HttpResponse(contenido.valor)
        except Contenido.DoesNotExist:
            contenido = Contenido(clave=clave, valor=valor)
        contenido.save()


def index(request):
    contenidos = Contenido.objects.all()
    # Cargo la template
    template = loader.get_template('index.html')
    # Genero el contexto
    context = {
        'contenidos': contenidos,
        'usuario': request.user.is_authenticated
    }
    return HttpResponse(template.render(context, request))


def logged_users(request):
    if request.user.is_authenticated:
        return HttpResponse(
            "Estas logeado con el usuario " +
            request.user.username)
    else:
        return HttpResponse(
            "No estas logeado. <a href='/admin'>Logueate aqui</a>")


def logout_view(request):
    logout(request)
    return redirect("/cms/")


class Counter():
    def __init__(self):
        self.count: int = 0

    def increment(self):
        self.count += 1
        return self.count
