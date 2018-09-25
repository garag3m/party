from django.contrib import admin
from .models import Responsavel, EmitirCertificado, Inscrito

# Register your models here.

admin.site.register([Responsavel, EmitirCertificado, Inscrito])
