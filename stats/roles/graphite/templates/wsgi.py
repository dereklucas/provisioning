import os
import sys

path = '/opt/graphite/webapp/'
if path not in sys.path:
    sys.path.append(path)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "graphite.settings")

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
