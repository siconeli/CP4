from django.contrib import admin
from .models import UnidadeFederativa, ProcessoAdministrativo, Municipio, CadAndamentos , Andamento

@admin.register(UnidadeFederativa)
class UnidadeFederativaAdmin(admin.ModelAdmin):
    list_display = ('uf',)

@admin.register(Municipio)
class MunicipioAdmin(admin.ModelAdmin):
    list_display = ('municipio',)

@admin.register(CadAndamentos)
class CadAndamentosAdmin(admin.ModelAdmin):
    list_display = ('cadandamento',)

@admin.register(Andamento)
class AndamentoAdmin(admin.ModelAdmin):
    list_display = ('andamento', 'datandamento')


@admin.register(ProcessoAdministrativo)
class ProcessoAdministrativoAdmin(admin.ModelAdmin):
    list_display = ('pat', 'municipio', 'uf')

