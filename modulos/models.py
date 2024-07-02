from django.db import models

# Create your models here.

class procedencia(models.Model):
    id = models.AutoField(primary_key=True)
    descrip_corta = models.TextField()    
    descrip_larga = models.TextField()    
    cod_proced_superior = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='subcategorias')
    def __str__(self):
        fila =  str(self.descrip_corta)
        return fila
    
class tipo_requerimiento(models.Model):
    id = models.AutoField(primary_key=True)
    descrip_corta = models.TextField()    
    def __str__(self):
        fila =  str(self.descrip_corta)
        return fila
    
class categoria_req(models.Model):
    id = models.AutoField(primary_key=True)
    descrip_corta = models.TextField()
    def __str__(self):
        fila = str(self.descrip_corta)
        return fila
    
class estado_req(models.Model):
    id = models.AutoField(primary_key=True)
    descrip_corta = models.TextField()
    def __str__(self):
        fila = str(self.descrip_corta)
        return fila   
    
class Requerimientos(models.Model):
    id = models.AutoField(primary_key=True)
    descrip_corta = models.TextField()
    descrip_larga = models.TextField()
    descrip_resol = models.TextField(null=True, blank=True)
    num_exp = models.CharField(max_length=50)
    fch_rec = models.DateField()
    fch_fin = models.DateField(null=True, blank=True)
    respo_rec = models.CharField(max_length=50, null=True, blank=True)
    respo_ejec = models.CharField(max_length=50, null=True, blank=True)
    img_req = models.FileField(upload_to='Req_Rec/', null = True, blank= True)
    img_resol = models.FileField(upload_to='Req_Resol/', null = True, blank= True)
    cod_tp_req = models.ForeignKey(tipo_requerimiento, on_delete=models.CASCADE)
    cod_proc = models.ForeignKey(procedencia, on_delete=models.CASCADE)
    cod_cat_req = models.ForeignKey(categoria_req, on_delete=models.CASCADE)
    cod_est_req = models.ForeignKey(estado_req, on_delete=models.CASCADE)
    def __str__(self):
        fila = "- Descripcion:" + str(self.descrip_corta)
        return fila
