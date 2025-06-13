from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_comunas, name='listar_comunas'),
    path('nueva/', views.crear_comuna, name='crear_comuna'),
    path('editar/<int:pk>/', views.editar_comuna, name='editar_comuna'),
    path('eliminar/<int:pk>/', views.eliminar_comuna, name='eliminar_comuna'),
]
