# Generated by Django 2.0 on 2018-11-13 03:24

import datetime
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Evento',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=150)),
                ('finalizado', models.CharField(choices=[('Finalizado', 'Finalizado'), ('Não Finalizado', 'Não Finalizado'), ('Acontecendo', 'Acontecendo')], help_text='Marcar o campo referente ao estado atual do evento', max_length=20, verbose_name='Status do evento')),
                ('descricao', models.TextField(verbose_name='Descrição')),
                ('edicao', models.PositiveIntegerField(default=1, verbose_name='Edição')),
                ('tema', models.CharField(max_length=150)),
                ('carga_h', models.CharField(max_length=5, verbose_name='Carga horaria prevista')),
                ('data', models.DateField(default=datetime.date.today, verbose_name='Inicio do evento')),
                ('data_fim', models.DateField(default=datetime.date.today, verbose_name='Final do evento')),
            ],
            options={
                'verbose_name': 'Evento',
                'verbose_name_plural': 'Eventos',
                'db_table': 'evento',
                'ordering': ('nome',),
            },
        ),
        migrations.CreateModel(
            name='Foto',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('autor', models.CharField(max_length=100, verbose_name='Autor')),
                ('descricao', models.CharField(max_length=255, verbose_name='Descrição')),
                ('imagem', models.FileField(upload_to='imagem', verbose_name='Imagem')),
            ],
            options={
                'verbose_name': 'Foto',
                'verbose_name_plural': 'Fotos',
                'db_table': 'foto',
                'ordering': ('autor',),
            },
        ),
        migrations.CreateModel(
            name='Galeria',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('titulo', models.CharField(max_length=100, verbose_name='Titulo')),
                ('evento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='galerias', to='core.Evento', verbose_name='Evento')),
            ],
            options={
                'verbose_name': 'Galeria',
                'verbose_name_plural': 'Galerias',
                'db_table': 'galeria',
                'ordering': ('titulo',),
            },
        ),
        migrations.CreateModel(
            name='Noticia',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('titulo', models.CharField(max_length=150, verbose_name='Titulo')),
                ('autor', models.CharField(max_length=100, verbose_name='Autor')),
                ('texto', models.TextField(verbose_name='Sobre')),
                ('data_public', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Publicado em')),
                ('evento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='noticias', to='core.Evento')),
            ],
            options={
                'verbose_name': 'Noticia',
                'verbose_name_plural': 'Noticias',
                'db_table': 'noticia',
                'ordering': ('data_public',),
            },
        ),
        migrations.AddField(
            model_name='foto',
            name='galeria',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fotos', to='core.Galeria'),
        ),
    ]
