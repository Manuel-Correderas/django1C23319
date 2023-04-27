from . import views
from django.urls import path

urlpatterns = [
    path('index', views.index, name='inicio'),
    path('menu', views.menu, name="menu"),
    path('pedido',views.pedido,name="pedido"),
    path('promociones',views.promociones,name="promociones"),
]