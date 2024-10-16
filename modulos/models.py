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
    
class tp_pc(models.Model):
    id = models.AutoField(primary_key=True)
    descrip_corta = models.TextField()
    def __str__(self):
        fila = str(self.descrip_corta)
        return fila      

class Mem_Ram(models.Model):
    id = models.AutoField(primary_key=True)
    descrip_corta = models.TextField()
    def __str__(self):
        fila = str(self.descrip_corta)
        return fila      

class Almac(models.Model):
    id = models.AutoField(primary_key=True)
    descrip_corta = models.TextField()
    def __str__(self):
        fila = str(self.descrip_corta)
        return fila      

class Sis_Oper(models.Model):
    id = models.AutoField(primary_key=True)
    descrip_corta = models.TextField()
    def __str__(self):
        fila = str(self.descrip_corta)
        return fila      

class Estado(models.Model):
    id = models.AutoField(primary_key=True)
    descrip_corta = models.TextField()
    def __str__(self):
        fila = str(self.descrip_corta)
        return fila     

class Officeq(models.Model):
    id = models.AutoField(primary_key=True)
    descrip_corta = models.TextField()
    def __str__(self):
        fila = str(self.descrip_corta)
        return fila 
    
class Marca(models.Model):
    id = models.AutoField(primary_key=True)
    descrip_corta = models.TextField()
    def __str__(self):
        fila = str(self.descrip_corta)
        return fila      

class Office(models.Model):
    id = models.AutoField(primary_key=True)
    descrip_corta = models.TextField()
    def __str__(self):
        fila = str(self.descrip_corta)
        return fila      

class Computadora(models.Model):
    id = models.AutoField(primary_key=True)
    numero_serie = models.TextField()
    modelo = models.TextField()
    procesador = models.TextField()
    Usuario_AD = models.TextField()
    Nom_Equipo_AD = models.TextField()
    Ip_Asig = models.TextField()
    Mac_Eth = models.TextField()
    Antivirus = models.BooleanField()
    observaciones = models.TextField(blank=True, null=True)
    Tipo_PC = models.ForeignKey(tp_pc, on_delete=models.CASCADE)
    Mem_Ram = models.ForeignKey(Mem_Ram, on_delete=models.CASCADE)
    Almac = models.ForeignKey(Almac, on_delete=models.CASCADE)
    Sis_Oper = models.ForeignKey(Sis_Oper, on_delete=models.CASCADE)
    Estado = models.ForeignKey(Estado, on_delete=models.CASCADE)
    Marca = models.ForeignKey(Marca, on_delete=models.CASCADE)
    Office = models.ForeignKey(Office, on_delete=models.CASCADE)
    cod_proc = models.ForeignKey(procedencia, on_delete=models.CASCADE)
    def __str__(self):
        fila = "- Descripcion:" + str(self.Nom_Equipo_AD)
        return fila
    
class tp_manto_pc(models.Model):
    id = models.AutoField(primary_key=True)
    descrip_corta = models.TextField()
    def __str__(self):
        fila = str(self.descrip_corta)
        return fila

class titulo_tecnico(models.Model):
    id = models.AutoField(primary_key=True)
    descrip_corta = models.TextField()    
    def __str__(self):
        fila =  str(self.descrip_corta)
        return fila
    
class tecnico(models.Model):
    id = models.AutoField(primary_key=True)
    descrip_corta = models.CharField(max_length=50)    
    def __str__(self):
        fila =  str(self.descrip_corta)
        return fila

class tipo_soporte_correos(models.Model):
    id = models.AutoField(primary_key=True)
    descrip_corta = models.TextField()    
    def __str__(self):
        fila =  str(self.descrip_corta)
        return fila

class Soporte_Correos(models.Model):
    id = models.AutoField(primary_key=True)
    cuenta_correo = models.TextField()
    solicitante = models.TextField()
    contacto = models.TextField()
    fch_sop = models.DateField()
    observ = models.TextField()
    tecnico = models.ForeignKey(tecnico, on_delete=models.CASCADE)
    tipo_sop = models.ForeignKey(tipo_soporte_correos, on_delete=models.CASCADE)
    def __str__(self):
        fila = "- Descripcion:" + str(self.cuenta_correo)
        return fila

