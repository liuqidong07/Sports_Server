"""
WSGI config for Sports_Server project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/howto/deployment/wsgi/
"""

import os,sys
from django.core.wsgi import get_wsgi_application

sys.path.append('/var/www/Sports_Server')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Sports_Server.settings")
application = get_wsgi_application()
