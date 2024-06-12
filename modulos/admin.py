from django.contrib import admin
from .models import Requerimientos, procedencia, estado_req, categoria_req, tipo_requerimiento, Soporte_Correos, tipo_soporte_correos, titulo_tecnico
# Register your models here.
admin.site.register(Requerimientos)
admin.site.register(procedencia)
admin.site.register(estado_req)
admin.site.register(categoria_req)
admin.site.register(tipo_requerimiento)
admin.site.register(Soporte_Correos)
admin.site.register(tipo_soporte_correos)
admin.site.register(titulo_tecnico)