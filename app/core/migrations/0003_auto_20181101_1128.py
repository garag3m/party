# Generated by Django 2.0 on 2018-11-01 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20181101_0732'),
    ]

    operations = [
        migrations.AlterField(
            model_name='foto',
            name='imagem',
            field=models.FileField(upload_to='imagem', verbose_name='Imagem'),
        ),
    ]
