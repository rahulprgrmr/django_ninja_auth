# Generated by Django 5.0.7 on 2024-07-30 10:58

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0002_alter_user_managers"),
    ]

    operations = [
        migrations.CreateModel(
            name="Token",
            fields=[
                (
                    "key",
                    models.CharField(max_length=40, primary_key=True, serialize=False),
                ),
                ("created", models.DateTimeField(auto_now_add=True)),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="auth_token",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
