# Generated by Django 4.0.3 on 2022-04-01 22:27

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20220402_0117'),
    ]

    operations = [
        migrations.RenameField(
            model_name='todo',
            old_name='check',
            new_name='checked',
        ),
        migrations.AlterField(
            model_name='todo',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='user',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False),
        ),
    ]
