from django.db import models

# Create your models here.

class procedencia(models.Model):
    id = models.AutoField(primary_key=True)
    descrip_corta = models.CharField(max_length=50)    
    descrip_larga = models.CharField(max_length=50)    
    cod_proced_superior = models.IntegerField(null=True, blank=True)
    def __str__(self):
        fila =  str(self.descrip_corta)
        return fila
    
class tipo_requerimiento(models.Model):
    id = models.AutoField(primary_key=True)
    descrip_corta = models.CharField(max_length=50)    
    def __str__(self):
        fila =  str(self.descrip_corta)
        return fila
    
class categoria_req(models.Model):
    id = models.AutoField(primary_key=True)
    descrip_corta = models.CharField(max_length=50)
    def __str__(self):
        fila = str(self.descrip_corta)
        return fila
    
class estado_req(models.Model):
    id = models.AutoField(primary_key=True)
    descrip_corta = models.CharField(max_length=50)
    def __str__(self):
        fila = str(self.descrip_corta)
        return fila   
    
class Requerimientos(models.Model):
    id = models.AutoField(primary_key=True)
    descrip_corta = models.CharField(max_length=50)
    descrip_larga = models.CharField(max_length=50)    
    descrip_resol = models.CharField(max_length=50, null=True, blank=True)
    num_exp = models.CharField(max_length=50)
    fch_rec = models.DateField()
    fch_fin = models.DateField(null=True, blank=True)
    respo_rec = models.CharField(max_length=50)
    respo_ejec = models.CharField(max_length=50, null=True, blank=True)
    img_req = models.ImageField(upload_to='Req_Rec/', null = True, blank= True)
    img_resol = models.ImageField(upload_to='Req_Resol/', null = True, blank= True)
    cod_tp_req = models.ForeignKey(tipo_requerimiento, on_delete=models.CASCADE)
    cod_proc = models.ForeignKey(procedencia, on_delete=models.CASCADE)
    cod_cat_req = models.ForeignKey(categoria_req, on_delete=models.CASCADE)
    cod_est_req = models.ForeignKey(estado_req, on_delete=models.CASCADE)
    def __str__(self):
        fila = "- Descripcion:" + str(self.descrip_corta)
        return fila
