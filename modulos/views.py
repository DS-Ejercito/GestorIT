from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Requerimientos, estado_req, tipo_requerimiento, procedencia, categoria_req 
#Inventario de Computadoras
from .models import Computadora, Marca, Estado, Mem_Ram, Sis_Oper, Almac, Office, tp_pc, Manto_Computadora, tp_manto_pc, Diagnostico_tecnico

from .models import Soporte_Correos, tipo_soporte_correos, tecnico, titulo_tecnico  

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

tecnicos = tecnico.objects.all()
titulo_tecnico = titulo_tecnico.objects.all()
tipo_soporte_correoss = tipo_soporte_correos.objects.all()

def inicio(request):
    return render(request, 'base.html')

def requerimientos(request):
    Req = Requerimientos.objects.all()
    return render(request, 'requerimientos/req_gen.html', {'Req'  : Req })

def req_create(request):
    print(procedencias)
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
    Req = Requerimientos.objects.all()
    return render(request, 'requerimientos/req_gen.html', {'Req'  : Req })

def req_delete(request, id):
    Req = Requerimientos.objects.get(id=id)
    Req.delete()
    Req = Requerimientos.objects.all()
    return render(request, 'requerimientos/req_gen.html', {'Req'  : Req })

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
    print(Req1.cod_tp_req)
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
        Req.img_req = request.FILES.get('img_resol')
    Req.save()
    Req = Requerimientos.objects.all()
    return render(request, 'requerimientos/req_gen.html', {'Req'  : Req } )

def Inv_PC(request):
    Inv_pc = Computadora.objects.all()
    return render(request, 'Inventario/Inv_pc_gen.html', {'Inv_pc'  : Inv_pc })

def delete_PC(request, id):
    Inv_pc = Computadora.objects.get(id=id)
    Inv_pc.delete()
    return Inv_PC(request)

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
    return Inv_PC(request)

def Inv_pc_update(request, id):
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
        'PC': PC
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
    return Inv_PC(request)

def Manto_PC(request, id):
    print(id)
    PCs = Computadora.objects.get(id=id)
    Mantos = Manto_Computadora.objects.all()
    context = {
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
        obs = request.POST['obs']
    )
    Manto_PC.save()
    PCs = Computadora.objects.get(id=id)
    Mantos = Manto_Computadora.objects.all()
    context = {
        'PC': PCs,
        'TP_Manto_PC' : tp_manto_pcs,
        'Manto_PC' : Mantos
    }
    return render(request, 'Manto/Manto_PC.html', context)
    
def Manto_delete_bd(request, id, id2):
    Mant_PC = Manto_Computadora.objects.get(id=id)
    Mant_PC.delete()
    PCs = Computadora.objects.get(id=id2)
    Mantos = Manto_Computadora.objects.all()
    context = {
        'PC': PCs,
        'TP_Manto_PC' : tp_manto_pcs,
        'Manto_PC' : Mantos
    }
    return render(request, 'Manto/Manto_PC.html', context)

def Diagn_Tec(request, id):
    PCs = Computadora.objects.get(id=id)
    Diagn_Tec = Diagnostico_tecnico.objects.all()
    context = {
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
    return soporte_correo(request)

def sopcor_create_bd(request):
    soporte_correos = Soporte_Correos(cuenta_correo = request.POST['cuenta_correo'] ,
                                    solicitante = request.POST['solicitante'],
                                    contacto = request.POST['contacto'], 
                                    fch_sop = request.POST['fch_sop'],
                                    observ = request.POST['observ'],
                                    tipo_sop = tipo_soporte_correos.objects.get(id=request.POST['tipo_sop']),
                                    tecnico = tecnico.objects.get(id=request.POST['tecnico']) )
    soporte_correos.save()
    return soporte_correo(request)
