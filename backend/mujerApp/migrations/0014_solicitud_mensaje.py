# Generated by Django 3.2.8 on 2021-10-27 01:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mujerApp', '0013_alter_solicitud_idcentro'),
    ]

    operations = [
        migrations.AddField(
            model_name='solicitud',
            name='mensaje',
            field=models.CharField(default=1, max_length=1000),
            preserve_default=False,
        ),
    ]