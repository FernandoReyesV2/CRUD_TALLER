from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('obtener_usuarios/', views.obtener_usuarios),
    path('crear_usuario/', views.crear_usuario),
    path('editar_usuario/<int:id>/', views.editar_usuario),
    path('eliminar_usuario/<int:id>/', views.eliminar_usuario),
]
