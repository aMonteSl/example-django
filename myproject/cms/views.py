from django.shortcuts import render
from django.http import HttpResponse, Http404
from .models import Contenido, Comentario
from django.views.decorators.csrf import csrf_exempt
import datetime
from django.template import loader



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
def get_content(request, clave):
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
            c = Contenido.objects.get(clave = clave)
            com_db = Comentario(titulo = titulo, cuerpo = cuerpo, fecha = datetime.datetime.now(), contenido = c)
            com_db.save()



    try:
        """contenido = Contenido.objects.get(clave = clave)
        comentarios = contenido.comentario_set.all()

        # Preparo la respuesta
        respuesta = contenido.valor
        for comentario in comentarios:
            respuesta += "<p><b>" + comentario.titulo + "</b><br>" + comentario.cuerpo + "<br>" + comentario.fecha.strftime("%Y-%m-%d %H:%M:%S") +"</p>"
        
        respuesta += formulario_contenido + formulario_comentario
        return HttpResponse(respuesta)"""
        # Mandar la template contenido.html
        contenido = Contenido.objects.get(clave = clave)
        comentarios = contenido.comentario_set.all()
        template = loader.get_template('contenido.html')
        context = {
            'contenido': contenido,
            'comentarios': comentarios
            
        }
        return HttpResponse(template.render(context, request))
    
    except Contenido.DoesNotExist:
        raise Http404("No existe para contenido para " + clave)
    

def actualizar_contenido(request, clave, valor):
    if request.method in ["PUT", "POST"]:
        try:
            contenido = Contenido.objects.get(clave = clave)
            contenido.valor = valor
            return HttpResponse(contenido.valor)
        except Contenido.DoesNotExist:
            contenido = Contenido(clave = clave, valor = valor)
        contenido.save()


def index(request):
    contenidos = Contenido.objects.all()
    # Cargo la template
    template = loader.get_template('index.html')
    # Genero el contexto
    context = {
        'contenidos': contenidos
    }
    return HttpResponse(template.render(context, request))









class Counter():
    def __init__(self):
        self.count: int = 0

    def increment(self):
        self.count += 1
        return self.count