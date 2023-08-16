from django.urls import path
from .views import CadProcessoAdmCreate
from .views import CadProcessoAdmUpdate
from .views import CadProcessoAdmDelete
from .views import CadProcessoAdmList


urlpatterns = [
    ###### CREATE ######
    path('cadastrar/administrativo/', CadProcessoAdmCreate.as_view(), name='cre-proc-adm'),  

    ###### UPDATE ######
    path('editar/administrativo/<int:pk>/', CadProcessoAdmUpdate.as_view(), name='upd-proc-adm'),

    ###### DELETE ######
    path('excluir/administrativo/<int:pk>/', CadProcessoAdmDelete.as_view(), name='del-proc-adm'),

    ###### LIST ######
    path('listar/administrativo/', CadProcessoAdmList.as_view(), name='list-proc-adm'),
]