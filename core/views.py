from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = 'core/index.html'
    
class BaseView(TemplateView):
    template_name = 'core/base.html'