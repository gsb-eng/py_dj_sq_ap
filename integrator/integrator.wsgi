import os
import sys

sys.path.append('/prog/FOSS/py_dj_sq_ap/integrator/')

os.environ['DJANGO_SETTINGS_MODULE'] = 'integrator.settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()

