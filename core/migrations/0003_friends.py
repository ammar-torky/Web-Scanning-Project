# Generated by Django 5.1.6 on 2025-02-26 21:51

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_user_bio_post'),
    ]

    operations = [
        migrations.CreateModel(
            name='Friends',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_A', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_A', to=settings.AUTH_USER_MODEL)),
                ('user_B', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_B', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
