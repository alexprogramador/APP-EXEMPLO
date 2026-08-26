"""
Django settings for myapp project.
"""

from pathlib import Path
import os
import dj_database_url


# ==================================================
# CONFIGURAÇÃO BÁSICA
# ==================================================

BASE_DIR = Path(__file__).resolve().parent.parent


SECRET_KEY = os.environ.get(
    "SECRET_KEY",
    "django-insecure-&6prrj=8=$#h^rk43wla@^t8)#h46an*6erxq5d4p47bc&ntny"
)


# ==================================================
# DEBUG
# ==================================================

DEBUG = os.environ.get("DEBUG", "True").lower() == "true"


# ==================================================
# HOSTS PERMITIDOS
# ==================================================

# Host fornecido automaticamente pelo Render
RENDER_EXTERNAL_HOSTNAME = os.environ.get(
    "RENDER_EXTERNAL_HOSTNAME"
)

ALLOWED_HOSTS = [
    "localhost",
    "127.0.0.1",
]

# Adiciona automaticamente o domínio do Render
if RENDER_EXTERNAL_HOSTNAME:
    ALLOWED_HOSTS.append(RENDER_EXTERNAL_HOSTNAME)

# Mantém também o domínio atual do projeto
ALLOWED_HOSTS.append("app-exemplo.onrender.com")


# ==================================================
# APLICAÇÕES
# ==================================================

INSTALLED_APPS = [

    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",

    # Django REST Framework
    "rest_framework",

    # Nossa aplicação
    "core",
]


# ==================================================
# MIDDLEWARE
# ==================================================

MIDDLEWARE = [

    "django.middleware.security.SecurityMiddleware",

    # WhiteNoise
    "whitenoise.middleware.WhiteNoiseMiddleware",

    "django.contrib.sessions.middleware.SessionMiddleware",

    "django.middleware.common.CommonMiddleware",

    "django.middleware.csrf.CsrfViewMiddleware",

    "django.contrib.auth.middleware.AuthenticationMiddleware",

    "django.contrib.messages.middleware.MessageMiddleware",

    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]


# ==================================================
# URLS
# ==================================================

ROOT_URLCONF = "myapp.urls"


# ==================================================
# TEMPLATES
# ==================================================

TEMPLATES = [

    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",

        "DIRS": [],

        "APP_DIRS": True,

        "OPTIONS": {

            "context_processors": [

                "django.template.context_processors.request",

                "django.contrib.auth.context_processors.auth",

                "django.contrib.messages.context_processors.messages",

            ],

        },

    },

]


# ==================================================
# WSGI
# ==================================================

WSGI_APPLICATION = "myapp.wsgi.application"


# ==================================================
# BANCO DE DADOS
# ==================================================

DATABASES = {

    "default": dj_database_url.config(

        # No Render:
        # utiliza DATABASE_URL / PostgreSQL

        # Localmente:
        # utiliza SQLite

        default=f"sqlite:///{BASE_DIR / 'db.sqlite3'}",

        conn_max_age=600,

        ssl_require=not DEBUG,

    )

}


# ==================================================
# VALIDAÇÃO DE SENHAS
# ==================================================

AUTH_PASSWORD_VALIDATORS = [

    {
        "NAME":
        "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },

    {
        "NAME":
        "django.contrib.auth.password_validation.MinimumLengthValidator",
    },

    {
        "NAME":
        "django.contrib.auth.password_validation.CommonPasswordValidator",
    },

    {
        "NAME":
        "django.contrib.auth.password_validation.NumericPasswordValidator",
    },

]


# ==================================================
# INTERNACIONALIZAÇÃO
# ==================================================

LANGUAGE_CODE = "pt-br"

TIME_ZONE = "America/Sao_Paulo"

USE_I18N = True

USE_TZ = True


# ==================================================
# ARQUIVOS ESTÁTICOS
# ==================================================

STATIC_URL = "static/"

STATIC_ROOT = BASE_DIR / "staticfiles"


# ==================================================
# WHITENOISE
# ==================================================

STATICFILES_STORAGE = (
    "whitenoise.storage.CompressedManifestStaticFilesStorage"
)


# ==================================================
# DJANGO REST FRAMEWORK
# ==================================================

REST_FRAMEWORK = {

    "DEFAULT_RENDERER_CLASSES": [

        "rest_framework.renderers.JSONRenderer",

        "rest_framework.renderers.BrowsableAPIRenderer",

    ],

}


# ==================================================
# SEGURANÇA HTTPS / RENDER
# ==================================================

SECURE_PROXY_SSL_HEADER = (
    "HTTP_X_FORWARDED_PROTO",
    "https",
)