# Generated by Django 2.0 on 2018-09-24 04:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadastro', '0003_emitircertificado'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emitircertificado',
            name='qt_falta',
            field=models.CharField(max_length=3, verbose_name='Quantidade de faltas'),
        ),
    ]