# Generated by Django 3.2.8 on 2021-10-23 22:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mujerApp', '0007_auto_20211023_1734'),
    ]

    operations = [
        migrations.AlterField(
            model_name='solicitud',
            name='ciudad',
            field=models.CharField(max_length=30, verbose_name='ciudad'),
        ),
    ]