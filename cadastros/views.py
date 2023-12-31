from django.db.models.query import QuerySet
# from django.views.generic import View # Módulo apenas para visualizar 
from typing import Any, Dict
from django.views.generic.edit import CreateView, UpdateView, DeleteView # Módulo para criar, atualizar e deletar
from django.views.generic.list import ListView # Módulo para listar

from .models import ProcessoAdministrativo, Andamento

from django.urls import reverse, reverse_lazy

from django.contrib.auth.mixins import LoginRequiredMixin # Módulo para controlar o acesso de um usuário a determinada url, através de autenticação de login
from braces.views import GroupRequiredMixin # Para realizar o controle de grupos de permissões de usuários juntamente com o painel admin

from .forms import CadProcessoAdmForm, AndamentoForm  # Para preencher o campo processo automaticamente no cadastro de andamento, de acordo com o ID do processo passada pela URL

from docx2pdf import convert

###### VISUALIZAR ######


###### CREATE ######
class CadProcessoAdmCreate(GroupRequiredMixin, LoginRequiredMixin, CreateView): # Cadastro Processo Administrativo
    login_url = reverse_lazy('login')
    group_required = u"Consultores AEG"  # O usuário precisa estar no grupo 'consultores AEG' para ter permissão de realizar cadastros.
    model = ProcessoAdministrativo
    form_class = CadProcessoAdmForm
    template_name = 'cadastros/cadprocessoadm-cadastrar.html'
    success_url = reverse_lazy('list-proc-adm')  # name da url, irá direcionar para a url        
       
# View do create de andamentos, preenche automaticamente o Campo processo
class CadAndamentoCreate(GroupRequiredMixin, LoginRequiredMixin, CreateView): # Cadastro Andamento Administrativo
    login_url = reverse_lazy('login')
    group_required = u"Consultores AEG"
    model = Andamento
    form_class = AndamentoForm
    template_name = 'cadastros/cadandprocessoadm-cadastrar.html'
    # success_url = reverse_lazy('list-proc-adm')

    # Funções para preencher o campo processo automaticamente no cadastro de andamento, de acordo com o ID do processo passada pela URL
    def get_context_data(self, **kwargs): 
        context = super().get_context_data(**kwargs)
        context['processo_pk'] = self.kwargs.get('processo_pk')
        return context

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['processo_pk'] = self.kwargs.get('processo_pk') # Passa a processo_pk para o formulário
        return kwargs

    # Após realizar o create do andamento com sucesso, reverte para a lista de andamentos do processo
    def get_success_url(self):
        processo_pk = self.kwargs.get('processo_pk') # Pega a PK do processo através da URL       

        return reverse('list-and-proc-adm', args=[processo_pk])
    
    def get(self, request, documento_id):
        documento = 

    convert(r"C:\Users\luisf\OneDrive\Área de Trabalho\Siconeli\PARTICULAR\ProjetoCP4\CP4\media\uploads\teste.docx", r"C:\Users\luisf\OneDrive\Área de Trabalho\Siconeli\PARTICULAR\ProjetoCP4\CP4\media\uploads\pdf_converted_file.pdf")





###### UPDATE ######
class CadProcessoAdmUpdate(GroupRequiredMixin, LoginRequiredMixin, UpdateView): # Update Processo Administrativo
    login_url = reverse_lazy('login')
    group_required = u"Consultores AEG"
    model = ProcessoAdministrativo
    fields = ['municipio', 'uf', 'datini', 'datfin', 'datdivat', 'valtrib', 'valmul', 'valcred', 'valatu', 'datvalatu', 'nomecontribuinte', 'pessoa', 'doc', 'nomefantasia', 'email', 'endereco', 'complemento', 'municipiocontri', 'ufcontri', 'cep', 'tel', 'cel'] 
    template_name = 'cadastros/cadprocessoadm-editar.html'
    success_url = reverse_lazy('list-proc-adm')


class CadAndamentoUpdate(GroupRequiredMixin, LoginRequiredMixin, UpdateView): # Update Andamento Administrativo
    login_url = reverse_lazy('login')
    group_required = u"Consultores AEG"
    model = Andamento
    fields = ['processo', 'datandamento', 'andamento', 'dias', 'dataprazo', 'funcionario', 'datrecebimento', 'complemento', 'arq1', 'arq2', 'arq3']
    template_name = 'cadastros/cadandprocessoadm-editar.html'
    # success_url = reverse_lazy('list-and-proc-adm')

    # Após realizar o update com sucesso, reverte para a lista de andamentos do processo
    def get_success_url(self):
        andamento_pk = self.kwargs.get('pk') # Pega a PK do andamento ao fazer o update através da URL
        andamento = Andamento.objects.get(pk=andamento_pk) # Busca o andamento através da PK do andamento
        processo_pk = andamento.processo_id # Busca a PK do processo através do andamento (processo_id é a ForeignKey entre o processo administrativo e o andamento)

        return reverse('list-and-proc-adm', args=[processo_pk]) # URL da lista de andamentos + pk do processo 



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
    success_url = reverse_lazy('list-proc-adm')




###### LIST ######
# View da lista de processos
class CadProcessoAdmList(LoginRequiredMixin, ListView): # List Processo Administrativo
    login_url = reverse_lazy('login')
    model = ProcessoAdministrativo
    template_name = 'cadastros/listas/cadprocessoadm-listar.html'
    # paginate_by = 6 # Número de registros listados na minha list

    # Para filtrar dados através do campo input (fazendo busca)
    # def get_queryset(self):
    #     buscaprocesso = self.request.GET.get('processo') # processo é o 'name' la do input da pesquisa

    #     if buscaprocesso:
    #         processos = ProcessoAdministrativo.objects.filter(pat__icontains=buscaprocesso)
    #     else:
    #         processos = ProcessoAdministrativo.objects.all()

    #     return processos
    

# View da Lista de andamentos do processo
class CadAndamentosList(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = ProcessoAdministrativo
    template_name = 'cadastros/listas/cadandprocessoadm-listar.html'  
    Paginate_by = 10

    # Irá buscar os andamentos vinculados ao processo e listar
    def get_queryset(self):
        
        busca_pk_processo = self.kwargs.get('processo_pk') # Pega a pk(primary key) da URL, pk do processo
        
        processo = ProcessoAdministrativo.objects.get(pk=busca_pk_processo)  # Pega o processo que possui a pk recebida (pk é a primary key do processo)
        andamentos = processo.andamento_set.all()  # Pega todos os atributos do andamento
        
        return andamentos


# View da Lista de arquivos do andamento
class CadArquivosAdmList(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = Andamento
    template_name = 'cadastros/listas/cadarquivoand-listar.html'
    context_object_name = 'arquivos' # Da um nome ao object_list da iteração criada no template

    def get_queryset(self):
    
        andamento_pk = self.kwargs.get('andamento_pk') # Pega a pk(primary key) da URL
        
        andamento = Andamento.objects.filter(pk=andamento_pk)  # Pega o andamento que possui a pk recebida (pk é a primary key do processo)
        # Usei o 'filter' para conseguir iterar com o objeto.

        return andamento


