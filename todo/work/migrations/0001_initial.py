# Generated by Django 4.0 on 2022-01-16 16:01

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0006_alter_user_birthdaydate_alter_user_uuid'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('repo_url', models.CharField(max_length=512)),
                ('users', models.ManyToManyField(to='users.User')),
            ],
        ),
        migrations.CreateModel(
            name='ToDo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=1024)),
                ('create_date', models.DateField(default=datetime.datetime(2022, 1, 16, 16, 1, 20, 857310))),
                ('update_date', models.DateField(default=datetime.datetime(2022, 1, 16, 16, 1, 20, 857329))),
                ('is_active', models.BooleanField()),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='work.project')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='users.user')),
            ],
        ),
    ]