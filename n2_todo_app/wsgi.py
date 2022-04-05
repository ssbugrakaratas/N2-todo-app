"""
Copyright (c) 2022 - present Samed Buğra KARATAŞ
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'n2_todo_app.settings')

application = get_wsgi_application()
