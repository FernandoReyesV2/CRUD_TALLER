from django.shortcuts import render, redirect
from django.http import JsonResponse
from bson import json_util
from django.views.decorators.csrf import csrf_exempt
from .models import Usuario
from bson import ObjectId
import json
from bson import ObjectId
from mongoengine.errors import DoesNotExist

def index(request):
    return render(request, 'index.html')

@csrf_exempt
def crear_usuario(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            usuario = Usuario(
                nombre=data.get('nombre'),
                email=data.get('email')
            ).save()
            
            return JsonResponse({
                'success': True,
                'id': str(usuario.id)
            }, status=201)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)

def obtener_usuarios(request):
    try:
        usuarios = Usuario.objects.all()
        usuarios_json = []
        
        for usuario in usuarios:
            usuario_dict = json.loads(usuario.to_json())
            usuario_dict['id'] = str(usuario.id)
            usuarios_json.append(usuario_dict)
            
        return JsonResponse({'usuarios': usuarios_json}, safe=False)
    
    except Exception as e:
        print(f"Error en obtener_usuarios: {str(e)}")
        return JsonResponse({'error': str(e)}, status=500)

@csrf_exempt
def actualizar_usuario(request, id):
    if request.method in ['PUT', 'PATCH']:
        try:
            data = json.loads(request.body)
            usuario = Usuario.objects.get(id=ObjectId(id))
            
            if 'nombre' in data:
                usuario.nombre = data['nombre']
            if 'email' in data:
                usuario.email = data['email']
            
            usuario.save()
            
            return JsonResponse({'success': True})
            
        except DoesNotExist:
            return JsonResponse({'error': 'Usuario no encontrado'}, status=404)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)

@csrf_exempt
def eliminar_usuario(request, id):
    if request.method == 'DELETE':
        try:
            usuario = Usuario.objects.get(id=ObjectId(id))
            usuario.delete()
            
            return JsonResponse({'success': True})
            
        except DoesNotExist:
            return JsonResponse({'error': 'Usuario no encontrado'}, status=404)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)

@csrf_exempt
def verificar_email(request, email):
    if request.method == 'GET':
        try:
            existe = Usuario.objects.filter(email=email).count() > 0
            
            return JsonResponse({
                'existe': existe,
                'email': email
            })
            
        except Exception as e:
            return JsonResponse({
                'error': str(e),
                'existe': False
            }, status=500)
