# Generated by Django 3.0.6 on 2020-08-23 20:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theblog', '0014_auto_20200823_2219'),
    ]

    operations = [
        migrations.AlterField(
            model_name='porfile',
            name='profile_pic',
            field=models.ImageField(blank=True, null=True, upload_to='images/profile/'),
        ),
    ]