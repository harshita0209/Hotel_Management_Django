# Generated by Django 3.2.4 on 2021-07-06 00:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_transactions', '0009_auto_20210706_0536'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user_booking',
            old_name='rooms',
            new_name='no_rooms',
        ),
    ]
