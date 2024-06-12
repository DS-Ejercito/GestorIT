from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Requerimientos, estado_req, tipo_requerimiento, procedencia, categoria_req
from .models import Soporte_Correos, tipo_soporte_correos, tecnico, titulo_tecnico  

estados_req = estado_req.objects.all()
tipos_requerimiento = tipo_requerimiento.objects.all()
procedencias = procedencia.objects.all()
categorias_req = categoria_req.objects.all()
tecnico = tecnico.objects.all()
titulo_tecnico = titulo_tecnico.objects.all()
tipo_soporte_correos = tipo_soporte_correos.objects.all()

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

def soporte_correo(request):
    context = {
        'tecnico': tecnico,
        'titulo_tecnico': titulo_tecnico,
        'tipo_soporte_correos': tipo_soporte_correos
    }
    return render(request, 'soporte_correo/SopCorreo.html', context)