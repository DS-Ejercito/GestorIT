# Generated by Django 5.0.2 on 2024-05-16 22:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='categoria_req',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('descrip_corta', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='estado_req',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('descrip_corta', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='procedencia',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('descrip_corta', models.CharField(max_length=50)),
                ('descrip_larga', models.CharField(max_length=50)),
                ('cod_proced_superior', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='tipo_requerimiento',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('descrip_corta', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Requerimientos',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('descrip_corta', models.CharField(max_length=50)),
                ('descrip_larga', models.CharField(max_length=50)),
                ('descrip_resol', models.CharField(blank=True, max_length=50, null=True)),
                ('num_exp', models.CharField(max_length=50)),
                ('fch_rec', models.DateField()),
                ('fch_fin', models.DateField(blank=True, null=True)),
                ('respo_rec', models.CharField(max_length=50)),
                ('respo_ejec', models.CharField(blank=True, max_length=50, null=True)),
                ('img_req', models.ImageField(upload_to='imagenes/')),
                ('img_resol', models.ImageField(blank=True, null=True, upload_to='imagenes/')),
                ('cod_cat_req', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='modulos.categoria_req')),
                ('cod_est_req', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='modulos.estado_req')),
                ('cod_proc', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='modulos.procedencia')),
                ('cod_tp_req', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='modulos.tipo_requerimiento')),
            ],
        ),
    ]