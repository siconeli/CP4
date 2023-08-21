from django.urls import path
from .views import CadProcessoAdmCreate
from .views import CadProcessoAdmUpdate
from .views import CadProcessoAdmDelete
from .views import CadProcessoAdmList
from .views import AndamentosList
from .views import CadAndamentoCreate
from .views import CadAndamentoUpdate
from .views import CadAndamentoDelete

urlpatterns = [
    ###### VISUALIZAR ######


    ###### CREATE ######
    path('cadastrar/administrativo/', CadProcessoAdmCreate.as_view(), name='cre-proc-adm'), 
    path('cadastrar/andamentos/administrativo/', CadAndamentoCreate.as_view(), name='cre-and-proc-adm' ), 

    ###### UPDATE ######
    path('editar/administrativo/<int:pk>/', CadProcessoAdmUpdate.as_view(), name='upd-proc-adm'),
    path('editar/andamento/administrativo/<int:pk>/', CadAndamentoUpdate.as_view(), name='upd-and-proc-adm'),

    ###### DELETE ######
    path('excluir/administrativo/<int:pk>/', CadProcessoAdmDelete.as_view(), name='del-proc-adm'),
    path('excluir/andamento/administrativo/<int:pk>/', CadAndamentoDelete.as_view(), name='del-and-proc-adm' ), #continuar

    ###### LIST ######
    path('listar/administrativo/', CadProcessoAdmList.as_view(), name='list-proc-adm'),
    path('listar/andamentos/administrativo/', AndamentosList.as_view(), name='list-and-proc-adm'),

]