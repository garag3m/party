# Generated by Django 2.0 on 2018-11-13 03:24

import datetime
from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0009_alter_user_last_name_max_length'),
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyUser',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Atividade',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('tipo', models.CharField(max_length=255, verbose_name='Tipo')),
                ('ministrante', models.CharField(max_length=100, verbose_name='Ministrante')),
                ('titulo', models.CharField(max_length=255, verbose_name='Titulo')),
                ('qt_inscritos', models.PositiveIntegerField(verbose_name='Quantidade de inscritos')),
                ('descricao', models.TextField(verbose_name='Descrição')),
                ('data', models.DateField(default=datetime.date.today, verbose_name='Data')),
                ('local', models.CharField(max_length=255, verbose_name='Local')),
                ('carga_h', models.PositiveIntegerField(verbose_name='Duração')),
                ('evento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Evento')),
            ],
        ),
        migrations.CreateModel(
            name='EmitirCertificado',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('qt_falta', models.CharField(max_length=3, verbose_name='Quantidade de faltas')),
                ('emitir_cert', models.IntegerField(choices=[(0, 'Autorizo'), (1, 'Não autorizo')], verbose_name='Emissão do certificado')),
                ('evento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='evento', to='core.Evento')),
            ],
            options={
                'verbose_name': 'Emitir certificado',
                'verbose_name_plural': 'Emitir certificados',
                'db_table': 'emitircertificado',
            },
        ),
        migrations.CreateModel(
            name='Inscrito',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=100)),
                ('idade', models.PositiveIntegerField()),
                ('cidade', models.CharField(max_length=100)),
                ('uf', models.CharField(max_length=4)),
                ('cpf', models.PositiveIntegerField()),
                ('rg', models.PositiveIntegerField()),
                ('telefone', models.CharField(max_length=15)),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='inscritos', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Inscrito',
                'verbose_name_plural': 'Inscritos',
                'db_table': 'inscrito',
                'ordering': ('nome',),
            },
        ),
        migrations.CreateModel(
            name='Responsavel',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('evento', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='core.Evento')),
                ('usuario', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='responsaveis', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Responsavel',
                'verbose_name_plural': 'Responsaveis',
                'db_table': 'responsavel',
            },
        ),
        migrations.AddField(
            model_name='emitircertificado',
            name='inscrito',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='inscrito', to='cadastro.Inscrito'),
        ),
    ]
