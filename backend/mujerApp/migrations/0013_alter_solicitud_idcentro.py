# Generated by Django 3.2.8 on 2021-10-24 19:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mujerApp', '0012_solicitud_idcentro'),
    ]

    operations = [
        migrations.AlterField(
            model_name='solicitud',
            name='idcentro',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='centro', to='mujerApp.centro'),
        ),
    ]
