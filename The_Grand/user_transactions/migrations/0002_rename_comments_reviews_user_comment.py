# Generated by Django 3.2.4 on 2021-06-30 23:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_transactions', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reviews',
            old_name='comments',
            new_name='user_comment',
        ),
    ]
