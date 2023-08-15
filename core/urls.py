from django.urls import path
from .views import IndexView
from cadastros.views import CadProcessoAdmView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('administrativo/', CadProcessoAdmView.as_view(), name="cadprocadm")  #Essa view vem da aplicação 'cadastros'
]