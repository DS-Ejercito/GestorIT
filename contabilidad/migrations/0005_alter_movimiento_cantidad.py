# Generated by Django 4.2.7 on 2024-04-14 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contabilidad', '0004_cierre_diario_ing_fondo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movimiento',
            name='cantidad',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
    ]