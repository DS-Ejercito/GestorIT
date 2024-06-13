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
    path('req_update_bd/<int:id>', views.req_update_bd, name='req_update_bd'),
    #Invetario de Computadoras
    path('Inv_pc', views.Inv_PC , name='Inv_pc'),
    path('delete_PC/<int:id>', views.delete_PC, name='delete_PC'),
    path('Inv_pc_create', views.Inv_pc_create, name='Inv_pc_create'),
    path('Inv_pc_bd/', views.Inv_pc_bd, name='Inv_pc_create_bd'),
    path('Inv_pc_update/<int:id>', views.Inv_pc_update, name='Inv_pc_update'),
    path('Inv_update_bd/<int:id>', views.Inv_update_bd, name='Inv_update_bd'),
    path('Manto_PC/<int:id>', views.Manto_PC, name='Manto_PC'),
    path('Manto_PC_create_bd/<int:id>', views.Manto_PC_create_bd, name='Manto_PC_create'),
    path('Manto_delete_bd/<int:id>/<int:id2>', views.Manto_delete_bd, name='Manto_delete_bd'),
    path('Diagn_Tec/<int:id>', views.Diagn_Tec, name='Diagn_Tec'),
    path('soporte_correo', views.soporte_correo, name='soporte_correo')
] + static(MEDIA_URL ,document_root = MEDIA_ROOT)