from django.contrib import admin
from .models import Requerimientos, procedencia, estado_req, categoria_req, tipo_requerimiento
# Register your models here.
admin.site.register(Requerimientos)
admin.site.register(procedencia)
admin.site.register(estado_req)
admin.site.register(categoria_req)
admin.site.register(tipo_requerimiento)