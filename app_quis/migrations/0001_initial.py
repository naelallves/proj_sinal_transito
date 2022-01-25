# Generated by Django 4.0.1 on 2022-01-24 23:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Alternativa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('conteudo', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'Alternativas',
            },
        ),
        migrations.CreateModel(
            name='Dificuldade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'Dificuldades',
            },
        ),
        migrations.CreateModel(
            name='Pergunta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('código', models.CharField(max_length=50, null=True)),
                ('enunciado', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('id_dificuldade', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_quis.dificuldade')),
            ],
            options={
                'verbose_name_plural': 'Perguntas',
            },
        ),
        migrations.CreateModel(
            name='RelPerguntaAlternativa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('certa', models.BooleanField(default=False)),
                ('id_alternativa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_quis.alternativa')),
                ('id_pergunta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_quis.pergunta')),
            ],
        ),
    ]
