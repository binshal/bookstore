# Generated by Django 5.1.2 on 2024-11-10 00:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_app', '0002_rename_user_cart_username'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cart',
            old_name='username',
            new_name='user',
        ),
    ]