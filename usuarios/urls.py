from django.urls import path

from django.contrib.auth import views as auth_views   # Views naturais do django para autenticação de usuário, não preciso criar uma view manuamente.

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(
        template_name = 'usuarios/login.html'  # Como eu não criei a view, utilizei uma já existente do módulo, eu informo o template aqui.
    ), name="login"),
]