from django.contrib import admin
from .models import UnidadeFederativa, ProcessoAdministrativo, Municipio, CadAndamentos , Andamento

admin.site.register(UnidadeFederativa)
admin.site.register(ProcessoAdministrativo)
admin.site.register(Municipio)
admin.site.register(CadAndamentos)
admin.site.register(Andamento)