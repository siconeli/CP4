from django.views.generic.edit import CreateView, UpdateView, DeleteView # Módulo para criar, atualizar e deletar
from django.views.generic.list import ListView # Módulo para listar

from .models import ProcessoAdministrativo

from django.urls import reverse_lazy

from django.contrib.auth.mixins import LoginRequiredMixin # Módulo para controlar o acesso de um usuário a determinada url, através de autenticação de login


###### CREATE ######
class CadProcessoAdmCreate(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    model = ProcessoAdministrativo
    fields = ['pat', 'munic', 'uf', 'datini', 'datfin', 'datdivat', 'valtrib', 'valmul', 'valcred', 'valatu', 'datvalatu', 'datand', 'anda', 'datprazo', 'upload']
    template_name = 'cadastros/cadprocessoadm-cadastrar.html'
    success_url = reverse_lazy('list-proc-adm')  # name da url, irá direcionar para a url 


###### UPDATE ######
class CadProcessoAdmUpdate(UpdateView):
    model = ProcessoAdministrativo
    fields = ['pat', 'munic', 'uf', 'datini', 'datfin', 'datdivat', 'valtrib', 'valmul', 'valcred', 'valatu', 'datvalatu', 'datand', 'anda', 'datprazo', 'upload']
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