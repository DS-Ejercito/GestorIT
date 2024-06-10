from django.urls import path
from . import views
from django.conf.urls.static import static
from gestor_admin_it.settings import MEDIA_ROOT, MEDIA_URL
urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('requerimientos', views.requerimientos, name='requerimientos'),
    path('req_create', views.req_create, name='req_create'),
    path('req_create_bd/', views.req_create_bd),
    path('req_delete/<int:id>', views.req_delete, name='req_delete'),
    path('req_update/<int:id>', views.req_update, name='req_update'),
    path('descargar/', views.descargar_archivo, name = "descargar"), 
    path('soporte_correos', views.soporte_correos, name='soporte_correos')
] + static(MEDIA_URL ,document_root = MEDIA_ROOT)