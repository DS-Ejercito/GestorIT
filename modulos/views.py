# Create your views here.
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.http import JsonResponse
from .models import *
#Generar QR
import qrcode
from io import BytesIO
import base64
import pandas as pd
from django.db.models import F

estados_req = estado_req.objects.all()
tipos_requerimiento = tipo_requerimiento.objects.all()
procedencias = procedencia.objects.all()
categorias_req = categoria_req.objects.all()
Marcas = Marca.objects.all()
Estados = Estado.objects.all()
Mem_Rams = Mem_Ram.objects.all()
Sis_Opers = Sis_Oper.objects.all()
Almacs = Almac.objects.all()
Offices = Office.objects.all()
tp_pcs = tp_pc.objects.all()
tp_manto_pcs = tp_manto_pc.objects.all()
list_modelo_imp = modelo_imp.objects.all()
list_marca_imp = marca_imp.objects.all()
list_tipo_imp = tipo_imp.objects.all()

tecnicos = tecnico.objects.all()
titulo_tecnico = titulo_tecnico.objects.all()
tipo_soporte_correoss = tipo_soporte_correos.objects.all()

def inicio(request):
    return render(request, 'index.html')

def inicio_2(request):
    pcs = Computadora.objects.count()
    correo = Soporte_Correos.objects.count()
    equip_perso = Equip_Pers.objects.count()
    context = {
        'Computadora': pcs,
        'Correos' : correo,
        'EquiposPersonales' : equip_perso
        }
    return render(request, 'base.html', context)

def requerimientos(request):
    Req = Requerimientos.objects.all()
    return render(request, 'requerimientos/req_gen.html', {'Req'  : Req })

def req_create(request):
    context = {
        'tipos_requerimiento': tipos_requerimiento,
        'procedencias': procedencias,
        'categorias_req': categorias_req,
        'estados_req': estados_req
    }
    return render(request, 'requerimientos/req_create.html', context)

def req_create_bd(request):
    fch_fin = request.POST['fch_fin']
    if fch_fin == "":
        fch_fin = "2024-12-31"
    requerimiento = Requerimientos(descrip_corta = request.POST['descrip_corta'] ,
                                    descrip_larga = request.POST['descrip_larga'] ,
                                    descrip_resol = request.POST['descrip_resol'],
                                    num_exp = request.POST['num_exp'], 
                                    respo_rec = request.POST['respo_rec'],
                                    fch_rec = request.POST['fch_rec'],
                                    fch_fin = fch_fin,
                                    respo_ejec = request.POST['respo_ejec'],
                                    cod_tp_req = tipo_requerimiento.objects.get(id= request.POST['cod_tp_req']),
                                    cod_proc = procedencia.objects.get(id=request.POST['cod_proc']),
                                    cod_cat_req = categoria_req.objects.get(id=request.POST['cod_cat_req']),
                                    cod_est_req = estado_req.objects.get(id=request.POST['cod_est_req']),
                                    img_req = request.FILES.get('img_req'),
                                    img_resol = request.FILES.get('img_resol'))
    requerimiento.save()
    return redirect('requerimientos')

def req_delete(request, id):
    Req = Requerimientos.objects.get(id=id)
    Req.delete()
    return redirect('requerimientos')

def req_update(request, id):
    Req1 = Requerimientos.objects.get(id=id)
    Req1.fch_rec.isoformat
    context = {
        'tipos_requerimiento': tipos_requerimiento,
        'procedencias': procedencias,
        'categorias_req': categorias_req,
        'estados_req': estados_req,
        'Req1' : Req1
    }
    
    return render(request, 'requerimientos/req_update.html', context)

