# Generated by Django 5.1.2 on 2024-11-15 15:46

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0012_task_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='fecha',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]