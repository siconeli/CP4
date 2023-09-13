from django.urls import path

from .views import CadProcessoAdmCreate
from .views import CadAndamentoCreate


from .views import CadProcessoAdmUpdate
from .views import CadAndamentoUpdate


from .views import CadProcessoAdmDelete
from .views import CadAndamentoDelete


from .views import CadProcessoAdmList
from .views import CadAndamentosList
from .views import CadArquivosAdmList



urlpatterns = [
    ###### VIEW ######


    ###### CREATE ######
    path('cadastrar/processo/adm/', CadProcessoAdmCreate.as_view(), name='cre-proc-adm'), 
    path('cadastrar/andamento/adm/<int:processo_pk>', CadAndamentoCreate.as_view(), name='cre-and-proc-adm'),


    ###### UPDATE ######
    path('editar/processo/adm/<int:pk>/', CadProcessoAdmUpdate.as_view(), name='upd-proc-adm'),
    path('editar/andamento/adm/<int:pk>/', CadAndamentoUpdate.as_view(), name='upd-and-proc-adm'),


    ###### DELETE ######
    path('excluir/processo/adm/<int:pk>/', CadProcessoAdmDelete.as_view(), name='del-proc-adm'),
    path('excluir/andamento/adm/<int:pk>/', CadAndamentoDelete.as_view(), name='del-and-proc-adm' ),


    ###### LIST ######
    path('listar/processo/adm/', CadProcessoAdmList.as_view(), name='list-proc-adm'),
    path('listar/andamento/adm/<int:processo_pk>/', CadAndamentosList.as_view(), name='list-and-proc-adm'),
    path('listar/arquivo/andamento/adm/<int:andamento_pk>/', CadArquivosAdmList.as_view(), name='list-arq-and-adm'),

]