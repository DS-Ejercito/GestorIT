# Generated by Django 5.0.2 on 2024-10-10 20:41

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modulos', '0003_marca_imp_modelo_imp_tipo_imp_impresora'),
    ]

    operations = [
        migrations.AddField(
            model_name='modelo_imp',
            name='marca',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='modelo_imp', to='modulos.marca_imp'),
        ),
    ]
