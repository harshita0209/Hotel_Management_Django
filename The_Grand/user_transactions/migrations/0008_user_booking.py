# Generated by Django 3.2.4 on 2021-07-05 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_transactions', '0007_rooms_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='user_booking',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('user_id', models.TextField()),
                ('category', models.IntegerField(default=0)),
                ('room_type', models.TextField()),
                ('price', models.IntegerField(default=0)),
                ('rooms', models.IntegerField(default=0)),
                ('days', models.IntegerField(default=0)),
                ('total_price', models.IntegerField(default=0)),
            ],
        ),
    ]
