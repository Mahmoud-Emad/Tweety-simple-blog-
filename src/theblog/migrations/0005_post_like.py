# Generated by Django 3.1 on 2020-08-20 16:51

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('theblog', '0004_auto_20200816_2211'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='like',
            field=models.ManyToManyField(related_name='bloge_Post', to=settings.AUTH_USER_MODEL),
        ),
    ]
