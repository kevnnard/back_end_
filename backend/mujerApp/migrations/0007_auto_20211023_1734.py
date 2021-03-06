# Generated by Django 3.2.8 on 2021-10-23 22:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mujerApp', '0006_rename_dirección_centro_direccion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='solicitud',
            name='ciudad',
            field=models.CharField(max_length=30, verbose_name='niudad'),
        ),
        migrations.AlterField(
            model_name='solicitud',
            name='idcentro',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='centro', to='mujerApp.centro'),
        ),
        migrations.AlterField(
            model_name='solicitud',
            name='iduser',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='solicitud',
            name='nombreCliente',
            field=models.CharField(max_length=30, verbose_name='nombre'),
        ),
    ]
