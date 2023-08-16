from django.urls import path
from .views import IndexView
from cadastros.views import CadProcessoAdmCreate

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('cadastrar/administrativo/', CadProcessoAdmCreate.as_view(), name="cad-proc-adm")  #Essa view vem da aplicação 'cadastros'
]