from django.views.generic.edit import CreateView, UpdateView, DeleteView # Módulo para criar, atualizar e deletar
from django.views.generic.list import ListView # Módulo para listar

from .models import ProcessoAdministrativo

from django.urls import reverse_lazy

from django.contrib.auth.mixins import LoginRequiredMixin # Módulo para controlar o acesso de um usuário a determinada url, através de autenticação de login
from braces.views import GroupRequiredMixin # Para realizar o controle de grupos de permissões de usuários juntamente com o painel admin


###### CREATE ######
class CadProcessoAdmCreate(GroupRequiredMixin, LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    group_required = u"Consultores AEG"  # O usuário precisa estar no grupo 'consultores AEG' para ter permissão de realizar cadastros.
    model = ProcessoAdministrativo
    fields = ['pat', 'munic', 'uf', 'datini', 'datfin', 'datdivat', 'valtrib', 'valmul', 'valcred', 'valatu', 'datvalatu', 'datand', 'anda', 'datprazo', 'upload']
    template_name = 'cadastros/cadprocessoadm-cadastrar.html'
    success_url = reverse_lazy('list-proc-adm')  # name da url, irá direcionar para a url 


###### UPDATE ######
class CadProcessoAdmUpdate(GroupRequiredMixin, LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    group_required = u"Consultores AEG"
    model = ProcessoAdministrativo
    fields = ['pat', 'munic', 'uf', 'datini', 'datfin', 'datdivat', 'valtrib', 'valmul', 'valcred', 'valatu', 'datvalatu', 'datand', 'anda', 'datprazo', 'upload']
    template_name = 'cadastros/cadprocessoadm-cadastrar.html'
    success_url = reverse_lazy('list-proc-adm')


###### DELETE ######
class CadProcessoAdmDelete(GroupRequiredMixin, LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    group_required = u"Consultores AEG"
    model = ProcessoAdministrativo
    template_name = 'cadastros/cadprocessoadm-deletar.html'
    success_url = reverse_lazy('list-proc-adm')


###### LIST ######
class CadProcessoAdmList(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = ProcessoAdministrativo
    template_name = 'cadastros/listas/cadprocessoadm-listar.html'

