# Generated by Django 3.0.7 on 2021-06-27 06:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_auto_20210626_2037'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orders',
            name='verify_sign_sha2',
        ),
    ]
