# Generated by Django 4.0.1 on 2022-01-26 23:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_quis', '0002_rename_dificuldade_categoria_alter_categoria_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='alternativa',
            name='id_categoria',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app_quis.categoria'),
        ),
    ]