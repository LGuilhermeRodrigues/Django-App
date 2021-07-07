django_heroku.settings(locals())
TIME_ZONE = 'America/Sao_Paulo'
LANGUAGE_CODE = 'pt-BR'
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
DISABLE_COLLECTSTATIC=1