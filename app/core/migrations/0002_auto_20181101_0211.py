# Generated by Django 2.0 on 2018-11-01 05:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='evento',
            options={'ordering': ('nome',), 'verbose_name': 'Evento', 'verbose_name_plural': 'Eventos'},
        ),
        migrations.AlterModelOptions(
            name='foto',
            options={'ordering': ('autor',), 'verbose_name': 'Foto', 'verbose_name_plural': 'Fotos'},
        ),
        migrations.AlterModelOptions(
            name='galeria',
            options={'ordering': ('titulo',), 'verbose_name': 'Galeria', 'verbose_name_plural': 'Galerias'},
        ),
    ]
