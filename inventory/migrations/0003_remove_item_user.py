# Generated by Django 3.2 on 2021-04-22 01:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0002_auto_20210422_0111'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='user',
        ),
    ]
