"""
Django settings for app project.

Generated by 'django-admin startproject' using Django 3.0.2.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

#  Created by Alex Matos Iuasse.
#  Copyright (c) 2020.  All rights reserved.
#  Last modified 28/07/2020 11:46.

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'xj7o!^3d43#@0f9*ac#x(me59xtz*1y_2fggoamvpz$_c))!1x'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['localhost', '0.0.0.0', '192.168.18.16']

# CUSTOMIZATION DEFINITIONS
# GENERAL
NAME_OF_ENTERPRISE = "Nippon Ar"
# CONFIG CUSTOMIZATION
HEADER_CLASS_CONFIG_GENERAL = "card-header-primary"
HEADER_CLASS_CONFIG_TECHNICAL = "card-header-primary"
HEADER_CLASS_CONFIG_FINANTIAL = "card-header-primary"
# CONFIG BRAND CUSTOMIZATION
TITLE_VIEW_CONFIG_BRAND = "Marcas"
TITLE_CREATE_CONFIG_BRAND = "Nova Marca"
TITLE_EDIT_CONFIG_BRAND = "Editar Marca"
TITLE_DEL_CONFIG_BRAND = "Deletar Marca"
SUBTITLE_VIEW_CONFIG_BRAND = "Configuração de marcas"
# CONFIG CAPACITY CUSTOMIZATION
TITLE_VIEW_CONFIG_CAPACITY = "Capacidades"
TITLE_CREATE_CONFIG_CAPACITY = "Nova Capacidade"
TITLE_EDIT_CONFIG_CAPACITY = "Editar Capacidade"
TITLE_DEL_CONFIG_CAPACITY = "Deletar Capacidade"
SUBTITLE_VIEW_CONFIG_CAPACITY = "Configuração de capacidades"
# CONFIG MODEL CUSTOMIZATION
TITLE_VIEW_CONFIG_MODEL = "Modelos"
TITLE_CREATE_CONFIG_MODEL = "Novo Modelo"
TITLE_EDIT_CONFIG_MODEL = "Editar Modelo"
TITLE_DEL_CONFIG_MODEL = "Deletar Modelo"
SUBTITLE_VIEW_CONFIG_MODEL = "Configuração de modelos"
# CONFIG TYPE CUSTOMIZATION
TITLE_VIEW_CONFIG_TYPE = "Tipos"
TITLE_CREATE_CONFIG_TYPE = "Novo Tipo"
TITLE_EDIT_CONFIG_TYPE = "Editar Tipo"
TITLE_DEL_CONFIG_TYPE = "Deletar Tipo"
SUBTITLE_VIEW_CONFIG_TYPE = "Configuração de tipos"
# CONFIG CITY CUSTOMIZATION
TITLE_VIEW_CONFIG_CITY = "Cidades"
TITLE_CREATE_CONFIG_CITY = "Nova Cidade"
TITLE_EDIT_CONFIG_CITY = "Editar Cidade"
TITLE_DEL_CONFIG_CITY = "Deletar Cidade"
SUBTITLE_VIEW_CONFIG_CITY = "Configuração de cidades"
# CUSTOMER APP CUSTOMIZATION
# CUSTOMER
TITLE_VIEW_CUSTOMER = "Clientes"
SUBTITLE_VIEW_CUSTOMER = "Manejamento de clientes"
# INDIVIDUAL CUSTOMER
TITLE_VIEW_INDIVIDUAL_CUSTOMER = "Cliente - Pessoa Física"
TITLE_CREATE_INDIVIDUAL_CUSTOMER = "Novo Cliente - Pessoa Física"
TITLE_EDIT_INDIVIDUAL_CUSTOMER = "Editar Cliente - Pessoa Física"
TITLE_DEL_INDIVIDUAL_CUSTOMER = "Deletar Cliente - Pessoa Física"
SUBTITLE_INDIVIDUAL_CUSTOMER = "Configuração de clientes"
HEADER_CLASS_INDIVIDUAL_CUSTOMER = "card-header-rose"  # class of card header, basically just change the color
# JURIDICAL CUSTOMER
TITLE_VIEW_JURIDICAL_CUSTOMER = "Cliente - Pessoa Jurídica"
TITLE_CREATE_JURIDICAL_CUSTOMER = "Novo Cliente - Pessoa Jurídica"
TITLE_EDIT_JURIDICAL_CUSTOMER = "Editar Cliente - Pessoa Jurídica"
TITLE_DEL_JURIDICAL_CUSTOMER = "Deletar Cliente - Pessoa Jurídica"
SUBTITLE_JURIDICAL_CUSTOMER = "Configuração de clientes"
HEADER_CLASS_JURIDICAL_CUSTOMER = "card-header-danger"
# DEVICE
TITLE_VIEW_DEVICE = "Equipamentos"
TITLE_CREATE_DEVICE = "Novo Equipamento"
TITLE_EDIT_DEVICE = "Editar Equipamento"
TITLE_DEL_DEVICE = "Deletar Equipamento"
SUBTITLE_DEVICE = "Configuração de equipamentos"
HEADER_CLASS_DEVICE = "card-header-rose"  # class of card header, basically just change the color

CRISPY_TEMPLATE_PACK = 'bootstrap4'
AUTH_USER_MODEL = 'users.CustomUser'
DJANGO_TABLES2_TEMPLATE = "django_tables2/bootstrap4.html"

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'corsheaders',
    'simple_history',
    'background_task',
    'bootstrap4',
    'crispy_forms',
    'django_tables2',
    'django_filters',
    'users',
    'frontend',
    'base',
    'customer',
    'config',
    'device',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    # 'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    'simple_history.middleware.HistoryRequestMiddleware',
    'base.middleware.BaseMiddleware',
]

ROOT_URLCONF = 'app.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'frontend.context_processors.enterprise_name',
            ],
        },
    },
]

WSGI_APPLICATION = 'app.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'pt-br'
USE_I18N = True
USE_L10N = True
USE_TZ = True
TIME_ZONE = "America/Sao_Paulo"
DATE_INPUT_FORMATS = ['%d-%m-%Y']

# Login redirect
LOGIN_URL = "/login/"
LOGIN_REDIRECT_URL = '/'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static/')
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')
