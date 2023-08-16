from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView

from .models import ProcessoAdministrativo

from django.urls import reverse_lazy


###### CREATE ######
class CadProcessoAdmCreate(CreateView):
    model = ProcessoAdministrativo
    fields = ['pat', 'munic', 'uf', 'datini', 'datfin', 'datdivat', 'valtrib', 'valmul', 'valcred', 'valatu', 'datvalatu', 'datand', 'anda', 'datprazo']
    template_name = 'cadastros/cadprocessoadm-cadastrar.html'
    success_url = reverse_lazy('list-proc-adm')  #name da url, irá direcionar para a url


###### UPDATE ######
class CadProcessoAdmUpdate(UpdateView):
    model = ProcessoAdministrativo
    fields = ['pat', 'munic', 'uf', 'datini', 'datfin', 'datdivat', 'valtrib', 'valmul', 'valcred', 'valatu', 'datvalatu', 'datand', 'anda', 'datprazo']
    template_name = 'cadastros/cadprocessoadm-cadastrar.html'
    success_url = reverse_lazy('list-proc-adm')


###### DELETE ######
class CadProcessoAdmDelete(DeleteView):
    model = ProcessoAdministrativo
    template_name = 'cadastros/cadprocessoadm-deletar.html'
    success_url = reverse_lazy('list-proc-adm')


###### LIST ######
class CadProcessoAdmList(ListView):
    model = ProcessoAdministrativo
    template_name = 'cadastros/listas/cadprocessoadm-listar.html'