# Generated by Django 4.0.1 on 2022-01-30 21:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_placas', '0003_alter_placa_imagem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='placa',
            name='categoria',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='placa',
            name='codigo',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='placa',
            name='imagem',
            field=models.TextField(blank=True, null=True),
        ),
    ]