class Equip_Pers(models.Model):
    id = models.AutoField(primary_key=True)
    dir_mac = models.TextField(default= "XX:XX:XX:XX:XX:XX")
    dir_ip = models.TextField(default= "0.0.0.0")
    nom_equip_utm = models.TextField()
    nom_completo = models.TextField()
    fch_con = models.DateTimeField(auto_now_add=True)
    obs = models.TextField()
    cod_proc = models.ForeignKey(procedencia, on_delete=models.CASCADE)
    tecnico = models.ForeignKey(tecnico, on_delete=models.CASCADE)
    def __str__(self):
        return f'{self.nom_equip_utm}'

class programa(models.Model):
    id = models.AutoField(primary_key=True)
    descrip_corta = models.TextField()    
    def __str__(self):
        fila =  str(self.descrip_corta)
        return fila

class Prog_Inst_PC(models.Model):
    id = models.AutoField(primary_key=True)
    fch = models.DateField()
    id_Computadora = models.ForeignKey(Computadora, on_delete=models.CASCADE)
    cod_programa = models.ForeignKey(programa, on_delete=models.CASCADE)
    tecnico = models.ForeignKey(tecnico, on_delete=models.CASCADE)
    def __str__(self):
        fila = str( self.fch)
        return fila 

class Manto_Computadora(models.Model):
    id = models.AutoField(primary_key=True)
    fch = models.DateField()
    id_Computadora = models.ForeignKey(Computadora, on_delete=models.CASCADE)
    tp_manto_pc = models.ForeignKey(tp_manto_pc, on_delete=models.CASCADE)
    obs = models.TextField(blank=True, null=True)
    cod_tecnico = models.ForeignKey(tecnico, on_delete=models.CASCADE, null=True)
    def __str__(self):
        fila = str( self.obs)
        return fila  

class Diagnostico_tecnico(models.Model):
    id = models.AutoField(primary_key=True)
    fch = models.DateField()
    id_Computadora = models.ForeignKey(Computadora, on_delete=models.CASCADE)
    fallas = models.TextField(blank=True, null=True)
    recomendaciones = models.TextField(blank=True, null=True)
    cod_tecnico = models.ForeignKey(tecnico, on_delete=models.CASCADE, null=True)
    def __str__(self):
        fila = str( self.fch)
        return fila


class marca_imp(models.Model):
    id = models.AutoField(primary_key=True)
    descrip_corta = models.TextField()    
    def __str__(self):
        fila =  str(self.descrip_corta)
        return fila

class modelo_imp(models.Model):
    id = models.AutoField(primary_key=True)
    descrip_corta = models.TextField()
    marca = models.ForeignKey(marca_imp, on_delete=models.CASCADE, related_name='modelo_imp', null=True)    
    def __str__(self):
        fila =  str(self.descrip_corta)
        return fila

class tipo_imp(models.Model):
    id = models.AutoField(primary_key=True)
    descrip_corta = models.TextField()    
    def __str__(self):
        fila =  str(self.descrip_corta)
        return fila

    
class impresora(models.Model):
    id = models.AutoField(primary_key=True)
    serie = models.TextField()
    responsable = models.TextField()
    tp_imp = models.ForeignKey(tipo_imp, on_delete=models.CASCADE)
    modelo = models.ForeignKey(modelo_imp, on_delete=models.CASCADE)
    marca = models.ForeignKey(marca_imp, on_delete=models.CASCADE)
    ubicacion = models.ForeignKey(procedencia, on_delete=models.CASCADE)
    estado = models.ForeignKey(Estado, on_delete=models.CASCADE)
    obs = models.TextField( null=True)
    def __str__(self):
        fila =  str(self.serie)
        return fila