def req_update_bd(request, id):
    Req = get_object_or_404(Requerimientos, id = id)
    fch_fin = request.POST['fch_fin']
    if fch_fin == "":
        fch_fin = "2024-12-31"
    Req.descrip_corta = request.POST['descrip_corta'] 
    Req.descrip_larga = request.POST['descrip_larga'] 
    Req.descrip_resol = request.POST['descrip_resol']
    Req.num_exp = request.POST['num_exp']
    Req.respo_rec = request.POST['respo_rec']
    Req.fch_rec = request.POST['fch_rec']
    Req.fch_fin = fch_fin
    Req.respo_ejec = request.POST['respo_ejec']
    Req.cod_tp_req = tipo_requerimiento.objects.get(id= request.POST['cod_tp_req'])
    Req.cod_proc = procedencia.objects.get(id=request.POST['cod_proc'])
    Req.cod_cat_req = categoria_req.objects.get(id=request.POST['cod_cat_req'])
    Req.cod_est_req = estado_req.objects.get(id=request.POST['cod_est_req'])
    if request.FILES.get('img_req') is not None:
        Req.img_req = request.FILES.get('img_req')
    if request.FILES.get('img_resol') is not None:
        Req.img_resol = request.FILES.get('img_resol')
    Req.save()
    Req = Requerimientos.objects.all()
    return render(request, 'requerimientos/req_gen.html', {'Req'  : Req } )

def Inv_PC(request):
    Inv_pc = Computadora.objects.all()
    return render(request, 'Inventario/Inv_pc_gen.html', {'Inv_pc'  : Inv_pc })

def delete_PC(request, id):
    Inv_pc = Computadora.objects.get(id=id)
    Inv_pc.delete()
    return redirect('Inv_pc')

def Inv_pc_create(request):
    context = {
        'Marca': Marcas,
        'procedencias': procedencias,
        'Estado': Estados,
        'Mem_Ram': Mem_Rams,
        'Sis_Oper': Sis_Opers,
        'Almac': Almacs,
        'Office': Offices,
        'tp_pc': tp_pcs
    }
    return render(request, 'Inventario/Inv_pc_create.html', context)

def Inv_pc_bd(request):
    Antivirus = request.POST['Antivirus']
    Computadoras = Computadora(
        numero_serie = request.POST['numero_serie'] ,
        modelo = request.POST['modelo'] ,
        procesador = request.POST['procesador'],
        Usuario_AD = request.POST['Usuario_AD'], 
        Nom_Equipo_AD = request.POST['Nom_Equipo_AD'],
        Ip_Asig = request.POST['Ip_Asig'],
        Mac_Eth = request.POST['Mac_Eth'],
        Antivirus = Antivirus,
        observaciones = request.POST['observaciones'],
        Tipo_PC = tp_pc.objects.get(id=request.POST['Tipo_PC']),
        Mem_Ram = Mem_Ram.objects.get(id=request.POST['Mem_Ram']),
        Almac = Almac.objects.get(id=request.POST['Almac']),
        Sis_Oper = Sis_Oper.objects.get(id=request.POST['Sis_Oper']),
        Estado = Estado.objects.get(id=request.POST['Estado']),
        Marca = Marca.objects.get(id=request.POST['Marca']),
        Office = Office.objects.get(id=request.POST['Office']),
        cod_proc = procedencia.objects.get(id=request.POST['cod_proc']))
    Computadoras.save()
    return redirect('Inv_pc')

def Inv_pc_update(request, id):
    PC = get_object_or_404(Computadora, id=id)
        # Datos que se incluirán en el código QR
    data = f"\nUbicacion: {PC.cod_proc} \nIP: {PC.Ip_Asig} \nMAC: {PC.Mac_Eth} \nUsuario: {PC.Usuario_AD} \nNombre del Equipo: {PC.Nom_Equipo_AD} \nSerie: {PC.numero_serie}\nModelo: {PC.modelo}\nMarca: {PC.Marca}\nProcesador: {PC.Ip_Asig}\nRAM: {PC.Mem_Ram}\nAlmacenamiento: {PC.Almac}\nSO: {PC.Sis_Oper}"
        # Generar el código QR
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)
    
    img = qr.make_image(fill='black', back_color='white')
    buffer = BytesIO()
    img.save(buffer)
    img_str = base64.b64encode(buffer.getvalue()).decode()
    PC = Computadora.objects.get(id=id)
    context = {
        'Marca': Marcas,
        'procedencias': procedencias,
        'Estado': Estados,
        'Mem_Ram': Mem_Rams,
        'Sis_Oper': Sis_Opers,
        'Almac': Almacs,
        'Office': Offices,
        'tp_pc': tp_pcs,
        'PC': PC,
        'img_str': img_str
    }
    return render(request, 'Inventario/Inv_pc_update.html', context)

