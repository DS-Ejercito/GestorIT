# Generated by Django 5.0.6 on 2024-06-10 21:26

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modulos', '0005_alter_procedencia_cod_proced_superior'),
    ]

    operations = [
        migrations.CreateModel(
            name='tipo_soporte',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('descrip_corta', models.CharField(max_length=50)),
            ],
        ),
        migrations.AlterField(
            model_name='requerimientos',
            name='descrip_larga',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='requerimientos',
            name='descrip_resol',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.CreateModel(
            name='Soporte_Correos',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('cuenta_correo', models.CharField(max_length=100)),
                ('solicitante', models.CharField(max_length=50)),
                ('tecnico', models.CharField(max_length=50)),
                ('contacto', models.CharField(max_length=10)),
                ('fch_sop', models.DateField()),
                ('observ', models.TextField()),
                ('tipo_sop', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='modulos.tipo_soporte')),
            ],
        ),
    ]
