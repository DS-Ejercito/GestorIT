# Generated by Django 5.0.2 on 2024-07-19 14:21

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Almac',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('descrip_corta', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='categoria_req',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('descrip_corta', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Estado',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('descrip_corta', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='estado_req',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('descrip_corta', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Marca',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('descrip_corta', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Mem_Ram',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('descrip_corta', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Office',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('descrip_corta', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Officeq',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('descrip_corta', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='programa',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('descrip_corta', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Sis_Oper',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('descrip_corta', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='tecnico',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('descrip_corta', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='tipo_requerimiento',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('descrip_corta', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='tipo_soporte_correos',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('descrip_corta', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='titulo_tecnico',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('descrip_corta', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='tp_manto_pc',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('descrip_corta', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='tp_pc',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('descrip_corta', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='procedencia',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('descrip_corta', models.TextField()),
                ('descrip_larga', models.TextField()),
                ('cod_proced_superior', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='subcategorias', to='modulos.procedencia')),
            ],
        ),
        migrations.CreateModel(
            name='Computadora',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('numero_serie', models.TextField()),
                ('modelo', models.TextField()),
                ('procesador', models.TextField()),
                ('Usuario_AD', models.TextField()),
                ('Nom_Equipo_AD', models.TextField()),
                ('Ip_Asig', models.TextField()),
                ('Mac_Eth', models.TextField()),
                ('Antivirus', models.BooleanField()),
                ('observaciones', models.TextField(blank=True, null=True)),
                ('Almac', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='modulos.almac')),
                ('Estado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='modulos.estado')),
                ('Marca', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='modulos.marca')),
                ('Mem_Ram', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='modulos.mem_ram')),
                ('Office', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='modulos.office')),
                ('cod_proc', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='modulos.procedencia')),
                ('Sis_Oper', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='modulos.sis_oper')),
                ('Tipo_PC', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='modulos.tp_pc')),
            ],
        ),
        migrations.CreateModel(
            name='Prog_Inst_PC',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('fch', models.DateField()),
                ('id_Computadora', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='modulos.computadora')),
                ('cod_programa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='modulos.programa')),
                ('tecnico', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='modulos.tecnico')),
            ],
        ),
        migrations.CreateModel(
            name='Equip_Pers',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('dir_mac', models.TextField(default='XX:XX:XX:XX:XX:XX')),
                ('dir_ip', models.TextField(default='0.0.0.0')),
                ('nom_equip_utm', models.TextField()),
                ('nom_completo', models.TextField()),
                ('fch_con', models.DateTimeField(auto_now_add=True)),
                ('obs', models.TextField()),
                ('cod_proc', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='modulos.procedencia')),
                ('tecnico', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='modulos.tecnico')),
            ],
        ),
        migrations.CreateModel(
            name='Diagnostico_tecnico',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('fch', models.DateField()),
                ('fallas', models.TextField(blank=True, null=True)),
                ('recomendaciones', models.TextField(blank=True, null=True)),
                ('id_Computadora', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='modulos.computadora')),
                ('tecnico', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='modulos.tecnico')),
            ],
        ),
        migrations.CreateModel(
            name='Requerimientos',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('descrip_corta', models.TextField()),
                ('descrip_larga', models.TextField()),
                ('descrip_resol', models.TextField(blank=True, null=True)),
                ('num_exp', models.CharField(max_length=50)),
                ('fch_rec', models.DateField()),
                ('fch_fin', models.DateField(blank=True, null=True)),
                ('respo_rec', models.CharField(blank=True, max_length=50, null=True)),
                ('respo_ejec', models.CharField(blank=True, max_length=50, null=True)),
                ('img_req', models.FileField(blank=True, null=True, upload_to='Req_Rec/')),
                ('img_resol', models.FileField(blank=True, null=True, upload_to='Req_Resol/')),
                ('cod_cat_req', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='modulos.categoria_req')),
                ('cod_est_req', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='modulos.estado_req')),
                ('cod_proc', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='modulos.procedencia')),
                ('cod_tp_req', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='modulos.tipo_requerimiento')),
            ],
        ),
        migrations.CreateModel(
            name='Soporte_Correos',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('cuenta_correo', models.TextField()),
                ('solicitante', models.TextField()),
                ('contacto', models.TextField()),
                ('fch_sop', models.DateField()),
                ('observ', models.TextField()),
                ('tecnico', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='modulos.tecnico')),
                ('tipo_sop', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='modulos.tipo_soporte_correos')),
            ],
        ),
        migrations.CreateModel(
            name='Manto_Computadora',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('fch', models.DateField()),
                ('obs', models.TextField(blank=True, null=True)),
                ('id_Computadora', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='modulos.computadora')),
                ('tecnico', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='modulos.tecnico')),
                ('tp_manto_pc', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='modulos.tp_manto_pc')),
            ],
        ),
    ]