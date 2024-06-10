from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('contabilidad', views.contabilidad, name='contabilidad'),
    path('reporte_mensual', views.reporte_mensual, name='reporte_mensual'),
    path('reporte_diario', views.reporte_diario, name='reporte_diario'),
    path('form_reporte_diario', views.form_reporte_diario, name='form_reporte_diario'),
    path('form_reporte_mensual', views.form_reporte_mensual, name='form_reporte_mensual'),
    path('view_cierre_diario', views.view_cierre_diario, name='view_cierre_diario'),
    path('contabilidad/editar', views.mov_editar, name='mov_editar'),
    path('conta_cierre_diario', views.conta_cierre_diario, name='conta_cierre_diario'),
    path('mov_create/', views.mov_create),
    path('cierre_diario_create/', views.cierre_diario_create),
    path('mov_eliminar/<int:id>', views.mov_eliminar, name='mov_eliminar'),
    path('cierre_diario_eliminar/<int:id>', views.cierre_diario_eliminar, name='cierre_diario_eliminar'),
    path('mov_editar/<int:id>', views.mov_editar, name='mov_editar'),
]