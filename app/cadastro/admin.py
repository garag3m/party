from django.contrib import admin
from .models import Responsavel, EmitirCertificado

# Register your models here.

admin.site.register([Responsavel, EmitirCertificado])
