# Generated by Django 4.0.1 on 2022-02-01 01:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_quis', '0007_alter_pergunta_imagem'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pergunta',
            name='imagem',
        ),
    ]
