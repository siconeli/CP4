from django.contrib import admin
from .models import ProcessoAdministrativo, Andamento, ArquivosProcAdm


@admin.register(Andamento)
class AndamentoAdmin(admin.ModelAdmin):
    list_display = ('processo', 'andamento')


@admin.register(ProcessoAdministrativo)
class ProcessoAdministrativoAdmin(admin.ModelAdmin):
    list_display = ('pat',)

@admin.register(ArquivosProcAdm)
class ArquivosProcAdmAdmin(admin.ModelAdmin):
    list_display = ('arq1', 'arq2', 'arq3', 'arq4', 'arq5', 'arq6')
