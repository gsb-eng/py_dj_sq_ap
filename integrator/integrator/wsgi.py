"""
WSGI config for integrator project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/howto/deployment/wsgi/
"""

import os
import sys

sys.path.append('/prog/FOSS/py_dj_sq_ap/integrator/')

os.environ['DJANGO_SETTINGS_MODULE'] = 'integrator.settings'

# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "integrator.settings")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
