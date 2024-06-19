# Generated by Django 5.0.2 on 2024-06-14 14:15

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modulos', '0011_merge_20240613_1536'),
    ]

    operations = [
        migrations.CreateModel(
            name='Equip_Pers',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('direccion_mac', models.CharField(max_length=17, unique=True)),
                ('direccion_ip', models.CharField(max_length=16, unique=True)),
                ('nom_equip_utm', models.CharField(max_length=100)),
                ('nom_completo', models.CharField(max_length=100)),
                ('fch_con', models.DateTimeField(auto_now_add=True)),
                ('obs', models.TextField()),
                ('tecnico', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='modulos.tecnico')),
            ],
        ),
    ]