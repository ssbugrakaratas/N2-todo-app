"""
Copyright (c) 2022 - present Samed Buğra KARATAŞ
"""

from datetime import datetime
import uuid
from django.db import models

class user(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    username = models.CharField(max_length=256, default="")
    password = models.CharField(max_length=256, default="")
    updated_date = models.DateTimeField()
    created_date = models.DateTimeField(default=datetime.now)

    class Meta:
        db_table = 'user'

class todo(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    user_id = models.UUIDField()
    checked = models.BooleanField()
    title = models.CharField(max_length=256, default="")
    checked_date = models.DateTimeField()
    updated_date = models.DateTimeField()
    created_date = models.DateTimeField(default=datetime.now)

    class Meta:
        db_table = 'todo'

