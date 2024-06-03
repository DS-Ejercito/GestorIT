from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Requerimientos
from .models import tipo_requerimiento
from .models import procedencia
from .models import categoria_req
from .models import estado_req
#from .models import Cierre_Diario
from datetime import date
from django.utils import timezone
from django.db.models import Sum
from django.db.models.functions import ExtractYear, ExtractMonth

# Create your views here.
def inicio(request):
    return render(request, 'base.html')

def requerimientos(request):
    Req = Requerimientos.objects.all
    return render(request, 'requerimientos/req_gen.html', {'Req'  : Req })

def req_create(request):
    tipos_requerimiento = tipo_requerimiento.objects.all()
    procedencias = procedencia.objects.all()
    categorias_req = categoria_req.objects.all()
    estados_req = estado_req.objects.all()
    
    context = {
        'tipos_requerimiento': tipos_requerimiento,
        'procedencias': procedencias,
        'categorias_req': categorias_req,
        'estados_req': estados_req
    }
    return render(request, 'requerimientos/req_create.html', context)

def req_create_bd(request):
    descrip_corta = request.POST['descrip_corta']
    descrip_larga =   request.POST['descrip_larga']
    descrip_resol = request.POST['descrip_resol']
    num_exp = request.POST['num_exp']
    fch_rec = request.POST['fch_rec']
    fch_fin = request.POST['fch_fin']
    print(fch_rec)
    if fch_fin == "":
        fch_fin = "2024-12-31"
    respo_rec = request.POST['respo_rec']
    respo_ejec = request.POST['respo_ejec']
    img_req = request.FILES.get('img_req')
    img_resol = request.FILES.get('img_resol')
    cod_tp_req = tipo_requerimiento.objects.get(id= request.POST['cod_tp_req'])
    cod_proc = procedencia.objects.get(id=request.POST['cod_proc'])
    cod_cat_req = categoria_req.objects.get(id=request.POST['cod_cat_req'])
    cod_est_req = estado_req.objects.get(id=request.POST['cod_est_req'])
    requerimiento = Requerimientos(descrip_corta = descrip_corta ,
                                    descrip_larga = descrip_larga ,
                                    descrip_resol = descrip_resol,
                                    num_exp = num_exp, 
                                    respo_rec = respo_rec,
                                    fch_rec = fch_rec,
                                    fch_fin = fch_fin,
                                    respo_ejec = respo_ejec,
                                    cod_tp_req = cod_tp_req,
                                    cod_proc = cod_proc,
                                    cod_cat_req = cod_cat_req,
                                    cod_est_req = cod_est_req,
                                    img_req = img_req,
                                    img_resol = img_resol)
    requerimiento.save()
    Req = Requerimientos.objects.all
    return render(request, 'requerimientos/req_gen.html', {'Req'  : Req })
