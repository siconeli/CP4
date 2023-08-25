from django.contrib import admin
from .models import ProcessoAdministrativo, Andamento


@admin.register(ProcessoAdministrativo)
class ProcessoAdministrativoAdmin(admin.ModelAdmin):
    list_display = ('pat',)


@admin.register(Andamento)
class AndamentoAdmin(admin.ModelAdmin):
    list_display = ('processo', 'andamento', 'arq1', 'arq2', 'arq3', 'arq4', 'arq5', 'arq6')

