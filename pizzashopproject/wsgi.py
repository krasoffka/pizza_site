"""
WSGI config for pizzashopproject project.
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "pizzashopproject.settings")

application = get_wsgi_application()
