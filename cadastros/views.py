from typing import Any
from django.db.models.query import QuerySet
from django.views.generic import TemplateView # Módulo apenas para visualizar 
from django.views.generic.edit import CreateView, UpdateView, DeleteView # Módulo para criar, atualizar e deletar
from django.views.generic.list import ListView # Módulo para listar

from .models import ProcessoAdministrativo, Andamento

from django.urls import reverse_lazy

from django.contrib.auth.mixins import LoginRequiredMixin # Módulo para controlar o acesso de um usuário a determinada url, através de autenticação de login
from braces.views import GroupRequiredMixin # Para realizar o controle de grupos de permissões de usuários juntamente com o painel admin


###### VISUALIZAR ######
 



###### CREATE ######
class CadProcessoAdmCreate(GroupRequiredMixin, LoginRequiredMixin, CreateView): # Cadastro Processo Administrativo
    login_url = reverse_lazy('login')
    group_required = u"Consultores AEG"  # O usuário precisa estar no grupo 'consultores AEG' para ter permissão de realizar cadastros.
    model = ProcessoAdministrativo
    fields = ['pat', 'municipio', 'uf', 'datini', 'datfin', 'datdivat', 'valtrib', 'valmul', 'valcred', 'valatu', 'datvalatu', 'datand', 'datprazo']
    template_name = 'cadastros/cadprocessoadm-cadastrar.html'
    success_url = reverse_lazy('list-proc-adm')  # name da url, irá direcionar para a url


class CadAndamentoCreate(GroupRequiredMixin, LoginRequiredMixin, CreateView): # Cadastro Andamento Administrativo
    login_url = reverse_lazy('login')
    group_required = u"Consultores AEG"
    model = Andamento
    fields = ['processo', 'datandamento', 'andamento', 'dataprazo', 'locprocesso', 'Funcionario', 'datrecebimento', 'complemento']
    template_name = 'cadastros/cadandprocessoadm-cadastrar.html'
    success_url = reverse_lazy('list-and-proc-adm')




###### UPDATE ######
class CadProcessoAdmUpdate(GroupRequiredMixin, LoginRequiredMixin, UpdateView): # Update Processo Administrativo
    login_url = reverse_lazy('login')
    group_required = u"Consultores AEG"
    model = ProcessoAdministrativo
    fields = ['pat', 'municipio', 'uf', 'datini', 'datfin', 'datdivat', 'valtrib', 'valmul', 'valcred', 'valatu', 'datvalatu', 'datand', 'datprazo'] 
    template_name = 'cadastros/cadprocessoadm-cadastrar.html'
    success_url = reverse_lazy('list-proc-adm')


class CadAndamentoUpdate(GroupRequiredMixin, LoginRequiredMixin, UpdateView): # Update Andamento Administrativo
    login_url = reverse_lazy('login')
    group_required = u"Consultores AEG"
    model = Andamento
    fields = ['datandamento', 'andamento', 'dataprazo', 'locprocesso', 'Funcionario', 'datrecebimento', 'complemento']
    template_name = 'cadastros/cadandprocessoadm-cadastrar.html'
    success_url = reverse_lazy('list-and-proc-adm')




###### DELETE ######
class CadProcessoAdmDelete(GroupRequiredMixin, LoginRequiredMixin, DeleteView): # Delete Processo Administrativo
    login_url = reverse_lazy('login')
    group_required = u"Consultores AEG"
    model = ProcessoAdministrativo
    template_name = 'cadastros/cadprocessoadm-deletar.html'
    success_url = reverse_lazy('list-proc-adm')


class CadAndamentoDelete(GroupRequiredMixin, LoginRequiredMixin, DeleteView): # Delete Processo Administrativo
    login_url = reverse_lazy('login')
    group_required = u"Consultores AEG"
    model = Andamento
    template_name = 'cadastros/cadandprocessoadm-deletar.html'
    success_url = reverse_lazy('list-and-proc-adm')




###### LIST ######
class CadProcessoAdmList(LoginRequiredMixin, ListView): # List Processo Administrativo
    login_url = reverse_lazy('login')
    model = ProcessoAdministrativo
    template_name = 'cadastros/listas/cadprocessoadm-listar.html'
    paginate_by = 10 # Número de registros listados na minha list

    # Para filtrar dados através do campo input
    def get_queryset(self):
        buscaprocesso = self.request.GET.get('processo') # processo é o 'name' la do input da pesquisa

        if buscaprocesso:
            processos = ProcessoAdministrativo.objects.filter(pat__icontains=buscaprocesso)
        else:
            processos = ProcessoAdministrativo.objects.all()

        return processos
        

class CadAndamentosList(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = Andamento, ProcessoAdministrativo
    template_name = 'cadastros/listas/cadandprocessoadm-listar.html'   
    paginate_by = 10

    def get_queryset(self):
        # buscaanda = self.request.GET.get('anda')  #PRECISO ENTENDER COMO BUSCAR O PROCESSO_ID DO PROCESSO QUE DESEJO

        buscaanda = 7

        if buscaanda:
            buscaprocesso = Andamento.objects.filter(processo_id=buscaanda)
            #andamentos = Andamento.objects.filter(processo_id=buscaanda)
        else:
            buscaprocesso = Andamento.objects.all()


        #buscaprocesso = Andamento.objects.filter(processo_id=1) # É assim que se faz!

        return buscaprocesso

        

