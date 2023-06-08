from . import views
from django.urls import path
from django.urls import reverse_lazy


urlpatterns = [
    path('index', views.index, name='inicio'),
    path('menu/', views.menu, name="menu"),
    path('pedido/',views.pedido,name="pedido"),
    path('promociones/',views.promociones,name="promociones"),
    path('contacto/',views.contacto,name='contacto'),

    ]

