from django.contrib import admin
from .models import Tarea

class TareaAdmin(admin.ModelAdmin):
    readonly_fields = ("get_creado",)

    def get_creado(self, obj):
        return obj.fecha_creado

admin.site.register(Tarea, TareaAdmin)


'''
from django.contrib import admin
from .models import Tarea

class TareaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'descripcion', 'fecha_creado', 'fecha_completados', 'importante', 'usuarios')
    list_filter = ('fecha_creado', 'fecha_completados', 'importante', 'usuarios')
    search_fields = ('titulo', 'descripcion', 'usuarios__username')

admin.site.register(Tarea, TareaAdmin)
'''
