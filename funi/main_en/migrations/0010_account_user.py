# Generated by Django 4.2.2 on 2023-06-25 14:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main_en', '0009_alter_account_profile_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='user',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='account', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
