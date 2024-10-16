from django.urls import path
from . import views
from django.conf.urls.static import static
from Gestor_ITE6.settings import MEDIA_ROOT, MEDIA_URL

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('inicio_2/', views.inicio_2, name='inicio_2'),
    path('requerimientos', views.requerimientos, name='requerimientos'),
    path('req_create', views.req_create, name='req_create'),
    path('req_create_bd/', views.req_create_bd),
    path('req_delete/<int:id>', views.req_delete, name='req_delete'),
    path('req_update/<int:id>', views.req_update, name='req_update'),
    path('req_update_bd/<int:id>', views.req_update_bd, name='req_update_bd'),
    #Invetario de Computadoras
    path('Inv_pc', views.Inv_PC , name='Inv_pc'),
    path('Inv_imp', views.Inv_imp , name='Inv_imp'),
    path('delete_PC/<int:id>', views.delete_PC, name='delete_PC'),
    path('delete_Imp/<int:id>', views.delete_Imp, name='delete_Imp'),
    path('Inv_pc_create', views.Inv_pc_create, name='Inv_pc_create'),
    path('Inv_imp_create', views.Inv_imp_create, name='Inv_imp_create'),
    path('Inv_pc_bd/', views.Inv_pc_bd, name='Inv_pc_create_bd'),
    path('Inv_imp_bd/', views.Inv_imp_bd, name='Inv_imp_create_bd'),
    path('Inv_pc_update/<int:id>', views.Inv_pc_update, name='Inv_pc_update'),
    path('Inv_imp_update/<int:id>', views.Inv_imp_update, name='Inv_imp_update'),
    path('Inv_update_bd/<int:id>', views.Inv_update_bd, name='Inv_update_bd'),
    path('Inv_update_imp_bd/<int:id>', views.Inv_update_imp_bd, name='Inv_update_imp_bd'),
    path('Manto_PC/<int:id>', views.Manto_PC, name='Manto_PC'),
    path('Manto_PC_create_bd/<int:id>', views.Manto_PC_create_bd, name='Manto_PC_create'),
    path('Manto_delete_bd/<int:id>/<int:id2>', views.Manto_delete_bd, name='Manto_delete_bd'),
    path('Diagn_Tec/<int:id>', views.Diagn_Tec, name='Diagn_Tec'),
    path('Diag_PC_create_bd/<int:id>', views.Diag_PC_create_bd, name='Diagn_PC_create'),
    path('soporte_correo', views.soporte_correo, name='soporte_correo'),
    path('soporte_correo', views.soporte_correo, name='soporte_correo'),
    path('sopcor_delete/<int:id>', views.sopcor_delete, name='sopcor_delete'),
    path('sopcor_create_bd/', views.sopcor_create_bd, name='sopcor_create_bd'),
    path('sop_equip_pers_r', views.Equip_Pers_Red, name='sop_equip_pers_r'),
    path('sop_equip_pers_create_bd/', views.sop_equip_pers_create_bd, name='sop_equip_pers_create_bd'),
    path('Equip_Pers_delete/<int:id>', views.sop_equip_pers_delete, name='Equip_Pers_delete'),
    path('export/', views.export_to_excel, name='export_to_excel'),
    path('load-modelos/', views.load_modelos, name='load_modelos'),
] + static(MEDIA_URL ,document_root = MEDIA_ROOT)