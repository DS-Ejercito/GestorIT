from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Movimiento
from .models import Cierre_Diario
from .forms import MovimientoForm
from datetime import date
from django.utils import timezone
from django.db.models import Sum
from django.db.models.functions import ExtractYear, ExtractMonth
import qrcode

fecha_hoy = date.today()
year = timezone.now().year
mes_actual = timezone.now().month

def inicio(request):
    return render(request, 'base.html')

def contabilidad(request):
    Movimientos = Movimiento.objects.filter(fecha__month=mes_actual).order_by('-fecha')
    #data = "https://www.ejemplo.com"
    #img = qrcode.make(data)
    #img.save("codigo_qr.png")
    return render(request, 'contabilidad/create.html', {'Movimientos': Movimientos})

def view_cierre_diario(request):
    Cierres = Cierre_Diario.objects.filter(fecha_cierre__year=year, fecha_cierre__month=mes_actual)
    return render(request, 'contabilidad/create_cierre_diario.html', {'Cierres': Cierres})

def conta_cierre_diario(request):

    return render(request, 'contabilidad/create_cierre_diario.html')

def reporte_mensual(request):
    return render(request, 'contabilidad/reporte_mensual.html')

def reporte_diario(request):
    return render(request, 'contabilidad/reporte_diario.html')

def form_reporte_diario(request):
    return render(request, 'contabilidad/form_reporte_diario.html')

def form_reporte_mensual(request):
    txtyear = request.POST['txtyear']
    txtmonth = request.POST['txtmonth']
    Suma = Cierre_Diario.objects.filter(fecha_cierre__year=txtyear, fecha_cierre__month=txtmonth).aggregate(POS=Sum('Ing_POS'), T=Sum('Ing_transferencia'), F=Sum('Ing_fondo'), E=Sum('Ing_efectivo'), A=Sum('Ing_abono') )
    if Suma.get('POS') == None :
        return render(request, 'contabilidad/reporte_mensual.html')
    else :
        Suma_Total = float(Suma.get('POS')) + float(Suma.get('T')) + float(Suma.get('F')) + float(Suma.get('A')) + float(Suma.get('E'))
        return render(request, 'contabilidad/form_reporte_mensual.html', {'Suma': Suma, 'Suma_Total': Suma_Total , 'txtyear': txtyear, 'txtmonth': txtmonth })


def mov_editar(request, id):
    Movimientos = Movimiento.objects.get(id=id)
    print(Movimientos)
    return render(request, 'contabilidad/mov_editar.html', {'Movimientos': Movimientos})

def mov_eliminar(request, id):
    movimiento = Movimiento.objects.get(id=id)
    movimiento.delete()
    return redirect('/contabilidad')

def mov_create(request):
    descripcion = request.POST['txtdescripcion']
    cantidad = request.POST['txtcantidad']
    cod_tp_pago = request.POST['txtcod_tp_pago']
    fecha = request.POST['txtfecha']

    movimiento = Movimiento.objects.create(descripcion=descripcion, cantidad=cantidad, cod_tp_pago=cod_tp_pago, fecha = fecha)
    return redirect('/contabilidad')

def cierre_diario_create(request):
    Ing_efectivo = request.POST['txtIng_efectivo']
    Ing_POS = request.POST['txtIng_POS']
    Ing_fondo = request.POST['txtIng_fondo']
    Ing_abono = request.POST['txtIng_abono']
    Ing_transferencia = request.POST['txtIng_transferencia']
    fecha_cierre = request.POST['txtfecha']

    cierre_diario = Cierre_Diario.objects.create(Ing_efectivo = Ing_efectivo, Ing_POS = Ing_POS, Ing_fondo = Ing_fondo, Ing_abono = Ing_abono, Ing_transferencia = Ing_transferencia, fecha_cierre = fecha_cierre)
    return redirect('view_cierre_diario')

def cierre_diario_eliminar(request, id):
    cierre = Cierre_Diario.objects.get(id=id)
    cierre.delete()
    return redirect('view_cierre_diario')
# Create your views here.
