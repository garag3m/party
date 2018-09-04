# Generated by Django 2.0.6 on 2018-08-13 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evento',
            name='finalizado',
            field=models.IntegerField(choices=[(0, 'Finalizado'), (1, 'Não Finalizado'), (2, 'Acontecendo')], help_text='Marcar o campo referente ao estado atual do evento', max_length=1, verbose_name='Status do evento'),
        ),
    ]
