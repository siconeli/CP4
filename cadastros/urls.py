from django.urls import path
from .views import CadProcessoAdmCreate, CadProcessoAdmUpdate


urlpatterns = [
    path('cadastrar/administrativo/', CadProcessoAdmCreate.as_view(), name='cad-proc-adm'),  
    path('editar/administrativo/<int:pk>', CadProcessoAdmUpdate.as_view(), name='upd-proc-adm')
]