"""
Copyright (c) 2022 - present Samed Buğra KARATAŞ
"""

from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("app.urls"))
]