def Inv_update_bd(request, id):
    PCs = get_object_or_404(Computadora, id = id)
    PCs.numero_serie = request.POST['numero_serie']
    PCs.modelo = request.POST['modelo']
    PCs.procesador = request.POST['procesador']
    PCs.Usuario_AD = request.POST['Usuario_AD']
    PCs.Nom_Equipo_AD = request.POST['Nom_Equipo_AD']
    PCs.Ip_Asig = request.POST['Ip_Asig']
    PCs.Mac_Eth = request.POST['Mac_Eth']
    PCs.Antivirus = request.POST['Antivirus']
    PCs.observaciones = request.POST['observaciones']
    PCs.Tipo_PC = tp_pc.objects.get(id=request.POST['Tipo_PC'])
    PCs.Mem_Ram = Mem_Ram.objects.get(id=request.POST['Mem_Ram'])
    PCs.Almac = Almac.objects.get(id=request.POST['Almac'])
    PCs.Sis_Oper = Sis_Oper.objects.get(id=request.POST['Sis_Oper'])
    PCs.Estado = Estado.objects.get(id=request.POST['Estado'])
    PCs.Marca = Marca.objects.get(id=request.POST['Marca'])
    PCs.Office = Office.objects.get(id=request.POST['Office'])
    PCs.cod_proc = procedencia.objects.get(id=request.POST['cod_proc'])
    PCs.save()
    return redirect('Inv_pc')

def Manto_PC(request, id):
    PCs = Computadora.objects.get(id=id)
    Mantos = Manto_Computadora.objects.all()
    context = {
        'tecnico': tecnicos,
        'PC': PCs,
        'TP_Manto_PC' : tp_manto_pcs,
        'Manto_PC' : Mantos
    }
    return render(request, 'Manto/Manto_PC.html', context)

def Manto_PC_create_bd(request, id):
    Manto_PC = Manto_Computadora(
        fch = request.POST['fch'] ,
        id_Computadora = Computadora.objects.get(id=id),
        tp_manto_pc = tp_manto_pc.objects.get(id=request.POST['tp_manto_pc']),
        cod_tecnico = tecnico.objects.get(id=request.POST['tecnico']),
        obs = request.POST['obs']
    )
    Manto_PC.save()
    PCs = Computadora.objects.get(id=id)
    Mantos = Manto_Computadora.objects.all()
    context = {
        'tecnico': tecnicos,
        'PC': PCs,
        'TP_Manto_PC' : tp_manto_pcs,
        'Manto_PC' : Mantos
    }
    return render(request, 'Manto/Manto_PC.html', context)
  
def Diag_PC_create_bd(request, id):
    Diagn_Tec_PC = Diagnostico_tecnico(
        fch = request.POST['fch'] ,
        id_Computadora = Computadora.objects.get(id=id),
        fallas = request.POST['fallas'],
        recomendaciones = request.POST['recomendaciones'],
        cod_tecnico = tecnico.objects.get(id=request.POST['tecnico']),
    )
    Diagn_Tec_PC.save()
    PCs = Computadora.objects.get(id=id)
    Diagn_Tec = Diagnostico_tecnico.objects.all()
    context = {
        'tecnico': tecnicos,
        'PC': PCs,
        'Diagn_Tec' : Diagn_Tec
    }
    return render(request, 'Manto/Diagn_Tec.html', context)  

def Manto_delete_bd(request, id, id2):
    Mant_PC = Manto_Computadora.objects.get(id=id)
    Mant_PC.delete()
    PCs = Computadora.objects.get(id=id2)
    Mantos = Manto_Computadora.objects.all()
    context = {
        'tecnico': tecnicos,
        'PC': PCs,
        'TP_Manto_PC' : tp_manto_pcs,
        'Manto_PC' : Mantos
    }
    return render(request, 'Manto/Manto_PC.html', context)

def Diagn_Tec(request, id):
    PCs = Computadora.objects.get(id=id)
    Diagn_Tec = Diagnostico_tecnico.objects.all()
    context = {
        'tecnico': tecnicos,
        'PC': PCs,
        'Diagn_Tec' : Diagn_Tec
    }
    return render(request, 'Manto/Diagn_Tec.html', context)

def soporte_correo(request):
    correos= Soporte_Correos.objects.all()
    context = {
        'tecnico': tecnicos,
        'tipo_soporte_correos': tipo_soporte_correoss,
        'correos': correos
    }
    return render(request, 'soporte_correo/SopCorreo.html', context)

