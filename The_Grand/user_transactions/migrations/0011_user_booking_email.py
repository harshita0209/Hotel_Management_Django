# Generated by Django 3.2.4 on 2021-07-06 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_transactions', '0010_rename_rooms_user_booking_no_rooms'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_booking',
            name='email',
            field=models.TextField(default=2),
            preserve_default=False,
        ),
    ]
