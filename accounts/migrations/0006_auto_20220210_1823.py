# Generated by Django 3.0.14 on 2022-02-10 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_userinfo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='classnet',
            name='classnet_cetification',
        ),
        migrations.AddField(
            model_name='classnet',
            name='classnet',
            field=models.BooleanField(default=False),
        ),
    ]
