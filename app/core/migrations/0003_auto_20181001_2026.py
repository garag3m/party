# Generated by Django 2.0 on 2018-10-01 23:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_evento_carga_h'),
    ]

    operations = [
        migrations.RenameField(
            model_name='evento',
            old_name='edicao',
            new_name='edicao_atual',
        ),
        migrations.AddField(
            model_name='evento',
            name='edicao_anterior',
            field=models.PositiveIntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='evento',
            name='nome',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='evento',
            name='tema',
            field=models.CharField(max_length=150),
        ),
    ]