def sopcor_delete(request, id):
    cor = Soporte_Correos.objects.get(id=id)
    cor.delete()
    return redirect('soporte_correo')

def sopcor_create_bd(request):
    soporte_correos = Soporte_Correos(cuenta_correo = request.POST['cuenta_correo'] ,
                                    solicitante = request.POST['solicitante'],
                                    contacto = request.POST['contacto'], 
                                    fch_sop = request.POST['fch_sop'],
                                    observ = request.POST['observ'],
                                    tipo_sop = tipo_soporte_correos.objects.get(id=request.POST['tipo_sop']),
                                    tecnico = tecnico.objects.get(id=request.POST['tecnico']) )
    soporte_correos.save()
    return redirect('soporte_correo')

def sop_equip_pers_delete(request, id):
    Equip_Pers_c = Equip_Pers.objects.get(id=id)
    Equip_Pers_c.delete()
    return redirect('sop_equip_pers_r')

def Equip_Pers_Red(request):
    Equip_Pers_a = Equip_Pers.objects.all()
    context = {
        'tecnico': tecnicos,
        'Equip_Pers_a': Equip_Pers_a,
        'procedencias': procedencias
        }
    return render(request, 'soporte_correo/Sop_Equip_Per_Red.html', context)

def sop_equip_pers_create_bd(request):
    Equip_Pers_c = Equip_Pers(
        direccion_mac = request.POST['direccion_mac'] ,
        direccion_ip = request.POST['direccion_ip'],
        nom_equip_utm = request.POST['nom_equip_utm'], 
        nom_completo = request.POST['nom_completo'],
        obs = request.POST['obs'],
        cod_proc = procedencia.objects.get(id=request.POST['cod_proc']),
        tecnico = tecnico.objects.get(id=request.POST['tecnico']))
    Equip_Pers_c.save()
    return redirect('sop_equip_pers_r')

def export_to_excel(request):
    data = Computadora.objects.all().annotate(RAM = F('Mem_Ram__descrip_corta'), Marc = F('Marca__descrip_corta'),SO = F('Sis_Oper__descrip_corta'), Almace = F('Almac__descrip_corta'), Ubi = F('cod_proc__descrip_corta'), Offi = F('Office__descrip_corta')).values('Ubi', 'Marc', 'modelo', 'SO', 'RAM', 'procesador', 'Almace', 'modelo', 'Offi', 'Usuario_AD')
    df = pd.DataFrame(data)
    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = 'attachment; filename=my_model_data.xlsx'
    with pd.ExcelWriter(response, engine='openpyxl') as writer:
        df.to_excel(writer, index=False, sheet_name='Sheet1')
    return response

def load_modelos(request):
    marca_id = request.GET.get('marca_id')  # Obtener la ID de la marca desde la solicitud Ajax
    modelos = modelo_imp.objects.filter(marca_id=marca_id).order_by('descrip_corta')  # Filtrar modelos por marca
    return JsonResponse(list(modelos.values('id', 'descrip_corta')), safe=False)  # Devolver la lista de modelos

def Inv_imp(request):
    Inv_imp = impresora.objects.all()
    return render(request, 'Inventario/Inv_imp_gen.html', {'Inv_imp'  : Inv_imp })

def Inv_imp_create(request):
    
    context = {
        'estado': Estados,
        'modelo': list_modelo_imp,
        'marca': list_marca_imp,
        'ubicacion': procedencias,
        'tipo_imp': list_tipo_imp      
    }
    return render(request, 'Inventario/Inv_imp_create.html', context)

def Inv_imp_bd(request):
    Impresora = impresora(
        serie = request.POST['numero_serie'] ,
        responsable = request.POST['Usuario_AD'] ,
        tp_imp = tipo_imp.objects.get(id=request.POST['Tipo_Imp']),
        modelo = modelo_imp.objects.get(id=request.POST['modelo']), 
        marca = marca_imp.objects.get(id=request.POST['Marca']),
        ubicacion = procedencia.objects.get(id=request.POST['cod_proc']),
        estado = Estado.objects.get(id=request.POST['Estado']))
    Impresora.save()
    return redirect('Inv_imp')