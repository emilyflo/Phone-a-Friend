# Generated by Django 4.0.3 on 2022-04-12 17:38

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_response_accepted'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='favorite',
            field=models.ManyToManyField(blank=True, related_name='favorited_question', to=settings.AUTH_USER_MODEL),
        ),
    ]
