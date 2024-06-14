from django.contrib import admin
from .models import Requerimientos, procedencia, estado_req, categoria_req, tipo_requerimiento
# Inventeraio de Equipo.
from .models import Computadora, Marca, Estado, Mem_Ram, Sis_Oper, Almac, Office, tp_pc, tp_manto_pc, Manto_Computadora, Diagnostico_tecnico
from .models import Requerimientos, procedencia, estado_req, categoria_req, tipo_requerimiento, Soporte_Correos, tipo_soporte_correos, titulo_tecnico, tecnico
# Soporte Equipos Personales a la Red.
from .models import Equip_Pers

# Register your models here.
admin.site.register(Requerimientos)
admin.site.register(procedencia)
admin.site.register(estado_req)
admin.site.register(categoria_req)
admin.site.register(tipo_requerimiento)
admin.site.register(Computadora)
admin.site.register(Marca)
admin.site.register(Estado)
admin.site.register(Mem_Ram)
admin.site.register(Sis_Oper)
admin.site.register(Almac)
admin.site.register(Office)
admin.site.register(tp_pc)
admin.site.register(tp_manto_pc)
admin.site.register(Manto_Computadora)
admin.site.register(Diagnostico_tecnico)
admin.site.register(Soporte_Correos)
admin.site.register(tipo_soporte_correos)
admin.site.register(tecnico)
admin.site.register(titulo_tecnico)
# Soporte Equipos Personales a la Red.
admin.site.register(Equip_Pers)
