from django.urls import path
from . import views

urlpatterns = [
    # Otras URLs existentes en el archivo

    # URL de la vista de la tarea
    path('tareas/', views.tareas, name='tareas'),
    path('tareas/crear/',views.crear_tarea, name='crear_tarea'),
]

