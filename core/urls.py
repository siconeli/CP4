from django.urls import path
from .views import IndexView, CadProcessoAdmView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('administrativo/', CadProcessoAdmView.as_view(), name='cadprocadm'),
]