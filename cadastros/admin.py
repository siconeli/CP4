from django.contrib import admin
from .models import ProcessoAdministrativo, Andamento


@admin.register(Andamento)
class AndamentoAdmin(admin.ModelAdmin):
    list_display = ('andamento', 'datandamento')


@admin.register(ProcessoAdministrativo)
class ProcessoAdministrativoAdmin(admin.ModelAdmin):
    list_display = ('pat', 'municipio', 'uf')

