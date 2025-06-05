from django.urls import path
from usuarios import views

urlpatterns = [
    path('', views.index, name='index'),
    path('crear/', views.crear_usuario, name='crear'),
    path('usuarios/', views.obtener_usuarios, name='obtener_usuarios'),
    path('eliminar/<str:id>/', views.eliminar_usuario, name='eliminar'),
    path('actualizar/<str:id>/', views.actualizar_usuario, name='actualizar'),
    path('verificar-email/<str:email>/', views.verificar_email, name='verificar_email'),
]