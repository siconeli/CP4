"""
Django settings for CP4 project.

Generated by 'django-admin startproject' using Django 4.2.4.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-l#8yh-^9#n*&*k6plcs!uvgg1xk)cpjma89jk^cu0+u&av9ts='

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True # Modo desenvolvimento

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'stdimage',
    'core.apps.CoreConfig', # Minha aplicação 'core'
    'cadastros.apps.CadastrosConfig', # Minha aplicação 'cadastros'
    'usuarios.apps.UsuariosConfig', # Minha aplicação 'usuários'
    'django_cleanup.apps.CleanupConfig', # Para excluir arquivos da pasta de uploads após editar o registro e adicionar um novo arquivo.
    'widget_tweaks', # Biblioteca Widget - Muito importante - Torna possível eu criar um formulário HTML próprio sincronizado com as Class Based Views.

]



MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


ROOT_URLCONF = 'CP4.urls'


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]


WSGI_APPLICATION = 'CP4.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'pt-br'

TIME_ZONE = 'America/Sao_Paulo'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

# Configuração dos arquivos estáticos: css, js, imagens
STATIC_URL = '/static/' # Usado durante o desenvolvimento
# STATIC_ROOT = str(BASE_DIR / 'staticfiles') # Usado durante a produção


#================================================================================================================
# Arquivos de Media (Para salvar em endereço Local na mesma máquina do código) (USAR DURANTE O DESENVOLVIMENTO)
MEDIA_URL = '/media/'
MEDIA_ROOT = str(BASE_DIR / 'media') #cria a pasta 'media' para onde irão todos os arquivos enviados

# # Arquivos de Media (Para salvar os arquivos em um servidor externo, acessado via IP) (USAR DURANTE A PRODUÇÃO)
# MEDIA_URL = '/uploads/' # Busca o arquivo na pasta uploads dentro do Servidor TrueNAS, quando é realizado um download.
# MEDIA_ROOT = ('//10.0.0.55/Geral/') # Encaminha o arquivo para o Servidor TrueNAS, quando é realizado um upload.
#================================================================================================================



# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# Configurações de autenticação padrão de login
LOGIN_REDIRECT_URL = 'index'  # Redireciona para a url de nome'index' após realizar o login
LOGOUT_REDIRECT_URL = 'login' # Ao fazer o logout(sair), ira direcionar para a url de nome 'login'
LOGIN_URL = 'login'  # Ao tentar acessar uma funcionalidade com permissão apenas para quem tem login, ira direcionar para a url de nome 'login'