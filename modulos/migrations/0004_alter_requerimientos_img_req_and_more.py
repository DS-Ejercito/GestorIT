# Generated by Django 5.0.2 on 2024-06-05 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modulos', '0003_alter_requerimientos_img_req_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='requerimientos',
            name='img_req',
            field=models.FileField(blank=True, null=True, upload_to='Req_Rec/'),
        ),
        migrations.AlterField(
            model_name='requerimientos',
            name='img_resol',
            field=models.FileField(blank=True, null=True, upload_to='Req_Resol/'),
        ),
    ]