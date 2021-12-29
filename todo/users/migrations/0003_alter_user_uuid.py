# Generated by Django 4.0 on 2021-12-25 04:34

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):
    dependencies = [
        ('users', '0002_alter_user_uuid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='uuid',
            field=models.UUIDField(default=uuid.UUID('e3d7f8cc-7ce8-4c26-9c64-e3a544d2bdac'), primary_key=True,
                                   serialize=False),
        ),
    ]
