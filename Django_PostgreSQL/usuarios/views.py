from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import Usuario
from django.views.decorators.csrf import csrf_exempt
import json

def index(request):
    return render(request, 'index.html')

def obtener_usuarios(request):
    usuarios = list(Usuario.objects.values('id', 'nombre', 'email'))
    return JsonResponse(usuarios, safe=False)

@csrf_exempt
def crear_usuario(request):
    data = json.loads(request.body)
    Usuario.objects.create(nombre=data['nombre'], email=data['email'])
    return JsonResponse({'mensaje': 'Usuario creado'})

@csrf_exempt
def editar_usuario(request, id):
    data = json.loads(request.body)
    usuario = get_object_or_404(Usuario, id=id)
    usuario.nombre = data['nombre']
    usuario.email = data['email']
    usuario.save()
    return JsonResponse({'mensaje': 'Usuario editado'})

@csrf_exempt
def eliminar_usuario(request, id):
    usuario = get_object_or_404(Usuario, id=id)
    usuario.delete()
    return JsonResponse({'mensaje': 'Usuario eliminado'})
