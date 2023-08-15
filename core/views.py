from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = 'core/index.html'


class CadProcessoAdmView(TemplateView):
    template_name = 'core/cadprocessoadm.html'