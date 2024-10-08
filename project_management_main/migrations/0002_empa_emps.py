# Generated by Django 5.0.7 on 2024-08-14 05:43

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project_management_main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmpA',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Employee Level-A',
                'verbose_name_plural': 'Employee Level-A',
            },
        ),
        migrations.CreateModel(
            name='EmpS',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Employee Level-S',
                'verbose_name_plural': 'Employee Level-S',
            },
        ),
    ]
