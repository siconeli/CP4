from django.views.generic import CreateView, UpdateView
from .models import ProcessoAdministrativo
from django.urls import reverse_lazy


###### CREATE ######
class CadProcessoAdmCreate(CreateView):
    model = ProcessoAdministrativo
    fields = ['pat', 'munic', 'uf', 'datini', 'datfin', 'datdivat', 'valtrib', 'valmul', 'valcred', 'valatu', 'datvalatu', 'datand', 'anda', 'datprazo']
    template_name = 'cadastros/cadprocessoadm.html'
    success_url = reverse_lazy('cad-proc-adm')  #Após salvar no banco direciona para a url


###### UPDATE ######
class CadProcessoAdmUpdate(UpdateView):
    model = ProcessoAdministrativo
    fields = ['pat', 'munic', 'uf', 'datini', 'datfin', 'datdivat', 'valtrib', 'valmul', 'valcred', 'valatu', 'datvalatu', 'datand', 'anda', 'datprazo']
    template_name = 'cadastros/cadprocessoadm.html'
    success_url = reverse_lazy('cad-proc-adm')
